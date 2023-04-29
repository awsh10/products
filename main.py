from datetime import date
from tkinter import Tk, RIGHT, NW

from bread import Bread
from my_widjets import BreadFrame, RadioButtonOptions

root = Tk()
root.title("Хлеб")
today_dt = date.today()

bread_frame = BreadFrame(root)
bread_frame.pack(side=RIGHT)
bread_frame.bread_inst = Bread(today_dt)

# Данные для создания начального окна (options_inst)
name_command_tpl = (('Форма для расчета длины кабеля', bread_frame.calc_frame_show),
                    ("Технологическая форма", bread_frame.technology_frame_show),
                    ('Технологические параметры по умолчанию', bread_frame.init_tech_params_frame_show),
                    ('выполнить тест', lambda: assert_func(*main_func(dough_in_forms_int_prm=2000,
                                                                      dough_humidity_flt_prm=0.55,
                                                                      leaven_int_prm=100,
                                                                      leaven_humidity_flt_prm=1,
                                                                      salinity_flt_prm=0.005,
                                                                      wastage_flt_prm=0.02,
                                                                      shrinkage_flt_prm=0.13))))

# Запуск начального окна
options_inst = RadioButtonOptions(root, name_command_tpl)
options_inst.pack(anchor=NW)

root.mainloop()
