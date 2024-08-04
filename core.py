from resources import (Variables, Xpaths, subtract_months, download_image, count_search_phrase, verify_money,
                       excel_file)
from RPA.Browser.Selenium import Selenium, ElementNotFound
from datetime import datetime
from time import sleep
import shutil
import os


class Scrapping:
    def __init__(self):
        # Initialize the Selenium driver and set date range for the search
        self.driver = Selenium()
        self.end_date = datetime.today().date()
        self.start_date = subtract_months(self.end_date, Variables.MONTHS)
        self.results = []

        # Clean up previous output files and directories
        for path in ["output/images", "output/result.xlsx"]:
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)

    def open_url(self, url):
        # Open a browser and navigate to the specified URL
        self.driver.open_available_browser(url)

    def search(self, text):
        # Perform a search using the given text
        print(f"Searching for '{text}'")
        self.driver.click_element_when_clickable(Xpaths.Home.BUTTON_SEARCH)
        self.driver.input_text_when_element_is_visible(Xpaths.Home.INPUT_SEARCH, text)
        self.driver.click_button(Xpaths.Home.BUTTON_SUBMIT)

    def select_categories(self, categories):
        # Select specified categories for filtering search results
        category_list = ""
        if categories:
            for category in categories:
                try:
                    category_list += f"{category}, "
                    self.driver.click_element_when_clickable(Xpaths.NewsPage.SPAN_SHOW_CATEGORIES)
                    self.driver.click_element_when_clickable(f"xpath://span[text()='{category}']/preceding::input[1]")
                except Exception as e:
                    print(f"Error while selecting '{category}' topic. \nError: {e}")

            category_list = category_list[:-3]
            print(f"Topics: {category_list}")
        else:
            print("Any categories selected.")

    def sort_results(self):
        # Sort search results by the newest first
        self.driver.select_from_list_by_label(Xpaths.NewsPage.SELECT_SORT, "Newest")
        sleep(3)

    def retrieve_results(self):
        # Retrieve search results within the specified date range
        base_xpath = f"{Xpaths.NewsPage.UL_RESULTS}"
        all_news = self.driver.find_elements(base_xpath)

        index = 1

        while index <= len(all_news):
            news_element = base_xpath + f"[{index}]//"

            # Extract news date and verify it falls within the range
            timestamp = self.driver.get_element_attribute(f"{news_element}{Xpaths.Result.DATE}", "data-timestamp")
            news_date = datetime.fromtimestamp(int(timestamp[:-3])).date()

            if self.start_date <= news_date <= self.end_date:
                # Retrieve title, image, and description of each news item
                news_title = self.driver.get_text(f"{news_element}{Xpaths.Result.TITLE}")

                img_link = self.driver.get_element_attribute(f"{news_element}{Xpaths.Result.PICTURE}", "src")
                img_name = f"{str(img_link).split('%2F')[-1].split('.')[0]}.jpg"
                download_image(img_link, img_name)

                try:
                    news_description = self.driver.get_text(f"{news_element}{Xpaths.Result.DESCRIPTION}")
                except ElementNotFound:
                    news_description = "Description not available."

                # Store the results with additional metadata
                news_object = {
                    "title": news_title,
                    "date": str(news_date),
                    "description": news_description,
                    "img_name": img_name,
                    "search_phrases_in_title": count_search_phrase(news_title, Variables.SEARCH_PHRASE),
                    "search_phrases_in_description": count_search_phrase(news_description, Variables.SEARCH_PHRASE),
                    "contains_money": verify_money(news_title, news_description)
                }

                self.results.append(news_object)

                # Check if more pages of results are available
                if index == len(all_news):
                    self.driver.click_element(Xpaths.NewsPage.DIV_NEXT_PAGE)
                    index = 1
                    sleep(3)
                else:
                    index += 1
            else:
                break

        print(f"Retrieving {len(self.results)} results from {self.start_date} until {self.end_date}.")

    def run(self):
        # Main method to execute the full scraping process
        self.open_url(Variables.URL)
        self.search(Variables.SEARCH_PHRASE)
        self.select_categories(Variables.CATEGORIES)
        self.sort_results()
        self.retrieve_results()
        excel_file(self.results)