d = {}
alpha = "abcdefghijklmnopqrstuvwxyz"

n1, n2 = 0, 1
count = 0
l = []

while count < 26:
    l.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count = count + 1
    
print(l)
for i in range(len(l)):
    d[alpha[i]] = l[i]
    
print(d)

input1= input()
sum = 0
for i in input1:
    sum = sum  + d[i]
    
print(sum)

