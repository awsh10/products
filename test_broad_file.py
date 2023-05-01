from datetime import date
from pytest import fixture
from cable import DefaultParams
from varname import nameof

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
    var_tpl = ((box_80_len_int_intvar, nameof(box_80_len_int_intvar)),
               (box_100_len_int_intvar, nameof(box_100_len_int_intvar)),
               (box_140_len_int_intvar, nameof(box_140_len_int_intvar)),
               (takeaway_len_int_intvar, nameof(takeaway_len_int_intvar)))
    default_params_inst = DefaultParams().get_default_params_inst_func()
    print()
    print(default_params_inst.__dict__)
    default_params_inst.get_params_value(var_tpl)
    assert var_tpl == (None, None, None, None)
