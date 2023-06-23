
from selenium import webdriver
from selenium.webdriver.common.by import By 



class Details:
    def __init__(self):
        self.job_info = dict()
        

    def display(self):
        for j in self.job_info:
            print(f"{j}: \t{self.job_info[j]}")
        print("\n\n")

    def display_raw(self):
        print(self.job_info)
        

    def write_to_file(self, filename):
        with open(f"{filename}.txt", "w") as f:
            for j in self.job_info:
                f.write(f"{j}: \t{self.job_info[j]}\n")
            f.write("\n\n")
         
        
# **************************************************


class Use_details:
    def __init__(self, search="cook"):
        self.search = search
        # self.search = "cook"
        radius = ""
        location = ""
        self.url = "https://www.pnet.co.za/jobs/{}/in-cape-town?radius=10".format(self.search)
        self.driver = webdriver.Chrome()
        self.jobs = []
        

    def start(self):
        self.driver.get(self.url)

        job_titles = self.driver.find_elements(By.CLASS_NAME, "res-v1ywpt")
        location= self.driver.find_elements(By.CLASS_NAME, "res-9pcvyh")

        for j in range(len(job_titles)):
            details = Details()
            details.job_info["job"] = job_titles[j].text
            details.job_info["url"] = job_titles[j].get_attribute("href")
            details.job_info["location"] = location[j].text

            self.jobs.append(details)


        print("\n<SUCCESS>\n")
        self.driver.quit()


    def display(self):
        count = 0
        for j in self.jobs:
            j.display()
            j.write_to_file("new")

            count += 1

        print(f"{count} jobs")

        print("\n<COMPLETED>\n")


# # **************************************************

user_job = input("Enter a job: ")
# user_job = "programmer"
use = Use_details(user_job)
use.start()
use.display()

# search = "programmer"
# radius = ""
# location = ""
# url = "https://www.pnet.co.za/jobs/{}/in-cape-town?radius=10".format(search)
# driver = webdriver.Chrome()
# driver.get(url)


# jobs = []
# job_titles = driver.find_elements(By.CLASS_NAME, "res-v1ywpt")
# location= driver.find_elements(By.CLASS_NAME, "res-9pcvyh")

# for j in range(len(job_titles)):
#     details = Details()
#     details.job_info["job"] = job_titles[j].text
#     details.job_info["url"] = job_titles[j].get_attribute("href")
#     details.job_info["location"] = location[j].text

#     jobs.append(details)


# print("\n<SUCCESS>\n")
# driver.quit()

# count = 0
# for j in jobs:
#     j.display()
    # j.write_to_file("new_file")

#     count += 1

# print(f"{count} jobs")
# print("\n<COMPLETED>\n")
