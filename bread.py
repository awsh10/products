class Bread():
    def __init__(self, date_prm, flour_int_prm=None, water_int_prm=None, sourdough_int_prm=None, salt_dbl_prm=None,
                 dough_int_prm=None, form_dough_int_prm=None,
                 expected_bread_int_prm=None, bread_int_prm=None,
                 bakery_sourdough_moisture_int_prm=None, bakery_dough_moisture_int_prm=None, salinity_flt_prm=None,
                 bread_moisture_int_prm=None,
                 wastage_flt_prm=None, shrinkage_flt_prm=None, total_losses_flt_prm=None,
                 dough_kneading_str_prm ="", dough_proofing_str_prm="", baking_bread_str_prm=""):
        self.date = date_prm
        self.flour_int = flour_int_prm
        self.water_int = water_int_prm
        self.sourdough_int = sourdough_int_prm
        self.salt_flt = salt_dbl_prm
        # self.dough_int = dough_int_prm
        self.forms_dough_int = form_dough_int_prm
        self.bread_int = bread_int_prm
        self.bakery_sourdough_moisture_int = bakery_sourdough_moisture_int_prm
        self.bakery_dough_moisture_int = bakery_dough_moisture_int_prm
        self.salinity_flt = salinity_flt_prm
        self.bread_moisture_int = bread_moisture_int_prm

        self.wastage_flt = wastage_flt_prm
        self.shrinkage_flt = shrinkage_flt_prm
        self.total_losses_flt = total_losses_flt_prm
        # self.bread_moisture_int = bread_moisture_int_prm

        self.dough_kneading_str = dough_kneading_str_prm
        self.dough_proofing_str = dough_proofing_str_prm
        self.baking_bread_str = baking_bread_str_prm

    @property
    def __sourdough_flouer_int(self):
        return self.int_round_func(self.sourdough_int / (1 + self.bakery_sourdough_moisture_int / 100))

    @property
    def __sourdough_water_int(self):
        return self.sourdough_int - self.__sourdough_flouer_int

    @property
    def __dough_int(self):
        return self.int_round_func(self.forms_dough_int / (1 - self.wastage_flt / 100))

    @property
    def dough_int(self):
        return sum((self.flour_int, self.water_int, self.sourdough_int, self.salt_flt))

    def calc_ingredient_func(self, bread_bln_prm=None):
        """
        расчет муки, воды, соли
        :param bread_bln_prm: True: расчет по готовому хлебк ,False: по тесту в формах
        :return:
        """
        if not bread_bln_prm:
            self.bread_int = self.int_round_func(self.forms_dough_int * (1 - self.shrinkage_flt / 100))
        else:
            self.forms_dough_int = self.int_round_func(self.bread_int / (1 - self.shrinkage_flt / 100))

        self.salt_flt = round((self.bread_int * (self.salinity_flt / 100) /
                               (1 - self.wastage_flt / 100)), 1)
        total_flour_int_ = self.int_round_func((self.__dough_int - self.salt_flt) / (1 + self.bakery_dough_moisture_int / 100))
        total_water_int_ = self.int_round_func((self.__dough_int - self.salt_flt) - total_flour_int_)
        self.flour_int = total_flour_int_ - self.__sourdough_flouer_int
        self.water_int = total_water_int_ - self.__sourdough_water_int
        self.form_dough_int = self.int_round_func(self.dough_int * (1 - self.wastage_flt / 100))

    @staticmethod
    def int_round_func(passed_flt):
        """
        преобразует флоат в целое
        :param passed_flt:
        :return:
        """
        return int(round(passed_flt))

    def calc_bread_technology_data_func(self):
        sourdough_flour_int = self.int_round_func(self.sourdough_int / (1 + self.bakery_sourdough_moisture_int / 100))
        sourdough_water_int = self.sourdough_int - sourdough_flour_int
        self.bakery_dough_moisture_int = self.int_round_func((self.water_int + sourdough_water_int) /
                                                             (self.flour_int + sourdough_flour_int) * 100)
        if self.forms_dough_int:
            self.wastage_flt = round((1 - self.forms_dough_int/ self.dough_int) * 100, 1)
        if self.bread_int:
            self.total_losses_flt = round((1 - self.bread_int / self.dough_int) * 100, 1)
            if self.forms_dough_int:
                self.shrinkage_flt = round((1 - self.bread_int / self.forms_dough_int) * 100, 1)
        self.salinity_flt = round(self.salt_flt / self.bread_int * 100, 1)
        self.bread_moisture_int = self.int_round_func(self.water_int * (1 - self.wastage_flt / 100) *
                                                      (1 - self.shrinkage_flt / 100) / self.bread_int * 100)




