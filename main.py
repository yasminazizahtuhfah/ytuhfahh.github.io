from selenium import webdriver

PATH = "E:\scrap\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/chart/top/")

for movie in driver.find_elements_by_class_name("lister-list"):
    print(movie.text)
driver.quit()







