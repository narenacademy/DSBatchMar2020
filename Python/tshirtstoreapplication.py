<<<<<<< HEAD
takeorder()
print "hello"
print'hiiii'
=======
def validate(size,color,cloth):
    if((size=='S' or size== 'M' or size == 'L') and (color=='R' or color== 'G' or color== 'B') and (cloth=='C' or cloth== 'S')):
        placeorder(size,color,cloth,'True')
    else:
        placeorder(size,color,cloth,'False')
>>>>>>> 31c80fa8d15ba4bea244434340f2a49e9504a66d
def placeorder(size,color,cloth,orderstatus):
if (orderstatus == true)
    print('your order is placed with size or color or clothe type:',size,color,cloth)
else
    print('your order is not placed as its out of stock')