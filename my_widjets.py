import shelve
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askokcancel
from varname import nameof

from definition import *


class Quitter(Frame):
    """
    a Quit button that verifies exit requests;
    to reuse, attach an instance to other GUIs, and re-pack as desired
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.pack()
        widget = Button(self, text="Выход", command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Подтверждение выхода', "Выйти?")
        if ans:
            super().quit()


class ButtonOptions(Frame):
    def __init__(self, name_commands_tpl_prm, parent_prm=None, **options_prm):
        super().__init__(parent_prm, **options_prm)
        Label(self, text='Действия').pack()
        for (name, command) in name_commands_tpl_prm:
            Button(self, text=name, command=command).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)


class RadioButtonOptions(LabelFrame):
    def __init__(self, parent_prm=None, name_commands_tpl_prm=None, **options_prm):
        super().__init__(parent_prm)
        self.config(text='Опции')
        self.var = StringVar()
        for (name, command) in name_commands_tpl_prm:
            Radiobutton(self, text=name,
                        command=command,
                        variable=self.var,
                        value=name).pack(anchor=NW)
        Quitter(self).pack(side=TOP, fill=BOTH)


class StrVar(StringVar):
    def __init__(self, func_prm=str, none_value_prm=''):
        super().__init__()
        self.func = func_prm
        self.none_value = none_value_prm

    def get(self):
        # TODO: воврат при пустой строке сделать None вместо 0?
        value_str = super().get()
        if not value_str:
            return None
        return self.func(value_str)

    def set(self, value_prm):
        super().set(str(value_prm))


class InitMix:
    """
    примесный класс
    """
    def __init__(self):
        self.bread_frame= None

    @staticmethod
    def add_labels_entries_func(parent_prm, widget_data_prm, label_length_int_prm):
        """
        Создание фрейма с лейбой и полем ввода и упаковка в родительский виджет, обмен данными между Bread и фреймом
        :param parent_prm:
        :param widget_data_prm: данные конфигурации поля ввода
        :param label_length_int_prm: длина лкйбы
        :return:
        """
        for text, var, fg, state in widget_data_prm:
            frame = Frame(parent_prm)
            Label(frame, text=text, width=label_length_int_prm).pack(side=LEFT)
            en = Entry(frame, textvariable=var, foreground=fg, state=state)
            en.pack(side=RIGHT)
            frame.pack()

    def set_bread_data_func(self):
        """
        Передача данных из переменных фрейма в экземпляр bread
        :return:
        """
        name_this_func_str = "set_bread_data_func"
        for frame_attribute_name, bread_attr_name in attr_names_matching_tpl:
            try:
                value = (getattr(self, frame_attribute_name).get())
            except AttributeError:
                print(f"{self.__class__.__name__}, {name_this_func_str}: {frame_attribute_name}")
            except Exception as inst:
                print(type(inst))
                print(inst.args)
                print(inst)
                raise ValueError
            try:
                # if value:
                setattr(self.bread_frame.bread_inst, bread_attr_name, value)
            except AttributeError:
                print(f"{self.bread_frame.bread_inst.__name__}, {name_this_func_str}: {bread_attr_name}")

    def get_bread_data_func(self):
        """
        Передача данных в переменные фрейма из экземпляра bread
        """
        name_this_func_str = "get_bread_data_func"
        for frame_attribute_name, bread_attr_name in attr_names_matching_tpl:
            try:
                attr_obj = getattr(self, frame_attribute_name)
            except AttributeError:
                print(f"{self.__class__.__name__}, {name_this_func_str}: {frame_attribute_name}")
            try:
                attr_value = str(getattr(self.bread_frame.bread_inst, bread_attr_name))
            except AttributeError:
                print(f"{self.bread_frame.bread_inst.__name__}, {name_this_func_str}: {bread_attr_name}")
            attr_obj.set(attr_value)


class ParamMix:
    """
    Работа с параметрами хлеба. Подмешивается в классы, где треюуются параметры
    """
    def __init__(self):
        (self.bread_strvar, self.sourdough_strvar, self.bakery_dough_moisture_strvar,
         self.bakery_sourdough_moisture_strvar, self.salinity_strvar, self.wastage_strvar, self.shrinkage_strvar) = \
            (StrVar(func_prm=int), StrVar(int), StrVar(int), StrVar(int), StrVar(float), StrVar(float), StrVar(float))
        pass
    @property
    def key_param_tpl(self):
        """
        :return: кортеж из кортежей тк-переменная-ключ в хранидище shelve
        """
        return ((self.bread_strvar, bread_key_str),
                (self.sourdough_strvar, sourdough_key_str),
                (self.bakery_dough_moisture_strvar, bakery_dough_moisture_key_str),
                (self.bakery_sourdough_moisture_strvar, bakery_sourdough_moisturey_key_str),
                (self.salinity_strvar, salinity_key_str),
                (self.wastage_strvar, wastage_key_str),
                (self.shrinkage_strvar, shrinkage_key_str))

    def get_params_value_func(self):
        """
        ППрисваивает тк-переменным хначения из соответсвующих ключей в хранилище
        :return:
        """
        shelve_db, default_params_dct = self.get_default_params_dct_func()
        for var, key_str in self.key_param_tpl:
            try:
                var.set(default_params_dct[key_str])
                pass
            except KeyError:
                pass
        shelve_db.close()

    def set_params_value_func(self):
        """
        Присваивает значения параметрам в хранилище из соответсвующих тк-переменных
        :return:
        """
        shelve_db, default_params_dct = self.get_default_params_dct_func()
        for var, key_str in self.key_param_tpl:
            default_params_dct[key_str] = var.get()
        shelve_db[default_params_key_str] = default_params_dct
        shelve_db.close()

    @staticmethod
    def get_default_params_dct_func():
        """
        оькрывает хранилище и получает словарб с параметрами
        :return:
        """
        db = shelve.open(shelve_db_name_str)
        default_params_dct = db[default_params_key_str]
        return db, default_params_dct


class ScrolledListLabelFrame(LabelFrame):
    def __init__(self, parent_prm=None, data_tpl_prm=''):
        super().__init__(parent_prm)
        label_frame = LabelFrame(parent_prm, text="Изделия")
        scroll_bar = Scrollbar(label_frame)
        list_box = Listbox(label_frame, relief=SUNKEN)
        scroll_bar.config(command=list_box.yview)
        list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side=RIGHT, fill=Y)
        list_box.pack(side=LEFT, expand=YES, fill=BOTH)


class ProductsFrame(LabelFrame):
    def __init__(self, parent_prm, text="Изделия и кабели"):
        super().__init__(parent_prm, text=text)
        self.common_frame_1 = Frame(self)
        self.common_frame_1.pack(side=RIGHT)
        self.products_list_box = self.create_products_list_box(self.common_frame_1)
        self.products_list_box.pack()
        self.create_cables_list_box()
        self.cable_frame = self.create_cable_frame

    @staticmethod
    def create_products_list_box(parent_prm):
        label_frame = LabelFrame(parent_prm, text="Изделия")
        scroll_bar = Scrollbar(label_frame)
        list_box = Listbox(label_frame, relief=SUNKEN)
        scroll_bar.config(command=list_box.yview)
        list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side=RIGHT, fill=Y)
        list_box.pack(side=LEFT, expand=YES, fill=BOTH)
        return label_frame

    def create_cables_list_box(self):
        pass

    def create_cable_frame(self):
        pass







class BreadFrame(Frame):
    """
    Родителский фрейм для фремов расчетных данных, реальных данных, технологических данных
    """
    def __init__(self, parent_prm, bread_inst_prm=None, **config_prm):
        super().__init__(parent_prm, **config_prm)
        self.bread_inst = bread_inst_prm
        self.calc_frame = None
        self.technology_frame = None
        self.technology_frame_callback_func = None
        self.init_tech_params_frame = None

    @property
    def __frames_to_destroy(self):
        """
        При создании любого фрейма из кортежа остальные фреймы этого крртежа д. б. разрушены
        :return: кортеж фреймов
        """
        return self.calc_frame, self.technology_frame, self.init_tech_params_frame

    def init_tech_params_frame_show(self):
        """
        Указывает параметры, необходимые для создания соответствующего фрейма, и передает их в функцию создания фреймов
        :return:
        """
        obj_dct = {frame_name_key: "init_tech_params_frame", create_func_key: self.create_init_tech_params_frame,
                   }
        self.create_frame(obj_dct)

    def technology_frame_show(self):
        """
        Указывает параметры, необходимые для создания соответствующего фрейма, и передает их в функцию создания фреймов
        :return:
        """
        obj_dct = {frame_name_key: "technology_frame", create_func_key: self.create_technology_frame}
        self.create_frame(obj_dct)

    def calc_frame_show(self):
        """
        Указывает параметры, необходимые для создания соответствующего фрейма, и передает их в функцию создания фреймов
        :return:
        """
        obj_dct = {frame_name_key: "calc_frame", create_func_key: self.create_calc_frame}
        self.create_frame(obj_dct)

    def create_frame(self, obj_dct_prm):
        """
        Общая для нескольких функций. Разрушает подлежащие разрушению фреймы и вызывает соответствующую функцию
         создания соответствующего фрейма  на основании вхожящих параметров в виде словаря
        :param obj_dct_prm: словарь с параметрами фрейма
        :return:
        """
        # Разрушение открытых фреймов из списка подлежащих разрушению фремов
        for frame in self.__frames_to_destroy:
            if frame:
                frame.destroy()
        # Вызов указанной в словаре фунцкии создания фрейма
        obj_dct_prm[create_func_key]()
        # Получение объекта указанного фрема и его упаковка
        frame = getattr(self, obj_dct_prm[frame_name_key])
        frame.pack()

    def create_init_tech_params_frame(self):
        self.init_tech_params_frame = InitTechParamsFrame(self, text=init_tech_params_form_name_str)

    def create_technology_frame(self):
        self.technology_frame = TechnologyFrame(self, text=technology_form_name_str)

    def create_calc_frame(self):
        self.calc_frame = CalculatedFrame(self, text=calc_form_name_str)


class InitTechParamsFrame(LabelFrame, ParamMix):
    def __init__(self, parent_prm, text="", **config_prm):
        LabelFrame.__init__(self, parent_prm, text=text, **config_prm)
        ParamMix.__init__(self)
        self.info_label = None
        self.set_params_button = Button(self, text="Сохранить параметры", command=self.set_params_value_func)
        self.get_params_button = Button(self, text="Извлечь параметры", command=self.get_params_value_func)

        self.__create_frame_elements_func()
        self.get_params_value_func()

    def __create_frame_elements_func(self):
        Label(self).pack()

        label_var_tpl = (('Хлеб, гр', self.bread_strvar),
                           ("Закваска, гр", self.sourdough_strvar),
                           ("Пекарская Влажность теста, %", self.bakery_dough_moisture_strvar),
                           ("Пекарская влажность закваски, %", self.bakery_sourdough_moisture_strvar),
                           ("Соленость хлеба, %", self.salinity_strvar),
                           ("Потери теста при замесе, %", self.wastage_strvar),
                           ("Усушка, %", self.shrinkage_strvar))

        label_width = max((len(tuple_element[0]) for tuple_element in label_var_tpl))
        for label_name, tk_var in label_var_tpl:
            frame = Frame(self)
            frame.pack()
            Label(frame, text=label_name, width=label_width).pack(side=LEFT)
            Entry(frame, textvariable=tk_var).pack(side=RIGHT)

        Label(self).pack()
        self.get_params_button.pack(side=LEFT)
        self.set_params_button.pack(side=RIGHT)


class ScrolledText(LabelFrame):
    def __init__(self, parent=None, text='', name='', file=None, height=None, width=None):
        super().__init__(parent, text=name)
        self.text_txt = None
        self.pack(expand=YES, fill=BOTH) # сделать растягиваемым
        self.make_widgets(height, width)
        self.set(text, file)

    def make_widgets(self, height, width):
        s_bar = Scrollbar(self)
        text_txt = Text(self, relief=SUNKEN, height=height, width=width)
        s_bar.config(command=text_txt.yview) # связать sbar и text
        text_txt.config(yscrollcommand=s_bar.set) # сдвиг одного = сдвиг другого
        s_bar.pack(side=RIGHT, fill=Y) # первым добавлен - посл. обрезан
        text_txt.pack(side=LEFT, expand=YES, fill=BOTH) # Text обрезается первым
        self.text_txt = text_txt

    def set(self, text="", file=None):
        if file:
            text = open(file, 'r').read()
            self.text_txt.delete('1.0', END) # удалить текущий текст
            self.text_txt.insert('1.0', text) # добавить в стр. 1, кол. 0
            self.text_txt.mark_set(INSERT, '1.0') # установить курсор вставки
            self.text_txt.focus() # сэкономить щелчок мышью
        else:
            self.text_txt.insert('1.0', text)

    def get(self): # возвращает строку
        return self.text_txt.get('1.0', END + '-1c') # от начала до конца


class TechnologyFrame(LabelFrame, InitMix):
    # TODO: расчет параметров
    def __init__(self, parent_prm, text="", **config_prm):
        LabelFrame.__init__(self, parent_prm, text=text, **config_prm)
        InitMix.__init__(self)
        self.info_label = None
        self.bread_frame = parent_prm
        (self.flour_strvar, self.water_strvar, self.sourdough_strvar, self.salt_strvar,
         self.bakery_sourdough_moisture_strvar,
         self.forms_dough_strvar, self.bread_strvar,) = \
            (StrVar(int), StrVar(int), StrVar(int), StrVar(float), StrVar(float), StrVar(int), StrVar(int))

        self.bakery_dough_moisture_strvar, self.salinity_strvar, self.wastage_strvar, self.shrinkage_strvar = \
            StrVar(float), StrVar(float), StrVar(float), StrVar(float)
        self.total_losses_strvar, self.bread_strvar, self.bread_moisture_strvar = StrVar(float), StrVar(int), \
            StrVar(float)
        self.dough_kneading_txt = self.dough_proofing_txt = self.baking_bread_txt = None
        self.calc_button = Button(self, text="Рассчитать", command=self.calc_data)
        self.save_button = Button(self, text="Сохранить в базе", command=self.save_data)
        self.volume_increase_strvar, self.bread_volume_increase_strvar = StrVar(float), StrVar(float)

        self.bread_height_strvar = StrVar(int)
        self.final_depth_strvar = StrVar(int)
        self.init_depth_strvar = StrVar(int)

        self.__create_frame_elements()
        self.init_data()

    def init_data(self):
        self.flour_strvar.set(500)
        self.water_strvar.set(300)
        self.sourdough_strvar.set(60)
        self.bakery_sourdough_moisture_strvar.set(150)
        self.salt_strvar.set(4)
        self.forms_dough_strvar.set(835)
        self.bread_strvar.set(750)

    def calc_data(self):
        self.set_bread_data_func()
        self.bread_frame.bread_inst.calc_bread_technology_data_func()
        self.get_bread_data_func()

    def save_data(self):
        db = shelve.open(shelve_db_name_str)
        breads_dct = db.get(breads_key_str, {})
        date_str = str(self.bread_frame.bread_inst.date)
        self.calc_data()
        breads_dct[date_str] = self.bread_frame.bread_inst

    def __create_frame_elements(self):
        Label(self).pack()
        self.__create_ingredients_frame()
        Label(self).pack()
        self.__create_technology_frame()
        Label(self).pack()
        self.__create_outer_data_frame()
        self.calc_button.pack(side=LEFT)
        self.save_button.pack(side=RIGHT)

    def __create_ingredients_frame(self):
        label_frame = LabelFrame(self, text="Ингредиенты")
        label_frame.pack()
        widget_data_tpl = (("Мука, гр", self.flour_strvar, black, visible),
                           ("Вода, гр", self.water_strvar, black, visible),
                           ("Закваска, гр", self.sourdough_strvar, black, visible),
                           ("Пекарская влажность закваски, %", self.bakery_sourdough_moisture_strvar, black, visible),
                           ("Соль, гр", self.salt_strvar, black, visible),
                           ("Глубина начальная, мм", self.init_depth_strvar, black, visible))
        Label(label_frame).pack()

        label_width_int = max((len(tuple_element[0]) for tuple_element in widget_data_tpl))
        self.add_labels_entries_func(label_frame, widget_data_tpl, label_width_int)
        Label(label_frame).pack()

    def __create_technology_frame(self):
        label_frame = LabelFrame(self, text="Технология")
        label_frame.pack()
        label_var_tpl = (("Замес", nameof(self.dough_kneading_txt)),
                         ("Расстойка", nameof(self.dough_proofing_txt)),
                         ("Выпечка", nameof(self.baking_bread_txt)))
        Label(label_frame).pack()

        for label_name, var in label_var_tpl:
            widget_txt = ScrolledText(label_frame, name=label_name, width=50, height=5)
            widget_txt.pack()
            setattr(self, var, widget_txt)
        Label(label_frame).pack()

    def __create_outer_data_frame(self):
        label_frame = LabelFrame(self, text="Выходные данные")
        label_frame.pack()

        widget_data_tpl = (("Тесто в формах, гр", self.forms_dough_strvar, black, visible),
                           ('Хлеб, гр', self.bread_strvar, black, visible),
                           ("Глубина конечная, мм", self.final_depth_strvar, black, visible),
                           ("Высота готового хлеба, мм", self.bread_height_strvar, black, visible),
                           ("Коэф. увеличения объема теста", self.volume_increase_strvar, red, disable),
                           ("Коэф. увеличения объема хлеба", self.bread_volume_increase_strvar, red, disable),
                           ("Пекарская Влажность теста, %", self.bakery_dough_moisture_strvar, red, disable),
                           ("Соленость хлеба, %", self.salinity_strvar, red, disable),
                           ("Потери теста при замесе, %", self.wastage_strvar, red, disable),
                           ("Усушка, %", self.shrinkage_strvar, red, disable),
                           ("Суммарные потери, %", self.total_losses_strvar, red, disable),
                           ("Влажность хлеба, %", self.bread_moisture_strvar, red, disable))
        Label(label_frame).pack()

        label_width = max((len(tuple_element[0]) for tuple_element in widget_data_tpl))
        self.add_labels_entries_func(label_frame, widget_data_tpl, label_width)
        Label(label_frame).pack()


class CalculatedFrame(LabelFrame, InitMix, ParamMix):
    """
    Расчет данных по хлебу. Исходный параметр либо вес теста в форме либо вес готового хлеба
    """
    def __init__(self, parent_prm, text='', **config_prm):
        LabelFrame.__init__(self, parent_prm, text=text, **config_prm)
        InitMix.__init__(self)
        ParamMix.__init__(self)
        (self.flour_strvar, self.water_strvar, self.sourdough_strvar, self.salt_strvar,
         self.dough_strvar, self.forms_dough_strvar,  self.bread_strvar) = \
            (StrVar(int), StrVar(int), StrVar(int), StrVar(float),
             StrVar(int), StrVar(int), StrVar(int))
        self.bread_frame = parent_prm
        self.info_label = None

        self.calc_button = Button(self, text="Рассчитать", command=self.calc_ingredient_func)
        self.set_params_button = Button(self, text="Сохранить параметры", command=self.set_params_value_func)
        self.get_params_button = Button(self, text="Извлечь параметры", command=self.get_params_value_func)
        self.radiobutton_strvar = StrVar()
        self.__create_frame_elements()
        self.get_params_value_func()

    def __create_frame_elements(self):
        """
        Управление заполнением фрейма (self)
        :return:
        """
        radiobutton_frame = LabelFrame(self, text="Объект расчета")
        radiobutton_frame.pack()
        self.info_label = Label(self)
        self.info_label.pack()
        label_1, label_2, entry_1, entry_2 = self.__create_widgets()
        self.__create_radiobutton_frame(radiobutton_frame, label_1, label_2, entry_1, entry_2)
        self.calc_button.pack()
        self.get_params_button.pack(side=LEFT)
        self.set_params_button.pack(side=RIGHT)
        init_radiobutton_value = label_names_dict[bread_str]
        self.radiobutton_strvar.set(init_radiobutton_value)
        self.__config_label_entry(label_1, label_2, entry_1, entry_2)

    def __create_widgets(self):
        """
        Заполнение фрейма виджетами Entry с их Label
        :return:
        """
        max_text_len_int = max(len(value) for value in (label_names_dict.values()))

        # Создание первого виджета с переменными источниками данных (хлеб в форме/ готовый хлеб
        frame = Frame(self)
        label_1 = Label(frame, width=max_text_len_int)
        label_1.pack(side=LEFT)
        entry_1 = Entry(frame, state="visible", foreground="blue")
        entry_1.pack(side=RIGHT)
        frame.pack()

        # Создание виджета закваски
        frame = Frame(self)
        Label(frame, width=max_text_len_int, text=label_names_dict[sourdough_str]).pack(side=LEFT)
        Entry(frame, textvariable=self.sourdough_strvar, foreground="blue").pack(side=RIGHT)
        frame.pack()

        # создание фрейма с технологическими параметрами
        label_frame = LabelFrame(self, text="Технологические параметры")
        label_frame.pack()
        Label(label_frame).pack()
        widget_data_tpl = (
            (label_names_dict[bakery_dough_moisture_str], self.bakery_dough_moisture_strvar, black, visible),
            (label_names_dict[bakery_sourdough_moisture_str], self.bakery_sourdough_moisture_strvar, black, visible),
            (label_names_dict[salinity_str], self.salinity_strvar, black, visible),
            (label_names_dict[wastage_str], self.wastage_strvar, black, visible),
            (label_names_dict[shrinkage_str], self.shrinkage_strvar, black, visible),
            # (label_names_dict[salt_key], self.bread_frame.salt_dblvar, red, disable)
        )
        self.add_labels_entries_func(label_frame, widget_data_tpl, max_text_len_int)

        # Создание второго виджета с переменными источниками данных (хлеб в форме/ готовый хлеб
        frame = Frame(self)
        label_2 = Label(frame, width=max_text_len_int)
        label_2.pack(side=LEFT)
        entry_2 = Entry(frame, state="disable", foreground='red')
        entry_2.pack(side=RIGHT)
        frame.pack()

        Label(self).pack()  # вместо пустой строки
        # Создание виджетов с расчитанными данными
        widget_data_tpl = (
            (label_names_dict[flour_str], self.flour_strvar, red, disable),
            (label_names_dict[water_str], self.water_strvar, red, disable),
            (label_names_dict[salt_str], self.salt_strvar, red, disable))
        self.add_labels_entries_func(label_frame, widget_data_tpl, max_text_len_int)
        return label_1, label_2, entry_1, entry_2

    def __create_radiobutton_frame(self, parent_prm, label_1_prm, label_2_prm, entry_1_prm, entry_2_prm):
        """
        Создание фрейма радиокнопками для выбора теста или хлеба в качестве исходного параметра для расчета
        :param parent_prm: родительский фрейм
        :param label_1_prm:
        :param label_2_prm:
        :param entry_1_prm: Исходный параметр (хлеб или тесто в формах)
        :param entry_2_prm: Расчетный парметр (тесто в формах или хлеб)
        :return:
        """
        frame_1 = Frame(parent_prm)
        frame_1.pack(side=LEFT)
        Radiobutton(frame_1,
                    text=label_names_dict[forms_dough_str],
                    command=lambda: self.__config_label_entry(label_1_prm, label_2_prm,
                                                              entry_1_prm, entry_2_prm),
                    variable=self.radiobutton_strvar,
                    value=label_names_dict[forms_dough_str]
                    ).pack(side=LEFT)
        Radiobutton(frame_1,
                    text=label_names_dict[bread_str],
                    command=lambda: self.__config_label_entry(label_1_prm, label_2_prm,
                                                              entry_1_prm, entry_2_prm),
                    variable=self.radiobutton_strvar,
                    value=label_names_dict[bread_str]
                    ).pack(side=RIGHT)

    def __config_label_entry(self, label_1_prm, label_2_prm, entry_1_prm, entry_2_prm,):
        """
        колбэк
        меняет исходный параметр / расчетный параметр (готовый хлеб / тесто в формах) для первого и последнего виджетов
        :param radiobutton_value: значение радиокнопки
        :return:
        """
        radiobutton_value_str = self.radiobutton_strvar.get()
        if radiobutton_value_str == label_names_dict[forms_dough_str]:
            # TODO: можно упростить
            label_1_prm.config(text=label_names_dict[expected_forms_dough_str])
            entry_1_prm.config(textvariable=self.bread_frame.forms_dough_strvar)
            label_2_prm.config(text=expected_bread_str)
            entry_2_prm.config(textvariable=self.bread_frame.bread_strvar)
        elif radiobutton_value_str == label_names_dict[bread_str]:
            label_1_prm.config(text=label_names_dict[bread_str])
            entry_1_prm.config(textvariable=self.bread_strvar)
            label_2_prm.config(text=label_names_dict[forms_dough_str])
            entry_2_prm.config(textvariable=self.forms_dough_strvar)

    def calc_ingredient_func(self):
        """
        Расчет игредиентов
        :return:
        """
        bread_bln = None
        # определение главного исходного параметра (готовый хлеб или тесто в формах)
        radiobutton_value = self.radiobutton_strvar.get()
        if radiobutton_value == label_names_dict[bread_str]:
            bread_bln = True
            self.forms_dough_strvar.set('')
        elif radiobutton_value == label_names_dict[forms_dough_str]:
            bread_bln = False
            # self.bread_strvar.set(0)
        #
        # self.water_strvar.set(0)
        # self.salt_strvar.set(0)
        # Выдача визульной информации о начале расчета
        # self.root.after_idle(self.info_1_func)
        # Передача данных из виджетов (переменных) в экземпляр класса Bread
        self.set_bread_data_func()
        # Расчет и передача расчитанных данных в переменные (следовательно, в виджеты формы)
        self.bread_frame.bread_inst.calc_ingredient_func(bread_bln)
        self.get_bread_data_func()
        # Выдача визульной информации об окончании расчета
        # self.root.after(100, self.info_2_func)
        # Расчет
        # Стирание инормации о ходе расчета
        # self.root.after(400, self.info_3_func)


    def info_1_func(self):
        self.info_label.config(text='Идет расчет....', foreground="red")

    def info_2_func(self):
        self.info_label.config(text='Расчет выполнен', foreground="red")

    def info_3_func(self, n=2):
        self.info_label.config(text='')


