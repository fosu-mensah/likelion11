list = ['A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 
        'A', 'B', 'O', 'AB', 'A', 'B', 'O']
A = 0
B = 0
O = 0
AB = 0

for i in list :
    if i == 'A':
        A = A + 1
    elif i == 'B':
        B = B + 1
    elif i == 'O':
        O = O + 1
    elif i == 'AB':
        AB = AB + 1

print(A,B,O,AB)
