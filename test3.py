import os
import unittest
from appium import webdriver
from time import sleep


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class AppInstallation(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='7.0'
        desired_caps['deviceName']='Gigaset GS170'
        desired_caps['app']= PATH('C:\Androidtesty\ContactManager.apk')
        desired_caps['appPackage'] ='com.example.android.contactmanager'
        desired_caps['appActivity'] ='com.example.android.contactmanager.ContactManager'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['unicodeKeyboard'] = 'True'

        # connect to appium server
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_form(self):
        el = self.driver.find_element_by_accessibility_id("Add Contact")
        el.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys('Jan Kowalski')
        textfields[1].send_keys('555777888')
        textfields[2].send_keys('janek@wsb.pl')

        sleep(3)

        el1 = self.assertEqual('Jan Kowalski',textfields[0].text)
        el2 = self.assertEqual('555777888',textfields[1].text)
        el3 = self.assertEqual('janek@wsb.pl',textfields[2].text)

        button = self.driver.find_element_by_class_name("android.widget.Button")
        button.click()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppInstallation)
    unittest.TextTestRunner(verbosity=2).run(suite)