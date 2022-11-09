import requests
import bs4

search = 'requests'
response = requests.get(f"https://pypi.org/search/?q={search}&0=")
print(response.status_code)

tree = bs4.BeautifulSoup(response.text, 'html.parser')
# print(tree)
# print(tree.select('.package-snippet'))

for item in tree.select('.package-snippet'):
    name_tag = item.select_one('.package-snippet__name')
    name=name_tag.text
    version = item.select_one('.package-snippet__version').text
    link=item.attrs['href']
    print(name,version,f"https://pypi.org{link}")

print(tree.select_one("#content").text.strip()[:10])
print(tree.select("img"))