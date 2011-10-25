import time
from selenium import webdriver
from django.test import TestCase

class GoogleMapClickTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_user_can_click_on_marker(self):
        self.driver.get('http://localhost:8000/maps/?latitude=-33.442697&longitude=-70.620312&zoom=15')

        mouse = webdriver.ActionChains(self.driver)
        google_map = self.driver.find_element_by_id('map')
        mouse.move_to_element_with_offset(google_map, 300, 275).click().perform()
        time.sleep(2)
        marker_html_container = self.driver.find_element_by_class_name('mensaje')
        
        self.assertEqual(marker_html_container.text, u'Texto ejemplo\nfoo')
        
    def tearDown(self):
        self.driver.close()
