from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://za.indeed.com/m/jobs?sc=0kf%3Ajt%28parttime%29%3B&q=casual+work&l=cape+town%2C+western+cape"
driver = webdriver.Chrome()
driver.get(url)

job_title = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
company = driver.find_elements(By.CLASS_NAME, "companyName")
location = driver.find_elements(By.CLASS_NAME, "companyLocation")

class Details:
    def __init__(self):
        self.all_job_details = {
            "job title": "",
            "url": "",
            "company name": "",
            "suburban area": "",
            "job type": "",
            "other details": []
        }

    def display(self):
        for d in self.all_job_details:
            print(f"{d}: {self.all_job_details[d]}")
        print("\n\n")
        

job_details_list = []


for i in range(len(job_title)):
    # details = "name" + str(i)
    details = Details()
    # print(job_title[i].text)

    details.all_job_details["job title"] = job_title[i].text
    details.all_job_details["url"] = job_title[i].get_attribute("href")
    details.all_job_details["company name"] = company[i].text
    details.all_job_details["suburban area"] = location[i].text
    # job_details_list.append("1")
    job_details_list.append(details)
    
print(job_details_list[i-1].display())


driver.quit()

print("\n<SUCCESS>\n")



for job_details in job_details_list:
    print()
    job_details.display()
