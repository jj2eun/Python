n = int(input())

h = 0
m = 0
s = 0
count = 0
while(h < n+1):
    if(s == 60):
        s = 0
        m += 1
    if(m == 60):
        m = 0
        h += 1
    if(s%10 == 3 or s//10 == 3 or m%10 == 3 or m//10 == 3 or h%10 == 3 or h//10 == 3):
        count += 1
    s += 1
print(count)