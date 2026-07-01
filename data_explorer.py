from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Data_explorer:
    def data_explorer_check_version(driver):
        #navigate to data explorer
        driver.get(config.data_explorer_URl)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path,config.error + "Error present in data explorer while checking version")
            print("error present in data explorer while checking version")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # select dropdown
            de_version_dropdown = Functions.wait_and_find_element_30(driver,xpath.data_explorer_dropdown)
            if de_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown element not present in data explorer")
                print("Dropdown element not present in data explorer")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                de_version_dropdown.click()
                # get version text
                de_version_text = Functions.wait_and_find_element_10(driver,xpath.data_explorer_version_text)
                if de_version_text is None:
                    Functions.append_to_notepad(config.file_path, config.error + "Version element not present in data explorer ")
                    print("Version element not present in data explorer")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Data_explorer_version_element = de_version_text.text
                    Data_explorer_version_current = Data_explorer_version_element
                    print(config.data_explorer + Data_explorer_version_current)
                    # compare version
                    if config.Data_explorer_version_expected == Data_explorer_version_current:
                        Data_explorer_version = config.Data_explorer_version_expected + config.correct
                        print(Data_explorer_version)
                        Functions.append_to_notepad(config.file_path, Data_explorer_version)
                    else:
                        Data_explorer_version = Data_explorer_version_current + config.not_correct
                        print(Data_explorer_version)
                        Functions.append_to_notepad(config.file_path, Data_explorer_version)
    def data_explorer_module1(driver):
        driver.get(config.data_explorer_View1_URl)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path,config.error + "Error present in Data Explorer")
            print("Error present in Data Explorer")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Explorer")

