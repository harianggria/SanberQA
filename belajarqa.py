import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('jagoqaindonesia@gmail.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)

        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon_welcome, 'Welcome Jago QA')
        self.assertEqual(respon_berhasil, 'Anda Berhasil Login')
    
    def test_b_failed_login_email_not_registered(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)

        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertIn('not found',respon_welcome)
        self.assertIn('Salah', respon_berhasil)
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')

    def test_email_blank(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)

        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertIn('not found',respon_welcome)
        self.assertIn('Salah', respon_berhasil)
        self.assertEqual(respon_welcome, "Wrong Format")
        self.assertEqual(respon_berhasil, 'Harap mengisi email dan password terlebih dahulu')
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
unittest.main()