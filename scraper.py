import requests
from bs4 import BeautifulSoup


########### Looking at all the a tags in itai's website
########### itai is a bing alum and hackbu director in 2015 and 2016

webpage = requests.get("https://itaiferber.net/")

soup = BeautifulSoup(webpage.text, "html.parser")

# print(soup.prettify())
a = soup.find_all("a")


for link in a:
    print(link.get("href"))
    pass


# finding all the images in binghamton.edu which is the first link in the list of links from above
# then, after cleaning the urls (line 36 to 41), we download all the images and save them to the current directory

webpage_2 = requests.get(a[0].get("href"))
soup_2 = BeautifulSoup(webpage_2.text, "html.parser")

binghamton_images = soup_2.find_all("img")

img_sources = []

for image in binghamton_images:
    img_sources.append(image.get("src"))

# print(img_sources)

for index, url in enumerate(img_sources):
    if url.startswith("/") and not url.startswith("//"):
        print(url)
        img_sources[index] =  "https://binghamton.edu"+ url
    if url.startswith("//"):
        img_sources[index] = "http://" + url[2:]


for index, url in enumerate(img_sources):
    our_image = requests.get(url)
    with open(str(index) + ".jpeg", "wb") as image_file:
        image_file.write(bytes(our_image.content))
