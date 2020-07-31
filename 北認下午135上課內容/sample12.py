#!/usr/bin/env python3.7
"""
這個範例是下載網路資料，政府開放平台
"""
no = 1
scores = dict()
if __name__ == "__main__":
    while True:
        score = int(input('請輸入第'+str(no)+'號的成績:(-1結束輸入)'))
        if score == -1:
            break
        scores[no] = score
        no += 1

    file=open('scores.txt', 'w', encoding='utf-8')
    file.write(str(scores))
    file.close()