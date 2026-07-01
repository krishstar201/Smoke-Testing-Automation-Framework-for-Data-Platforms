# Smoke Testing Automation Framework for Data Platforms

## Overview
This project is a Python-based automation framework designed to perform smoke testing across multiple modules of a data platform.

It automates login, validates system versions, checks UI workflows, detects errors, and logs results across different modules.

---

## Features

- Automated login with authentication handling
- Smoke testing across multiple platform modules
- Version validation (Pipeline, KPI, Core services)
- UI validation using Selenium
- Error detection and logging
- Screenshot capture for failures
- Modular and scalable design

---

## Modules Covered

- Data Pipeline
- Data Catalog
- Relationship Manager
- Reference Data Manager
- Data Profiler
- Data Bridging
- Enhanced View
- Data Explorer
- KPI Library
- Core Services

---

## Project Structure

- `app.py` → Main execution entry point  
- `functions.py` → Common reusable utilities  
- `config.py` → Configuration and environment setup  
- `xpath.py` → Centralized UI locators  

### Module Files
- pipeline.py  
- data_catalog.py  
- relationship_manager.py  
- data_profiler.py  
- data_bridging.py  
- enhanced_view.py  
- reference_data_manager.py  
- business_rule_manager.py  
- others (modular checks)

---

## Tech Stack

- Python  
- Selenium  
- Requests  

---

## How to Run

### Step 1: Install dependencies

    pip install -r requirements.txt

### Step 2: Run the automation

    python app.py

---

## Output

The framework generates logs and screenshots for:

- Version validations  
- Error detection  
- UI checks  
- Module health  

---

## Notes

- This project uses Selenium for browser automation.
- OTP/email integrations are configured for local environments and may require additional setup.
- URLs and credentials in this repository are placeholders for demonstration purposes.

---

## Use Case

This framework can be used for:

- Smoke testing after deployments  
- Validating data platform modules  
- Monitoring system health  
- Automating QA workflows  

---

## Author

Suraj K
