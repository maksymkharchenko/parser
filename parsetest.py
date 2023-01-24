from bs4 import BeautifulSoup
import requests
import json


# #посилання на сайт (всі сторінки (204))
url = ("https://uakino.club/filmy/page/1/")

# #Прописую Юзер-Агенти (без них 404)
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# # Отримую код сторінки
req = requests.get(url, headers=headers)
src = req.text
# print(src)

# # Записую html фвйл в index.html, виставляю кодування utf-8 
# with open("index.html", "w", encoding="utf-8") as file: 
#     file.write(src)

# with open("index.html", encoding="utf-8") as file: 
#     src = file.read()


# Створюю словник , який містить посилання на фільм та назву, зберігаю інформацію в json файлі   
# soup = BeautifulSoup(src, "lxml")
# all_films = soup.find_all(class_ ="movie-title")


# all_films_dict = {}
# for item in all_films:
#     item_text = item.text
#     item_href = item.get("href")
#     print(f"{item_text}: {item_href}")

#     all_films_dict[item_text] = item_href

# with open("all_films_dict.json", "w") as file:
#     json.dump(all_films_dict, file, indent=4, ensure_ascii=False)
    
with open("all_films_dict.json") as file:
    all_title = json.load(file)

count = 0    
for title_name, title_href in all_title.items():
    try:
    
        rep = [ "\n","\t","," , " ", "-"]
        for item in rep:
            if item in title_name:
                title_name = title_name.replace(item, " ")
                print(title_name)
                
        req = requests.get(url= title_href, headers= headers)
        src = req.text
        
        with open(f"data/{count}{title_name}.html","w",encoding="utf-8") as file :
            file.write(src)
            
        count += 1
        
    except:
        OSError
            
        
