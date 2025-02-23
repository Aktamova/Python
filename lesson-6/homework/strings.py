Task 1
reverse word
a = input("Write a word ")
c = len(a)- 1
r = ''
while c >= 0:
    b = a[c] 
    c -=1
    r += b
print(r)
Task 2
Count vowels from word 
txt = input("Write a word ")
a = 0
for x in txt:
    if x in '[aeiouAEIOU]':
        a+=1
a
Task 3 Find max number from list
ls = [5, 3, 8, 2, 9, 4]

max = 0
for x in ls:
    if x > max:
        max = x
max
