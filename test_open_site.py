from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAbc:

    def test_abc(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.ibm.com")
        driver.find_element(By.LINK_TEXT, "Learn more").click()
        # driver.close()
        # driver.quit()
