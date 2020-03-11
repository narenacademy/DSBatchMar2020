<<<<<<< HEAD
takeorder()
<<<<<<< HEAD
print'hi'
=======
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
<<<<<<< HEAD
>>>>>>> deb6ae704a54daeabdca260b6ca9e62ab4484c5f
=======
def placeorder(size,color,cloth,orderstatus):
if (orderstatus == true)
    print('your order is placed with size or color or clothe type:',size,color,cloth)
else
    print('your order is not placed as its out of stock')
>>>>>>> 6690afd39111b44a6070f4467c17f7a43a76d001
ttyt