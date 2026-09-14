import requests
from config import API_KEY
#enter their city
city=input("Enter the city toget weather for:")
#api url-where we will get the data from
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#get a response
response=requests.get(url)
#convert into json
data=response.json()
if response.status_code==200:
    #successfull respose
    temperature=data["main"]["temp"]#get the temperature
    weather=data["weather"][0]["description"]#weather description
    #display the output
    print("\nWeather Information")
    print("-"*30)#seperation
    print("City:",city)
    print("Temperature (°C):", temperature)
    print("Description:", weather)
    print("-"*30)
else:
    print("City Not Found.")