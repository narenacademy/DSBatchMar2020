
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

def placeorder(size,color,cloth,orderstatus):
if (orderstatus == true)
    print('your order is placed with size or color or clothe type:',size,color,cloth)
else
    print('your order is not placed as its out of stock')
