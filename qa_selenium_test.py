import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Test setup: Initialize WebDriver
@pytest.fixture(scope="module")
def setup():
    # Setup WebDriver (Make sure to specify your path to chromedriver if needed)
    serv_obj = Service("C:\\Python Practice Codes\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
    driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
    driver.maximize_window()

    yield driver
    driver.quit()

# Test case: Search for "New York" and validate results
def test_search_new_york(setup):
    driver = setup
    
    # Locate the search box and enter search term
    search_box = driver.find_element(By.XPATH, '//input[@type = "search"]')
    search_box.send_keys("New York")
    time.sleep(2)  # Wait for the search results to update

    # Count the number of rows displayed in the table
    rows = driver.find_elements(By.XPATH, '//table[@id="example"]//tbody/tr')
    displayed_results = len(rows)
    
    # Assert that 5 results are displayed
    assert displayed_results == 5, f"Expected 5 entries, but got {displayed_results}."

    # Validate that the total number of entries is 24
    total_entries_text = driver.find_element(By.ID,"example_info").text
    assert "24" in total_entries_text, f"Expected 24 total entries, but got {total_entries_text}."
