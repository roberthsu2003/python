import random

a=1
b=2
c=3
def get_description():
    possibilities = ['rain', 'snow', 'sleep', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)
#print("現在report的name是"+__name__)
if __name__ == "__main__":
    print(get_description())