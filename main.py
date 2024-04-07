# importing required libraries
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Download and install 'chromedriver' on your pc and give its path
ser = Service(r"D:\Downloads\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
sleep(50)

# locate email form by_id
username = driver.find_element(By.ID, 'session_key')

# send_keys() to simulate keystrokes
username.send_keys('@gmail.com')  # Your log-in Email
sleep(50)

# locate password form by_id
password = driver.find_element(By.ID, "session_password")

# send_keys() to simulate keystrokes
password.send_keys('password')  # Your log-in password
sleep(50)

# locate submit button by_class_name
sign_in_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")))
sign_in_button.click()
# .click() to mimic button click
# sign_in_button.click()

# To wait till all page HTML loads of the user account
sleep(50)

# Navigating to required profile
link = 'https://www.linkedin.com/in/maryamkamal/'  # Profile link which you want to scrape
driver.get(link)

# To wait till all page HTML loads of the required profile
sleep(30)

# Getting all the page HTML code and organizing it using BeautifulSoup
src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

# To get link of current page (profile link)
profile_link = driver.current_url

# personal details modules
try:
    parent1_div = soup.find('div', {'class': 'ph5'})
    child1 = parent1_div.find('div', {'class': 'mt2 relative'})
    child2 = parent1_div.find('ul', {'class': 'pv-top-card--list pv-top-card--list-bullet'})
except IndexError:  # To ignore any kind of error
    parent1_div = 'NULL'
    child1 = 'NULL'
    child2 = 'NULL'
except AttributeError:
    parent1_div = 'NULL'
    child1 = 'NULL'
    child2 = 'NULL'

# name
try:
    name = child1.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).getText().strip()
except IndexError:
    name = 'null'
except AttributeError:
    name = 'NULL'

# location
try:
    location = child1.find('span', {'class': 'text-body-small inline t-black--light break-words'}).get_text().strip()
except IndexError:
    location = 'NULL'
except AttributeError:
    location = 'NULL'

# contact information
try:
    contact_information = child1.find('span', {'class': 'pv-text-details__separator t-black--light'})
    contact_link = 'https://www.linkedin.com' + contact_information.find('a')['href']
except IndexError:
    contact_information = 'NULL'
    contact_link = 'NULL'
except AttributeError:
    contact_information = 'NULL'
    contact_link = 'NULL'

# current_level
try:
    current_level = child1.find('div', {'class': 'text-body-medium break-words'}).get_text().strip()
except IndexError:
    current_level = 'NULL'
except AttributeError:
    current_level = 'NULL'

# No. of connections
try:
    connections = child2.find('span', {'class': 'link-without-visited-state'}).get_text().strip()
except IndexError:
    connections = 'NULL'
except AttributeError:
    connections = 'NULL'

# saving outputs
output = (
    {
        'Linked Link': profile_link,
        'Name': name,
        'Location': location,
        'Current Position': current_level,
        'No. of Connections': connections,
        'Contact Link': contact_link,
    }
)

print(output)

# # Experience module
# job_title = ''
# company_name = ''
# duration = ''
#
# try:
#     experience_section = soup.find_all('ul', {'class': 'pvs-list'})
#     experience_list = experience_section[3].find_next('li', {
#         'class': 'artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column'})
#     """try varying the value of experience_section[] between 0-9 to get the correct list element, varying with the profile details"""
# except IndexError:
#     experience_section = 'NULL'
#     experience_list = 'NULL'
# except AttributeError:
#     experience_section = 'NULL'
#     experience_list = 'NULL'
#
# # Job Title
# try:
#     job_title_section = experience_list.find('span', {'class': 'mr1 t-bold'})
#     job_title = job_title_section.find('span', {'class': 'visually-hidden'}).get_text().strip()
# except IndexError:
#     job_title_section = 'NULL'
#     job_title = 'NULL'
# except AttributeError:
#     job_title_section = 'NULL'
#     job_title = 'NULL'
#
# # Company Name
# try:
#     company_name_section = experience_list.find('span', {'class': 't-14 t-normal'})
#     company_name = company_name_section.find('span', {'class': 'visually-hidden'}).get_text().strip()
# except IndexError:
#     company_name_section = 'NULL'
#     company_name = 'NULL'
# except AttributeError:
#     company_name_section = 'NULL'
#     company_name = 'NULL'
#
# # Duration
# try:
#     duration_section = experience_list.find('span', {'class': 't-14 t-normal t-black--light'})
#     duration = duration_section.find('span', {'class': 'visually-hidden'}).get_text().strip()
# except NameError:
#     duration_section = 'NULL'
#     duration = 'NULL'
# except IndexError:
#     duration_section = 'NULL'
#     duration = 'NULL'
# except AttributeError:
#     duration_section = 'NULL'
#     duration = 'NULL'
