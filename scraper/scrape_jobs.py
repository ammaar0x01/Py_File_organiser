
# for za.indeed.com

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

url = "https://za.indeed.com/m/jobs?sc=0kf%3Ajt%28parttime%29%3B&q=casual+work&l=cape+town%2C+western+cape"
driver = webdriver.Chrome()
driver.get(url)

# items = driver.find_element(By.ID, "job_1e416a868e6a2be7")
# items = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
job_title = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle") 
company = driver.find_elements(By.CLASS_NAME, "companyName")
location = driver.find_elements(By.CLASS_NAME, "companyLocation")
                                 

class Details:
    all_job_details = {
            "job title": "",
            "url": "",
            "company name": "",
            "suburban area": "",
            "job type": "",
            "other details": [],
        }


    test = "jams"

    def display(self):
        print(self.all_job_details)

# print(type(location))


items_list = []
items_list0 = []

for i in range(len(job_title)):
    items_list.append(job_title[i].text)
    items_list0.append(job_title[i].get_attribute("href"))

# items_list1 = []
# for i in range(len(company)):
#     items_list.append(company[i].text)


# items_list2 = []
# for i in range(len(location)):
#     items_list2.append(location[i].text)


# job_seen_beacon div
# attribute_snippet div

print(items_list)
print(items_list0)
# print(items_list1)
# print(items_list2)

# print(items.text)
driver.quit()
print("\n<SUCCESS>\n")


# d1 = Details()
# d1.all_job_details["job title"]
# d1.all_job_details["url"]
# d1.all_job_details["company name"]
# d1.all_job_details["location"]
# d1.all_job_details["other"]

name = Details()
print(name.test)
name.all_job_details["job title"] = items_list[0]
print(name.display())


# count = 0
# names = []
# for a in items_list:
#     name = ("name" + str(count))
#     name = Details()

#     name.all_job_details["job title"] = items_list[a]

#     for b in items_list0:
#         name.all_job_details["url"] = items_list[b]
#         names.append(name)

# print(names[0].display())


class Present:
    def __init__(self, obj):
        self.obj = obj 

    def organise(self):
        self.obj.all_job_details["job title"]
        self.d1.all_job_details["url"]
        # d1.all_job_details["company name"]
        # d1.all_job_details["location"]
        # d1.all_job_details["other"]

    
    def display():
        print()

# ============================================
