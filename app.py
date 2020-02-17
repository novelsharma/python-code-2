

def logic(a,b,c='a'):
    if c == 'a':
        return a+b 
    elif c== 'sub':
        return a-b 
    elif c == 'mul':
        return a * b 
    elif c == 'div':
        return a / b
    elif c == 'sqr':
        return a ** b
    else:
        return ''

def add(a,b):
    print(a+b)

    def sub():
        x = 120 
        y = 200 
        return y - x
    print(sub())

add(2,3)


# print(logic(10,20,'mul'))
# print(logic(5,6,'add'))
# print(logic(5,2,'div'))

a = 1
b = 1 
c = 3 

if not (a == b and (a < c or b == c)):
    print('hello')
else:
    print('hey')