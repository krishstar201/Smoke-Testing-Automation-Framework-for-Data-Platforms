from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from datetime import date
from functions import Functions
import config
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def data_flow(driver):
    driver.get(config.data)
    time.sleep(2)
    # function to open new tab
    Functions.handle_error(driver)
    time.sleep(2)
    df_task = Functions.wait_and_find_element_30(driver, "//*[contains(text(), 'Task executions')]")
    if df_task is None:
        print("error while selecting task execution")
    else:
        df_task.click()
        df_dropdown = Functions.wait_and_find_element_30(driver, "//select[contains(@class,'clr-page-size-select')]")
        if df_dropdown is not None:
            # Wait for the dropdown to be interactable
            df_dropdown.send_keys(Keys.ENTER)
            time.sleep(7)
        else:
            print("Dropdown element not found or clickable.")
        df_100 = Functions.wait_and_find_element_10(driver, "//*[text()='100']")
        if df_100 is None:
            print("error while selecting 100 in dropdown")
            Functions.append_to_notepad(config.file_path, "error while selecting 100 in dropdown")
        else:
            df_100.click()
            time.sleep(20)
            df_execution = Functions.wait_and_find_element_click_10(driver, "//*[contains(text(), 'Execution Id')]")
            if df_execution is None:
                print("error while selecting execution")
                Functions.append_to_notepad(config.file_path, "error while selecting execution" )
            else:
                df_execution.click()
                time.sleep(15)

                #for new tab automation
                window_handles = driver.window_handles

                #get today's date
                today = date.today()
                today_string = today.strftime("%Y-%m-%d")
                print("Today's date (string):", today_string)
                time.sleep(5)
                #get all row's
                list = driver.find_elements(By.XPATH, "//clr-dg-row[@role='rowgroup']")
                for each in list:
                    start_date_element = each.find_element(By.XPATH, ".//clr-dg-cell[@role='gridcell'][5]")
                    status_element = each.find_element(By.XPATH, ".//clr-dg-cell[@role='gridcell'][7]")
                    start_date = start_date_element.text
                    status = status_element.text
                    if today_string in start_date and (status == "1" or status == "2"):
                        element_id = each.find_element(By.XPATH, ".//clr-dg-cell[@role='gridcell'][1]//a")
                        link = element_id.get_attribute("href")
                        print(link)
                        # Open the link in a new tab
                        driver.execute_script("window.open('{}', '_blank');".format(link))
                        time.sleep(5)
                        # Switch back to the original tab
                        driver.switch_to.window(driver.window_handles[0])
                        Functions.append_to_notepad(config.file_path, "link for error DF" + link)

                print("Testing was Done Successfully in Data Flow")
                Functions.append_to_notepad(config.file_path, "Testing was Done Successfully in Data Flow")




