#selecting type of crop

print('1- Oats')
print('2- Peas')
print('3- Wheat')
print('Please select a crop from the list given above:')
n=int(input())
print('The selected Number is:'+str(n))
crop=0
if(n==1):
    crop='Oats'
elif(n==2):
    crop='Peas'
elif(n==3):
    crop='Wheat'
else:
    crop='Invalid'
print('Selected crop is :'+' '+crop)