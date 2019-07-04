# CIF2Excel
Python script for extracting data from CIFs into an Excel file. Enables easy tabulation of data from related CIFs.

Written for python 2.7. The only external dependancy is xlsxwriter, which is available via pip.

Run Cif2Excel.py to run the program.

Use:
Use the Add CIF(s) button to add cifs to the program. They can be removed from the list by selecting and using the "remove current CIF item" button. Once the the appropriate list of CIFs has been selected (they can be dragged to re-order, which will change the order in the generated tables), click the "Generate to Excel" button to create an Excel spreadsheet with tables for general cif data, bond lengths, angles, torsion angles (all with and without uncertainties). The program can then be reset with the "Reset program" button.
