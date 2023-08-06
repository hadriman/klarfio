#!/usr/bin/env python
# coding: utf-8

# Existing Klarf libraies are not good
# 
# I'm gonna write one myself
# 
# Note : my code is based on a single sample klarf 1.8 file
# 
# 3 main tasks : 
# 1. read klarf 
# 2. hold the klarf data in a python object that makes some sense
# 3. write klarf
# 
# klarf is essentially a json with modified syntax but I don't really want to ahve to dig into other libraries to copypaste the code. The issue being that i'll have to spend a significant amount of time understanding their code to modify it.
# Better approach is to write it all myself, the understanding part should flow from tackling the issues that pop up.
# 
# A klarf file is mostly self documenting so, for reading the thing there is very little prior knowledge to be had.
# In particular I don't need to know all the fields that will be present or their expected size.
# The only things needed are the general syntax with the spaces { } , ; characters and "Columns" and "Data" types of entries.
# 
# For writing the klarf file we need to know a little bit more but not that much either
# 
# TODO : 
# write the helper functions to better navigate the data


class klarf(object):
    def __init__(self,filename=None,populate=False):
        if (filename is None) and (populate == True):
            self.data = {"LotRecord" : 
                    {"FirstLotID" : 
                         {"WaferRecord" : 
                              {"FirstWaferID" : {
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
                                      ]

                            }
                         },
                    },
                "FileTimestamp" : ["01-01-2000", "00:00:00"],
               }
            
        elif filename is not None:
            self.data = {}
            self.parse_klarf(filename,dest_dict=self.data)
            
        else :
            self.data = {}
        return
    
    def get_defect_data(self,WaferID=None,LotID=None):
        return defects
    
    def get_defect_classes(self,LotID=None):
        return classes
    
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
