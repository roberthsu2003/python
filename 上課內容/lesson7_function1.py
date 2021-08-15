#!/bin/python3.8

def temperature(value_c):
    return 1.8 * value_c + 32


if __name__ == "__main__":
    print(f'攝氏10度轉華氏溫度={temperature(10)}')
    print('-------------------------')