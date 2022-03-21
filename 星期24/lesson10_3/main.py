import youbike

if __name__ == "__main__":
    youbikeList = youbike.get_youbike_info()
    for item in youbikeList:
        print(item)
