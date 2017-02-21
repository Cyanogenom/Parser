import requests
from bs4 import BeautifulSoup
import time

file = open("Texts.txt", "a")
kol = 0

for i in range(10000, 329835):
    site = requests.get("http://4pda.ru/2000/01/01/" + str(i))
    if site.status_code == 200:
        file.write("Статья # " + str(kol) + "\n")
        kol += 1
        title = site.text.split("<title>")[1].split("</title>")[0]
        text = site.text.split('<div class="content">')[1].split('<div class="materials-box">')[0]
        file.write(title + "\n")
        soup = BeautifulSoup(text, "html.parser")
        text = soup.find_all("p")
        for tag_text in text:
            if tag_text.text != "" and tag_text.text != " " and tag_text.text != "\n":
                try:
                    file.write(tag_text.text + "\n")
                except BaseException:
                    print("Can't write this text into file!")
        print(i, "Осталось:", str(i // 3298.35) + "%", title, "kol =", kol)
        time.sleep(0.5)
    else:
        time.sleep(0.001)
file.close()