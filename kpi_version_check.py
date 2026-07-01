from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from functions import Functions
import config
import xpath


def kpi_version_check(driver):
    driver.get(config.full_url+"/admin/kpi-library")
    time.sleep(5)
    # Check for error on the page
    error_element = Functions.error(driver, xpath.error_xpath)
    if error_element is not None:
        Functions.append_to_notepad(config.file_path, config.error + "Error present in kpi version while checking version")
        print("error present in kpi version while checking version")
        time.sleep(1)
        # Call the save_screen method to save the screenshot
        driver.save_screenshot(config.screenshot + "Error present in kpi version while checking version.png")
        # function to open new tab
        Functions.handle_error(driver)
    else:
        # checking pipeline version
        kpi_version_dropdown = Functions.wait_and_find_element_10(driver, "//mat-icon[normalize-space()='arrow_drop_down']")
        if kpi_version_dropdown is None:
            Functions.append_to_notepad(config.file_path, config.error +"dropdown present in kpi version while checking version")
            print("dropdown present in kpi version while checking version")
            # function to open new tab
            Functions.handle_error(driver)
        else:
            kpi_version_dropdown.click()
            #version
            kpi_version_text = Functions.wait_and_find_element_10(driver,"//div[@class='apollo-version']")
            if kpi_version_text is None:
                Functions.append_to_notepad(config.file_path, config.error +"version not found in kpi version")
                print("version not found in kpi version")
                # function to open new tab
                Functions.handle_error(driver)
            else:
                KPI_Version_element = kpi_version_text.text
                KPI_Version_current = KPI_Version_element
                print(config.kpi + KPI_Version_current)
                # compare version
                if config.KPI_version_expected == KPI_Version_current:
                    KPI_version = config.KPI_version_expected + config.correct
                    print(KPI_version)
                    Functions.append_to_notepad(config.file_path,config.kpi + KPI_version)
                else:
                    KPI_version = KPI_Version_current + config.not_correct
                    print(KPI_version)
                    Functions.append_to_notepad(config.file_path,config.kpi + KPI_version)
