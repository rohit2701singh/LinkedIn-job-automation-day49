from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class LinkedinJobs:

    def __init__(self, login_mail, login_pass):
        """create driver and take email and password to login."""

        self.__email = login_mail
        self.__password = login_pass

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(chrome_options)
        self.__driver.get("https://www.linkedin.com/home")

        # self.login_page()

    def login_page(self):
        """fill login details and goto home screen. no more execution."""
        try:
            email = self.__driver.find_element(By.NAME, "session_key")
            email.click()
            time.sleep(2)
            email.send_keys(self.__email)
            time.sleep(2)

            user_pass = self.__driver.find_element(By.NAME, "session_password")
            user_pass.click()
            time.sleep(3)
            user_pass.send_keys(self.__password)
            time.sleep(3)

            user_pass.submit()
        except:
            pass

    def home_page(self, job_detail, job_location):
        """check home page for jobs tab, gets inside and fill job details, save first company, open easy apply"""

        self.login_page()

        while input("have you completed verification? type 'yes or no': ").lower() != "yes":
            print("please complete you verification manually.")

        print("you can now proceed on driver")
        time.sleep(10)

        self.__driver.maximize_window()
        home_job_tab = (self.__driver.find_elements(By.CSS_SELECTOR, ".global-nav__content nav ul li"))[2]
        home_job_tab.click()
        time.sleep(2)

        search_box = self.__driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
        search_box.click()
        time.sleep(2)

        job_name = self.__driver.find_element(By.CLASS_NAME, "jobs-search-box__keyboard-text-input")
        time.sleep(2)
        job_name.send_keys(job_detail)
        time.sleep(2)
        job_name.send_keys(Keys.TAB, job_location, Keys.ENTER)
        time.sleep(5)

        try:
            easy_apply = self.__driver.find_element(By.CSS_SELECTOR, "div.search-reusables__filter-binary-toggle button.artdeco-pill.artdeco-pill--slate.artdeco-pill--2.artdeco-pill--choice.ember-view.search-reusables__filter-pill-button")
            easy_apply.click()
        except:
            print("sorry! easy apply element not found.")

        try:
            time.sleep(5)
            save_company = self.__driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button")
            save_company.click()

        except:
            print("sorry! unable to save company.")

        try:
            time.sleep(5)
            easy_apply = self.__driver.find_element(by="xpath", value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/li-icon')
            easy_apply.click()

        except:
            print("sorry! some error occurs.")
