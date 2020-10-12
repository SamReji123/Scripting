def colatz(num):
    if(num%2==0):
        num=num/2
        print(num)
    else:
        num = (3*num)+1
        print(num)
    if(num==1):
        exit()
    else:
        colatz(num)

print('enter the number')
try:
    number=int(input())
except:
    print('Incorrect entry')
    exit()
colatz(number)
