char_count = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)
inputed_word_list = []

while True:
    inputed_word = input("英単語を入力してください：")
    
    if inputed_word == "":
        break;
        
    inputed_char_list = list(inputed_word)
    
    for inputed_char in inputed_char_list:
        char_count[inputed_char] += 1
    
    inputed_word_list.append(inputed_word)

inputed_word_list.sort()
print("入力した英単語：", inputed_word_list)

for key, value in char_count.items():
    if value == 0:
        continue
    
    print(f"{key}が{value}個ありました")