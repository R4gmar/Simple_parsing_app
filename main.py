from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.olx.pl/motoryzacja/samochody/poznan/?search%5Bfilter_float_price:from%5D=6000&search%5Bfilter_float_price:to%5D=10000&search%5Bfilter_float_year:from%5D=2005&search%5Bfilter_float_year:to%5D=2010&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_condition%5D%5B0%5D=notdamaged")
data = response.text

soup = BeautifulSoup(data, 'html.parser')
name_list = []
link_list = []
price_list = []
name_and_price = soup.find_all(name="div", class_="css-u2ayx9")
for title in name_and_price:
    name = title.getText()
    name_list.append(name)


link_tag = soup.find_all(name="a", class_="css-rc5s2u")
for link in link_tag:
    car_link = link.get("href")
    link_list.append(car_link)
olx_list = [f"olx.pl{name}" for name in link_list]

price_tag = soup.find_all(name="p", class_="css-10b0gli er34gjf0")
for price in price_tag:
    price_list.append(price.getText())
new_price_list = [int(''.join(filter(str.isdigit, element))) for element in price_list]

# print(name_list)
# print(olx_list)
# print(new_price_list)
for price in new_price_list:
    if price < 7000:
        position = new_price_list.index(price)
        print(link_list[position])

