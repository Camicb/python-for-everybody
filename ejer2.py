found=False #(False is a constant in python)
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value ==3:
        found=True #si encuentro un value=3, todos los found se convierten en true
    print(found,value)
print('After', found)
