from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath

class Pipeline:
    def pipeline_version_check(driver):
        driver.get(config.pipeline_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "error present in datapipeline while checking version")
            print(config.error + "error present in datapipeline while checking version")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in datapipeline while checking version.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # checking pipeline version
            # try clicking the dropdown arrow
            dp_version_dropdown = Functions.wait_and_find_element_30(driver, xpath.pipeline_dropdown)
            if dp_version_dropdown is None:
                Functions.append_to_notepad(config.file_path, config.error + "Dropdown not found in datapipeline")
                print(config.error + "Dropdown not found in datapipeline")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_version_dropdown.click()
                #try getting pipeline version
                dp_version_text = Functions.wait_and_find_element_10(driver, xpath.pipeline_version_text)
                if dp_version_text is None:
                    Functions.append_to_notepad(config.file_path, config.error + "error present in datapipeline while checking version")
                    print(config.error + "error present in datapipeline while checking version")
                    # function to open new tab
                    Functions.handle_error(driver)
                else:
                    PipeLine_Version_element = dp_version_text.text
                    PipeLine_Version_current = PipeLine_Version_element
                    print(config.data_pipeline + PipeLine_Version_current)
                    #compare version
                    if config.Pipeline_version_expected == PipeLine_Version_current:
                        Pipeline_version = config.Pipeline_version_expected + config.correct
                        print(Pipeline_version)
                        Functions.append_to_notepad(config.file_path, config.data_pipeline + Pipeline_version)
                    else:
                        Pipeline_version = PipeLine_Version_current + config.not_correct
                        print(Pipeline_version)
                        Functions.append_to_notepad(config.file_path,config.data_pipeline + Pipeline_version)

    def pipeline_module1(driver):
        # Click first module
        driver.get(config.pipeline_module1_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in datapipeline")
            print("Error present in datapipeline")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in datapipeline.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            time.sleep(2)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "pipeline_view1.png")
            # Select 500
            dp_view1_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view1_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading data pipeline")
                print("Error in loading data pipeline")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error in loading data pipeline.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view1_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                # Click first task and check if element is present
                dp_view1_task = Functions.wait_and_find_element_10(driver, xpath.pipeline_first_task)
                time.sleep(3)
                if dp_view1_task is None:
                    Functions.append_to_notepad(config.file_path, config.error + "Error No data pipelines found")
                    print("Error No data pipelines found")
                    print("Testing was done successfully in Datapipeline")
                    Functions.append_to_notepad(config.file_path, "Testing was done successfully in Datapipeline ")
                else:
                    # Select first task
                    dp_view1_task.click()
                    #navigating to schema field
                    dp_view1_navigate_schema = Functions.wait_and_find_element_30(driver, xpath.pipeline_navigate_schema)
                    if dp_view1_navigate_schema is None:
                        Functions.append_to_notepad(config.file_path, config.error + "Error in opening task group definition")
                        print("Error in opening task group definition")
                        time.sleep(1)
                        # Call the save_screen method to save the screenshot
                        driver.save_screenshot(config.screenshot + "Error in opening task group definition.png")
                        # function to open new tab
                        Functions.handle_error(driver)
                    else:
                        time.sleep(2)
                        dp_view1_navigate_schema.click()
                        # Checking schema
                        dp_view1_scheme_dropdown = Functions.wait_and_find_element_10(driver, xpath.pipeline_schema_dropdown)
                        if dp_view1_scheme_dropdown is None:
                            Functions.append_to_notepad(config.file_path,config.error + "Error in connection name")
                            print("Error in connection name")
                            time.sleep(1)
                            # Call the save_screen method to save the screenshot
                            driver.save_screenshot(config.screenshot + "Error in connection name.png")
                            # function to open new tab
                            Functions.handle_error(driver)
                        else:
                            dp_view1_scheme_dropdown.click()
                            # Log module 1 completion
                            print("Testing was done successfully in Datapipeline")
                            Functions.append_to_notepad(config.file_path,"Testing was done successfully in Datapipeline ")

    def pipeline_module2(driver):
        # go to next module 2
        driver.get(config.pipeline_module2_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data orchestration")
            print("Error present in Data orchestration")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data orchestration.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click 500
            dp_view2_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view2_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading Data orchestration")
                print("Error in loading Data orchestration")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error in loading Data orchestration.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view2_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data orchestration")
                print("Testing was done successfully in Data orchestration")
    def pipeline_module3(driver):
        # go to next module 2
        driver.get(config.pipeline_module3_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Quality Library")
            print("Error present in Data Quality Library")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Quality Library.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click 500
            dp_view2_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view2_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading Data Quality Library")
                print("Error in loading Data Quality Library")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error in loading Data Quality Library.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view2_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path,"Testing was done successfully in Data Quality Library")
                print("Testing was done successfully in Data Quality Library")

    def pipeline_module4(driver):
        # go to module 3
        driver.get(config.pipeline_module4_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Business Quality Library")
            print("Error present in Business Quality Library")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Business Quality Library.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click 500
            dp_view3_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view3_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading Business Rule Library")
                print("Error in loading Business Rule Library")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error in loading Business Rule Library")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view3_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Business Quality Library")
                print("Testing was done successfully in Business Quality Library")

    def pipeline_module5(driver):
        # go to module 4
        driver.get(config.pipeline_module5_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Pipeline Template Library")
            print("Error present in Pipeline Template Library")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Pipeline Template Library.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click 500
            dp_view4_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view4_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading Pipeline Template Library")
                print("Error in loading Pipeline Template Library")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error present in Pipeline Template Library.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view4_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Pipeline Template Library")
                print("Testing was done successfully in Pipeline Template Library")

    def pipeline_module6(driver):
        # go to module 5
        driver.get(config.pipeline_module6_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Asset Management")
            print("Error present in Data Asset Management")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Asset Management.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            # click 500
            dp_view5_500 = Functions.wait_and_find_element_10(driver, xpath.pipeline_500_element)
            if dp_view5_500 is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in loading Data Asset Management")
                print("Error in loading Data Asset Management")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error present in Data Asset Management.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view5_500.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Asset Management")
                print("Testing was done successfully in Data Asset Management")

    def pipeline_module7(driver):
        # go to module 6
        driver.get(config.pipeline_module7_URL)
        time.sleep(2)
        # Check for error on the page
        error_element = Functions.error(driver, xpath.error_xpath)
        if error_element is not None:
            Functions.append_to_notepad(config.file_path, config.error + "Error present in Data Pipeline Maintenance")
            print("Error present in Data Pipeline Maintenance")
            time.sleep(1)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "Error present in Data Pipeline Maintenance.png")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            time.sleep(2)
            # Call the save_screen method to save the screenshot
            driver.save_screenshot(config.screenshot + "pipeline_view7.png")
            #click view all connection string
            dp_view6_cstring = Functions.wait_and_find_element_10(driver, xpath.pipeline_view_connection_string)
            if dp_view6_cstring is None:
                Functions.append_to_notepad(config.file_path, config.error + "Error in Connection strings")
                print("Error in Connection strings")
                time.sleep(1)
                # Call the save_screen method to save the screenshot
                driver.save_screenshot(config.screenshot + "Error present in Data Pipeline Maintenance.png")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                dp_view6_cstring.click()
                # Scroll to the bottom of the page
                Functions.scroll(driver)
                Functions.append_to_notepad(config.file_path, "Testing was done successfully in Data Pipeline Maintenance")
                print("Testing was done successfully in Data Pipeline Maintenance")
