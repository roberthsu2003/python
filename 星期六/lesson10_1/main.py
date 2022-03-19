#from tools import game
#from tools.game import guess_num
from tools import weather

if __name__ == "__main__":
    weatherlist = weather.get_weather_of_taiwan()
    if weatherlist is not None:
        for item in weatherlist:
            print(item)
