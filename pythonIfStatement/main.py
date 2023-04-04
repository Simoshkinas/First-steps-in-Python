is_male = True
is_tall = True


def give_gender(male_female):
    if male_female:
        print("You are a male")
    else:
        print("You are a female")


def give_state1(male_female, short_tall):
    if male_female or short_tall:
        print("you are a male, or you are tall, or both")
    else:
        print("You are neither male, nor tall")


def give_state2(male_female, short_tall):
    if male_female and short_tall:
        print("You are a tall male")
    else:
        print("you are not male, or not tall, or both")


def give_state3(male_female, short_tall):
    if male_female and short_tall:
        print("You are a tall male")
    elif male_female and not short_tall:
        print("You a short male")
    elif not male_female and short_tall:
        print("You are a tall female")
    else:
        print("You are a short female")


give_gender(is_male)
is_male = False
give_gender(is_male)
give_state1(is_male, is_male)
is_male = False
give_state1(is_male, is_male)
is_male = True
give_state2(is_male, is_tall)
is_tall = False
give_state2(is_male, is_tall)
is_tall = True
give_state3(is_male, is_tall)
is_male = False
give_state3(is_male, is_tall)
is_male = True
is_tall = False
give_state3(is_male, is_tall)
is_male = False
give_state3(is_male, is_tall)
