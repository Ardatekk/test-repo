customer_profile = []

name = input("quelle est votre nom ?")
age = int(input("quelle est votre age ?"))
favorite_genre = input("quelle est votre favorite_genre literaire préféré ? ")
customer_profile.append({"Nom": name, "Âge": age, "Genre littéraire préféré": favorite_genre})
if age < 18 :
    print("je vous propose uniquement de litérature jeunesse. ")
else:
    print("je vous propose tout les litérature, y compris la litérature adulte. ")  

print (customer_profile)
