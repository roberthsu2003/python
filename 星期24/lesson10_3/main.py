import youbike

if __name__ == "__main__":
    youbike_info= youbike.get_youbike_info()
    if youbike_info is None:
        print("請等一下再試")
    else:
        print(youbike_info)