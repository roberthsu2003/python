#from tools import game
#from tools.game import guess_num
from tools import weather

if __name__ == "__main__":
    data = weather.get_weather_of_taiwan()
    if data is not None:
        print(f"資料是:{data}")
