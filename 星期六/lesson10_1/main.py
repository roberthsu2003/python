#from tools import game
#from tools.game import guess_num
from tools import weather

if __name__ == "__main__":
    locations = weather.get_weather_of_taiwan()
    if locations is not None:
        for item in locations:
            print(item)
