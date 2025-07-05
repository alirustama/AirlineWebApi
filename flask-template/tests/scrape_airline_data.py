import requests
from bs4 import BeautifulSoup

def scrape_airline_data():
    url = "https://www.exampleairline.com/flights"  # Replace with a real URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for flight in soup.find_all('div', class_='flight-info'):
        route = flight.find('span', class_='route').text
        price = flight.find('span', class_='price').text
        date = flight.find('span', class_='date').text
        data.append({'route': route, 'price': price, 'date': date})

    return data
