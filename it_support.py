from functions import Functions
import config
from data_flow import data_flow
from orchflow import  orch_flow

class it_support_task:
    def Data_flow(driver):
        data_flow(driver)
        Functions.append_to_notepad(config.file_path, "Data Flow done")

    def Orch_flow(driver):
        orch_flow(driver)
        Functions.append_to_notepad(config.file_path, "Orch Flow done")

    def it_support(driver):
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, "It Support start")
        Functions.append_to_notepad(config.file_path, "Data Flow")
        data_flow(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, "Orch Flow")
        orch_flow(driver)
        Functions.append_to_notepad(config.file_path, "It Support Ends")
