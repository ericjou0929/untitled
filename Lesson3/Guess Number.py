# import random as r
# ans = r.randint(1,99)
# min = 0
# max = 100
# while True:
#     Guess = int(input('請輸入數字 %d ~ %d :' % (min , max)))
#     if Guess == ans:
#         print("恭喜答對了")
#         break;
#     elif Guess < ans:
#         min = Guess
#     else:
#         max = Guess

import random as r
ans = r.randint(1,99)
min = 0
max = 100
while True:
    Guess = int(input('請輸入數字 %d ~ %d :' % (min , max)))
    # 先驗證數字是否在範圍內
    if Guess <= min or Guess >= max:
        print("數字範圍錯誤,重新輸入 : ")
        continue
    # 進行遊戲比對
    if Guess == ans:
        print("恭喜答對了")
        break;
    elif Guess < ans:
        min = Guess
    else:
        max = Guess


