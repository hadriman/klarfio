import klarfio

# to create an empty object
klarf_file = klarfio.klarf()

# to create an empty object with a bunch of fields pre-populated with bogus data so that you have an actual klarf structure to work with
klarf_file = klarfio.klarf(populate=True)

# this is to load klarf data from a file
klarf_file = klarfio.klarf("./testfile_v1.8.klarf")

# lets print some defect data contained in that klarf
columns = klarf_file.data['FileRecord_1.8']['LotRecord_aLot.String']["WaferRecord_FirstWaferId"]['DefectList']['Columns']
first_defect = klarf_file.data['FileRecord_1.8']['LotRecord_aLot.String']["WaferRecord_FirstWaferId"]['DefectList']['Data'][0]
print("Here is the data of the first defect :")
for col,value in  zip(columns,first_defect ):
    print(f'{col["Column"]} : {value}')

#this is to export klarf data to a file
klarf_file.export_klarf("./test_output_v1.8.klarf")
