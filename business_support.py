from pipeline import Pipeline
from relationship_manager import Relationship_manager
from data_catalog import Data_catalog
from reference_data_manager import Reference_data_manager
from data_profiler import Data_profiler
from data_bridging import Data_bridging
from enhanced_view import Enhanced_view
from data_explorer import Data_explorer
from business_rule_manager import Business_rule_manager
from sql import Sql
from functions import Functions
import config

class Businessupport_task:
    def pipeline(driver):
        Pipeline.pipeline_version_check(driver)
        Pipeline.pipeline_module1(driver)
        Pipeline.pipeline_module2(driver)
        Pipeline.pipeline_module3(driver)
        Pipeline.pipeline_module4(driver)
        Pipeline.pipeline_module5(driver)
        Pipeline.pipeline_module6(driver)
        Pipeline.pipeline_module7(driver)
        Functions.append_to_notepad(config.file_path, "Data Pipeline Module Testing done")

    def relationship_manager(driver):
        Relationship_manager.relationship_manager_version_check(driver)
        Relationship_manager.relationship_manager_module1(driver)
        Relationship_manager.relationship_manager_module2(driver)
        Relationship_manager.relationship_manager_module3(driver)
        Relationship_manager.relationship_manager_module4(driver)
        Relationship_manager.relationship_manager_module5(driver)
        Relationship_manager.relationship_manager_module6(driver)
        Relationship_manager.relationship_manager_module7(driver)
        Functions.append_to_notepad(config.file_path, "Relationship done")

    def data_catalog(driver):
        Data_catalog.data_catalog_version_check(driver)
        #Data_catalog.data_catalog_module1(driver)
        Data_catalog.data_catalog_module2(driver)
        Functions.append_to_notepad(config.file_path, "data catalog done")

    def reference_data_manager(driver):
        Reference_data_manager.reference_data_manager_version_check(driver)
        Reference_data_manager.reference_data_manager_module1(driver)
        Functions.append_to_notepad(config.file_path, "reference data manager done")

    def data_profiler(driver):
        Data_profiler.data_profiler_check_version(driver)
        Data_profiler.data_profiler(driver)
        Functions.append_to_notepad(config.file_path, "data profiler done")

    def data_bridging(driver):
        Data_bridging.data_bridging_check_version(driver)
        Data_bridging.data_bridging_module1(driver)
        Data_bridging.data_bridging_module2(driver)
        Data_bridging.data_bridging_module3(driver)
        Data_bridging.data_bridging_module4(driver)
        Data_bridging.data_bridging_module5(driver)
        Functions.append_to_notepad(config.file_path, "data bridging done")

    def enhanced_view(driver):
        Enhanced_view.enhanced_view_check_version(driver)
        Enhanced_view.enhanced_view_module1(driver)
        Enhanced_view.enhanced_view_module2(driver)
        Enhanced_view.enhanced_view_module3(driver)
        Functions.append_to_notepad(config.file_path, "enhanced view done")

    def data_explorer(driver):
        Data_explorer.data_explorer_check_version(driver)
        Data_explorer.data_explorer_module1(driver)
        Functions.append_to_notepad(config.file_path, "data explorer done")

    def business_rule_manager(driver):
        Business_rule_manager.business_rule_manager_check_version(driver)
        Business_rule_manager.business_rule_manager_module1(driver)
        Business_rule_manager.business_rule_manager_module2(driver)
        Functions.append_to_notepad(config.file_path, "business rule manager done")


    def sql(driver):
        Sql.sql(driver)
        Functions.append_to_notepad(config.file_path, "sql done")

    def business_support(driver):
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.Business_support_start)
        Businessupport_task.pipeline(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.relationship_manager)
        Businessupport_task.relationship_manager(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.data_catalog)
        Businessupport_task.data_catalog(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.reference_data_manager)
        Businessupport_task.reference_data_manager(driver)
        #Functions.append_to_notepad(config.file_path, config.new_line)
        #Functions.append_to_notepad(config.file_path, config.sql)
        #Businessupport_task.sql(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.data_profiler)
        Businessupport_task.data_profiler(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.data_bridging)
        Businessupport_task.data_bridging(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.enhanced_view)
        Businessupport_task.enhanced_view(driver)
        # Functions.append_to_notepad(config.file_path, config.new_line)
        # Functions.append_to_notepad(config.file_path, config.data_explorer)
        # Businessupport_task.data_explorer(driver)
        Functions.append_to_notepad(config.file_path, config.new_line)
        Functions.append_to_notepad(config.file_path, config.business_rule_manager)
        Businessupport_task.business_rule_manager(driver)
        Functions.append_to_notepad(config.file_path, config.Business_support_done)


