from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from datetime import date
from functions import Functions
import config
from selenium.webdriver.common.keys import Keys

def orch_flow(driver):
    driver.get(config.orch)
    time.sleep(2)
    # function to open new tab
    Functions.handle_error(driver)
    time.sleep(2)

    print("Testing was Done Successfully in Orch Flow")
    Functions.append_to_notepad(config.file_path, "Testing was Done Successfully in Orch Flow")
