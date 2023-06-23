from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()
url = "https://za.indeed.com/m/jobs?sc=0kf%3Ajt%28parttime%29%3B&q=casual+work&l=cape+town%2C+western+cape"
driver.get(url)

# Find elements using the appropriate selectors
job_title = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
company = driver.find_elements(By.CLASS_NAME, "companyName")
location = driver.find_elements(By.CLASS_NAME, "companyLocation")

# Define the Details class
class Details:
    all_job_details = {
        "job title": "",
        "url": "",
        "company name": "",
        "suburban area": "",
        "job type": "",
        "other details": []
    }

    test = "jams"

    def display(self):
        print(self.all_job_details)

# Extract the job details and store them in lists
job_titles_list = [title.text for title in job_title]
job_urls_list = [title.get_attribute("href") for title in job_title]
company_names_list = [comp.text for comp in company]
location_list = [loc.text for loc in location]

# Quit the WebDriver
driver.quit()
print("\n<SUCCESS>\n")

# Create an instance of the Details class
details = Details()

# Assign the first job title to the "job title" key in the "all_job_details" dictionary
details.all_job_details["job title"] = job_titles_list[0]

# Print the contents of the "all_job_details" dictionary using the display method
details.display()
