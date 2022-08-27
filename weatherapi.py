# setup account at https://home.openweathermap.org/users/sign_up
# training at https://app.pluralsight.com/course-player?clipId=bea1b3e4-27e6-461b-8363-922520d641a1 
import requests
def get_weather_desc_temp():
    api_key = 'a99cf0dda721cf441f976897272bc6b8'
    city = 'Detroit'
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units=imperial'
    request = requests.get(url)
    json = request.json()
    print(json)
    #json formatter url to parse the json. Copy the raw json to the site, parse, then copy the parsed data to weather.json in VS
    description = json.get('weather')[0].get('description')
    temp_min = json.get('main').get('temp_min')
    temp_max = json.get('main').get('temp_max')
    return {'description': description, 
            'temp_min': temp_min, 
            'temp_max': temp_max}
def main():
    #print the results
    weather_dict = get_weather_desc_temp()
    print('Todays forecast is', weather_dict.get('description'))
    print('The minimum temp is', weather_dict.get('temp_min'))
    print('The maximum temp is', weather_dict.get('temp_max'))
main()

