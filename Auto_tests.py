from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
from Locators import Locators
import time


class Fresh_Market(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://svezhiy.market/"
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.loc = Locators()


    def test_AddingFoodToFoodBasket(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get(self.url)

        try:# Vegetables section
            self.driver.find_element(By.XPATH, self.loc.section_vegetable).click() # Choosing vegetable section

            try: # Tomato
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_tomato).click() # Choosing tomato subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_MAHITOS).click() # Adding tomato to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click() # Back to previous page
                print("Tomato is added")
            except: print("Tomato is NOT added")

            try: # Pepper
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_pepper).click() # Choosing pepper subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_SpicyRed).click() # Adding pepper to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click() # Back to previous page
                print("Pepper is added")
            except: print("Pepper is NOT added")

            try: # Beet
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_beet).click()  # Choosing beet subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_BeetYoung).click()  # Adding beet to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Beet is added")
            except: print("Beet is NOT added")

            try: # Zucchini
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_zuchini).click()  # Choosing zucchini subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_zucch).click()  # Adding zucchini to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Zucchini is added")
            except: print("Zucchini is NOT added")

            try: # Cucumber
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_cucumber).click()  # Choosing cucumber subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_cucu).click()  # Adding cucumber to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Cucumber is added")
            except: print("Cucumber is NOT added")

            try: # Garlic
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_garlic).click()  # Choosing garlic subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_garlic).click()  # Adding garlic to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Garlic is added")
            except: print("Garlic is NOT added")

            try: # Radish
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_radish).click()  # Choosing radish subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_radish).click()  # Adding radish to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Radish is added")
            except: print("Radish is NOT added")

            try: # Turnip
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_turnip).click()  # Choosing turnip subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_turnip).click()  # Adding turnip to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Turnip is added")
            except: print("Turnip is NOT added")

            try: # Potatoes
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_potatoes).click()  # Choosing potatoes subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_pot).click()  # Adding potatoes to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Potatoes is added")
            except: print("Potatoes is NOT added")

            try: # Broccoli
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_broccoli).click()  # Choosing broccoli subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_broc).click()  # Adding broccoli to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Broccoli is added")
            except: print("Broccoli is NOT added")

            try: # Cabbage
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_cabbage).click()  # Choosing cabbage subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_cabb).click()  # Adding cabbage to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Cabbage is added")
            except: print("Cabbage is NOT added")

            try: # Onion
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_onion).click()  # Choosing onion subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_onion).click()  # Adding onion to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Onion is added")
            except: print("Onion is NOT added")

            try: # Carrot
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_carrot).click()  # Choosing carrot subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_carrot).click()  # Adding carrot to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Carrot is added")
            except: print("Carrot is NOT added")

            try: # Eggplants
                self.driver.find_element(By.XPATH, self.loc.subsection_veg_eggplants).click()  # Choosing eggplants subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_eggpl).click()  # Adding eggplants to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Eggplants is added")
            except: print("Eggplants is NOT added")

            print("__________Vegetables section is added__________\n")
        except: print("Any food in Vegetables section is NOT added ")


        self.driver.find_element(By.XPATH, self.loc.button_menu).click() # Moved to main page

        try: # Fruit section
            self.driver.find_element(By.XPATH, self.loc.section_fruit).click()  # Choosing fruit section

            try: # Apples
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_apple).click()  # Choosing apples subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_apple).click()  # Adding apple to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Apple is added")
            except: print("Apple is NOT added")

            try: # Tangerines
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_tangerine).click()  # Choosing tangerines subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_tangerine).click()  # Adding tangerine to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Tangerine is added")
            except: print("Tangerine is NOT added")

            try: # Peaches
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_peach).click()  # Choosing peaches subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_peach).click()  # Adding peach to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Peach is added")
            except: print("Peach is NOT added")

            try: # Figs
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_figs).click()  # Choosing figs subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_figs).click()  # Adding figs to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Figs is added")
            except: print("Figs is NOT added")

            try: # Pears
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_pear).click()  # Choosing pear subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_pear).click()  # Adding pear to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Pear is added")
            except: print("Pear is NOT added")

            try: # Lemon
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_lemon).click()  # Choosing lemon subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_lemon).click()  # Adding lemon to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Lemon is added")
            except: print("Lemon is NOT added")

            try: # Nectarines
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_nectarine).click()  # Choosing nectarines subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_nectarine).click()  # Adding nectarine to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Nectarine is added")
            except: print("Nectarine is NOT added")

            try: # Melon
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_melon).click()  # Choosing melon subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_melon).click()  # Adding melon to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Melon is added")
            except: print("Melon is NOT added")

            try: # Bananas
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_banana).click()  # Choosing bananas subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_banana).click()  # Adding banana to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Banana is added")
            except: print("Banana is NOT added")

            try: # Lime
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_lime).click()  # Choosing lime subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_lime).click()  # Adding lime to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Lime is added")
            except: print("Lime is NOT added")

            try: # Kiwi
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_kiwi).click()  # Choosing kiwi subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_kiwi).click()  # Adding kiwi to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Kiwi is added")
            except: print("Kiwi is NOT added")

            try: # Watermelon
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_watermelon).click()  # Choosing watermelon subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_watermelon).click()  # Adding watermelon to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Watermelon is added")
            except: print("Watermelon is NOT added")

            try: # Orange
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_orange).click()  # Choosing orange subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_orange).click()  # Adding orange to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Orange is added")
            except: print("Orange is NOT added")

            try: # Grapefruit
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_grapefruit).click()  # Choosing grapefruit subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_grapefruit).click()  # Adding grapefruit to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Grapefruit is added")
            except: print("Grapefruit is NOT added")

            try: # Plum
                self.driver.find_element(By.XPATH, self.loc.subsection_fru_plum).click()  # Choosing plum subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_plum).click()  # Adding plum to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Plum is added")
            except: print("Plum is NOT added")
            print("__________Fruit section is added__________\n")
        except: print("Any food in Fruit section is NOT added")


        self.driver.find_element(By.XPATH, self.loc.button_menu).click()  # Moved to main page

        try: # Parsley section
            self.driver.find_element(By.XPATH, self.loc.section_parsley).click()  # Choosing parsley section

            try: # Salad
                self.driver.find_element(By.XPATH, self.loc.subsection_par_salad).click()  # Choosing salad subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_salad).click()  # Adding salad to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Salad is added")
            except: print("Salad is NOT added")

            try: # Green_onion
                self.driver.find_element(By.XPATH, self.loc.subsection_par_GreenOnion).click()  # Choosing green onion subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_GreenOnion).click()  # Adding green onion to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Green onion is added")
            except: print("Green onion is NOT added")

            try: # Dill
                self.driver.find_element(By.XPATH, self.loc.subsection_par_dill).click()  # Choosing dill subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_dill).click()  # Adding dill to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Dill is added")
            except: print("Dill is NOT added")

            try: # Basil
                self.driver.find_element(By.XPATH, self.loc.subsection_par_basil).click()  # Choosing basil subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_basil).click()  # Adding basil to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Basil is added")
            except: print("Basil is NOT added")

            try: # Parsley
                self.driver.find_element(By.XPATH, self.loc.subsection_par_parsley).click()  # Choosing parsley subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_parsley).click()  # Adding parsley to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Parsley is added")
            except: print("Parsley is NOT added")

            try: # Mint
                self.driver.find_element(By.XPATH, self.loc.subsection_par_mint).click()  # Choosing mint subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_mint).click()  # Adding mint to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Mint is added")
            except: print("Mint is NOT added")

            try: # Cilantro
                self.driver.find_element(By.XPATH, self.loc.subsection_par_cilantro).click()  # Choosing cilantro subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_cilantro).click()  # Adding cilantro to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Cilantro is added")
            except: print("Cilantro is NOT added")
            print("__________Parsley section is added__________\n")
        except: print("Any food in Parsley section is NOT added")


        self.driver.find_element(By.XPATH, self.loc.button_menu).click()  # Moved to main page

        try: # Berries section
            self.driver.find_element(By.XPATH, self.loc.section_berries).click()  # Choosing berries section

            try: # Strawberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_strawberry).click()  # Choosing strawberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_strawberry).click()  # Adding strawberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Strawbery is added")
            except: print("Strawberry is NOT added")

            try: # Currant
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_currant).click()  # Choosing currant subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_currant).click()  # Adding currant to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Currant is added")
            except: print("Currant is NOT added")

            try: # Cowberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_cowberry).click()  # Choosing cowberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_cowberry).click()  # Adding cowberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Cowberry is added")
            except: print("Cowberry is NOT added")

            try: # Grape
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_grape).click()  # Choosing grape subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_grape).click()  # Adding grape to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Grape is added")
            except: print("Grape is NOT added")

            try: # Blackberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_blackberry).click()  # Choosing blackberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_blackberry).click()  # Adding blackberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Blackberry is added")
            except: print("Blackberry is NOT added")

            try: # Cranberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_cranberry).click()  # Choosing cranberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_cranberry).click()  # Adding cranberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Cranberry is added")
            except: print("Cranberry is NOT added")

            try: # Raspberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_Raspberry).click()  # Choosing raspberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_Raspberry).click()  # Adding raspberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Raspberry is added")
            except: print("Raspberry is NOT added")

            try: # Watermelon
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_watermelon).click()  # Choosing watermelon subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_watermelon).click()  # Adding watermelon to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Watermelon is added")
            except: print("Watermelon is NOT added")

            try: # Sea_buckthorn
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_SeaBuckthorn).click()  # Choosing sea buckthorn subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_SeaBuckthorn).click()  # Adding sea buckthorn to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Sea buckthorn is added")
            except: print("Sea buckthorn is NOT added")

            try: # Blueberry
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_Blueberry).click()  # Choosing blueberry subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_Blueberry).click()  # Adding blueberry to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Blueberry is added")
            except: print("Blueberry is NOT added")

            try: # Hawthorn
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_Hawthorn).click()  # Choosing hawthorn subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_Hawthorn).click()  # Adding hawthorn to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Hawthorn is added")
            except: print("Hawthorn is NOT added")

            try: # Dogwood
                self.driver.find_element(By.XPATH, self.loc.subsection_ber_Dogwood).click()  # Choosing dogwood subsection
                self.driver.find_element(By.XPATH, self.loc.button_add_Dogwood).click()  # Adding dogwood to basket food
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.loc.button_back).click()  # Back to previous page
                print("Dogwood is added")
            except: print("Dogwood is NOT added")
            print("__________Berrise section is added__________\n")
        except: print("Any food in Berries category is NOT added")


        self.driver.find_element(By.XPATH, self.loc.button_source).click() # Moved to basket foot
        
        try: # Checking chosen food (Vegetables section)
            self.driver.find_element(By.XPATH, self.loc.TomatoMAHITOS)
            self.driver.find_element(By.XPATH, self.loc.SpicyRedPepper)
            self.driver.find_element(By.XPATH, self.loc.Beet)
            self.driver.find_element(By.XPATH, self.loc.Zucchini)
            self.driver.find_element(By.XPATH, self.loc.Cucumber)
            self.driver.find_element(By.XPATH, self.loc.Garlic)
            self.driver.find_element(By.XPATH, self.loc.Redish)
            self.driver.find_element(By.XPATH, self.loc.Turnip)
            self.driver.find_element(By.XPATH, self.loc.Potatoes)
            self.driver.find_element(By.XPATH, self.loc.Broccoli)
            self.driver.find_element(By.XPATH, self.loc.Cabbage)
            self.driver.find_element(By.XPATH, self.loc.Onion)
            self.driver.find_element(By.XPATH, self.loc.Carrot)
            self.driver.find_element(By.XPATH, self.loc.Eggplants)
            print("__________Vegetables section to Basket_food is correct__________\n")
        except: print("Vegetables section to Basket_food is NOT correct")

        try: # Checking chosen food (Fruit section)
            self.driver.find_element(By.XPATH, self.loc.Apple)
            self.driver.find_element(By.XPATH, self.loc.Tangerine)
            self.driver.find_element(By.XPATH, self.loc.Peach)
            self.driver.find_element(By.XPATH, self.loc.Figs)
            self.driver.find_element(By.XPATH, self.loc.Pear)
            self.driver.find_element(By.XPATH, self.loc.Lemon)
            self.driver.find_element(By.XPATH, self.loc.nectarine)
            self.driver.find_element(By.XPATH, self.loc.melon)
            self.driver.find_element(By.XPATH, self.loc.banana)
            self.driver.find_element(By.XPATH, self.loc.lime)
            self.driver.find_element(By.XPATH, self.loc.kiwi)
            self.driver.find_element(By.XPATH, self.loc.watermelon)
            self.driver.find_element(By.XPATH, self.loc.orange)
            self.driver.find_element(By.XPATH, self.loc.grapefruit)
            self.driver.find_element(By.XPATH, self.loc.plum)
            print("__________Fruit section to Basket_food is correct__________\n")
        except: print("Fruit section to Basket_food is NOT correct")

        try: # Checking chosen food (Parsley section)
            self.driver.find_element(By.XPATH, self.loc.Salad)
            self.driver.find_element(By.XPATH, self.loc.GreenOnion)
            self.driver.find_element(By.XPATH, self.loc.dill)
            self.driver.find_element(By.XPATH, self.loc.basil)
            self.driver.find_element(By.XPATH, self.loc.parsley)
            self.driver.find_element(By.XPATH, self.loc.Mint)
            self.driver.find_element(By.XPATH, self.loc.cilantro)
            print("__________Parsley section to Basket_food is correct__________\n")
        except: print("Parsley section to Basket_food is NOT correct")

        try: # Checking chosen food (Berries section)
            self.driver.find_element(By.XPATH, self.loc.Strawberry)
            self.driver.find_element(By.XPATH, self.loc.Cowberry)
            self.driver.find_element(By.XPATH, self.loc.Grape)
            self.driver.find_element(By.XPATH, self.loc.Blackberry)
            self.driver.find_element(By.XPATH, self.loc.Cranberry)
            self.driver.find_element(By.XPATH, self.loc.Raspberry)
            self.driver.find_element(By.XPATH, self.loc.Watermelon)
            self.driver.find_element(By.XPATH, self.loc.SeaBuckthorn)
            self.driver.find_element(By.XPATH, self.loc.Blueberry)
            self.driver.find_element(By.XPATH, self.loc.Hawthorn)
            self.driver.find_element(By.XPATH, self.loc.Dogwood)
            print("__________Berries section to Basket_food is correct__________\n")
        except: print("Berries section to Basket_food is NOT correct")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()