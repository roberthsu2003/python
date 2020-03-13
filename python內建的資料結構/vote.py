#!usr/bin/python3.8

'''
#============================================================================
# Name        : vote.py
#設計一個投票統計表，包含計算各四位歌手3個地區投票數及總得票數，最後顯示得票數和得票率(計算至小數4位)
#===============================================================

names[0]:周華見
names[1]:劉得華
names[2]:張學有
names[3]:梁朝為
周華見總票數為:1623
周華見得票率為22.7025%

劉得華總票數為:1726
劉得華得票率為24.1432%

張學有總票數為:1519
張學有得票率為21.2477%

梁朝為總票數為:2281
梁朝為得票率為31.9066%

'''

if __name__ == '__main__':
    names = ["周華見", "劉得華", "張學有", "梁朝為"]
    for index,name in enumerate(names):
        print('name[{0:d}]:{1:s}'.format(index,name))

    votes = [[713, 600, 310],[999, 512, 215],[543, 689,287],[1125,387, 769]]

    totalVotes = 0
    for personVotes in votes:
        for vote in personVotes:
            totalVotes += vote;

    data = {}
    for index,name in enumerate(names):
        item = {name:votes[index]}
        data.update(item)

    #comprehension
    #data = {name:votes[index] for index,name in enumerate(names)}
    #print(data)

    for item in data.items():
        name = item[0]
        scores = item[1]
        personScore = 0
        for score in scores:
            personScore += score

        print('{0:s}總票數為:{1:d}'.format(name,personScore))
        print('{0:s}得票率為:{1:.4f}%\n'.format(name,personScore/totalVotes))




