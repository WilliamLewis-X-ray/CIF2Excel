"""
Module for turning a set of CIF objects (provided by the CifClass.py module) 
into an excel spreadsheet.

Static things provided by Cif2Excel_statics
"""
import Cif2Excel_statics
import xlsxwriter
import copy


class Cif_to_Excel(object):
    """
    Takes a list of CifClassStructure objects and generates an excel spreadsheet from them.
    Writes the excel file somewhere.
    """
    
    def __init__(self, cif_objects_list, 
                 excel_filename_full, cif_objects_names_list):
        
        self.excel_filename = excel_filename_full
        self._setup_spreadsheet()
        self._number_of_cifs = len(cif_objects_list)
        self._cif_objects_list = cif_objects_list
        self._cif_objects_names_list = cif_objects_names_list
        t = copy.copy(self._cif_objects_names_list)
        t.insert(0,'Parameters')
        self.spreadsheet_order = Cif2Excel_statics.spreadsheet_order
        self._titles = copy.copy(self._cif_objects_names_list)
        self._titles.insert(0, 'Parameters')
        self._data_addition()
        self._workbook.close()
        
        
    
    def _setup_spreadsheet(self):
        """
        Sets up an instance of the xlsxwriter object.
        Creates all the worksheets for it as well.
        """
        
        self._workbook = xlsxwriter.Workbook(self.excel_filename)
        self._worksheet_data = self._workbook.add_worksheet('Data')
        self._worksheet_bonds = self._workbook.add_worksheet('Bond Lengths')
        self._worksheet_bonds_esd = self._workbook.add_worksheet('Bond Lengths esd')
        self._worksheet_angles = self._workbook.add_worksheet('Bond Angles')
        self._worksheet_angles_esd = self._workbook.add_worksheet('Bond Angles esd')
        self._worksheet_torsions = self._workbook.add_worksheet('Torsion Angles')
        self._worksheet_torsions_esd = self._workbook.add_worksheet('Torsion Angles esd')
        
        return True
    
    def _excel_style(_row, _col):
        """ Convert given row and column number to an Excel-style cell name. """
        _LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        _result = []
        while _col:
            _col, _rem = divmod(_col-1, 26)
            _result[:0] = _LETTERS[rem]
        return ''.join(_result) + str(_row)     
    
    def _create_table_header(self, _worksheet):
        """
        Creates the header row for a worksheet instance.
        """
        _row_length = self._number_of_cifs # number of columns
        _worksheet.write_row(0,0, self._titles)
        
        return True
    
    def _data_addition(self):
        """
        Writes data to the spreadsheet worksheets.
        Has a refactored method.
        """
                    
        def _worksheet_data_add(self, _worksheet, _dictionary_name, _order_list=[], _exclusions=[]):
            """
            Generalise adding data to a worksheet.
            _worksheet is the worksheet
            _dictionary is a dictionary called from the CifClass
            _order_list is the list of the worksheet order
            _exclusions is any excluded datanames
            """
            for _cif in self._cif_objects_list:
                for item in getattr(_cif, _dictionary_name).keys():
                    if item in _order_list or item in _exclusions or '_vrf_' in item:
                        pass
                    else:
                        _order_list.append(item)
                
            # make the table
            # add the table header
            self._create_table_header(_worksheet)
            # write the first column
            _worksheet.write_column(1, 0, _order_list)
            # set column wdiths
            _worksheet.set_column(0, 0, 30)
            #set up the data
            _temp_list_collection = []
            for _cif in self._cif_objects_list:
                _cif_list_temp = []
                _temp_dict = getattr(_cif, _dictionary_name)
                for item in _order_list:
                    try:
                        _cif_list_temp.append(_temp_dict[item])
                    except KeyError:
                        _cif_list_temp.append('')
                _temp_list_collection.append(_cif_list_temp) 
            # write the data to the columns
            i = 1
            for _cif_list in _temp_list_collection:
                if _worksheet==self._worksheet_data:
                    _worksheet.set_column(i, i, 20)
                else:
                    _worksheet.set_column(i, i, 15)
                _worksheet.write_column(1, i, _cif_list)
                i +=1
            return True
        
        # add the data
        # general data first because special
        _worksheet_data_add(self, 
                            self._worksheet_data, 
                            'cif_dict', 
                            _order_list = self.spreadsheet_order, 
                            _exclusions = Cif2Excel_statics.exclusion_list)
        # the rest programmatically, as straighforward
        _t = [[self._worksheet_angles, 'bond_angles_as_dicts_no_esd'], 
              [self._worksheet_angles_esd, 'bond_angles_as_dicts'],
              [self._worksheet_bonds, 'bond_lengths_as_dicts_no_esd'],
              [self._worksheet_bonds_esd, 'bond_lengths_as_dicts'],
              [self._worksheet_torsions, 'torsion_angles_as_dicts_no_esd'],
              [self._worksheet_torsions_esd, 'torsion_angles_as_dicts']]
        
        for item in _t:
            _worksheet_data_add(self, item[0], item[1], _order_list = [], _exclusions = [])
        
        return True
        
    
    
