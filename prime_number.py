for number in range(1, 101):
    
    if number == 1:
        continue
        
    if number == 2 or number == 3 or number == 5 or number == 7:
        print(number)
        continue
    
    if (number % 2) == 0:
        continue
    
    if (number % 3) == 0:
        continue
    
    if (number % 5) == 0:
        continue
        
    if (number % 7) == 0:
        continue
    
    print(number)