import klarfio

# these are part of the standard library
import time
import difflib


# found this function on stackoverflow I haven't checked the code but seems to work ok
# https://stackoverflow.com/a/53818532/5847976
# Code by Gabe CC BY-SA 4.0
def recursive_dict_compare(d1, d2, level='root'):
    dict_are_the_same = True
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            s1 = set(d1.keys())
            s2 = set(d2.keys())
            print('{:<20} + {} - {}'.format(level, s1-s2, s2-s1))
            common_keys = s1 & s2
        else:
            common_keys = set(d1.keys())

        for k in common_keys:
            dict_are_the_same = dict_are_the_same  and recursive_compare(d1[k], d2[k], level='{}.{}'.format(level, k))

    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) != len(d2):
            print('{:<20} len1={}; len2={}'.format(level, len(d1), len(d2)))
            dict_are_the_same = False
        common_len = min(len(d1), len(d2))

        for i in range(common_len):
            dict_are_the_same = dict_are_the_same  and recursive_compare(d1[i], d2[i], level='{}[{}]'.format(level, i))

    else:
        if d1 != d2:
            print('{:<20} {} != {}'.format(level, d1, d2))
            dict_are_the_same = False

    return dict_are_the_same

def file_diff(filename1,filename2):
    with open(filename1, 'r') as file1:
        with open(filename2, 'r') as file2:
            diff = difflib.unified_diff(
                file1.readlines(),
                file2.readlines(),
                fromfile=filename1,
                tofile=filename2,
            )
            lines = list(diff)
            for i,line in enumerate(lines):
                
                if i>0 and i<len(lines)-1:
                    if line.startswith("-") and lines[i-1].startswith("-") and lines[i+1].startswith("-"):
                        continue
                    if line.startswith("+") and lines[i-1].startswith("+") and lines[i+1].startswith("+"):
                        continue

                    if line.startswith("-") and lines[i+1].startswith("-") and (not lines[i-1].startswith("-")):
                        print(line,end="")
                        print("  [...]")
                        continue

                    if line.startswith("+") and lines[i+1].startswith("+") and (not lines[i-1].startswith("+")):
                        print(line,end="")
                        print("  [...]")
                        continue
                        
                print(line,end="")
                #if the files are very large and slightly different we can overwhelm the terminal if we don't add a delay
                time.sleep(0.0001)



print("I will do two tests : first I will load a klarf file with the lib, then export it to a new file and re-load the exported version")
print("If everything is good the data of the two loaded klarf should match perfectly")
print("After this first test I will modify the data on one klarf and check that the comparison does fail")


#klarf_file = klarf()
klarf_file_ref = klarfio.klarf("./testfile_v1.8.klarf")
klarf_file_ref.export_klarf("./test_output_v1.8.klarf")
klarf_file_after_export = klarfio.klarf("./test_output_v1.8.klarf")

print("Any diff ?")
assert recursive_dict_compare(klarf_file_ref.data, klarf_file_after_export.data)


#lets try to modify one entry and see if the recursive compare catches it 
klarf_file_after_export.data["FileRecord_1.8"]["LotRecord_aLot.String"]["WaferRecord_FirstWaferId"]["DefectList"]["Data"][2][4] += 1

print("And now ?")

assert recursive_dict_compare(klarf_file_ref.data, klarf_file_after_export.data)
