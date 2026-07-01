import os
import time
import win32com.client
import re
from selenium.common.exceptions import TimeoutException
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

class Functions:
    @staticmethod
    def clear_outlook_folder(folder_name, subfolder_name, email):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        folder = outlook.Folders(email).Folders(folder_name)
        subfolder = folder.Folders(subfolder_name)

        while subfolder.Items.Count > 0:
            try:
                item = subfolder.Items.GetFirst()
                item.Delete()
                time.sleep(.3)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                break

        print(f"The subfolder '{subfolder_name}' in folder '{folder_name}' has been cleared.")

    @staticmethod
    def wait_and_find_element_10(driver, xpath):
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def wait_and_find_element_30(driver, xpath):
        try:
            wait = WebDriverWait(driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def wait_and_find_element_click_10(driver, xpath):
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def wait_and_find_element_5(driver, xpath):
        try:
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def error(driver, xpath):
        try:
            wait = WebDriverWait(driver, 3)
            element_click = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element_click
        except TimeoutException:
            print("No error found in this page")
            return None

    @staticmethod
    def otp(folder_name, subfolder_name, email, url_to_match, max_attempts=10, wait_time=10):
        for _ in range(max_attempts):
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

            folder = outlook.Folders(email).Folders(folder_name)
            subfolder = folder.Folders(subfolder_name)

            # Sort messages by received time in descending order
            messages = sorted(subfolder.Items, key=lambda x: x.ReceivedTime, reverse=True)

            for message in messages:
                body = message.Body
                match = re.search(r'\b\d{6}\b', body)
                if match:
                    six_digit_number = match.group()
                    #return six_digit_number
                    # Check if the body contains the specified URL
                    if f"{url_to_match}" in body:
                        return six_digit_number
            time.sleep(wait_time)
        return None

    @staticmethod
    def login(driver, auth_url):
        driver.get(auth_url)
        Functions.wait_and_find_element_30(driver, "//input[@id='username']").send_keys(config.username)
        Functions.wait_and_find_element_10(driver, "//input[@id='password']").send_keys(config.password)
        Functions.wait_and_find_element_10(driver, "//button[normalize-space()='Log in']").click()

    @staticmethod
    def login_and_verify_loop(driver,auth_url, full_url, outlookfolder, outlooksubfolder, email, max_attempts, wait_time):
        while True:
            # Calling the function to clear the Outlook box
            # Functions.clear_outlook_folder(outlookfolder, outlooksubfolder, email)
            # time.sleep(3)

            # Call the login function to log in
            Functions.login(driver, auth_url)

            # Use the otp function to retrieve the OTP
            FA = Functions.otp(outlookfolder, outlooksubfolder, email, full_url, max_attempts=max_attempts,wait_time=wait_time)

            # Check if FA is None
            if FA is None:
                print("FA is None. Retrying...")
                time.sleep(2)
            else:
                print(f"Six-digit number from the email with matching Tenant URL: {FA}")
                # Sleep for 1 second (if needed)
                time.sleep(1)
                # Automating to enter 2FA
                Functions.wait_and_find_element_10(driver, "//input[@id='TwoFactorCode']").send_keys(FA)
                Functions.wait_and_find_element_10(driver, "//button[normalize-space()='Verify code']").click()
                break  # Exit the loop if FA has a value

    @staticmethod
    def get_chrome_driver():
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def create_folder(folder_name, folder_path):
        folder_path = os.path.join(folder_path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created successfully at '{folder_path}'")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists at '{folder_path}'")
        except Exception as e:
            print(f"An error occurred while creating the folder: {e}")

    @staticmethod
    def scroll(driver):
        start_time = time.time()
        while True:
            body_element = Functions.wait_and_find_element_10(driver, "//body")
            #body_element = driver.find_element(By.XPATH, "//body")
            body_element.send_keys(Keys.END)
            time.sleep(1)
            if driver.execute_script("return window.innerHeight + window.scrollY >= document.body.scrollHeight"):
                break
            if time.time() - start_time > 3:
                break

    @staticmethod
    def scroll_to_top(driver):
        start_time = time.time()
        while True:
            body_element = Functions.wait_and_find_element_10(driver, "//body")
            #body_element = driver.find_element(By.XPATH, "//body")
            # Pressing HOME key to scroll to the top
            body_element.send_keys(Keys.HOME)
            time.sleep(1)
            # Check if scrolled to the top
            if driver.execute_script("return window.scrollY == 0"):
                break
            if time.time() - start_time > 3:
                break

    @staticmethod
    def check_for_error(driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath)
            print("Error in this page.")
            time.sleep(5)
        except NoSuchElementException:
            print("No error.")
            time.sleep(3)

    @staticmethod
    def append_to_notepad(file_path, content):
        try:
            # Open the file in append mode
            with open(file_path, "a") as file:
                # Write the content to the file
                file.write(content + '\n')
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    @staticmethod
    def handle_error(driver):
        current_url = driver.current_url
        driver.execute_script(f"window.open('{current_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
