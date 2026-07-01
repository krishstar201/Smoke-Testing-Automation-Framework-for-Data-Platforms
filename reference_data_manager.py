from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Reference_data_manager:
    def reference_data_manager_version_check(driver):
        driver.get(config.reference_data_manager_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in reference data manager while checking version")
            print("error present in reference data manager while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in reference data manager while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # select dropdown
            rdm_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.reference_data_manager_dropdown)
            if rdm_version_dropdown is  None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown element not present in reference data manager")
                print("Dropdown element not present in reference data manager")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                rdm_version_dropdown.click()
                # get version text
                rdm_version_element = Functions.wait_and_find_element_10(driver,xpath.reference_data_manager_version_text)
                if rdm_version_element is None:
                    Functions.append_to_notepad(config.file_path,config.error + "Version element not present in reference data manager ")
                    print("Version element not present in reference data manager ")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Reference_data_manager_Version_element = rdm_version_element.text
                    Reference_data_manager_Version_current = Reference_data_manager_Version_element
                    print(config.reference_data_manager + Reference_data_manager_Version_current)
                    # compare version
                    if config.Reference_data_manager_version_expected == Reference_data_manager_Version_current:
                        Reference_data_manager_version = config.Reference_data_manager_version_expected + config.correct
                        print(Reference_data_manager_version)
                        Functions.append_to_notepad(config.file_path, Reference_data_manager_version)
                    else:
                        Reference_data_manager_version = Reference_data_manager_Version_current + config.not_correct
                        print(Reference_data_manager_version)
                        Functions.append_to_notepad(config.file_path, Reference_data_manager_version)

    def reference_data_manager_module1(driver):
        driver.get(config.reference_data_manager_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path,config.error + "Error in Lookup Type")
            print("Error in Lookup Type")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error in Lookup Type.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            print("Testing was done successfully in Lookup Type")
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Lookup Type")

