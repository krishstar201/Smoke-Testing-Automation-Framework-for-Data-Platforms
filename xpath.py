# ==========================
# Common XPath Locators
# ==========================

# Version / Dropdown
dropdown_icon = "//mat-icon[normalize-space()='arrow_drop_down']"
version_text = "//*[@class='apollo-version']"

# ==========================
# Pipeline
# ==========================
pipeline_dropdown = dropdown_icon
pipeline_version_text = version_text
pipeline_table = "//*[contains(@class, 'container')]"
pipeline_rows_500 = "//button[contains(text(), '500')]"
pipeline_first_task = "//tr[@role='row']//a[contains(@class,'btn-link')]"
pipeline_schema_navigation = "//*[text()='Task Group Definition']"
pipeline_schema_dropdown = "//*[@class='ng-arrow-wrapper']"
pipeline_connection_strings = "//*[contains(text(), 'View all connection strings')]"

# ==========================
# Relationship Manager
# ==========================
relationship_dropdown = dropdown_icon
relationship_version_text = "//div[contains(@class,'version')]"
relationship_click_item = "//*[contains(@class,'cell-link-decoration')]"

# ==========================
# Data Catalog
# ==========================
data_catalog_dropdown = "//*[@class='mat-icon notranslate material-icons mat-icon-no-color']"
data_catalog_version_text = "//*[@class='version']"
data_catalog_card = "//*[contains(@class,'card-container')]"
data_catalog_element = "//*[contains(@class,'cell-link-decoration')]"

data_catalog_general_tab = "//*[contains(text(), 'General')]"
data_catalog_values_tab = "//*[contains(text(), 'Values')]"
data_catalog_relationship_tab = "//*[contains(text(), 'Relationship')]"
data_catalog_activity_tab = "//*[contains(text(), 'Activity Log')]"

# ==========================
# Reference Data Manager
# ==========================
rdm_dropdown = dropdown_icon
rdm_version_text = "//*[@class='version']"

# ==========================
# Data Profiler
# ==========================
data_profiler_dropdown = dropdown_icon
data_profiler_version_text = "//div[@class='version']"
data_profiler_scroll = "//app-data-profiler[contains(@class,'ng-star-inserted')]"
data_profiler_failed_status = "//*[@class='dot-status dot-failed']"

# ==========================
# Data Bridging
# ==========================
data_bridging_dropdown = dropdown_icon
data_bridging_version_text = "//*[contains(@class,'version')]"
data_bridging_failed = "//*[contains(@style,'background') and contains(@class,'status-coin')]"

# ==========================
# Enhanced View
# ==========================
enhanced_view_dropdown = dropdown_icon
enhanced_view_version_text = "//*[contains(@class,'version')]"

# ==========================
# Data Explorer
# ==========================
data_explorer_dropdown = dropdown_icon
data_explorer_version_text = "//*[contains(@class,'version')]"

# ==========================
# Business Rule Manager
# ==========================
brm_dropdown = dropdown_icon
brm_version_text = "//*[contains(@class,'version')]"

# ==========================
# Error Handling
# ==========================
error_icon = "//*[@class='mat-icon notranslate mr-20 cursor-pointer close-icon material-icons mat-ligature-font mat-icon-no-color']"