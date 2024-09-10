from bs4 import BeautifulSoup as bsp
import requests

user = input("Enter username: ")
web = requests.get(f"https://reddit.com/user/{user}")
soup = bsp(web.text, "html.parser")

name = soup.findAll("h1", attrs={"class": "text-24 font-bold m-0"})
bio = soup.findAll("p", attrs={"class": "text-12 text-neutral-content-weak mt-md"})
if(bio):
    bio = ''.join(bio.text.split())
else:
    bio = None
karma = soup.findAll("span", attrs={"class": "font-semibold text-14"})
post_karma = ''.join(karma[0].text.split())
comment_karma = ''.join(karma[1].text.split())
kekde = ''.join(soup.findAll("p", attrs={"class": "m-0 text-neutral-content-strong text-14 font-semibold whitespace-nowrap"})[0].text.split())

if(name): 
    text = ''.join(name[0].text.split())
    print(f"Username: {text}\nReddit Tag: {user.lower()}\nBio:\n{bio}\n")
    print(f"Post Karma: {post_karma}\nComment Karma: {comment_karma}\nCake Day: {kekde}")
else:
    print("That user doesn't exist on Reddit!")