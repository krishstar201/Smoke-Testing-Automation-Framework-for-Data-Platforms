from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Business_rule_manager:
    def business_rule_manager_check_version(driver):
        driver.get(config.business_rule_manager_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, config.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "error present in business rule manager while checking version")
            print("error present in business rule manager while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in business rule manager while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #select dropdown
            brm_version_dropdown = Functions.wait_and_find_element_10(driver, xpath.business_rule_dropdown)
            if brm_version_dropdown is None:
               Functions.append_to_notepad(config.file_path, config.error + "Dropdown element not present in business rule manager")
               print("Dropdown element not present in business rule manager")
               # function to open new tab
               Functions.handle_error(driver)
            else:
                brm_version_dropdown.click()
                #get version
                brm_version_text = Functions.wait_and_find_element_10(driver, xpath.business_rule_version_text)
                if brm_version_text is None:
                    Functions.append_to_notepad(config.file_path,config.error + "Version element not present in business rule manager")
                    print("Version element not present in business rule manager")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Business_rule_manager_version_element = brm_version_text.text
                    Business_rule_manager_version_current = Business_rule_manager_version_element
                    print(config.business_rule_manager + Business_rule_manager_version_current)
                    # compare version
                    if config.Business_rule_manager_version_expected == Business_rule_manager_version_current:
                        Business_rule_manager_version = config.Business_rule_manager_version_expected + config.correct
                        print(Business_rule_manager_version)
                        Functions.append_to_notepad(config.file_path, Business_rule_manager_version)
                    else:
                        Business_rule_manager_version = Business_rule_manager_version_current + config.not_correct
                        print(Business_rule_manager_version)
                        Functions.append_to_notepad(config.file_path, Business_rule_manager_version)


    def business_rule_manager_module1(driver):
        driver.get(config.business_rule_manager_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path,config.error + "Error present in Business Rule Manager")
            print("Error present in Business Rule Manager")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Business Rule Manager.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            print(config.no_error_in_page)
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            Functions.append_to_notepad(config.file_path, "Testing was done successfully Business Rule Manager")
            print("Testing was done successfully Business Rule Manager")

    def business_rule_manager_module2(driver):
        driver.get(config.business_rule_manager_module2_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Business Rule Library")
            print("Error present in Business Rule Library")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Business Rule Library.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Business Rule Library")
            print("Testing was done successfully in Business Rule Library")


