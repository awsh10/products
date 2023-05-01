from datetime import date
from tkinter import Tk, RIGHT, NW

from cable import Cable
from my_widjets import BreadFrame, RadioButtonOptions, ProductsFrame

root = Tk()
root.title("Расчет длины кабеля")
today_dt = date.today()

products_frame = ProductsFrame(root)
products_frame.pack(side=RIGHT)
name_command_tpl =( #(('Форма для расчета длины кабеля', products_frame.create_products_list_box()),
                    # ("Технологическая форма", bread_frame.technology_frame_show),
                    # ('Пfраметры по умолчанию', bread_frame.init_tech_params_frame_show),
                    # ('выполнить тест', lambda: assert_func(*main_func(dough_in_forms_int_prm=2000,
                    #                                                   dough_humidity_flt_prm=0.55,
                    #                                                   leaven_int_prm=100,
                    #                                                   leaven_humidity_flt_prm=1,
                    #                                                   salinity_flt_prm=0.005,
                    #                                                   wastage_flt_prm=0.02,
                    #                                                   shrinkage_flt_prm=0.13)))
)

options_frame = RadioButtonOptions(root, name_command_tpl)
options_frame.pack(anchor=NW)
'''
bread_frame = BreadFrame(root)
bread_frame.pack(side=RIGHT)
bread_frame.bread_inst = Cable(today_dt)

# Данные для создания начального окна (options_inst)

# Запуск начального окна
options_inst = RadioButtonOptions(root, name_command_tpl)
options_inst.pack(anchor=NW)
'''
root.mainloop()
