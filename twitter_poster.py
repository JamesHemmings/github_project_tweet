import time

from selenium import webdriver


class TwitterPoster:

    def __init__(self,
                 chrome_driver_path="chromedriver.exe",
                 chrome_profile_dir=r'--user-data-dir=C:\Users\james\AppData\Local\Google\Chrome Beta\User Data',
                 binary_location="C:\Program Files\Google\Chrome Beta\Application\chrome.exe",
                 options=webdriver.ChromeOptions()
                 ):
        self.chrome_driver_path = chrome_driver_path
        self.chrome_profile_dir = chrome_profile_dir
        self.binary_location = binary_location

        self.options = options
        self.options.add_argument(self.chrome_profile_dir)
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=options)
        self.driver.implicitly_wait(time_to_wait=10)

    def tweet(self, message):
        self.driver.get("https://twitter.com/home")
        tweet_entry = self.driver.find_element_by_css_selector('.DraftEditor-root br')
        tweet_entry.send_keys(message)
        submit_tweet = self.driver.find_elements_by_xpath("//span[contains( text(), 'Tweet')]")
        submit_tweet[2].click()

