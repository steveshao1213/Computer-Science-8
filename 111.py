#Local scope
def dbl(x):

    x = 2*x

    return x
#Global scope
y = 2

x = 5

x=dbl(y)

print(x, y, dbl(y))
#At this case, x has been changed into dbl(y), which is 2*x

z = dbl(12, 2)
print(z)