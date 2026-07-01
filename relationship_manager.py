from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Relationship_manager:
    def relationship_manager_version_check(driver):
        driver.get(config.relationship_manager_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            # drop down not found
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Relationship Manager while checking version")
            print("error present in Relationship Manager while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Relationship Manager while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # checking relationship version
            #dropdown
            rm_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.relationship_manager_dropdown)
            if rm_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown not found in relationship manager")
                print("Dropdown not found in relationship manager")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                rm_version_dropdown.click()
                #get version
                rm_version_text = Functions.wait_and_find_element_10(driver,xpath.relationship_manager_version_text)
                if rm_version_text is None:
                    # drop down not found
                    Functions.append_to_notepad(config.file_path, config.error + "Version not found in Relationship Manager")
                    print("Version not found in Relationship Manager")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    Relationship_manager_Version_element = rm_version_text.text
                    Relationship_manager_Version_current = Relationship_manager_Version_element
                    print(config.relationship_manager + Relationship_manager_Version_current)
                    # compare version
                    if config.Relationship_manager_version_expected == Relationship_manager_Version_current:
                        Relationship_manager_version = config.Relationship_manager_version_expected + config.correct
                        print(Relationship_manager_version)
                        Functions.append_to_notepad(config.file_path, Relationship_manager_version)
                    else:
                        Relationship_manager_version = Relationship_manager_Version_current + config.not_correct
                        print(Relationship_manager_version)
                        Functions.append_to_notepad(config.file_path, Relationship_manager_version)

    def relationship_manager_module1(driver):
        driver.get(config.Relationship_Manager_Module1_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Relationship")
            print("Error present in Relationship")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Relationship.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            #click relation
            rm_view1_relation= Functions.wait_and_find_element_10(driver, xpath.relationship_manager_module1_relation)
            if rm_view1_relation is None:
                # Log if no relations are present
                print("No relationship are present")
                Functions.append_to_notepad(config.file_path, config.error + "No relationship are present" )
                print("Testing was done successfully in Relationship")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Relationship")
            else:
                rm_view1_relation.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                # Log view 1 completion
                print("Testing was done successfully in Relationship")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Relationship")

    def relationship_manager_module2(driver):
        driver.get(config.Relationship_Manager_Module2_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Configuration")
            print("Error present in Configuration")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Configuration.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click first relation
            rm_view2_relation = Functions.wait_and_find_element_10(driver, xpath.relationship_manager_module2_relation)
            if rm_view2_relation is None:
                # Log if no relations are present
                print("No Configurations are present")
                Functions.append_to_notepad(config.file_path, config.error + "No Configurations are present")
                print("Testing was done successfully in Configurations")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Configurations")
            else:
                rm_view2_relation.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                # Log view 2 completion
                print("Testing was done successfully in Configurations")
                Functions.append_to_notepad(config.file_path,"Testing was done successfully in Configurations")

    def relationship_manager_module3(driver):
        driver.get(config.Relationship_Manager_Module3_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Entity")
            print("Error present in Entity")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Entity.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click first relation
            rm_view3_relation = Functions.wait_and_find_element_10(driver, xpath.relationship_manager_module3_relation)
            if rm_view3_relation is None:
                # Log if no relations are present
                print("No Entity are present")
                Functions.append_to_notepad(config.file_path, config.error + "No Entity are present")
                print("Testing was done successfully in Entity")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Entity")
            else:
                rm_view3_relation.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                # Log module 3 completion
                print("Testing was done successfully in Entity")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Entity")

    def relationship_manager_module4(driver):
        driver.get(config.Relationship_Manager_Module4_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Relationship Logs")
            print("Error present in Relationship Logs")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Relationship Logs.png")
            #function to open new tab
            Functions.handle_error(driver)
        else:
            # click first relation
            rm_view4_relation = Functions.wait_and_find_element_10(driver, xpath.relationship_manager_module4_relation)
            if rm_view4_relation is None:
                # Log if no relations are present
                print("No Relationship Logs")
                Functions.append_to_notepad(config.file_path, config.error + "No Relationship Logs")
                print("Testing was done successfully in Relationship Logs")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Relationship Logs")
            else:
                rm_view4_relation.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                # Log module 4 completion
                print("Testing was done successfully in Relationship Logs")
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Relationship Logs")

    def relationship_manager_module5(driver):
        driver.get(config.Relationship_Manager_Module5_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in RM Maintenance")
            print("Error present in RM Maintenance")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            print("Testing was done successfully in RM Maintenance")
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in RM Maintenance")

    def relationship_manager_module6(driver):
        driver.get(config.Relationship_Manager_Module6_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Stewardship")
            print("Error present in Stewardship")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            print("Testing was done successfully in Stewardship")
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Stewardship")

    def relationship_manager_module7(driver):
        driver.get(config.Relationship_Manager_Module7_url)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Bulk Action")
            print("Error present in Bulk Action")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            print("Testing was done successfully in Bulk Action")
            Functions.append_to_notepad(config.file_path, "Testing was done successfully in Bulk Action")
