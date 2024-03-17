from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    try:
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        print("Searching in google......\n")

        soup = BeautifulSoup(res.text, 'html.parser')

        location = soup.find('div', class_='BNeawe iBp4i AP7Wnd').getText()
        time = soup.find('div', class_='BNeawe tAd8D AP7Wnd').getText()
        info = soup.find('div', class_='BNeawe tAd8D AP7Wnd').getText()
        weather = soup.find('span', class_='BNeawe').getText()

        print(location)
        print(time)
        print(info)
        print(weather)
    except Exception as e:
        print("An error occurred:", e)


print("Enter the city name:")
city = input()
city = city + " weather"
weather(city)
