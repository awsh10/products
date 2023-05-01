from datetime import date
from pytest import fixture
from cable import DefaultParams
from tkinter import *
from tkinter.ttk import *
from my_widjets import ScrolledListLabelFrame

def test_default_params():

    class Var:
        def __init__(self):
            self.value_int = None

        def set(self, value_int_prm):
            self.value_int = value_int_prm

        def get(self):
            return self.value_int

    box_140_len_int_intvar = Var()
    box_100_len_int_intvar = Var()
    box_80_len_int_intvar = Var()
    takeaway_len_int_intvar = Var()
    var_tpl = ((box_80_len_int_intvar, "box_80_len_int_intvar"),
               (box_100_len_int_intvar, "box_100_len_int_intvar"),
               (box_140_len_int_intvar, "box_140_len_int_intvar"),
               (takeaway_len_int_intvar, "takeaway_len_int_intvar"))
    default_params_inst = DefaultParams().get_default_params_inst_func()
    print()
    # print(default_params_inst.__dict__)
    default_params_inst.get_params_value(var_tpl)
    var_value_tpl = tuple(var[0].get() for var in var_tpl)
    assert var_value_tpl == (None, None, None, None)

def test_scrolled_list_label_frame():
    root = Tk()
    scrolled_frame = ScrolledListLabelFrame(root, (1, 2, 3, 4))
    scrolled_frame.pack()
    root.mainloop()