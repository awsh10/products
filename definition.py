# dough -тесто, flour - мука, sourdough - закваска, moisture - ВЛАЖНОСТЬ, salt - соль, salinity - соленость
# shrinkage - усушка, wastage - потери (теста), total_losses - суммарные потери

# Для удобства сделана замена строковых значений ключей словарей на переменные
flour_str = "flour"
water_str = "water"
sourdough_str = "sourdough"
salt_str = "salt"

dough_str = "dough"
forms_dough_str = "forms_dough"
bread_str = "bread"

bakery_dough_moisture_str = "bakery dough moisture"
expected_bread_humidity_str = "expected_bread_humidity"
bakery_sourdough_moisture_str = "bakery_sourdough_moisture"
salinity_str = "salinity"
wastage_str = "wastage"
shrinkage_str = "shrinkage"
total_losses_str = "total_losses"
bread_moisture_str = "bread_moisture"

# Обозначение имен аттрибутов классов Bread и BreadFrame. Позволяет создать общую функцию аередачи данных в Bread из
# фрейма и обратно с помощью функций getattr и setattr
flour_strvar, flour_int = "flour_strvar", "flour_int"
water_strvar, water_int = "water_strvar", "water_int"
sourdough_strvar, sourdough_int = "sourdough_strvar", "sourdough_int"
salt_strvar, salt_flt = "salt_strvar", "salt_flt"
dough_strvar, dough_int = "dough_strvar", "dough_int"
forms_dough_strvar, forms_dough_int = "forms_dough_strvar", "forms_dough_int"
bread_strvar, bread_int = "bread_strvar", "bread_int"
bakery_dough_moisture_strvar, bakery_dough_moisture_int = "bakery_dough_moisture_strvar", "bakery_dough_moisture_int"
bakery_sourdough_moisture_strvar, bakery_sourdough_moisture_int = ("bakery_sourdough_moisture_strvar",
                                                                   "bakery_sourdough_moisture_int")
salinity_strvar, salinity_flt = "salinity_strvar", "salinity_flt"
wastage_strvar, wastage_flt = "wastage_strvar", "wastage_flt"
shrinkage_strvar, shrinkage_flt = "shrinkage_strvar", "shrinkage_flt"
total_losses_strvar, total_losses_flt = "total_losses_strvar", "total_losses_flt"
bread_moisture_strvar, bread_moisture_int = "bread_moisture_strvar", "bread_moisture_int"

dough_kneading_txt, dough_kneading_str = "dough_kneading_txt", "dough_kneading_str"
dough_proofing_txt, dough_proofing_str = "dough_proofing_txt", "dough_proofing_str"
baking_bread_txt, baking_bread_str = "baking_bread_txt", "baking_bread_str"

# Кортеж параметров
param_names_tpl = (salinity_str, bakery_sourdough_moisture_str, bakery_dough_moisture_str, wastage_str, shrinkage_str,
                   bread_str, sourdough_str)

# Cловарь имен для удобства работы с лэйблами
label_names_dict = {flour_str: "Мука, гр",
                    water_str: "Вода, гр",
                    sourdough_str: "Закваска, гр",
                    salt_str: "Соль, гр",

                    dough_str: "Тесто, гр",
                    forms_dough_str: "Тесто в формах, гр",
                    bread_str: "Хлеб, гр",

                    bakery_dough_moisture_str: "Пекарская влажность теста",
                    bakery_sourdough_moisture_str: "Пекарская влажность закваски, %",
                    salinity_str: "Процент соли в готовом хлебе, %",
                    wastage_str: "Потери теста, %",
                    shrinkage_str: "Усушка, %",
                    total_losses_str: "Суммарные потери, %"}


# Соответствие  имен переменных именам аттрибутам класса bread
attr_names_matching_tpl = ((flour_strvar, flour_int),
                           (water_strvar, water_int),
                           (sourdough_strvar, sourdough_int),
                           (salt_strvar, salt_flt),
                           (forms_dough_strvar, forms_dough_int),
                           (bread_strvar, bread_int),
                           (bakery_dough_moisture_strvar, bakery_dough_moisture_int),
                           (bakery_sourdough_moisture_strvar, bakery_sourdough_moisture_int),
                           (salinity_strvar, salinity_flt),
                           (wastage_strvar, wastage_flt),
                           (shrinkage_strvar, shrinkage_flt),
                           (total_losses_strvar, total_losses_flt),
                           (bread_moisture_strvar, bread_moisture_int),
                           (dough_kneading_txt, dough_kneading_str),
                           (dough_proofing_txt, dough_proofing_str),
                           (baking_bread_txt, baking_bread_str))

# Названия форм
calc_form_name_str = "Форма для расчета"
technology_form_name_str = "Технологическая форма"
init_tech_params_form_name_str = "Установленные параметры"

# Параметры виджетов
visible, disable = 'visible', "disable"
red, blue, black = "red", "blue", "black"

# для словаря в breadFrame
frame_name_key = "frame_name_key"
create_func_key = "create_func_key"
callback_func_key = "callback_func"

# Нужны в последней ветке
shelve_db_name_str = 'bread'
breads_key_str = "breads"
default_params_key_str = "default_params"
bread_key_str = "bread"
sourdough_key_str = "sourdough"
bakery_dough_moisture_key_str = 'bakery_dough_moisture'
bakery_sourdough_moisturey_key_str = "bakery_sourdough_moisture"
salinity_key_str = "salinity"
wastage_key_str = "wastage"
shrinkage_key_str = "shrinkage"
