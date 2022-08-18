price = int(input("税抜価格を入力してください："))
totalprice = int(price * 1.1)
if totalprice < 2000:
    print("送料として350円かかります")
    totalprice += 350
else:
    print("送料は無料です")
print("送料込みの価格は", totalprice, "円です。")