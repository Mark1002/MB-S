from selenium import webdriver
import unittest


class WebStartTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_web_sart(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('MB/s', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
