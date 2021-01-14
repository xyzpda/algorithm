totalScore = 0
totalCount = 0

while True:
    inputedScore = int(input("点数を入力してください：")) 
    if inputedScore == -1:
        break
    totalScore += inputedScore
    totalCount += 1
    
print(totalCount, "人のテストの平均点は", totalScore / totalCount ,"点です")