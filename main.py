def mmiw_fund():
    print('Hello! My name is Alexis and I am raising money for Missing and Murdered Indigenous Women (MMIW). No more missing sisters.')
    return

mmiw_fund()

print()
print('If we raise over $250 we will make missing person flyers.')
print()
print('If we raise over $350 we will make and sell T-shirts.')
print()
print('If we raise over $500 we will host a powwow.')
print()
print('If we raise over $1000 we will donate to MMIW.')
print()




x = 0
name = [0,1,2,3]
amt = [0,1,2,3]

while x < 4:
    print("What is the doner's first and last name? -Please include space between first and last name-")
    name[x] = input()
    print("What amount of money would the doner like to give?")
    amt[x] = int(input())
    x = x + 1


myString0 = name[0]
value = myString0.split()

myString1 = name[1]
onevalue = myString1.split()

myString2 = name[2]
twovalue = myString2.split()

myString3 = name[3]
threevalue = myString3.split()

    
print("Thank you", value[0], "for your contribution of", amt [0], "dollars." )
print()
print("Thank you", onevalue[0], "for your contribution of", amt [1], "dollars." )
print()
print("Thank you", twovalue[0], "for your contribution of", amt [2], "dollars." )
print()
print("Thank you", threevalue[0], "for your contribution of", amt [3], "dollars." )
print()

tot_list = ( amt[0] + amt[1] + amt[2] + amt[3] ) 

if tot_list >= 1000:
    print('Congrats! All funds raised will be donated to MMIW.')
elif tot_list >= 500:
    print('We have raised enough funds to host a powwow.')
elif tot_list >= 350:
    print('Yay! We have enough money for T-shirts.')
elif tot_list >= 250:
    print('We now have enough funds to create missing person flyers.')
else:
    print("Aw too bad :(. Let's try to raise more next time")
    

