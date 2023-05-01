import shelve
# from varname import nameof
from datetime import datetime

from definition import *

shelve_db_name = "products"

class DefaultParams:

    default_params_key_str = "default_params"

    def __init__(self):
        self.socket_len_int = self.box_80_len_int = self.box_100_len_int = self.box_140_len_int = self.other_len_int = None
        self.look_len_int = self.takeaway_len_int = None
        self.default_params_tpl = (self.socket_len_int, self.box_80_len_int, self.box_100_len_int, self.box_140_len_int,
                                   self.other_len_int, self.look_len_int, self.takeaway_len_int)

    def get_default_params_inst_func(self):
        """
        оькрывает хранилище и получает словарб с параметрами
        :return:
        """
        shelve_db = shelve.open(shelve_db_name)
        default_params_inst = shelve_db.get(self.default_params_key_str, None)
        if not default_params_inst:
            default_params_inst = self
            shelve_db[self.default_params_key_str] = self
        return default_params_inst

    def set_params_value_func(self, vars_tpl):
        """
        Присваивает значения параметрам в хранилище из соответсвующих тк-переменных
        :return:
        """
        shelve_db = shelve.open(shelve_db_name)
        for var in vars_tpl:
            attr_name = var[1].rpartition("_")[0]
            setattr(self, attr_name, var[0].get())
        shelve_db[self.default_params_key_str] = self
        shelve_db.close()

    def get_params_value(self, vars_tpl):
        for var in vars_tpl:
            attr_name = var[1].rpartition("_")[0]
            # if attr_name == "box_80_len_int":
            #     continue
            var[0].set(getattr(self, attr_name))


class Product:
    def __init__(self, date_prm=datetime.today(), name_str_prm="", cable_inst_lst_prm=[]):
        self.cable_inst_lst = cable_inst_lst_prm
        self.date = date_prm
        self.name_str = name_str_prm


class CuttingLen:
    def __init__(self, socket_len_int_prm=50, box_80_len_int_prm=200, box_100_len_int_prm=250,
                 box_140_len_int_prm=310, look_len_int_prm=50, other_len_int_prm=10):
        self.socket_len_int = socket_len_int_prm
        self.box_80_len = box_80_len_int_prm
        self.box_100_len_int = box_100_len_int_prm
        self.box_140_len_int = box_140_len_int_prm
        self.other_len_int = other_len_int_prm
        self.look_int = look_len_int_prm


class Cable:
    def __init__(self, symbol_str_prm="", percent_stock_int_prm=0,
                 cable_loads_str_tpl_prm=(), init_stock_int_prm=0, takeaway_stock_int_prm=0,
                 cutting_type_str_tpl_prm=()):
        self.symbol_str = symbol_str_prm
        self.percent_stock_int = percent_stock_int_prm
        self.init_stock_int = init_stock_int_prm
        self.cable_loads_str_tpl = cable_loads_str_tpl_prm
        self.takeaway_stock_int = takeaway_stock_int_prm
        self.cutting_type_str_tpl = cutting_type_str_tpl_prm

        self.percentage_stock_flt, self.cutting_len_int_tpl = 0, ()
        self.cable_len_flt, self.part_len_int_tpl, self.stock_flt = 0, (), 0

    def calc_cables_len(self):
        pass

        # self.pure_cable_len_flt = sum(self.part_len_int_tpl) +

    def cutting_len_func(self):
        lst= []
        for cutting_type_str in self.cutting_type_str_tpl:
            lst.append(cutting_type_str)
            self.cutting_type_str_tpl = tuple(lst)

    def cabel_len_func(self):
        return sum(self.part_len_int_tpl)


if __name__ == "__main__":
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
    # var_tpl = ((box_80_len_int_intvar, nameof(box_80_len_int_intvar)),
    #            (box_100_len_int_intvar, nameof(box_100_len_int_intvar)),
    #            (box_140_len_int_intvar, nameof(box_140_len_int_intvar)),
    #            (takeaway_len_int_intvar, nameof(takeaway_len_int_intvar)))
    var_tpl = ((box_80_len_int_intvar, "box_80_len_int_intvar"),
              (box_100_len_int_intvar, "box_100_len_int_intvar"),
              (box_140_len_int_intvar, "box_140_len_int_intvar"),
              (takeaway_len_int_intvar, "takeaway_len_int_intvar"))
    default_params_inst = DefaultParams().get_default_params_inst_func()



    default_params_inst.get_params_value(var_tpl)
    # var_tpl = tuple(var[0].get() for var in var_tpl)
    # print(var_tpl)
    # assert var_tpl == (None, None, None, None)
    box_80_len_int_intvar.set(10)
    box_100_len_int_intvar.set(20)
    box_140_len_int_intvar.set(30)
    takeaway_len_int_intvar.set(40)
    default_params_inst.set_params_value_func(var_tpl)
    default_params_inst.get_params_value(var_tpl)
    print(var_tpl)
    var_tpl = tuple(var[0].get() for var in var_tpl)

    var = var_tpl[0]
    # while 1:
    #     var = var.get()
    #     print(var)
    #     pass

    print(var_tpl)

