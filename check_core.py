from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

def core_version(driver):
    # Checking core version
    Functions.append_to_notepad(config.file_path, config.version_check)
    time.sleep(5)
    # Check for error on the page
    error_element = Functions.error(driver, xpath.error_xpath)
    if error_element is not None:
        Functions.append_to_notepad(config.file_path, config.error + "Warning - Error present in data catalog while checking version")
        print("Warning - Error present in Data Catalog while checking version")
        # function to open new tab
        Functions.handle_error(driver)
    else:
        core_version_dropdown = Functions.wait_and_find_element_30(driver, "//mat-icon[normalize-space()='arrow_drop_down']")
        if core_version_dropdown is None:
            Functions.append_to_notepad(config.file_path, config.error + "Warning - Dropdown not found in core")
            print("Dropdown not found in core")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            core_version_dropdown.click()
            Core_version_text = Functions.wait_and_find_element_10(driver, "//div[@class='apollo-version']")
            if Core_version_text is None:
                Functions.append_to_notepad(config.file_path, config.error + "version not found in core")
                print("version not found in core")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                Core_Version_element = Core_version_text.text
                Core_Version_current = Core_Version_element
                print(config.core + Core_Version_current)
                #check if the version is correct
                if config.Core_version_expected == Core_Version_current:
                    Core_version = config.Core_version_expected + config.correct
                    print(Core_version)
                    Functions.append_to_notepad(config.file_path, config.core + Core_version)
                else:
                    Core_version = Core_Version_current + config.not_correct
                    print(Core_version)
                    Functions.append_to_notepad(config.file_path, config.core + Core_version)
