from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Enhanced_view:
    def enhanced_view_check_version(driver):
        driver.get(config.enhanced_view_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "error present in enhanced view while checking version")
            print("error present in enhanced view while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "error present in enhanced view while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #select dropdown
            ev_version_dropdown = Functions.wait_and_find_element_30(driver,xpath.enhanced_view_dropdown)
            if ev_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown element not present in enhanced view")
                print("Dropdown element not present in enhanced view")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                try:
                    ev_version_dropdown.click()
                    #view version
                    ev_version_text = Functions.wait_and_find_element_10(driver,xpath.enhanced_view_version_text)
                    if ev_version_text is None:
                        Functions.append_to_notepad(config.file_path, config.error + "Version element not present in enhanced view")
                        print("Version element not present in enhanced view")
                        # function to open new tab
                        Functions.handle_error(driver)
                    else:
                        Enhanced_view_element = ev_version_text.text
                        Enhanced_view_current = Enhanced_view_element
                        print(config.enhanced_view + Enhanced_view_current)
                        # compare version
                        if config.Enhanced_view_version_expected == Enhanced_view_current:
                            Enhanced_view_version = config.Enhanced_view_version_expected + config.correct
                            print(Enhanced_view_version)
                            Functions.append_to_notepad(config.file_path, Enhanced_view_version)
                        else:
                            Enhanced_view_version = Enhanced_view_current + config.not_correct
                            print(Enhanced_view_version)
                            Functions.append_to_notepad(config.file_path, Enhanced_view_version)
                except Exception as e:
                    time.sleep(1)
                    # Call the save_screen method to save the screenshot
                    driver.save_screenshot(config.screenshot + "Error present in Enhancedview.png")
                    # function to open new tab
                    Functions.handle_error(driver)


    def enhanced_view_module1(driver):
        driver.get(config.enhanced_view_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Views")
            print("Error present in Views")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Views.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            Functions.append_to_notepad(config.file_path,"Testing was done successfully in Views")

    def enhanced_view_module2(driver):
        driver.get(config.enhanced_view_module2_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Models")
            print("Error present in Data Models")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Models.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Models")

    def enhanced_view_module3(driver):
        driver.get(config.enhanced_view_module3_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, config.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Jobs List")
            print("Error present in Jobs List")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Jobs List.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # Scroll to the bottom of the page
            Functions.scroll(driver)
            print("Testing was done successfully in Jobs List")
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Jobs List")

