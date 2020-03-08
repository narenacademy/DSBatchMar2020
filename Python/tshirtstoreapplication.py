<<<<<<< HEAD
takeorder()
print "hello"
print'hiiii'
=======
def takeorder():
    size=input('Enter size as S,M,L')
    colour=input ('Enter Colour as R,G,B')
    cloth=input ('Enter Cloth as C,S')
    validate(size,color,cloth)
def takeorder():
    size=input('Enter size as S,M,L')
    colour=input ('Enter Colour as R,G,B')
    cloth=input ('Enter Cloth as C,S')
    validate(size,color,cloth)
def validate(size,color,cloth):
    if((size=='S' or size== 'M' or size == 'L') and (color=='R' or color== 'G' or color== 'B') and (cloth=='C' or cloth== 'S')):
        placeorder(size,color,cloth,'True')
    else:
        placeorder(size,color,cloth,'False')
>>>>>>> 31c80fa8d15ba4bea244434340f2a49e9504a66d
