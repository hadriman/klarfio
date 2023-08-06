import klarflib

# to create an empty object
klarf_file = klarflib.klarf()

# to create an empty object with a bunch of fields pre-populated with bogus data so that you have an actual klarf structure to work with
klarf_file = klarflib.klarf(populate=True)

# this is to load klarf data from a file
klarf_file = klarflib.klarf("./testfile_base.klarf")

#this to export klarf data to a file
klarf_file.export_klarf("./test_output.klarf")