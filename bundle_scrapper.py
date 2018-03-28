import requests
from bs4 import BeautifulSoup

tier_dict = {}
url = "https://www.humblebundle.com/books/diy-electronics-books"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Tiers
tiers = soup.select(".dd-game-row")

for tier in tiers:
	#only headline selections
	if tier.select(".dd-header-headline"):
		#grab tier name (and price)
		tiername = (tier.select(".dd-header-headline")[0].text.strip()).split()[1]
		#grab tier product names
		product_names = tier.select(".dd-image-box-caption")
		product_names = [prodname.text.strip() for prodname in product_names]
		#aa one product to our data structure
		tier_dict[tiername] = {"products": product_names}




#after building data structure			
for tiername, tierinfo in tier_dict.items():
	print(tiername)
	print("##################")
	print("\n".join(tierinfo['products']))
	print("\n\n")
