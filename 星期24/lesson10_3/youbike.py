def get_youbike_info():
    list1 = [10, 20, 30, 40]
    try:
        print(list1[5])
    except IndexError as e:
        print(e)
    except:
        print("other Error")
    return "info"