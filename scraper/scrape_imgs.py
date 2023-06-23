
import requests
from bs4 import BeautifulSoup


class Find_images:
    # def scraper_unsplash(url=str):
    # base_url = "https://unsplash.com/"

    #     r = requests.get(url)
    #     soup = BeautifulSoup(r.text, "lxml")

    #     counter = 0
    #     # all_images = soup.find_all("a", class_="rEAWd")
    #     all_images = soup.find_all("img", class_="tB6UZ a5VGX")
    #     for i in all_images:
    #         # complete url
    #         print(i["src"])
    #         # print(base_url + i["href"])
    #         counter += 1

    #     print(f"\nNumber of images: {counter}")
    # =========================================
   
    
    # def scraper_pexels(url=str):
    #     r = requests.get(url)
    #     soup = BeautifulSoup(r.text, "lxml")

    #     print(r.text)
    #     counter = 0
    #     all_images = soup.find_all("img", class_="spacing_noMargin__Q_PsJ MediaCard_image__ljFAl")
    #     for i in all_images:
    #         # complete url
    #         print(i["src"])
    #         # print(base_url + i["href"])
    #         counter += 1

    #     print(f"\nNumber of images: {counter}")
    # =========================================

    def scraper_wallpapers(url=str, tag_name=str):
        base_url_wallpapers = "https://wallpapers.com"

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        counter = 0
        # all_images = soup.find_all("a", class_="rEAWd")
        all_images = soup.find_all(tag_name)
        for i in all_images:
            # complete url
            print(base_url_wallpapers + i["srcset"])
            counter += 1

        print(f"\nNumber of images: {counter}")
    # =========================================

# *************************************************

# url_cars = "https://unsplash.com/wallpapers/cars"
# url_food = "https://unsplash.com/s/photos/food"
# url_nature = "https://unsplash.com/s/photos/nature"
# Find_images.scraper_unsplash(url_cars)


# url_coffee = "https://www.pexels.com/search/coffee/"
# Find_images.scraper_pexels("https://www.pexels.com/search/coffee/")


url = "https://wallpapers.com/search/games"
Find_images.scraper_wallpapers(url, "source")