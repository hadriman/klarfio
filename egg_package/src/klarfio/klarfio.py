#!/usr/bin/env python
# coding: utf-8

# 3 main tasks : 
# 1. read klarf 
# 2. hold the klarf data in a python object that makes some sense
# 3. write klarf without losing any information
# 
# klarf v1.8 is essentially a json with modified syntax but I don't really want to ahve to dig into other libraries to copypaste the code. 
# The issue being that i'll have to spend a significant amount of time understanding their code to modify it.
# Better approach is to write it all myself, the understanding part should flow from tackling the issues that pop up.
# 
# A klarf file is mostly self documenting so, for reading the thing there is very little prior knowledge to be had.
# In particular I don't need to know all the fields that will be present or their expected size.
# The only things needed are the general syntax with the spaces { } , ; characters and "Columns" and "Data" types of entries.
# 
# For writing the klarf file we need to know a little bit more but not that much either

# klarf v1.2 files are a bit less straight forward, it's mostly a simple list of entries (no nesting, just entries terminated by ";")
# The issues with klarfs v1.2 is that the rely on new lines for the parsing and that the structure of a bunch of entries depend on the name of the entry
# This means there is a bit more "knowledge" that have to be embeded in the code

# warnings is a built-in librairy so not a real dependency
import warnings

def debug_print(*args,**kwargs):
    print(*args,**kwargs)

def klarf(filename=None,populate=False,version=None,debug=False):
        """
        This is a function to spit out objects with the proper class
        """
        if version == None:
            if filename==None:
                # If nothing is specified we'll use v1.8
                version = "1.8"
            else:
                # if we have a file we'll match the file version
                version = identify_klarf_version(filename)

        if debug : debug_print(f"{version=}")
        if version == "1.8":
            return klarf_v1_8(filename=filename,populate=populate)

        elif version == "1.2":
            return klarf_v1_2(filename=filename,populate=populate)

        else :
            raise ValueError("Invalid version. Supported klarf versions are '1.8' and '1.2'.")
   
def identify_klarf_version(filename,debug=False):
        with open(filename) as f :
            lines = f.readlines()
            for line in lines:
                if "FileRecord" in line:
                    #Record FileRecord  "1.8"
                    line = line.strip()
                    elements = line.split(" ")
                    version = elements[-1].replace('"','')
                    break

                elif "FileVersion" in line:
                    #FileVersion 1 2;
                    line = line.strip().split(";")[0]
                    elements = line.split(" ")
                    version = ".".join(elements[-2:])
                    break
            else:
                raise ValueError("Could not identify version from file.")
        
        if debug : debug_print(f"{version=}")

        return version

class klarf_v1_8(object):
    def __init__(self,filename=None,populate=False):
        self.version = "1.8"

        if (filename is None) and (populate == True):

            self.data = {'FileRecord_1.8': {
                'RecordName': '1.8',
                 "LotRecord_FirstLotID" :  {
                     'RecordName': 'FirstLotID',
                           "WaferRecord_FirstWaferID" :   {
                               'RecordName': "FirstWaferID" ,
                                "DieOrigin" : [0, 0],
                                "OrientationInstructions": [""],
                                "ProcessEquipmentState" :  ["NONE", "", "", "", "", ""],
                                "SampleCenterLocation" : [0, 0],
                                "SlotNumber" : [0],
                                "DefectList" : {
                                      "Columns" : [
                                        {"Type" : "int32",
                                        "Column" : "DEFECTID"},

                                        {"Type" : "int32",
                                        "Column" : "XREL"},

                                        {"Type" : "int32",
                                        "Column" : "YREL"},

                                        {"Type" : "int32",
                                        "Column" : "XINDEX"},

                                        {"Type" : "int32",
                                        "Column" : "YINDEX"},

                                        {"Type" : "int32",
                                        "Column" : "XSIZE"},

                                        {"Type" : "int32",
                                        "Column" : "YSIZE"},

                                        {"Type" : "float",
                                        "Column" : "DEFECTAREA"},

                                        {"Type" : "int32",
                                        "Column" : "DSIZE"},

                                        {"Type" : "int32",
                                        "Column" : "CLASSNUMBER"},

                                        {"Type" : "int32",
                                        "Column" : "TEST"},

                                        {"Type" : "int32",
                                        "Column" : "ROUGHBINNUMBER"},

                                        {"Type" : "int32",
                                        "Column" : "FINEBINNUMBER"},

                                        {"Type" : "int32",
                                        "Column" : "SAMPLEBINNUMBER"},

                                        {"Type" : "float",
                                        "Column" : "CONTRAST"},

                                        {"Type" : "int32",
                                        "Column" : "CHANNELID"},

                                        {"Type" : "int32",
                                        "Column" : "MANSEMCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "AUTOONSEMCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "MICROSIGCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "MACROSIGCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "AUTOOFFSEMCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "AUTOOFFOPTADC"},

                                        {"Type" : "int32",
                                        "Column" : "FACLASS"},

                                        {"Type" : "int32",
                                        "Column" : "INTENSITY"},

                                        {"Type" : "float",
                                        "Column" : "KILLPROB"},

                                        {"Type" : "int32",
                                        "Column" : "MACROSIGID"},

                                        {"Type" : "int32",
                                        "Column" : "REGIONID"},

                                        {"Type" : "int32",
                                        "Column" : "EVENTTYPE"},

                                        {"Type" : "int32",
                                        "Column" : "EBRLINE"},

                                        {"Type" : "int32",
                                        "Column" : "POLARITY"},

                                        {"Type" : "float",
                                        "Column" : "CRITICALAREA"},

                                        {"Type" : "int32",
                                        "Column" : "MANOPTCLASS"},

                                        {"Type" : "float",
                                        "Column" : "PHI"},

                                        {"Type" : "int32",
                                        "Column" : "DBCLASS"},

                                        {"Type" : "int32",
                                        "Column" : "DBGROUP"},

                                        {"Type" : "float",
                                        "Column" : "DBCRITICALITYINDEX"},

                                        {"Type" : "float",
                                        "Column" : "CELLSIZE"},

                                        {"Type" : "int32",
                                        "Column" : "CAREAREAGROUPCODE"},

                                        {"Type" : "float",
                                        "Column" : "PCI"},

                                        {"Type" : "float",
                                        "Column" : "LINECOMPLEXITY"},

                                        {"Type" : "float",
                                        "Column" : "DCIRANGE"},
                                      ],
                                      "Data" : [[1]+[0,]*40],
                                },
                                "TestRecord" : {
                                    "FirstTestRecordID" :  
                                      {"AreaPerTest" : [1],
                                       "SampleTestPlanList" : {
                                           "Columns" : [
                                               {"Type" : "int32",
                                                "Column" : "XINDEX"},
                                               {"Type" : "int32",
                                                "Column" : "YINDEX"}
                                                 ],
                                           "Data" : [[0,0],],
                                           },
                                      },
                                },
                                "SummaryRecord" : {
                                    "TestSummaryList"  : {
                                        "Columns" : [
                                           {"Type" : "int32",
                                            "Column" : "TESTNO"},
                                           {"Type" : "int32",
                                            "Column" : "NDEFECT"},
                                           {"Type" : "float",
                                            "Column" : "DEFDENSITY"},
                                           {"Type" : "int32",
                                            "Column" : "NDIE"},
                                           {"Type" : "int32",
                                            "Column" : "NDEFDIE"},
                                           {"Type" : "float",
                                            "Column" : "HAZEREGION"},
                                           {"Type" : "float",
                                            "Column" : "HAZEAVERAGE"},
                                           {"Type" : "float",
                                            "Column" : "HAZESTDDEV"},
                                           {"Type" : "float",
                                            "Column" : "HAZEMEDIAN"},
                                           {"Type" : "float",
                                            "Column" : "HAZEPEAK"},
                                           {"Type" : "float",
                                            "Column" : "AREAPERTEST"},
                                             ],
                                       "Data" : [[1, 4, 3.0e-308,  4,  4, 2.0e+032,  0,  2.0e-039,  2.0e-039,  2.0e-039,  2.00e+015 ],], 
                                    },
                                }, 
                               },
                            
                          "DeviceID" : ["aDevice"],
                          "DiePitch" : [1, 1],
                          "InspectionStationID"  : ["NONE", "A", "B"],
                          "OrientationMarkLocation" : [0],
                          "RecipeID" : ["ARecipe", "01-01-2000", "00:00:00"],
                          "RecipeVersion"  : ["", "NONE", ""],
                          "ResultTimestamp" : ["01-01-2000", "00:00:00"],
                          "SampleOrientationMarkType" : ["NOTCH"],
                          "SampleSize": [1, 1],
                          "SampleType" : ["WAFER"],
                          "StepID" :  ["AStepId"],
                          "ClassLookupList" : 
                            {"Columns" : [{"Type" : "int32",
                                          "Column" : "CLASSNUMBER"},
                                          {"Type" : "string",
                                          "Column" : "CLASSNAME"},
                                          {"Type" : "string",
                                          "Column" : "CLASSCODE"},
                                         ],
                             "Data" : [
                                [0,"Unclassified",""],
                                      ],

                            },  
                        },
                "FileTimestamp" : ["01-01-2000", "00:00:00"],                         
                },
               }
            
        elif filename is not None:
            self.data = {}

            self.parse_klarf(filename,dest_dict=self.data)
            
        else :
            self.data = {}
        return
    
    def get_defect_data(self,WaferID=None,LotID=None):
        if LotID == None:
            LotID = self.get_LotIDs()[0]
        if WaferID == None:
            WaferID = self.get_WaferIDs(self,LotID=LotID)[0]

        return self.data['FileRecord_1.8'][f'LotRecord_{LotID}'][f'WaferRecord_{WaferID}']['DefectList']
    
    def get_defect_classes(self,LotID=None):
        if LotID == None:
            LotID = self.get_LotIDs()[0]
        return self.data['FileRecord_1.8'][f'LotRecord_{LotID}']['ClassLookupList']

    def get_LotIDs(self):
        keys = self.data['FileRecord_1.8'].keys()
        LotIDs = [key for key in keys if key.starswith("LotRecord")]
        LotIDs = [key.split("LotRecord_")[-1] for key in LotIDs]
        return LotIDs
    
    def get_WaferIDs(self,LotID=None):
        keys = self.data['FileRecord_1.8'][f'LotRecord_{LotID}'].keys()
        WaferIDs = [key for key in keys if key.starswith("WaferRecord")]
        WaferIDs = [key.split("WaferRecord_")[-1] for key in WaferIDs]
        return WaferIDs    
    
    # the following functions are the ones for the parsing
    def select_wafer(self,WaferID=None,LotID=None):
        """
        set the current wafer to read and write the data to the ID specified
        if LotID == None the first wafer with the given id will be selected
        if no wafer with that ID was found raise an error
        """
        return None
    
    def seek_matching_brace(self,file_content,start=0):
        """find the bracket that matches the first one open before the seek position"""
        i = start-1
        #print(file_content[i+1])

        count = 0
        while count>=0:
            i+=1

            if file_content[i] == "{":
                count +=1
            elif file_content[i] == "}":
                count -=1
        return i

    def seek_next_caracter(self,file_content,caracter,start=0):
        i = start-1
        while file_content[i] != caracter:
            i+=1

        return i

    def parse_level(self,file_content, level_start, level_stop, dest_dict,debug=False):

        if debug:
            print()
            print("Current level : ")
            print(file_content[level_start:level_stop])

        if file_content[level_start:level_stop].strip() == "":
            # If we just have an empty string to parse it means this level is done
            return 
        if file_content[level_start:level_stop].strip() == "EndOfFile;":
            # If what's left is the EoF then we're done with the entire processing
            return

        head_stop = self.seek_next_caracter(file_content,caracter="{",start=level_start)
        next_level_stop = self.seek_matching_brace(file_content,start=head_stop+1)

        entry  = file_content[level_start:head_stop].strip()

        parts = entry.split(" ")
        if len(parts) == 3:
            entry_type,entry_name,entry_value = parts
        elif len(parts) == 2:
            entry_type,entry_name = parts

        else : 
            print(f"Got these parts that I couldn't parse : {parts}")
            raise Exception

        #print(parts)
        #print(entry_type)
        if entry_type in ["Columns"]:
            #print(head_stop+1)
            #print(next_level_stop+1)
            columns_text = file_content[head_stop+1:next_level_stop]
            #print(columns_text)
            column_lines = columns_text.split(",")
            column_list = []
            for column_line in column_lines:
                column_type, column_name = column_line.strip().split(" ")
                column_list.append({"Type" : column_type,
                                   "Column" : column_name})

            dest_dict["Columns"] = column_list 

        elif entry_type in ["Data"]:
            #print(head_stop+1)
            #print(next_level_stop+1)
            data_text = file_content[head_stop+1:next_level_stop]
            #print(data_text)
            data_lines = data_text.split(";")
            data_list = []
            for data_line in data_lines:
                if data_line.strip() == "":
                    continue
                values = data_line.strip().split(" ")
                values = [eval(value) for value in values]
                data_list.append(values)

            dest_dict["Data"] = data_list

        elif entry_type in ["Field"]:
            #values_end = seek_matching_brace(file_content,start=head_stop+1)
            values_text = file_content[head_stop+1:next_level_stop]
            values = [eval(value.strip()) for value in values_text.split(",")]
            dest_dict[entry_name] = values

        elif entry_type in ["Record"] :
            if len(parts) == 3:
                entry_value = entry_value.replace('"','')
                dest_dict[f"{entry_name}_{entry_value}"] = {"RecordName" : entry_value}
                self.parse_level(file_content, head_stop+2, next_level_stop, dest_dict[f"{entry_name}_{entry_value}"])

            else:
                dest_dict[entry_name] = {}
                self.parse_level(file_content, head_stop+2, next_level_stop, dest_dict[entry_name])

                #sub_level_stop = 

        else : 
            dest_dict[entry_name] = {}
            #sub_level_stop = 
            self.parse_level(file_content, head_stop+2, next_level_stop, dest_dict[entry_name])

        try:
            #once we have processed all the sublevels we can move on to the next entry in our level
            self.parse_level(file_content, level_start=next_level_stop+1, level_stop=level_stop, dest_dict=dest_dict)
        except Exception as e:
            print(f"level_start={next_level_stop+1}, level_stop={level_stop}")
            print(file_content[next_level_stop+1: level_stop])
            print()
            raise e

        # there should be nothing returned, each level inserts its info recursiveley into the main klarf.data dictionnary
        return

    def parse_klarf(self,file,dest_dict):
        """
        This parse funciton will be recursive
        The main logic will be inside the parse_level function
        """
        with open(file,"r") as f:
            file_content = f.read()

        #remove newlines, there are usefull for parsing visually but I don't think they're needed for the parsing
        file_content = file_content.replace("\n","")

        # collapse duplicate space
        # initialy I used this : re.sub(' +', ' ', file_content)
        # but to remove the dependency I'll do it like that :  (I think it should fairly fast as n iterations will remove up to 2**n spaces) 
        l = len(file_content)
        while True:
            l = len(file_content)
            file_content = file_content.replace("  "," ")
            if len(file_content) == l:
                break

        end = len(file_content)
        start = 0
        self.parse_level(file_content, level_start=0, level_stop=end, dest_dict=dest_dict)

        return
    
    # the following functions are the ones for the export
    def recurse_and_export(self,sub_dict,output_file):
        for key,val in sub_dict.items():
            #print(key)
            
            if "Record" in key:
                if "RecordName" in key:
                    # RecordName is a special field I added to keep track of the name of these
                    continue
                    
                # for the record I added the record name at the end of the key to 
                # distinguish between the several possible entries
                # so I have to remove them now from the key
                # this line will also work for the Records that did not have record names
                key = key.split("_")[0]
                #print("Field")
                if 'RecordName' in val.keys():
                    record_name = val['RecordName']
                    s = f"Record {key} {repr(record_name)} \n{{\n"
                else : 
                    s = f"Record {key} \n{{\n"

                s = s.replace("'",'"')
                output_file.write(s)
                self.recurse_and_export(val,output_file)
                output_file.write(f"}}\n")
                continue
               
            elif "Columns" in key:
                column_text = [f"{col['Type']} {col['Column']}, " for col in val]
                # There should be no coma after the last entry 
                column_text[-1] = column_text[-1].replace(",","")
                #add line break to make file more readable
                for i in range(len(column_text)):
                    if i%5 == 4:
                        column_text[i] = column_text[i].replace(",",",\n")
                output_file.write(f"Columns {len(val)} {{ {''.join(column_text)} }}\n")
                continue

            elif "Data" in key:
                #print("Data")
                #print(val)
                datalines = []
                for dataline in val:
                    datalines.append(" ".join([f"{repr(value)}" for value in dataline]))
                #print(datalines)
                datatext = ' ;\n'.join(datalines)
                datatext =  datatext.replace("'",'"')
                output_file.write(f"Data {len(val)}\n{{\n{datatext} ;\n }}\n")
                continue
                
            elif "List" in key :
                #print("List")
                output_file.write(f"List {key}\n{{\n")
                #print(val.keys())
                self.recurse_and_export(val,output_file)
                output_file.write(f"}}\n")
                continue
                
            else :
                #print("Field")
                s = f"Field {key} {len(val)} {{{val}}} \n"
                s = s.replace("[","")
                s = s.replace("]","")
                s = s.replace("'",'"')
                #print(s)
                output_file.write(s)   
            #if type(val) == type(dict()):
            #    self.recurse_and_export(val,output_file)

        return

    def export_klarf(self,dest_file):
        """
        we have to recursively go through the dictionnary and write the things piece by piece
        If there is List in the entryname -> it's a List
        If Record -> Record
        else it's a Field 
        """
        
        with open(dest_file,"w") as f:
            self.recurse_and_export(self.data,f)
            f.write("EndOfFile;")
            
        
        with open(dest_file,"r") as f:
            lines = f.readlines()
            
        indent = "  "
        indent_level = 0
        indentent_lines = []
        for line in lines:
            indentent_lines.append(indent*indent_level+line)
            indent_level += (line.count("{") - line.count("}"))

        
        with open(dest_file,"w") as f:
            lines = f.writelines(indentent_lines)
        return

class klarf_v1_2(object):
    def __init__(self,filename=None,populate=False):
        self.version = "1.2"

        if (filename is None) and (populate == True):
            self.data = {'FileRecord_1.2' : {
                'FileVersion': [1, 2],
                'FileTimeStamp': ["01-01-2000", "00:00:00"],
                'InspectionStationID': [""],
                'SampleType': [""],
                'ResultTimestamp': ["01-01-2000", "00:00:00"],
                'LotID': ['', ''],
                'SampleSize': [0, 0],
                'DeviceID': [''],
                'SetupID': [''],
                'StepID': [''],
                'SampleOrientationMarkType': [''],
                'OrientationMarkLocation': [''],
                'DiePitch': [1.0, 1.0],
                'DieOrigin': [0.0, 0.0],
                'WaferID': ['', 0],
                'Slot': [0],
                'SampleCenterLocation': [1.0, 1.0],
                'OrientationInstructions': [''],
                'CoordinatesMirrored': [''],
                'CoordinatesCentered': [''],
                'InspectionOrientation': [''],
                'InspectionTest': [1],
                'SampleTestPlan': [0, '\n', 0, 0],
                'AreaPerTest': [1.0],
                'ClusterClassificationOnelineList': [0, 0, 0],
                'DefectList': {'Columns': [{'Type': 'int32', 'Column': 'DEFECTID'},
                {'Type': 'float', 'Column': 'XREL'},
                {'Type': 'float', 'Column': 'YREL'},
                {'Type': 'int32', 'Column': 'XINDEX'},
                {'Type': 'int32', 'Column': 'YINDEX'},
                {'Type': 'float', 'Column': 'XSIZE'},
                {'Type': 'float', 'Column': 'YSIZE'},
                {'Type': 'float', 'Column': 'DEFECTAREA'},
                {'Type': 'float', 'Column': 'DSIZE'},
                {'Type': 'int32', 'Column': 'CLASSNUMBER'},
                {'Type': 'int32', 'Column': 'TEST'},
                {'Type': 'int32', 'Column': 'CLUSTERNUMBER'},
                {'Type': 'int32', 'Column': 'ROUGHBINNUMBER'},
                {'Type': 'int32', 'Column': 'FINEBINNUMBER'},
                {'Type': 'int32', 'Column': 'REVIEWSAMPLE'},
                {'Type': 'int32', 'Column': 'IMAGECOUNT'},
                {'Type': 'str', 'Column': 'IMAGELIST'}],
                'Data': []},
                'ProcessEquipmentIDOnelineList': [1, ''],
                'SummarySpec': [6, '\n',  '',  '',  '',  '',  ''],
                'SummaryShortList': [0, 0, 1.0, 0, 0],
                'FileTimestamp': ["01-01-2000", "00:00:00"],
                'TiffSpec': ['', '', ''],
                'ResultsID': ['', ''],
                'ProcessEquipmentIDShortList': ['']}
            }

            
        elif filename is not None:
            self.data = { "FileRecord_1.2": {}}

            self.parse_klarf(filename,dest_dict=self.data["FileRecord_1.2"])
            
        else :
            #Record FileRecord  "1.8"
            #FileVersion 1 2;
            self.data = { 'FileRecord_1.2': {}}
        return
    
    def get_defect_data(self,WaferID=None,LotID=None):
        return self.data['FileRecord_1.2']['DefectList']
    
    def get_defect_classes(self,LotID=None):
        # not present in my klarf v1.2 file so I don't know what it's supposed to look like
        return None
    
    # the following functions are the ones for the parsing
    
    def seek_end_of_entry(self,file_content,start=0,end_caracter=";"):
        """find the end caracter that signifies the end of the entry"""
        end_of_entry = file_content[start:].find(end_caracter)
        if end_of_entry == -1:
            raise ValueError("No termination caracter found")
        
        return end_of_entry

    def seek_next_caracter(self,file_content,caracter,start=0):
        i = start-1
        while file_content[i] != caracter:
            i+=1

        return i

    def parse_entry(self,entry,dest_dict,debug=False):
        #if debug : debug_print(f"{entry=}")
        if debug : 
            if "List" in entry : debug_print(f"{entry=}")
        lines = entry.split('\n')

        if len(lines) == 1:
            line = lines[0].strip()
            entry_name,*elements = line.split(" ")

            if entry_name == "EndOfFile":
                return 
            elif entry_name == "":
                return 
            
            elif entry_name == "TiffSpec":
                dest_dict[entry_name] = []
                for value in elements:
                    #data_type,casted_value = self.get_value_type(value)
                    dest_dict[entry_name].append(value)

            elif entry_name.endswith('Spec') :
                if entry_name == "DefectRecordSpec":
                    entry_name = "DefectSpec"
                entry_name = entry_name.replace("Spec","List")
                columns = [{"Type": "object", "Column": column_name} for column_name in elements[1:]]
                dest_dict[entry_name] = {"Columns": columns,
                                         "Data" : [],
                                         }
            elif entry_name.endswith('List') :
                entry_name = entry_name.replace('List','OnelineList')
                dest_dict[entry_name] = []
                for value in elements:
                    data_type,casted_value = self.get_value_type(value)
                    dest_dict[entry_name].append(casted_value)

            else :
                dest_dict[entry_name] = []
                for value in elements:
                    data_type,casted_value = self.get_value_type(value)
                    dest_dict[entry_name].append(casted_value)

        else:
            line = lines[0].strip()
            entry_name,*elements = line.split(" ")
            if len(lines)>2 and entry_name.endswith('List'):
                table = [line.strip().split(" ") for line in lines[1:]]
                if debug : debug_print(f"{dest_dict[entry_name]['Columns']=}")
                for row in table:
                    if debug : debug_print(f"{row=}")
                    dest_dict[entry_name]["Data"].append([])

                    for column_number,value in enumerate(row):
                        if column_number >= len(dest_dict[entry_name]["Columns"]):
                            # if we have more columns than expetected it means that the
                            # last columns are to be interpreted as a list
                            # I'll just make a string with the all the values and stuff it in the last column
                            # this will be the best to avoid confusing Pandas if I want to do further processing
                            value = " ".join(row[column_number-1:])
                            data_type,casted_value = self.get_value_type(value)
                            dest_dict[entry_name]["Columns"][column_number-1]["Type"] = data_type
                            # we replace the last value with the sequence
                            dest_dict[entry_name]["Data"][-1][-1]  = casted_value
                            break

                        data_type,casted_value = self.get_value_type(value)
                        dest_dict[entry_name]["Columns"][column_number]["Type"] = data_type
                        dest_dict[entry_name]["Data"][-1].append(casted_value)
        
            elif entry_name.endswith('List') and (len(lines) == 2):
                entry_name = entry_name.replace('List','ShortList')
                row = lines[1].strip().split(" ")
                dest_dict[entry_name] = []
                for column_number,value in enumerate(row):
                    data_type,casted_value = self.get_value_type(value)
                    dest_dict[entry_name].append(casted_value)

            elif len(lines) == 2 :
                """
                SampleTestPlan 1
                 0 0;
                """
                entry_name,n_mistery = lines[0].strip().split(" ")
                elements = lines[1].strip().split(" ")

                elements = [n_mistery,"\n"] + elements

                dest_dict[entry_name] = []
                for value in elements:
                    data_type,casted_value = self.get_value_type(value)
                    dest_dict[entry_name].append(casted_value)

        return
    
    def get_value_type(self,value,debug=False):
        if debug : debug_print(f"{value=}")
        if value.isdigit():
            return 'int32',int(value)
        try:
            float_value = float(value)
            return 'float',float_value
        except ValueError:
            return 'str',value
    
    def parse_klarf(self,file,dest_dict):
        """
        This parse funciton will be recursive
        The main logic will be inside the parse_level function
        """
        with open(file,"r") as f:
            file_content = f.read()

        #newlines are critical for parsing v1.2

        # collapse duplicate space
        # initialy I used this : re.sub(' +', ' ', file_content)
        # but to remove the dependency I'll do it like that :  (I think it should be fairly fast as n iterations will remove up to 2**n spaces) 
        l = len(file_content)
        while True:
            l = len(file_content)
            file_content = file_content.replace("  "," ")
            if len(file_content) == l:
                break

        end = len(file_content)
        start = 0
        #klarf v1.2 is structured as a sequence of entries separated by ";"
        # entries can span several lines
        # sometimes newlines are relevant other times not, seems arbitray for each tag (I've seen inconsistent behaviour for different "...List")
        entries = file_content.split(";")
        for entry in entries:
            entry = entry.strip()
            self.parse_entry(entry,dest_dict)

        return
    
    # the following functions are the ones for the export
    def format_and_export(self,data_dict,output_file):
        """
        klarf v1.2 are 'flat', ie there is a single level and all entries are layed out sequentially with ';' at the end of each entry 
        """
        try:
            data_dict = data_dict['FileRecord_1.2']
        except KeyError:
            raise KeyError("Dictionnary doesn't contain v1.2 klarf data")

        for key,val in data_dict.items():  
            if key.endswith("OnelineList"):
                key = key.replace("OnelineList","List")

                s = f"{key} {' '.join([self.format_value(_) for _ in val])};\n"
                output_file.write(s)

        
                continue
          
            elif key.endswith("ShortList"):
                key = key.replace("ShortList","List")
                s = f"{key}\n {' '.join([self.format_value(_) for _ in val])};\n"
                
                output_file.write(s)
                continue
                                    
            elif key.endswith("List"):
                columns_info =  val["Columns"]
                rows =  val["Data"]

                if key == "DefectList":
                    key_spec = "DefectRecordSpec"
                else : 
                    key_spec = key.replace("List","Spec")

                s = f"{key_spec} {len(columns_info)} {' '.join([str(_['Column']) for _ in columns_info])};\n"
                output_file.write(s)

                s = f"{key} \n"
                for row in rows:
                    s += f" {' '.join([str(_) for _ in row])}\n"
                
                s +=";\n"
                output_file.write(s)
                continue

            else :
                #print("Field")
                s = f"{key} {' '.join([self.format_value(_) for _ in val])};\n"
                #s = s.replace("[","")
                #s = s.replace("]","")
                #s = s.replace("'",'"')
                #print(s)
                output_file.write(s)   


        return
    
    def format_value(self,value):
        if isinstance(value, float):
            s = f"{value:.10E}"
            mantissa,exponent = s.split("E")
            exponent_sign = exponent[0]
            expanded_exponent = f"{int(exponent[1:]):03}"
            s = mantissa+"E"+exponent_sign+expanded_exponent
            return s
        
        if isinstance(value, int):
            return   f"{value}"
        if isinstance(value, str):
            return   f"{value}"
        
    def export_klarf(self,dest_file):
        
        with open(dest_file,"w") as f:
            self.format_and_export(self.data,f)
            f.write("EndOfFile;")
            
        return