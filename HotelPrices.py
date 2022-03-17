from datetime import date
import pandas as pd

import bs4
import requests
from openpyxl import load_workbook

url = [
    'https://sg.hotels.com/ho144875/?q-check-in=2022-11-05&q-check-out=2022-11-07&q-rooms=1&q-room-0-adults=2&q-room'
    '-0-children=0&sort-order=BEST_SELLER',
    'https://sg.hotels.com/ho148806/?q-check-in=2022-11-05&q-check-out=2022-11-07&q-rooms=1&q-room-0-adults=2&q-room'
    '-0-children=0',
    'https://sg.hotels.com/ho596781600/?q-check-in=2022-11-05&q-check-out=2022-11-07&q-rooms=1&q-room-0-adults=2&q'
    '-room-0-children=0&sort-order=BEST_SELLER',
    'https://sg.hotels.com/ho213384/?q-check-in=2022-11-05&q-check-out=2022-11-07&q-rooms=1&q-room-0-adults=2&q-room'
    '-0-children=0&sort-order=BEST_SELLER&WOD=6&WOE=1&MGT=2&ZSX=1&SYE=3&YGF=14']

x = True
while x:
    print("Is there any new hotels to add?")
    user_input = input()
    if user_input != "":
        url.append(user_input)
    else:
        print("No new hotels added.")
        print("Listing watchlist now...\n")
        # print()
        break

watchlist_name = []
watchlist_price = []
today = date.today()
print(today)
for i in range(len(url)):
    res = requests.get(url[i])
    result_text = res.text

    parse_result = bs4.BeautifulSoup(result_text, 'html.parser')
    hotel_name = parse_result.find_all('h1')
    room_price = parse_result.find_all('span', class_='_2R4dw5 _17vI-J')
    hotel = hotel_name[0].text.strip()
    watchlist_name.append(hotel)
    price = room_price[0].text.strip()
    watchlist_price.append(price)
    print(str(i + 1) + '. ' + hotel + ', ' + price)
    new_row = {'Name': hotel, 'Price': price}

watchlist = {'Name': watchlist_name, 'Price': watchlist_price}
df_watchlist = pd.DataFrame(watchlist)
# print(df_watchlist)

# writer = pd.ExcelWriter('HotelWatchlist.xlsx')
# df_watchlist.to_excel(writer, str(today))
# writer.save()

try:
    book = load_workbook('HotelWatchlist.xlsx')
    writer = pd.ExcelWriter('HotelWatchlist.xlsx', engine='openpyxl')

except:
    print('File does not exist. Creating file now...')
    writer = pd.ExcelWriter('HotelWatchlist.xlsx', engine='xlsxwriter')
    df_watchlist.to_excel(writer, '2022-02-22')
    writer.save()
    writer.close()
else:
    writer.book = book
    df_watchlist = pd.DataFrame(watchlist)
    df_watchlist.to_excel(writer, sheet_name=str(today))
    writer.save()
    # writer.close()








