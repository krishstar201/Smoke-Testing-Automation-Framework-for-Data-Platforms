import time
from functions import Functions
from pynput.keyboard import Key, Controller
import config
from plyer import notification


class Sql:
    @staticmethod
    def sql(driver):
        driver.get(config.sql_url)
        time.sleep(5)
        driver.get(config.sql_query_url)

        # Select database
        sql_database = Functions.wait_and_find_element_10(driver, "//span[contains(.,'Database')]/following-sibling::div")
        if sql_database is None:
            Functions.append_to_notepad(config.file_path, config.error + "database not found in sql")
            print("database not found in sql")
            Functions.handle_error(driver)
        else:
            sql_database_input = Functions.wait_and_find_element_10(driver, "//span[contains(.,'Database')]/following-sibling::div//input")
            sql_database_input.send_keys("sample_db")

            # Select schema
            sql_schema = Functions.wait_and_find_element_10(driver, "//label[text()='Schema']/../following-sibling::div//span[2]")
            if sql_schema is None:
                Functions.append_to_notepad(config.file_path, config.error + "schema not found in sql")
                print("schema not found in sql")
                Functions.handle_error(driver)
            else:
                sql_database_input = Functions.wait_and_find_element_10(driver, "//span[contains(.,'Schema')]/following-sibling::div//input")
                sql_database_input.send_keys("sample_schema")

                # Click input bar
                sql_input = Functions.wait_and_find_element_10(driver, "//div[@class='ace_scroller']")
                if sql_input is None:
                    Functions.append_to_notepad(config.file_path, config.error + "input not found in sql")
                    print("input not found in sql")
                    Functions.handle_error(driver)
                else:
                    # Notify the user before interacting with the SQL input
                    notification.notify(
                        title="Automation Running",
                        message="The browser window will now pop up for testing. Please avoid interacting with other windows.",
                        timeout=3  # Show for 5 seconds
                    )

                    # Minimize the window
                    driver.minimize_window()  # Minimize the browser window
                    time.sleep(1)  # Wait for the browser to minimize

                    # Maximize the window to bring it back to the foreground
                    try:
                        driver.maximize_window()  # Maximize the browser window
                    except:
                        print("Browser window already maximized.")

                    time.sleep(1)  # Allow time for the browser to maximize

                    # Focus on the SQL input element
                    sql_input.click()
                    time.sleep(2)

                    # Use keyboard to select all
                    keyboard = Controller()
                    keyboard.press(Key.ctrl)
                    keyboard.press('a')  # Select all text in the input box
                    keyboard.release('a')
                    keyboard.release(Key.ctrl)

                    # Delete all selected text
                    keyboard.press(Key.delete)
                    keyboard.release(Key.delete)
                    time.sleep(2)

                    # Input query
                    keyboard.type("show tables")
                    time.sleep(2)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)

                    # Select dropdown
                    sql_dropdown = Functions.wait_and_find_element_10(driver, "//*[contains(text(), 'LIMIT')]")
                    if sql_dropdown is None:
                        Functions.append_to_notepad(config.file_path, config.error + "dropdown not found in sql")
                        print("dropdown not found in sql")
                        Functions.handle_error(driver)
                    else:
                        sql_dropdown.click()
                        # Select 10 in dropdown
                        sql_10 = Functions.wait_and_find_element_10(driver, "//*[text()='10']")
                        if sql_10 is None:
                            Functions.append_to_notepad(config.file_path, config.error + "10 not found in sql")
                            print("10 not found in sql")
                            Functions.handle_error(driver)
                        else:
                            sql_10.click()
                            # Select run
                            sql_run = Functions.wait_and_find_element_10(driver, "//button[contains(span/text(), 'Run')]")
                            if sql_run is None:
                                Functions.append_to_notepad(config.file_path, config.error + "Run not found in sql")
                                print("run not found in sql")
                                Functions.handle_error(driver)
                            else:
                                sql_run.click()
                                time.sleep(10)
                                driver.save_screenshot(config.screenshot + "sql.png")
                                time.sleep(2)
                                Functions.append_to_notepad(config.file_path, "Testing was done successfully in SQL")
                                print("Testing was done successfully in SQL")
