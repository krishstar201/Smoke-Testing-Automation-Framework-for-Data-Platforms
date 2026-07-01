from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Data_catalog:
    def data_catalog_version_check(driver):
        driver.get(config.data_catalog_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in data catalog while checking version")
            print("error present in data catalog while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in data catalog while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #click dropdown
            dc_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.data_catalog_dropdown)
            if dc_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown not found in data catalog")
                print("Dropdown not found in data catalog")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dc_version_dropdown.click()
                #get data catalog version
                dc_version_text = Functions.wait_and_find_element_10(driver,xpath.data_catalog_version_text)
                if dc_version_text is None:
                    Functions.append_to_notepad(config.file_path, config.error + "Version not found in data catalog")
                    print("Version not found in data catalog")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Data_catalog_Version_element = dc_version_text.text
                    Data_catalog_Version_current = Data_catalog_Version_element
                    print(config.data_catalog + Data_catalog_Version_current)
                    # compare version
                    if config.Data_catalog_version_expected == Data_catalog_Version_current:
                        Data_catalog_version = config.Data_catalog_version_expected + config.correct
                        print(Data_catalog_version)
                        Functions.append_to_notepad(config.file_path, Data_catalog_version)
                    else:
                        Data_catalog_version = Data_catalog_Version_current + config.not_correct
                        print(Data_catalog_version)
                        Functions.append_to_notepad(config.file_path, Data_catalog_version)

    def data_catalog_module1(driver):
        driver.get(config.data_catalog_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in My Catalog")
            print("Error present in My Catalog")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in My Catalog.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #check one catalog
            dc_view1_catalog = Functions.wait_and_find_element_10(driver, xpath.data_catalog_catalog)
            if dc_view1_catalog is None:
                print("No Catalog found in My Catalog")
                Functions.append_to_notepad(config.file_path, config.error + "No Catalog found in My Catalog")
                print("Testing was done successfully in My Catalog")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in My Catalog")
            else:
                dc_view1_catalog.click()
                #check for an element in catalog
                dc_view1_element = Functions.wait_and_find_element_10(driver, xpath.data_catalog_element)
                if dc_view1_element is None:
                    print("No Objects found in My Catalog")
                    Functions.append_to_notepad(config.file_path, config.error + "No Objects found in My Catalog")
                    print("Testing was done successfully in My Catalog")
                    Functions.append_to_notepad(config.file_path, "Testing was done successfully in My Catalog")
                else:
                    dc_view1_element.click()
                    #scroll the page
                    Functions.scroll(driver)
                    print("No Error's in Attribute")
                    #select General
                    dc_view1_general = Functions.wait_and_find_element_10(driver, xpath.data_catalog_general)
                    if dc_view1_general is None:
                        print("Error in General-My Catalog")
                        Functions.append_to_notepad(config.file_path, config.error + "Error in General-My Catalog")
                        time.sleep(1)
                        # Call the save_screen method to save the screenshot
                        driver.save_screenshot(config.screenshot + "Error in General-My Catalog.png")
                        # function to open new tab
                        Functions.handle_error(driver)
                    else:
                        dc_view1_general.click()
                        # scroll the page
                        Functions.scroll(driver)
                        print("No Error's in General")
                        # select values
                        dc_view1_value = Functions.wait_and_find_element_10(driver, xpath.data_catalog_values)
                        if dc_view1_value is None:
                            print("Error in Values-My Catalog")
                            Functions.append_to_notepad(config.file_path, config.error + "Error in Values-My Catalog")
                            time.sleep(1)
                            # Call the save_screen method to save the screenshot
                            driver.save_screenshot(config.screenshot + "Error in Values-My Catalog.png")
                            # function to open new tab
                            Functions.handle_error(driver)
                        else:
                            dc_view1_value.click()
                            # scroll the page
                            Functions.scroll(driver)
                            print("No Error's in Values")
                            # select relationship
                            dc_view1_relationship = Functions.wait_and_find_element_10(driver, xpath.data_catalog_relationship)
                            if dc_view1_relationship is None:
                                print("Error in Relationship-My Catalog")
                                Functions.append_to_notepad(config.file_path,config.error + "Error in Relationship-My Catalog")
                                time.sleep(1)
                                # Call the save_screen method to save the screenshot
                                driver.save_screenshot(config.screenshot + "Error in Relationship-My Catalog.png")
                                # function to open new tab
                                Functions.handle_error(driver)
                            else:
                                dc_view1_relationship.click()
                                # scroll the page
                                Functions.scroll(driver)
                                print("No Error in Relationship")
                                # select activity log
                                dc_view1_activity =Functions.wait_and_find_element_10(driver, xpath.data_catalog_activity_log)
                                if dc_view1_activity is None:
                                    print("Error in Activity Log-My Catalog")
                                    Functions.append_to_notepad(config.file_path,config.error + "Error in Activity Log-My Catalog")
                                    time.sleep(1)
                                    # Call the save_screen method to save the screenshot
                                    driver.save_screenshot(config.screenshot + "Error in Activity Log-My Catalog.png")
                                    # function to open new tab
                                    Functions.handle_error(driver)
                                else:
                                    dc_view1_activity.click()
                                    # scroll the page
                                    Functions.scroll(driver)
                                    print("No Error in Activity Log")
                                    print("Testing was done successfully in My Catalog")
                                    Functions.append_to_notepad(config.file_path, "Testing was done successfully in My Catalog")


    def data_catalog_module2(driver):
        driver.get(config.data_catalog_module2_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Product Catalog")
            print("Error present in Product Catalog")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Product Catalog.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # select first catalog
            dc_view2_catalog = Functions.wait_and_find_element_10(driver, xpath.data_catalog_catalog_module2)
            if dc_view2_catalog is None:
                # Log if no catalog are present
                print("No Catalog found in Product Catalog")
                Functions.append_to_notepad(config.file_path, config.error + "No Catalog found in Product Catalog")
                print("Testing was done successfully in My Catalog")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in My Catalog")
            else:
                dc_view2_catalog.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                #select first element
                dc_view2_element = Functions.wait_and_find_element_10(driver, xpath.data_catalog_element_module2)
                if dc_view2_element is None:
                    # Log if no element are present
                    print("No Object found in Product Catalog")
                    Functions.append_to_notepad(config.file_path, config.error + "No Object found in Product Catalog")
                    print("Testing was done successfully in My Catalog")
                    Functions.append_to_notepad(config.file_path, "Testing was done successfully in My Catalog")
                else:
                    dc_view2_element.click()
                    # Scroll to the bottom of the page
                    Functions.scroll(driver)
                    # select General
                    dc_view2_general = Functions.wait_and_find_element_10(driver, xpath.data_catalog_general_module2)
                    if dc_view2_general is None:
                        # no general present
                        print("Error in General-Product Catalog")
                        Functions.append_to_notepad(config.file_path, config.error + "Error in General-Product Catalog")
                        time.sleep(1)
                        # Call the save_screen method to save the screenshot
                        driver.save_screenshot(config.screenshot + "Error in General-Product Catalog.png")
                        # function to open new tab
                        Functions.handle_error(driver)
                    else:
                        dc_view2_general.click()
                        # Scroll to the bottom of the page
                        Functions.scroll(driver)
                        # select Relationship
                        dc_view2_relationship = Functions.wait_and_find_element_10(driver, xpath.data_catalog_relationship_module2)
                        if dc_view2_relationship is None:
                            # no Relationship present
                            print("Error in Relationship-Product Catalog")
                            Functions.append_to_notepad(config.file_path,config.error + "Error in Relationship-Product Catalog")
                            time.sleep(1)
                            # Call the save_screen method to save the screenshot
                            driver.save_screenshot(config.screenshot + "Error in Relationship-Product Catalog.png")
                            # function to open new tab
                            Functions.handle_error(driver)
                        else:
                            dc_view2_relationship.click()
                            # Scroll to the bottom of the page
                            Functions.scroll(driver)
                            # Log if no element are present
                            print("Testing was done successfully in Product Catalog")
                            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Product Catalog")
