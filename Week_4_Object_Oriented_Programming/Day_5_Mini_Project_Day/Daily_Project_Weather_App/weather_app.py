from pyowm.owm import OWM
api_key = "889a67620e05d11ec46eb9dc6739f954"
owm = OWM(api_key)
mgr = owm.weather_manager()
polution_mgr = owm.airpollution_manager()


def weather_forecast():
    try:
        user_input = int(input(
            f"{"-"*30}\nPlease select input option:\n1. City name\n2. City id\n3. City coordinates\n4. Exit\n{"-"*30}"))
        if user_input == 1:
            city = input("Please select city...")
            weather = mgr.weather_at_place(city).weather
        elif user_input == 2:
            city_id = int(input("Please input city_id..."))
            weather = mgr.weather_at_id(city_id).weather
        elif user_input == 3:
            lat = float(input("Please input Latitude..."))
            lon = float(input("Please input Longitude ..."))
            weather = mgr.weather_at_coords(lat, lon).weather
        elif user_input == 4:
            return
        my_city_id = 2643743
        weather = mgr.weather_at_id(my_city_id).weather
        weather_discription = weather.detailed_status
        temp_celsius = weather.temperature('celsius')
        wind_speed = weather.wind()["speed"]
        sunrise_info = weather.sunrise_time(timeformat='iso')
        sunset_info = weather.sunset_time(timeformat='iso')

        print(f"Today weather: {weather_discription}\nTemperature: {temp_celsius["temp"]}\nFeels like:{
            temp_celsius["feels_like"]} \nWind speed: {wind_speed}\nSunrise time: {sunrise_info}\nSunset time: {sunset_info}")
        weather_forecast()

    except:
        print("Wrong input")
        weather_forecast()


weather_forecast()
