import BotBooking.booking.constants as const
from selenium import webdriver
from BotBooking.booking.bookingFiltration import BookingFiltration
from bookingReport import BookingReport

class Booking(webdriver.Chrome):
    def __init__(self, teardown = False):
        self.teardown = teardown
        super(Booking, self).__init__(executable_path='F:/SeleniumDrivers/chromedriver.exe')
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.find_element_by_id("onetrust-accept-btn-handler").click()

    def changeCurrency(self, currency=None):
        self.find_element_by_css_selector("button[data-tooltip-text='Wybierz walutę']").click()
        self.find_element_by_css_selector(f"a[data-modal-header-async-url-param*='selected_currency={currency}']").click()

    def selectDestination(self, destination):
        search_field = self.find_element_by_css_selector("input[placeholder='Dokąd się wybierasz?']")
        search_field.clear()
        search_field.send_keys(destination)
        self.find_element_by_css_selector("li[data-i='0']").click()

    def selectDates(self,check_in,check_out):
        self.find_element_by_css_selector(f"td[data-date='{check_in}']").click()
        self.find_element_by_css_selector(f"td[data-date='{check_out}']").click()

    def guests(self,adult=None,children=None,amountOfRooms=None):
        self.find_element_by_id("xp__guests__toggle").click()

        while int(self.find_element_by_id('group_adults').get_attribute('value')) > 1:
            self.find_element_by_css_selector("button[aria-label='Dorośli: zmniejsz liczbę']").click()

        for i in range(adult-1):
            self.find_element_by_css_selector("button[aria-label='Dorośli: zwiększ liczbę']").click()

        for x in range(children):
            self.find_element_by_css_selector("button[aria-label='Dzieci: zwiększ liczbę']").click()

        for y in range(amountOfRooms-1):
            self.find_element_by_css_selector("button[aria-label='Pokoje: zwiększ liczbę']").click()

    def clickSearch(self):
        self.find_element_by_css_selector("button[type='submit']").click()

    def applyFiltration(self):
        filtration = BookingFiltration(driver=self)
        filtration.applyStarRating(3,4)
        filtration.lowPriceFirst()

    def reportResults(self):
        hotel_boxes=self.find_elements_by_css_selector("div[class='_fe1927d9e _0811a1b54 _a8a1be610 _022ee35ec b9c27d6646 fb3c4512b4 fc21746a73']")
        report = BookingReport(hotel_boxes)