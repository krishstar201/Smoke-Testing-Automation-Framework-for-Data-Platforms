from functions import Functions
from kpi_version_check import kpi_version_check
from pipeline import Pipeline
from check_core import core_version
from data_service_version_check import data_service_version_check
import config

class Version_check:
    def version_check(driver):
        core_version(driver)
        Pipeline.pipeline_version_check(driver)
        kpi_version_check(driver)
        data_service_version_check(driver)


