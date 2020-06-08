import requests
from bs4 import BeautifulSoup

'''
Simple program to demonstrate the use of beautiful soup to pull the price of a product from a web page:
https://www.bigbasket.com/pd/10000200/fresho-tomato-hybrid-1-kg/
<td data-qa="productPrice" class="IyLvo">Rs <!-- -->18</td>
'''


url = 'https://www.bigbasket.com/pd/10000200/fresho-tomato-hybrid-1-kg/'
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

price = soup.find('td', {'data-qa': 'productPrice'})
print(price.text.strip())

item = soup.find('h1', {'class': 'GrE04'})
print(item.text.strip())
