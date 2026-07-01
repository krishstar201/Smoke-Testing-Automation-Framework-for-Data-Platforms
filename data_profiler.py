from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Data_profiler:
    def data_profiler_check_version(driver):
        driver.get(config.data_profiler_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data profiler while checking version")
            print("error present in Data profiler while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data profiler while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #select dropdown
            dp_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.data_profiler_manager_dropdown)
            if dp_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown element not present in data profiler")
                print("Dropdown element not present in data profiler")
            else:
                dp_version_dropdown.click()
                #get version
                dp_version_text = Functions.wait_and_find_element_10(driver,xpath.data_profiler_version_text)
                if dp_version_text is None:
                   Functions.append_to_notepad(config.file_path, config.error + "Version element not present in data profiler ")
                   print("Version element not present in data profiler ")
                   # function to open new tab
                   Functions.handle_error(driver)
                else:
                    Data_Profiler_element = dp_version_text.text
                    Data_Profiler_current = Data_Profiler_element
                    print(config.data_profiler + Data_Profiler_current)
                    # compare version
                    if config.Data_profiler_manager_version_expected == Data_Profiler_current:
                        Data_profiler_version = config.Data_profiler_manager_version_expected + config.correct
                        print(Data_profiler_version)
                        Functions.append_to_notepad(config.file_path, Data_profiler_version)
                    else:
                        Data_profiler_version = Data_Profiler_current + config.not_correct
                        print(Data_profiler_version)
                        Functions.append_to_notepad(config.file_path, Data_profiler_version)

    def data_profiler(driver):
        driver.get(config.data_profiler_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error in Profiles")
            print("Error in Profiles")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error in Profiles.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click search to interact with ui for scrolldown
            dp_element_scroll = Functions.wait_and_find_element_10(driver, xpath.data_profiler_element_scroll)
            if dp_element_scroll is None:
                Functions.append_to_notepad(config.file_path, config.error + "Scroll element not present")
                print("Scroll element not present")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Scroll element not present.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_element_scroll.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                time.sleep(2)
                #check for failed element
                dp_failed_element = Functions.wait_and_find_element_5(driver, xpath.data_profiler_status_failed)
                if dp_failed_element is None:
                    print("Testing was done successfully in Profiles")
                    Functions.append_to_notepad(config.file_path, "Testing was done successfully in Profiles")
                else:
                    print("Error present in Profiles")
                    dp_failed_element.click()
                    # Scroll to the top of the page
                    time.sleep(1)
                    Functions.scroll_to_top(driver)
                    time.sleep(2)
                    # Call the save_screen method to save the screenshot
                    driver.save_screenshot(config.screenshot + "Scroll element not present.png")
                    Functions.append_to_notepad(config.file_path, config.error + "Error present in Profiles")
                    time.sleep(1)
                    # function to open new tab
                    Functions.handle_error(driver)
