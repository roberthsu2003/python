import game
if __name__ == "__main__":
    print("＝＝＝＝＝＝＝＝＝猜數字遊戲===============:\n\n")
    while(True):
        game.guess_num()
        playagain = input("還要繼續嗎?(y,n)")
        if playagain == 'n':
            break
    print("GameOver")