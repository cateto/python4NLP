f = open('hitsong.csv', "w", encoding="UTF-8")

singers = ["박정현", "임창정", "izi", "아이유"]
songs = ["꿈에", "소주한잔", "응급실", "좋은날"]
for i in range(len(singers)):
    f.write(singers[i] + ',' + songs[i] + '\n')

f.close()