import os
import sys
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

load_dotenv()

resume_folder = "/Users/novosoftsolutions/Desktop/Personal/resume"
resume_files = [f for f in os.listdir(resume_folder) if os.path.isfile(os.path.join(resume_folder, f)) and not f.startswith('.')]
if not resume_files:
    print(f"Error: No files found in {resume_folder}")
    sys.exit(1)
resume_path = os.path.join(resume_folder, resume_files[0])
print(f"Using resume: {resume_path}")

def norm(s: str) -> str:
    return " ".join(s.replace("\r\n", "\n").replace("\r", "\n").split())


service = Service(executable_path="./chromedriver")

driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")

profile_summary1 = os.getenv("PROFILE_SUMMARY_1")
profile_summary2 = os.getenv("PROFILE_SUMMARY_2")
profile_summary3 = os.getenv("PROFILE_SUMMARY_3")

telegram_token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

# Validate environment variables
missing_vars = []
if not email: missing_vars.append("NAUKRI_EMAIL")
if not password: missing_vars.append("NAUKRI_PASSWORD")
if not profile_summary1: missing_vars.append("PROFILE_SUMMARY_1")
if not profile_summary2: missing_vars.append("PROFILE_SUMMARY_2")
if not profile_summary3: missing_vars.append("PROFILE_SUMMARY_3")

if missing_vars:
    now = datetime.now()
    formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Error: Missing environment variables: {', '.join(missing_vars)}" + formatted_time)
    print("Please check your .env file.")
    if 'driver' in locals() or 'driver' in globals():
        driver.quit()
    sys.exit(1)

driver.get("https://duckduckgo.com")

input_element = driver.find_element(By.ID, "searchbox_input")
input_element.send_keys("www.naukri.com")
input_element.send_keys(Keys.ENTER)

result = wait.until(
    ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "www.naukri.com"))
)
result.click()

login_button = wait.until(
    ec.element_to_be_clickable((By.ID, "login_Layer"))
)
login_button.click()

email_input = wait.until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Enter your active Email ID / Username"]'))
)
email_input.send_keys(email)

password_input = wait.until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Enter your password"]'))
)
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)


def check_login_status(d):
    err = d.find_elements(By.CLASS_NAME, "server-err")
    if err and err[0].is_displayed():
        return "error"
    drawer = d.find_elements(By.CLASS_NAME, "nI-gNb-drawer")
    if drawer and drawer[0].is_displayed():
        return "success"
    return False


login_status = wait.until(check_login_status)

if login_status == "error":
    now = datetime.now()
    formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print("Invalid details. Please check the Email ID - Password combination. " + formatted_time)
    driver.quit()
    sys.exit(1)

drawer_icon = wait.until(
    ec.element_to_be_clickable((By.CLASS_NAME, "nI-gNb-drawer"))
)
drawer_icon.click()

view_update_profile_txt_btn = wait.until(
    ec.element_to_be_clickable((By.CLASS_NAME, "nI-gNb-info__sub-link"))
)
view_update_profile_txt_btn.click()

summary_edit_icon_btn = wait.until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, "span.edit.icon"))
)
summary_edit_icon_btn.click()

summary_edit_text = wait.until(
    ec.element_to_be_clickable((By.ID, "resumeHeadlineTxt"))
)

cur_summary_content = summary_edit_text.get_attribute("value")

new_summary_content = ""
now = datetime.now()
formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")

if cur_summary_content == norm(profile_summary1):
    new_summary_content = profile_summary2
    print("Adding Summary 2 " + formatted_time)
elif cur_summary_content == norm(profile_summary2):
    new_summary_content = profile_summary3
    print("Adding Summary 3 " + formatted_time)
else:
    new_summary_content = profile_summary1
    print("Adding Summary 1 " + formatted_time)

summary_edit_text.clear()
summary_edit_text.send_keys(new_summary_content)

summary_save_btn = wait.until(
    ec.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Save"]'))
)

summary_save_btn.click()


cross_btn = driver.find_element(By.CLASS_NAME, "crossLayer")
driver.execute_script("arguments[0].click();", cross_btn)

file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(resume_path)


time.sleep(5)
driver.quit()
