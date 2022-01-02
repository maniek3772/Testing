#Include class with instance methods
# (after getting some results) to apply filtrations

#autocomplete methods
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def applyStarRating(self,*star_values):
        star_filtration_box = self.driver.find_element_by_xpath("//*[@id='searchboxInc']/div[1]/div/div/div[1]/div[6]")
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')

        for star_value in star_values:
            if star_value == 1:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == (f'{star_value} gwiazdka'):
                        star_element.click()

            elif star_value > 1 and star_value <= 4:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == (f'{star_value} gwiazdki'):
                        star_element.click()

            elif star_value == 5:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == (f'{star_value} gwiazdek'):
                        star_element.click()

            else:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == ('Bez kategorii'):
                        star_element.click()

    def lowPriceFirst(self):
        self.driver.find_element_by_css_selector("li[data-id='price']").click()