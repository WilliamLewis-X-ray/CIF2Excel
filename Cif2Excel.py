"""
GUI interface to Cif2Excel
"""

import Cif2Excel_gen
import CifClass
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from Tkinter import *
import os

class MainInterface(Tkinter.Frame):
    
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
        # button to add a CIF - no put a frame inside the parent frame which has this stuff
        self._current_dir = os.getcwd()
        self._top_frame = Tkinter.Frame(root)
        self._top_frame_options = {'row':0}
        self._top_frame.grid(self._top_frame_options)
        self._button_1_opt = {'padx': 5, 'pady': 5, 'row' : 0}
        self._button_1 = Tkinter.Button(self._top_frame, text = 'Add CIF(s)', command=self._addCIF)
        self._button_1.grid(**self._button_1_opt)
        # take out directory add
        # dict to hold cif objects
        self._name_to_cif_object_dict = dict()
        # add frame for list of CIFs to sit in
        self._cifs_listbox_parent = Tkinter.Frame(self._top_frame)
        # also add scrollbar
        self._cifs_scrollbar = Scrollbar(self._cifs_listbox_parent)
        self._cifs_scrollbar.pack(side=RIGHT, fill=Y)
        self._cifs_listbox = DDList(self._cifs_listbox_parent, selectmode=EXTENDED)
        self._cifs_listbox.config(width=128, height=25, yscrollcommand=self._cifs_scrollbar.set)
        self._cifs_scrollbar.config(command=self._cifs_listbox.yview)
        self._cifs_listbox.pack()
        self._cifs_listbox_parent_options = {'padx': 5, 'pady': 5, 'row' : 1}
        self._cifs_listbox_parent.grid(**self._cifs_listbox_parent_options)
        # line of explanatory text
        self._instructions = Tkinter.Label(self._top_frame, text="Cif objects can be dragged to re-order")
        self._instructions_options = {'padx': 5, 'pady': 5, 'row' : 2}
        self._instructions.grid(**self._instructions_options)
        # generate excel button
        self._button_4 = Tkinter.Button(self._top_frame, text = 'Generate to Excel', command=self._excel_generate)
        self._button_3_opt = {'padx': 5, 'pady': 5, 'row' : 3}
        self._button_4_opt = {'padx': 5, 'pady': 5, 'row' : 4}
        self._button_5_opt = {'padx': 5, 'pady': 5, 'row' : 5}
        self._button_5 = Tkinter.Button(self._top_frame, text = 'Reset Program', command=self._reset_program)
        self._button_3 = Tkinter.Button(self._top_frame, text='Remove current CIF item', command=lambda lb=self._cifs_listbox: lb.delete(ANCHOR))
        self._button_3.grid(**self._button_3_opt)
        self._button_4.grid(**self._button_4_opt)
        self._button_5.grid(**self._button_5_opt)
              
        
    def _addCIF(self):
        """
        Adds a CIF.
        """
        
        # first select a CIF
        _options = {'initialdir':self._current_dir, 
                    'parent':self._top_frame,
                    'title':'Please select CIF to open',
                    'filetypes':[('Crystallographic Information Files','.cif')]}
        _cif_file_names = tkFileDialog.askopenfilenames(**_options)
        
        _cif_file_names_list = list(self._top_frame.tk.splitlist(_cif_file_names))
        
        # change the default directory to where the CIF was
        self._current_dir = os.path.dirname(_cif_file_names_list[0])
        
        # get the CIF frames from the CIF
        
        for _item in _cif_file_names_list:
            self._get_CIF_blocks_from_CIF(_cif_filename_full=_item)
        
        return True
        
        
    def _addCIFs_from_dir(self):
        """
        Adds all the CIFs from a directory.
        Has been superseeded.
        """
        
        # first select a directory
        _options = {'initialdir':self._current_dir, 
                    'parent':self._top_frame,
                    'title':'Please select folder to open all CIFs in it'}
        _dirname = tkFileDialog.askdirectory(**_options)
        
        # change the default directory to where the directory was
        self._current_dir = os.path.dirname(_dirname)
        
        # find CIFs and get frames from them
        for _item in os.listdir(_dirname):
            if os.path.isfile(_item) and os.path.splitext(_item)[1].upper() == '.CIF':
                self._get_CIF_blocks_from_CIF(_cif_filename_full=os.path.join(_dirname, _item))
                
        return True
        
    def _get_CIF_blocks_from_CIF(self, _cif_filename_full):
        """
        Gets all the CIF blocks from a CIF (using CifClass.py).
        Adds them to the overall dictionary of CIFs.
        """
        _cif_file = CifClass.CifFileClass(_cif_filename_full)
        if _cif_file.cif_objects == []:
            self._empty_cif_error()
        else:
            # go through the cif objects
            for _cif in _cif_file.cif_objects:
                _index_name = os.path.splitext(os.path.split(_cif_filename_full)[1])[0] + '.' + _cif.cif_dict['data_'] 
                self._name_to_cif_object_dict[_index_name] = _cif
                self._cifs_listbox.insert(END, _index_name)
        return True
                                       
        
    def _empty_cif_error(self):
        tkMessageBox.showinfo("Error", "Empty CIF! Please check your file!")
        return True
        
    def _excel_generate(self):
        """
        Gives dialogue to name and locate excel file, then makes it.
        """
        # first popup dialogue to locate/create excel file
        _save_file_options = {'defaultextension':'.xlsx',
                              'filetypes':[('excel files', '.xlsx'), ('all files', '.*')],
                              'initialdir':self._current_dir,
                              'parent':self._top_frame,
                              'title':'Excel file to write'}
        _output_filename = tkFileDialog.asksaveasfilename(**_save_file_options)
        # make list of cif objects from listbox 
        _cif_names_list = list(self._cifs_listbox.get(0, END))
        _return_cif_objects_list = []
        for _item in _cif_names_list:
            _return_cif_objects_list.append(self._name_to_cif_object_dict[_item])                                          
        
        # now generate the excel file
        Cif2Excel_gen.Cif_to_Excel(cif_objects_list=_return_cif_objects_list, 
                                   excel_filename_full=_output_filename,
                                   cif_objects_names_list=_cif_names_list)
        self._reset_program()
        return True
    
    def _reset_program(self):
        """
        Resets the program - just empties the listbox
        """
        self._cifs_listbox.delete(0, END)
        return True
        
        
class DDList(Tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = Tkinter.SINGLE
        Tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None
        
    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)
        
    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i
        
        
if __name__ == '__main__':
    root = Tkinter.Tk()
    rtitle = root.title("Cif2Excel - Generates EXCEL spreadsheet from CIFs")
    rwidth = root.geometry("800x600")
    MainInterface(root).grid()
    root.mainloop()
