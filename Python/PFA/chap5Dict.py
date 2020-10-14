def func(b):
   SUM = sum(b)
   print "Total Number of items:",SUM

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
a=[]
a=stuff.values()
print('Inventory\n')
for x, y in stuff.items():
    print y, x
func(a)

