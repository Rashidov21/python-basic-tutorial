import requests
from bs4 import BeautifulSoup as bs
# pip install beautifulsoup4
# pip install requests
url = "https://pyblog.uz"
next_page = "https://pyblog.uz/?page=3"
# print(requests.get(url).status_code)  # 200

page = requests.get(url)
soup = bs(page.text, "html.parser")

links = []

images_link = soup.find_all("img")
for image in images_link:
    # url +  /pybloguz/media/posters/2022-06-22/batman.png
    # https://pyblog.uz/pybloguz/media/posters/2022-06-22/batman.png
    # links.append(url + image["src"])
    image_name = image["src"].split(
        "/")[len(image["src"].split("/")) - 1].replace(".png", "")
    links.append({"name": image_name, "src": url + image["src"]})

links.pop(0)
for x in links:

    img_data = requests.get(x["src"]).content

    with open(f'{x["name"]}.png', 'wb') as handler:
        handler.write(img_data)
