def list(x):
    k=(len(x)-1)
    e=x[k]
    del x[k]
    x.append('and '+ e)
    print ', '.join(x)

List = []

while True:
    print('Enter the list of elements')
    name = raw_input()
    if name == '':
        break
    List = List + [name]
print(List)
list(List)

