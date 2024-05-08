import requests


api_key = '' # Enter your valid OpenWeatherMap API key


while True: # Loop until valid location is entered
    location = input("Location: ")

    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}') # Get weather data
    
    if result.json()['cod'] == '404':
        print("Invalid location!")
        continue
    break
    
desc = result.json()['weather'][0]['description'] # Description of the weather

temp = round(result.json()['main']['temp']) # Temperature

feel = round(result.json()['main']['feels_like']) # Feels like temperature

print(f"The temperature in {location[0].upper()}{location[1:]} is {temp}° C, {desc}.")
print(f"The feels like temperature is {feel}° C.")