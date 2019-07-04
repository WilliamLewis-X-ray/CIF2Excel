"""
Module provinding a CIF class.
"""
import re
import CifClass_statics

class CifFileClass(object):
    """
    The class for a cif file.
    Has methods for:
    Making a file into a list of cif frames.
    Turning the frames into a list of CifStructureClass objects.
    Can return a list of data_ items. (i.e. names of data frames).
    Can return a list of cif objects (one for each data frame).
    """
    
    def __init__(self, _cif_filename):
        self._cif_filename = _cif_filename
        self._read_cif_file()
        self._cif_file_parse()
        self._cif_list_to_cif_objects()
        self.cif_objects = self._cif_objects
        self._return_cif_frame_data_names()
        self.data_items = self._data_items
        
    def _return_cif_frame_data_names(self):
        """
        Creates a list of data_ names for the frames from the CIF.
        Also sets this as a property
        """
        self._data_items = []
        for item in self._cif_objects:
            self._data_items.append(item.cif_dict['data_'])
        return True
        
    def _read_cif_file(self):
        """
        Reads CIF
        """
        with open(self._cif_filename, 'r') as handle:
            self._cif_as_string = handle.read()
        return True
        
    def _cif_file_parse(self):
        """
        Takes a cif as a string, pulls out any frames, then returns 
        them as a list of frames as strings.
        """
        # first get rid of comments
        self._cif_as_string = re.sub(r'^#.*\n', '', self._cif_as_string, flags=re.MULTILINE)
        # get rid of blank lines
        self._cif_as_string = re.sub(r'^[ \t]*[\n\r\f]+', '', self._cif_as_string, flags=re.MULTILINE)
        # do the stuff
        _search_expression = '(?:^data_)'
        _search_compiled = re.compile(_search_expression, flags=re.MULTILINE)
        _cif_split = _search_compiled.split(self._cif_as_string)
        self._list_of_frames = []
        for _item in _cif_split:
            if _item == 'data_' or _item == '':
                pass
            else:
                _item_fixed = 'data_' + _item
                self._list_of_frames.append(_item_fixed)
        return True
    
    def _cif_list_to_cif_objects(self):
        """
        Turns the list of cif frames into a list of 
        CifStructureClass objects.
        """
        self._cif_objects = []
        for item in self._list_of_frames:
            self._cif_objects.append(CifStructureClass(item))
        return True
        

class CifStructureClass(object):
    """
    The class for a single structure. When initialised, gets fed a single 
    cif frame (corrresponds to one structure, of perhaps many inside a cif 
    file).
    Has methods for:
    Making a dictionary of the cif (done on initialisation)
    Create lists of lists for loops as a special dict.
    Returning some stuff?
    """
    
    def __init__(self, _cif_frame):
        self._cif_frame = _cif_frame
        self._parse_cif_frame_to_dict()
        self.cif_dict = self._cif_dict        
        self._loop_parsing()
        self._loops_to_lists()
        self._loops_to_dicts()
        self._loop_dicts_to_structured_info()
                
        
    def _parse_cif_frame_to_dict(self):
        """
        Turns a CIF frame into a dictionary.
        """
        
        _search_expression = 'data_|loop_\s+(?:_[\S^_]+\s+)+|^_[\S^_]+'
        _s_compiled = re.compile(_search_expression, flags=re.MULTILINE)
        _search_match = _s_compiled.findall(self._cif_frame)
        _cif_split = _s_compiled.split(self._cif_frame)
        self._cif_dict = dict()
        n = 0
        while n < len(_search_match):
            self._cif_dict[(_search_match[n].rstrip())] = _cif_split[n+1].lstrip()
            n += 1
        return True
    
    # next need to do loop structure stuff
    # go through each loop and do some stuff
    
    def _loop_parsing(self):
        """
        General loop parsing.
        Gets loops into their own dictionary.
        """
        
        self._loops_dict = dict()
             
        # make expression for matching loops
        
        _loop_expression = 'loop_\s+(?:_[\S^_]+\s+)+'
        _l_e_compiled = re.compile(_loop_expression)
        for item in self.cif_dict.keys():
            if not _l_e_compiled.findall(item):
                pass
            else:
                self._loops_dict[item] = self.cif_dict[item]
        
        return True
    
    def _loops_to_lists(self):
        """
        Turns all the loops into lists of lists.
        Should be able to to lists of dicts at the same time.
        """
        
        # get number of items in loop header and 
        # therefore number of bits of info to pull from loop per line
        
        # expressions for matching loop headers and loop data items
        _loop_header_match = 'loop_|_[\S^_]+'
        _l_h_m_compiled = re.compile(_loop_header_match)
        _loop_data_match = """'[^']+'|"[^"]+"|;[^;]+;|\S+"""
        _l_d_m_compiled = re.compile(_loop_data_match)
        # will need to strip outer '," and ; from the data items
        self.loops_as_lists_of_lists = dict()
        self.loops_as_lists_of_dicts = dict()        
                
        for _header in self._loops_dict.keys():
            # split the header apart
            _loop_header_split = _l_h_m_compiled.findall(_header)
            # get number of items
            _loop_line_len = len(_loop_header_split[1:])
            # split the data apart
            _loop_data_split = _l_d_m_compiled.findall(self._loops_dict[_header])
            # go through and remove outer symmetric '," and ;
            for i in range(0,len(_loop_data_split)):
                if _loop_data_split[i][0] == _loop_data_split[i][-1] and _loop_data_split[i][0] == ("'" or '"' or ';'):
                    _loop_data_split[i] = _loop_data_split[i][1:-1]
            # pop off data items to make lists and dicts.
            _temp_l_of_l = []
            _temp_l_of_d = []
            while _loop_data_split != []:
                _temp_dict = dict()
                _temp_list = []
                for item in _loop_header_split[1:]:
                    _temp_item = _loop_data_split.pop(0)
                    _temp_list.append(_temp_item)
                    _temp_dict[item] = _temp_item
                _temp_l_of_l.append(_temp_list)
                _temp_l_of_d.append(_temp_dict)
            self.loops_as_lists_of_lists[_header] = _temp_l_of_l
            self.loops_as_lists_of_dicts[_header] = _temp_l_of_d
        
        return True
    
    def _loops_to_dicts(self):
        """
        Use the lists of lists and lists of dicts to make dicts of dicts and dicts of lists.
        Only do this for geometric parameters (bond lengths and angles etc).
        """
        
        # do bond lengths first
        self.bond_lengths_as_dicts = dict()
        self.bond_lengths_as_dicts_full = dict()
        try:
            _temp_item = self.loops_as_lists_of_dicts[CifClass_statics.loop_bond]
            _temp_lists = self.loops_as_lists_of_lists[CifClass_statics.loop_bond]
            for i in range(0,len(_temp_item)):
                # make key the two atom names
                _key = _temp_item[i]['_geom_bond_atom_site_label_1'] + ' ' + _temp_item[i]['_geom_bond_atom_site_label_2']
                # put symmtery in if necessary
                if _temp_item[i]['_geom_bond_site_symmetry_2'] != '.':
                    _key = _key + '_' + _temp_item[i]['_geom_bond_site_symmetry_2']
                self.bond_lengths_as_dicts[_key] = _temp_item[i]['_geom_bond_distance']
                self.bond_lengths_as_dicts_full[_key] = _temp_lists[i]
        except KeyError:
            pass
        
        # next is angles
        self.bond_angles_as_dicts = dict()
        self.bond_angles_as_dicts_full = dict()
        try:
            _temp_item = self.loops_as_lists_of_dicts[CifClass_statics.loop_angle]
            _temp_lists = self.loops_as_lists_of_lists[CifClass_statics.loop_angle]
            for i in range(0,len(_temp_item)):
                # make structured key
                if _temp_item[i]['_geom_angle_site_symmetry_1'] != '.':
                    _s1 = '_' + _temp_item[i]['_geom_angle_site_symmetry_1'] + ' '
                else:
                    _s1 = ' ' 
                if _temp_item[i]['_geom_angle_site_symmetry_3'] != '.':
                    _s3 = '_' + _temp_item[i]['_geom_angle_site_symmetry_3']
                else: 
                    _s3 = ''
                _key = _temp_item[i]['_geom_angle_atom_site_label_1'] + _s1 + _temp_item[i]['_geom_angle_atom_site_label_2'] + ' ' + _temp_item[i]['_geom_angle_atom_site_label_3'] + _s3
                self.bond_angles_as_dicts[_key] = _temp_item[i]['_geom_angle']
                self.bond_angles_as_dicts_full[_key] = _temp_lists[i]
        except KeyError:
            pass
        
        # next is torsions
        
        self.torsion_angles_as_dicts = dict()
        self.torsion_angles_as_dicts_full = dict()
        try:
            _temp_item = self.loops_as_lists_of_dicts[CifClass_statics.loop_tors]
            _temp_lists = self.loops_as_lists_of_lists[CifClass_statics.loop_tors]
            for i in range(0, len(_temp_item)):
                # make structured key
                if _temp_item[i]['_geom_torsion_site_symmetry_1'] != '.':
                    _s1 = '_' + _temp_item[i]['_geom_torsion_site_symmetry_1'] + ' '
                else:
                    _s1 = ' '
                if _temp_item[i]['_geom_torsion_site_symmetry_2'] != '.':
                    _s2 = '_' + _temp_item[i]['_geom_torsion_site_symmetry_2'] + ' '
                else:
                    _s2 = ' '
                if _temp_item[i]['_geom_torsion_site_symmetry_3'] != '.':
                    _s3 = '_' + _temp_item[i]['_geom_torsion_site_symmetry_3'] + ' '
                else:
                    _s3 = ' ' 
                if _temp_item[i]['_geom_torsion_site_symmetry_4'] != '.':
                    _s4 = '_' + _temp_item[i]['_geom_torsion_site_symmetry_4'] + ' '
                else:
                    _s4 = ''   
                _key = _temp_item[i]['_geom_torsion_atom_site_label_1'] + _s1 + _temp_item[i]['_geom_torsion_atom_site_label_2'] + _s2 + _temp_item[i]['_geom_torsion_atom_site_label_3'] + _s3 + _temp_item[i]['_geom_torsion_atom_site_label_4'] + _s4
                self.torsion_angles_as_dicts[_key] = _temp_item[i]['_geom_torsion']
                self.torsion_angles_as_dicts_full[_key] = _temp_lists[i]
        except KeyError:
            pass
        
        # hbonds? needs some thought
        return True
    
    def _loop_dicts_to_structured_info(self):
        """
        Makes new dictionaries out of the special dictionaries.
        These change the info to separate the uncertainty out of the numerical value.
        Also make dicts with no uncertainties.
        """
        
        def _change_dict(_dict):
            _return_dict = dict()
            for _key in _dict.keys():
                if _dict[_key][-1:] == ')':
                    _return_dict[_key] = _dict[_key][:-1].split('(')
                else:
                    _return_dict[_key] = [_dict[_key], '']
            return _return_dict
        def _change_dict_no_esd(_dict):
            _return_dict = dict()
            for _key in _dict.keys():
                if _dict[_key][-1:] == ')':
                    _return_dict[_key] = _dict[_key][:-1].split('(')[0]
                else:
                    _return_dict[_key] = _dict[_key]
            return _return_dict            
        self.bond_angles_as_dicts_structured = _change_dict(self.bond_angles_as_dicts)
        self.bond_lengths_as_dicts_structured = _change_dict(self.bond_lengths_as_dicts)
        self.torsion_angles_as_dicts_structured = _change_dict(self.torsion_angles_as_dicts)
        self.bond_angles_as_dicts_no_esd = _change_dict_no_esd(self.bond_angles_as_dicts)
        self.bond_lengths_as_dicts_no_esd = _change_dict_no_esd(self.bond_lengths_as_dicts)
        self.torsion_angles_as_dicts_no_esd = _change_dict_no_esd(self.torsion_angles_as_dicts)
        
        return True
    
        
                    
                
        
    
    
