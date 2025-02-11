from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from .models import Internship  # Import Django Model

def setup_webdriver():
    """Configure and return Chrome WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )

def scroll_to_load_more(driver):
    """Scroll down to load more content"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scrape_internships(skills):
    driver = None
    internships = []

    try:
        driver = setup_webdriver()
        search_url = f"https://internshala.com/internships/{','.join(skill + '-internship' for skill in skills)}/"
        driver.get(search_url)
        time.sleep(3)

      

        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="internship_list_container_1"]'))
        )
        internship_divs = container.find_elements(By.XPATH, './div')

        for i in range(1, len(internship_divs) + 1):
            try:
                internship_xpath = f'//*[@id="internship_list_container_1"]/div[{i}]'
                internship_element = driver.find_element(By.XPATH, internship_xpath)

                details = {
                    'internship_name': internship_element.find_element(By.XPATH, './div/div/div/h3/a').text.strip(),
                    'company_name': internship_element.find_element(By.XPATH, './div/div/div/div/div/p').text.strip(),
                    'location': internship_element.find_element(By.XPATH, './div/div[2]/div/div/span/a').text.strip(),
                    'time_period': internship_element.find_element(By.XPATH, './div/div[2]/div/div[2]/span').text.strip(),
                    'stipend': internship_element.find_element(By.XPATH, './div/div[2]/div/div[3]/span').text.strip(),
                    'internship_link': f"https://internshala.com{internship_element.get_attribute('data-href')}",
                }

                # ✅ **Skip if required fields are empty**
                if not details["internship_name"] or not details["company_name"]:
                    print(f"⚠ Skipping internship due to missing details: {details}")
                    continue

                # Save to Django database
                Internship.objects.create(**details)
                internships.append(details)

            except Exception as div_error:
                print(f"Error processing internship {i}: {div_error}")

    except Exception as e:
        print(f"Scraping error: {e}")

    finally:
        if driver:
            driver.quit()

    print(f"🎯 Total Internships Scraped: {len(internships)}")  # ✅ Debug Output
    return internships
