#!/usr/bin/python3
'''
#這個應用程式是做什麼的
#要注意什麼
'''
import datasource

def main():
    data_list = datasource.get_pm25()
    for record in data_list:
        print(record['sitename'])

if __name__ == "__main__":
    main()