#!/bin/python3
#andres
#Wed 09 Mar 2022 04:36:41 AM EST


shop= {"Zera Darksword":"$4000 zenny", "Xerathus Archblade":"$6000 zenny", "Divine Eclipse":"$3000 zenny"}

itemquery= input("Welcome to the Inn's Shop! How can I help you today?\n""-----[Commands]-----\n""Specific Weapon Price:type in full name, initials, or first three letters\n""Show available weapons: 'as'\n""Full list of swords with price: 'fl' \n")
 
if itemquery == "Zera Darksword" or itemquery  == "zd":
    print(shop['Zera Darksword'])

elif itemquery == 'Xerathus Archblade'or itemquery == "xa":
    print(shop['Xerathus Archblade'])

elif itemquery == 'Divine Eclipse'or itemquery == "de":
    print(shop['Divine Eclipse'])
elif itemquery=='fl':
    print(shop)
     
elif itemquery.casefold() == 'as':
    print("'Zera Darksword'","'Xerathus Archblade'","'Divine Eclipse'")
    itemquery=input("Which one are you interested in?\n") 
    if itemquery.casefold()   == "Zera Darksword".casefold() or itemquery  == "zd" or 'zer.+':
        print(shop['Zera Darksword'])

    elif itemquery.casefold()  == 'Xerathus Archblade'.casefold() or itemquery == "xa"or 'xer.+':
        print(shop['Xerathus Archblade'])

    elif itemquery.casefold() == 'Divine Eclipse'.casefold() or itemquery == "de" or 'div.+':
        print(shop['Divine Eclipse'])
    else:
        exit

elif itemquery=='fl':
    print(shop)
else:    
    print("We don't sell this item. Try again.")
exit
