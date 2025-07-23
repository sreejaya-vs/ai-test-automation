import os
import yaml
from dotenv import load_dotenv
from test_case_generator import generate_test_cases
from appium_script_generator import generate_appium_scripts

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    load_dotenv()
    config = load_config()
    
    user_story_path = input("Enter path to user story document: ")
    figma_url = input("Enter Figma file URL: ")
    app_path = input("Enter path to APK/IPA file: ")
    
    test_case_csv = generate_test_cases(user_story_path, figma_url, config)
    print(f"Test cases generated at: {test_case_csv}")
    
    script_path = generate_appium_scripts(test_case_csv, figma_url, app_path, config)
    print(f"Appium scripts generated at: {script_path}")

if __name__ == "__main__":
    main()