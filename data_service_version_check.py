from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath


def data_service_version_check(driver):
    driver.get(config.full_url+"/feature-designer/feature-stores")
    time.sleep(2)
    # Check for error on the page
    error_element = Functions.error(driver, xpath.error_xpath)
    if error_element is not None:
        Functions.append_to_notepad(config.file_path,config.error + "error present in datapipeline while checking version")
        print(config.error + "error present in datapipeline while checking version")
        time.sleep(1)
        # Call the save_screen method to save the screenshot
        driver.save_screenshot(config.screenshot + "Error present in datapipeline while checking version.png")
        # function to open new tab
        Functions.handle_error(driver)
    else:
        # checking pipeline version
        # try clicking the dropdown arrow
        dp_version_dropdown = Functions.wait_and_find_element_10(driver, xpath.pipeline_dropdown)
        if dp_version_dropdown is None:
            Functions.append_to_notepad(config.file_path, config.error + "Dropdown not found in Data Service")
            print(config.error + "Dropdown not found in Data Service")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            dp_version_dropdown.click()
            # try getting pipeline version
            dp_version_text = Functions.wait_and_find_element_10(driver, xpath.pipeline_version_text)
            if dp_version_text is None:
                Functions.append_to_notepad(config.file_path,config.error + "error present in datapipeline while checking version")
                print(config.error + "error present in datapipeline while checking version")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                Data_service_Version_element = dp_version_text.text
                Data_service_Version_current = Data_service_Version_element
                print(config.data_pipeline + Data_service_Version_current)
                # compare version
                if config.Data_service_version_expected == Data_service_Version_current:
                    Data_service_version = config.Data_service_version_expected + config.correct
                    print(Data_service_version)
                    Functions.append_to_notepad(config.file_path, config.data_service + Data_service_version)
                else:
                    Data_service_version = Data_service_Version_current + config.not_correct
                    print(Data_service_version)
                    Functions.append_to_notepad(config.file_path, config.data_service + Data_service_version)