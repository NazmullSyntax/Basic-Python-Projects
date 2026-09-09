import requests

city = input("Enter city: ")
api_key = "YOUR_API_KEY"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data['cod'] == 200:
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Temperature: {temp}°C")
    print(f"Description: {desc}")
else:
    print("City not found")