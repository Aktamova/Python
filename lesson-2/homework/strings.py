## Homework 1

Extract car names from this text.

txt = 'MsaatmiazD'


txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[-1::-2]
print(f"first car is {car1} Second car is {car2}")
## Homework 2

Extract residence are from this text.

txt = "I'am John. I am from London"
txt = "I'm John. I am from Paris."

r = txt.split()[-1]
r
