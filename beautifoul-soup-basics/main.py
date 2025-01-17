from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# #Fetch texts and elements from specific  tag
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# #Fetch only one specific item
# heading = soup.find(name="h1", id="name")
# print(heading)

# #Select a class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

#Selects the first instance when you want to get a specific link or sth
#Uses css selectors
company_url = soup.select_one(selector="p a")
headings = soup.select(".heading")
print(company_url)