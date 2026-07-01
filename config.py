import datetime
import os

# Base folder (portable, no local paths)
base_folder_path = "./logs"

# Create today's log file
today_date = datetime.date.today().strftime("%Y-%m-%d")
log_file_name = f"smoke_test_log_{today_date}.txt"
file_path = os.path.join(base_folder_path, log_file_name)

# Ensure folder exists
os.makedirs(base_folder_path, exist_ok=True)

#  Dummy credentials (safe for GitHub)
email = "example@email.com"
username = "your_username"
password = "your_password"

# Dummy URLs (replace internally when using locally)
full_url = "https://example.com"
auth_url = full_url + "/login"

# Module URLs (generic placeholders)
pipeline_URL = full_url + "/pipeline"
data_catalog_URL = full_url + "/data-catalog"
relationship_manager_URL = full_url + "/relationship-manager"
reference_data_manager_URL = full_url + "/reference-data-manager"
data_profiler_URL = full_url + "/data-profiler"
data_bridging_URL = full_url + "/data-bridging"
enhanced_view_URL = full_url + "/enhanced-view"
data_explorer_URL = full_url + "/data-explorer"

#  Extra modules
orch = full_url + "/orch"
stream = full_url + "/streams"

# Logging messages
error = "ERROR: "
correct = " ✅ correct"
not_correct = " ❌ mismatch"
no_error_in_page = "No error found in page"
new_line = " "

# Feature labels
data_pipeline = "Pipeline Version: "
data_catalog = "Data Catalog Version: "
relationship_manager = "Relationship Manager Version: "
reference_data_manager = "Reference Data Manager Version: "
data_profiler = "Data Profiler Version: "
data_bridging = "Data Bridging Version: "
enhanced_view = "Enhanced View Version: "
data_explorer = "Data Explorer Version: "
kpi = "KPI Version: "
core = "Core Version: "

# Expected versions (dummy values)
Pipeline_version_expected = "1.0.0"
Data_catalog_version_expected = "1.0.0"
Relationship_manager_version_expected = "1.0.0"
Reference_data_manager_version_expected = "1.0.0"
Data_profiler_manager_version_expected = "1.0.0"
Data_bridging_version_expected = "1.0.0"
Enhanced_view_version_expected = "1.0.0"
Data_explorer_version_expected = "1.0.0"
KPI_version_expected = "1.0.0"
Core_version_expected = "1.0.0"

#  Screenshot path
screenshot = "./logs/screenshots/"
os.makedirs(screenshot, exist_ok=True)

# Outlook placeholders (for OTP systems)
outlookfolder = "Inbox"
outlooksubfolder = "Subfolder"
