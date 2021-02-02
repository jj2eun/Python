# 문자열 재정렬
s = str(input())
str1=[]
str2=[]
for i in range(len(s)):
    if(ord(s[i]) >= 65 and ord(s[i]) <= 90):
        str1.insert(i,str(s[i]))
    else:
        str2.insert(i,str(s[i]))
str1.sort()
str1.sort()
print(''.join(str1+str2))

