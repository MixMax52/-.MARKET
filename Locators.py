class Locators:

    """xPath clickable"""
    def __init__(self): # __init__ это конструктор класса Locators
        self.button_back = "//a[@class='back']"
        self.button_menu = "//*[@id='menu-item-175']/a" #"//li[@id='menu-item-175']"
        self.button_source = "//li//a[@href='https://svezhiy.market/cart/']"

        # Vegetables section_____________________________________________________________________
        self.section_vegetable = "//h3[text()='Овощи']"

            # Tomato
        self.subsection_veg_tomato = "//h4[text()='Помидоры']"
        self.TomatoMAHITOS = "//h4[text()='Помидоры «Махитос»']"
        self.button_add_MAHITOS = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"
        self.status_add_MAHITOS = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Pepper
        self.subsection_veg_pepper = "//h4[text()='Перец']"
        self.SpicyRedPepper = "//h4[text()='Перец острый красный']"
        self.button_add_SpicyRed = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"
        self.status_add_SpicyRed = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"

            # Beet
        self.subsection_veg_beet = "//h4[text()='Свёкла']"
        self.Beet = "//h4[text()='Свёкла молодая']"
        self.button_add_BeetYoung = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"

            # Zucchini
        self.subsection_veg_zuchini = "//h4[text()='Цукини/Кабачки']"
        self.Zucchini = "//h4[text()='Кабачки']"
        self.button_add_zucch = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Cucumber
        self.subsection_veg_cucumber = "//h4[text()='Огурцы']"
        self.Cucumber = "//h4[text()='Огурцы ТСХА (Белая дача)']"
        self.button_add_cucu = "//*[@id='shop']/div/div[2]/div[3]/div/form/button"

            # Garlic
        self.subsection_veg_garlic = "//h4[text()='Чеснок']"
        self.Garlic = "//h4[text()='Чеснок молодой']"
        self.button_add_garlic = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Radish
        self.subsection_veg_radish = "//h4[text()='Редис']"
        self.Redish = "//h4[text()='Редис']"
        self.button_add_radish = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Turnip
        self.subsection_veg_turnip = "//h4[text()='Репка']"
        self.Turnip = "//h4[text()='Репка молодая']"
        self.button_add_turnip = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Potatoes
        self.subsection_veg_potatoes = "//h4[text()='Картофель']"
        self.Potatoes = "//h4[text()='Картофель «Невский». Белый.']"
        self.button_add_pot = "//*[@id='shop']/div/div[2]/div[3]/div/form/button"

            # Broccoli
        self.subsection_veg_broccoli = "//h4[text()='Брокколи']"
        self.Broccoli = "//h4[text()='Брокколи']"
        self.button_add_broc = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Cabbage
        self.subsection_veg_cabbage = "//h4[text()='Капуста']"
        self.Cabbage = "//h4[text()='«Цветная» капуста']"
        self.button_add_cabb = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Onion
        self.subsection_veg_onion = "//h4[text()='Лук']"
        self.Onion = "//h4[text()='Лук ялтинский']"
        self.button_add_onion = "//*[@id='shop']/div/div[2]/div[4]/div/form/button"

            # Carrot
        self.subsection_veg_carrot = "//h4[text()='Морковь']"
        self.Carrot = "//h4[text()='Морковь']"
        self.button_add_carrot = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Eggplants
        self.subsection_veg_eggplants = "//h4[text()='Баклажаны']"
        self.Eggplants = "//h4[text()='Баклажаны']"
        self.button_add_eggpl = "//*[@id='shop']/div/div[2]/div/div/form/button"


        # Fruit section_____________________________________________________________________
        self.section_fruit = "//h3[text()='Фрукты']"

            # Apples
        self.subsection_fru_apple = "//div[@class='list-item__content']//h4[text()='Яблоки']"
        self.Apple = "//h4[text()='Яблоки «Карамелька»']"
        self.button_add_apple = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"

            # Tangerines
        self.subsection_fru_tangerine = "//div[@class='list-item__content']//h4[text()='Мандарины']"
        self.Tangerine =  "//h4[text()='Мандарины испанские']"
        self.button_add_tangerine = "//*[@id='shop']/div/div[2]/div[3]/div/form/button"

            # Peaches
        self.subsection_fru_peach = "//div[@class='list-item__content']//h4[text()='Персики']"
        self.Peach = "//h4[text()='Персики люкс (Армения)']"
        self.button_add_peach = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Figs
        self.subsection_fru_figs = "//div[@class='list-item__content']//h4[text()='Инжир']"
        self.Figs = "//h4[text()='Инжир. Армения']"
        self.button_add_figs = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"

            # Pears
        self.subsection_fru_pear = "//div[@class='list-item__content']//h4[text()='Груши']"
        self.Pear = "//h4[text()='Груши «Конференц»']"
        self.button_add_pear = "//*[@id='shop']/div/div[2]/div[3]/div/form/button"

            # Lemon
        self.subsection_fru_lemon = "//div[@class='list-item__content']//h4[text()='Лимон']"
        self.Lemon = "//h4[text()='Лимон']"
        self.button_add_lemon = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Nectarines
        self.subsection_fru_nectarine = "//div[@class='list-item__content']//h4[text()='Нектарины']"
        self.nectarine = "//h4[text()='Нектарины']"
        self.button_add_nectarine = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Melon
        self.subsection_fru_melon = "//div[@class='list-item__content']//h4[text()='Дыня']"
        self.melon = "//h4[text()='Дыня «Торпеда»']"
        self.button_add_melon = "//*[@id='shop']/div/div[2]/div[2]/div/form/button"

            # Bananas
        self.subsection_fru_banana = "//div[@class='list-item__content']//h4[text()='Бананы']"
        self.banana = "//h4[text()='Бананы']"
        self.button_add_banana = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Lime
        self.subsection_fru_lime = "//div[@class='list-item__content']//h4[text()='Лайм']"
        self.lime = "//h4[text()='Лайм']"
        self.button_add_lime = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Kiwi
        self.subsection_fru_kiwi = "//div[@class='list-item__content']//h4[text()='Киви']"
        self.kiwi = "//h4[text()='Киви']"
        self.button_add_kiwi = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Watermelon
        self.subsection_fru_watermelon = "//div[@class='list-item__content']//h4[text()='Арбуз']"
        self.watermelon = "//h4[text()='Арбуз']"
        self.button_add_watermelon = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Orange
        self.subsection_fru_orange = "//div[@class='list-item__content']//h4[text()='Апельсины']"
        self.orange = "//h4[text()='Апельсины']"
        self.button_add_orange = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Grapefruit
        self.subsection_fru_grapefruit = "//div[@class='list-item__content']//h4[text()='Грейпфрут']"
        self.grapefruit = "//h4[text()='Грейпфрут']"
        self.button_add_grapefruit = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Plum
        self.subsection_fru_plum = "//div[@class='list-item__content']//h4[text()='Слива']"
        self.plum = "//h4[text()='Слива «Ренклод»']"
        self.button_add_plum = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"


        # Parsley section_____________________________________________________________________
        self.section_parsley = "//h3[text()='Зелень']"

            # Salad
        self.subsection_par_salad = "//div[@class='list-item__content']//h4[text()='Салат']"
        self.Salad = "//h4[text()='Салат']"
        self.button_add_salad = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Green_onion
        self.subsection_par_GreenOnion = "//div[@class='list-item__content']//h4[text()='Лук зелёный']"
        self.GreenOnion = "//h4[text()='Лук зелёный']"
        self.button_add_GreenOnion = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Dill
        self.subsection_par_dill = "//div[@class='list-item__content']//h4[text()='Укроп']"
        self.dill = "//h4[text()='Укроп']"
        self.button_add_dill = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Basil
        self.subsection_par_basil = "//div[@class='list-item__content']//h4[text()='Базилик']"
        self.basil = "//h4[text()='Базилик']"
        self.button_add_basil = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Parsley
        self.subsection_par_parsley = "//div[@class='list-item__content']//h4[text()='Петрушка']"
        self.parsley = "//h4[text()='Петрушка']"
        self.button_add_parsley = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Mint
        self.subsection_par_mint = "//div[@class='list-item__content']//h4[text()='Мята']"
        self.Mint = "//h4[text()='Мята']"
        self.button_add_mint = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Cilantro
        self.subsection_par_cilantro = "//div[@class='list-item__content']//h4[text()='Кинза']"
        self.cilantro = "//h4[text()='Кинза']"
        self.button_add_cilantro = "//*[@id='shop']/div/div[2]/div/div/form/button"


        # Berries section_____________________________________________________________________
        self.section_berries = "//h3[text()='Ягоды']"

            # Strawberry
        self.subsection_ber_strawberry = "//div[@class='list-item__content']//h4[text()='Клубника']"
        self.Strawberry = "//h4[text()='Клубника']"
        self.button_add_strawberry = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Currant
        self.subsection_ber_currant = "//div[@class='list-item__content']//h4[text()='Смородина']"
        self.Currant = "//h4[text()='Красная смородина']"
        self.button_add_currant = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Cowberry
        self.subsection_ber_cowberry = "//div[@class='list-item__content']//h4[text()='Брусника']"
        self.Cowberry = "//h4[text()='Брусника']"
        self.button_add_cowberry = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Grape
        self.subsection_ber_grape = "//div[@class='list-item__content']//h4[text()='Виноград']"
        self.Grape = "//h4[text()='Виноград красный без косточек']"
        self.button_add_grape = "//*[@id='shop']/div/div[2]/div[5]/div/form/button"

            # Blackberry
        self.subsection_ber_blackberry = "//div[@class='list-item__content']//h4[text()='Ежевика']"
        self.Blackberry = "//h4[text()='Ежевика']"
        self.button_add_blackberry = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Cranberry
        self.subsection_ber_cranberry = "//div[@class='list-item__content']//h4[text()='Клюква']"
        self.Cranberry = "//h4[text()='Клюква']"
        self.button_add_cranberry = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Raspberry
        self.subsection_ber_Raspberry = "//div[@class='list-item__content']//h4[text()='Малина']"
        self.Raspberry = "//h4[text()='Малина']"
        self.button_add_Raspberry = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Watermelon
        self.subsection_ber_watermelon = "//div[@class='list-item__content']//h4[text()='Арбуз']"
        self.Watermelon = "//h4[text()='Арбуз']"
        self.button_add_watermelon = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Sea_buckthorn
        self.subsection_ber_SeaBuckthorn = "//div[@class='list-item__content']//h4[text()='Облепиха']"
        self.SeaBuckthorn = "//h4[text()='Облепиха']"
        self.button_add_SeaBuckthorn = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Blueberry
        self.subsection_ber_Blueberry = "//div[@class='list-item__content']//h4[text()='Голубика']"
        self.Blueberry = "//h4[text()='Голубика']"
        self.button_add_Blueberry = "//*[@id='shop']/div/div[2]/div[1]/div/form/button"

            # Hawthorn
        self.subsection_ber_Hawthorn = "//div[@class='list-item__content']//h4[text()='Боярышник']"
        self.Hawthorn = "//h4[text()='Боярышник']"
        self.button_add_Hawthorn = "//*[@id='shop']/div/div[2]/div/div/form/button"

            # Dogwood
        self.subsection_ber_Dogwood = "//div[@class='list-item__content']//h4[text()='Кизил']"
        self.Dogwood = "//h4[text()='Кизил']"
        self.button_add_Dogwood = "//*[@id='shop']/div/div[2]/div/div/form/button"



    # """XPath for find in source"""

        # Vegetables section
        self.TomatoMAHITOS = "//a[text()='Помидоры «Махитос»']"
        self.SpicyRedPepper = "//a[text()='Перец острый красный']"
        self.Beet = "//a[text()='Свёкла молодая']"
        self.Zucchini = "//a[text()='Кабачки']"
        self.Cucumber = "//a[text()='Огурцы ТСХА (Белая дача)']"
        self.Garlic = "//a[text()='Чеснок молодой']"
        self.Redish = "//a[text()='Редис']"
        self.Turnip = "//a[text()='Репка молодая']"
        self.Potatoes = "//a[text()='Картофель «Невский». Белый.']"
        self.Broccoli = "//a[text()='Брокколи']"
        self.Cabbage = "//a[text()='«Цветная» капуста']"
        self.Onion = "//a[text()='Лук ялтинский']"
        self.Carrot = "//a[text()='Морковь']"
        self.Eggplants = "//a[text()='Баклажаны']"

        # Fruit section
        self.Apple = "//a[text()='Яблоки «Карамелька»']"
        self.Tangerine = "//a[text()='Мандарины испанские']"
        self.Peach = "//a[text()='Персики люкс (Армения)']"
        self.Figs = "//a[text()='Инжир. Армения']"
        self.Pear = "//a[text()='Груши «Конференц»']"
        self.Lemon = "//a[text()='Лимон']"
        self.nectarine = "//a[text()='Нектарины']"
        self.melon ="//a[text()='Дыня «Торпеда»']"
        self.banana = "//a[text()='Бананы']"
        self.lime = "//a[text()='Лайм']"
        self.kiwi = "//a[text()='Киви']"
        self.watermelon = "//a[text()='Арбуз']"
        self.orange = "//a[text()='Апельсины']"
        self.grapefruit = "//a[text()='Грейпфрут']"
        self.plum = "//a[text()='Слива «Ренклод»']"

        # Parsley section
        self.Salad = "//a[text()='Салат']"
        self.GreenOnion = "//a[text()='Лук зелёный']"
        self.dill = "//a[text()='Укроп']"
        self.basil = "//a[text()='Базилик']"
        self.parsley = "//a[text()='Петрушка']"
        self.Mint = "//a[text()='Мята']"
        self.cilantro = "//a[text()='Кинза']"

        # Berries section
        self.Strawberry = "//a[text()='Клубника']"
        self.Cowberry = "//a[text()='Брусника']"
        self.Grape = "//a[text()='Виноград красный без косточек']"
        self.Blackberry = "//a[text()='Ежевика']"
        self.Cranberry = "//a[text()='Клюква']"
        self.Raspberry = "//a[text()='Малина']"
        self.Watermelon = "//a[text()='Арбуз']"
        self.SeaBuckthorn = "//a[text()='Облепиха']"
        self.Blueberry = "//a[text()='Голубика']"
        self.Hawthorn = "//a[text()='Боярышник']"
        self.Dogwood = "//a[text()='Кизил']"