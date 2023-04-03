character_name = "John"
character_age = "65"
print("There was a nam named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + " years old.")


phrase = "Black Dog"
print(phrase)
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(phrase[5])
print(phrase.replace("Dog", "Cat"))
print(phrase.find("c"))
print(phrase.count("l"))
print(phrase + " Hates cats".lower())
print(phrase.capitalize())
new_phrase = phrase + " Hates Cats"
print(new_phrase)
print(new_phrase.index("Cat"))
print(new_phrase.capitalize())
print(new_phrase.replace("Cats", "Birds").capitalize())
print(new_phrase.casefold())
print(new_phrase.isdigit())
print(new_phrase.isprintable())
