from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Data_bridging:
    def data_bridging_check_version(driver):
        driver.get(config.data_bridging_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Bridging while checking version")
            print("error present in Data Bridging while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Bridging.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #select dropdown
            db_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.data_bridging_dropdown)
            if db_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown not found in Data Bridging")
                print("Dropdown not found in Data Bridging")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                db_version_dropdown.click()
                #get version
                db_version_text = Functions.wait_and_find_element_30(driver, xpath.data_bridging_version_text)
                if db_version_text is None:
                    Functions.append_to_notepad(config.file_path, config.error + "Version not found in Data Bridging")
                    print("Version not found in Data Bridging")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Data_bridging_element = db_version_text.text
                    Data_bridging_current = Data_bridging_element
                    print(config.data_bridging + Data_bridging_current)
                    # compare version
                    if config.Data_bridging_version_expected == Data_bridging_current:
                        Data_bridging_version = config.Data_bridging_version_expected + config.correct
                        print(Data_bridging_version)
                        Functions.append_to_notepad(config.file_path, Data_bridging_version)
                    else:
                        Data_bridging_version = Data_bridging_current + config.not_correct
                        print(Data_bridging_version)
                        Functions.append_to_notepad(config.file_path, Data_bridging_version)


    def data_bridging_module1(driver):
        driver.get(config.data_bridging_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Bridging")
            print("Error present in Data Bridging")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Bridging.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            time.sleep(1)
            Functions.scroll(driver)
            time.sleep(2)
            db_failed_module = Functions.wait_and_find_element_5(driver, xpath.data_bridging_module1_failed)
            if db_failed_module is None:
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Bridging")
                print("Testing was done successfully in Data Bridging")
            else:
                print("Error present in Data Bridging")
                Functions.wait_and_find_element_10(driver, xpath.data_bridging_module1_failed).click()
                # Scroll to the top of the page
                time.sleep(1)
                Functions.scroll_to_top(driver)
                time.sleep(2)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error present in Data Bridging.png")
                time.sleep(1)
                Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Bridging")
                # function to open new tab
                Functions.handle_error(driver)

    def data_bridging_module2(driver):
        driver.get(config.data_bridging_module2_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Assignment")
            print("Error present in Data Assignment")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Assignment.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Assignment")
            print("Testing was done successfully in Data Assignment")
    def data_bridging_module3(driver):
        driver.get(config.data_bridging_module3_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Keyword Library")
            print("Error present in Keyword Library")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Keyword Library.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Keyword Library")
            print("Testing was done successfully in Keyword Library")

    def data_bridging_module4(driver):
        driver.get(config.data_bridging_module4_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Bridge Template Libraries")
            print("Error present in Bridge Template Libraries")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Bridge Template Libraries.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Bridge Template Libraries")
            print("Testing was done successfully in Bridge Template Libraries")

    def data_bridging_module5(driver):
            driver.get(config.data_bridging_module5_URL)
            time.sleep(2)
            # Check for error on the page
            error_element = Functions.error(driver, xpath.error_xpath)
            if error_element is not None:
                Functions.append_to_notepad(config.file_path, config.error + "Error present in Machine Learning Algorithm")
                print("Error present in Machine Learning Algorithm")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error present in Machine Learning Algorithm.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Machine Learning Algorithm")
                print("Testing was done successfully in Machine Learning Algorithm")

