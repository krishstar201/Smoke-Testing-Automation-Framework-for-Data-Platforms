import time
from functions import Functions
import config
from version_check import Version_check
from businessupport import Businessupport_task
from Itsupport import it_support_task

# Record the start time
start_time = time.time()

# Get chromedriver
driver = Functions.get_chrome_driver()

# Call create_folder function to create the base folder
Functions.create_folder(config.tenant, config.base_folder_path)
Functions.create_folder("screenshot", config.screenshot_path)

# Maximize window
driver.maximize_window()

#print tenant name
Functions.append_to_notepad(config.file_path, config.tenant)

# Navigating to the website and performing login
Functions.login_and_verify_loop(driver,config.auth_url, config.full_url, config.outlookfolder, config.outlooksubfolder, config.email, max_attempts=15, wait_time=20)

#check version
Version_check.version_check(driver)

#test all module in Business support
Businessupport_task.business_support(driver)

#test all module in It support
#it_support_task.it_support(driver)

# Record the end time
end_time = time.time()
# Calculate the elapsed time in minutes
elapsed_time = (end_time - start_time) / 60
# Round the elapsed time to one decimal place
rounded_elapsed_time = round(elapsed_time, 1)
# Print the elapsed time
print("Elapsed time:", rounded_elapsed_time)
elapsed_time_str = str(rounded_elapsed_time)

Functions.append_to_notepad(config.file_path, "Total time taken" + elapsed_time_str + "Minutes" )

driver.get(config.it_support_url)

Functions.append_to_notepad(config.file_path, config.new_line)
Functions.append_to_notepad(config.file_path, "Smoke Testing done")





