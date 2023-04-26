from sentiment_api.sentiment import mongo_connection

from webdriver_manager.chrome import ChromeDriverManager

# selenium imports
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver



import time
import pandas as pd

commentsdata = mongo_connection.commentsdata
mydata = mongo_connection.mydata


class SeleniumScraper:
    def __init__(self, url, movie_name):
        self.video_url = url
        self.required_df = pd.DataFrame()
        self.movie = movie_name

    def scrape(self):

        data = []

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(0.5)

        driver.get(self.video_url)
        # wait for 17 seconds
        wait = WebDriverWait(driver, 17)
        for item in range(17):
            wait.until(ec.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(17)

        for comment in wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            data.append(comment.text)
        df = pd.DataFrame(data)
        driver.quit()
        df.rename(columns={df.columns[0]: 'comment'}, inplace=True)
        self.required_df = df

        return df

    def cleandata(self):
        the_df = self.required_df
        my_df = the_df.dropna()
        my_df.to_csv(f"{self.movie}.csv")
        return my_df



