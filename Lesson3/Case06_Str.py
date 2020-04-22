s = " she sell sea shell on the sea shore"
print(s)
print("有 %s 幾 s " % s.count('s'))
print("有 sea 這個字嗎 ? %d"  % s.find("sea"))

# 是否都是a-b,A-Z 英文字
# 技巧 : 先利用replace 去除空白

print(s.replace(" ", "").isalpha())

