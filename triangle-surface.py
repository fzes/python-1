from math import sqrt 

while True: 
    print('\n\nGive me three sides of triange.')
    try:
        a = int(input('first :'))
        b = int(input('second:'))
        c = int(input('thired:'))
    except:
        print('\nSorry!?\nYou should enter three numbers.\n-----------------------------\nAgain...\n\n\n')
        continue

    if a+b <= c or a+c <= b or b+c <= a:
        print('\nThese numbers can not be true.\n ')
        continue
    else:
        p = (a+b+c)/2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        print('---------------\nsurface is:' , s ,'\n\n')
        break