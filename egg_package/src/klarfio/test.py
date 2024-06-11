import klarfio




# found this function on stackoverflow I haven't checked the code but seems to work ok
# https://stackoverflow.com/a/53818532/5847976
# Code by Gabe CC BY-SA 4.0
def recursive_compare(d1, d2, level='root'):
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


print("I will do two tests : first I will load a klarf file with the lib, then export it to a new file and re-load the exported version")
print("If everything is good the data of the two loaded klarf should match perfectly")
print("After this first test I will modify the data on one klarf and check that the comparison does fail")


#klarf_file = klarf()
klarf_file_ref = klarfio.klarf("./testfile_v1.8.klarf")
klarf_file_ref.export_klarf("./test_output.klarf")
klarf_file_after_export = klarfio.klarf("./test_output.klarf")

print("Any diff ?")
assert recursive_compare(klarf_file_ref.data, klarf_file_after_export.data)


#lets try to modify one entry and see if the recursive compare catches it 
klarf_file_after_export.data["FileRecord_1.8"]["LotRecord_aLot.String"]["WaferRecord_FirstWaferId"]["DefectList"]["Data"][2][4] += 1

print("And now ?")

assert recursive_compare(klarf_file_ref.data, klarf_file_after_export.data)