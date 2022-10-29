import math
import random
import matplotlib.pyplot as plt
import collections


# 1-(1-p)^n
# p = the percent chance of rolling the given rarity (ie: 3*, 4*, 5*, 6*)
# n = the number of times rolled/will roll
def binomial(p, n):
    probability = 1 - math.pow(1 - p, n)
    return probability * 100


# 15,895 orundum
def roll_count(currency):
    x = math.floor(currency / 600)
    return x


def swap_to_percent(x):
    temp = x / 100
    return temp


def summon_sim(num_summons, limited_check):
    base_list = ["6*", "5*", "4*", "3*"]
    coinflip_six_star = ["limited", "base"]

    when_limited = []
    when_six_star = []
    default_ur = 2

    rolls_completed = 0
    ur_reset = False

    token = True
    while token:
        rarity_rolled = random.choices(base_list, weights=(default_ur, 8, 50, 40))
        if limited_check is True:
            if rarity_rolled[0] == "6*":
                limited_unit_check = random.choices(coinflip_six_star, weights=(70, 30))

                if limited_unit_check[0] == "limited":
                    when_limited.append(rolls_completed + 1)
                    return when_limited
        else:
            if rarity_rolled[0] == "6*":
                when_six_star.append(rolls_completed + 1)
                return when_six_star

        rolls_completed += 1
        if rolls_completed % 50 == 0:
            # ur_reset is supposed to be false by default, indicating no 6*
            if ur_reset is False:
                default_ur += 2

        if rolls_completed >= num_summons:
            token = False

    return when_six_star


def mode_distribution(given_list):
    mode = {}
    temp_count = 0
    try:
        for y in given_list:
            for x in range(len(given_list)):
                if y == given_list[x]:
                    temp_count += 1
            mode[y] = temp_count
            temp_count = 0

    except Exception as e:
        print(e)

    plt.bar(*zip(*sorted(mode.items())))
    plt.show()


# Only checks six stars/limited units
def multi_roll(number_of_rolls, check_if_limited):
    six_star_positions = []

    summon_length = 7500
    for x in range(summon_length):
        six_star_positions.append(summon_sim(number_of_rolls, check_if_limited))

    clean_six_star_list(six_star_positions)


# removes gacha pulls that don't have a six star, removes null
def clean_six_star_list(all_pulled):
    temp = []

    for x in all_pulled:
        try:
            if len(x) != 0:
                for y in range(len(x)):
                    temp.append(x[y])
        except Exception as e:
            print(e)
    temp.sort()
    mode_distribution(temp)


def arknights_main():
    token = False
    while token is False:
        try:
            user_input2 = int(input("Enter amount of usable currency: "))
            if type(user_input2) is int:
                x = roll_count(user_input2)
                token = True
            else:
                raise Exception("Invalid currency value")
        except Exception as e:
            print(e)

    token = False
    while token is False:
        user_input3 = input("Do you have any tickets? Y/N: ")
        try:
            if user_input3.lower() == "yes" or user_input3.lower() == "y":
                user_input4 = int(input("Enter the amount of summoning tickets available: "))
                x = x + user_input4
                print("{} rolls available".format(x))
                token = True
            elif user_input3.lower() == "no" or user_input3.lower() == "n":
                print("Number of rolls possible: " + str(x))
                token = True
            else:
                raise Exception("Invalid Input")
        # the catch-block does run, but nothing is printed (doesn't negatively affect the function)
        except Exception as e:
            print(e)

    token = False
    while token is False:
        user_input5 = input("Is this a limited banner? Y/N: ")
        try:
            if user_input5.lower() == "yes" or user_input5.lower() == "y":
                limited_check = True
                token = True
            elif user_input5.lower() == "no" or user_input5.lower() == "n":
                limited_check = False
                token = True
            else:
                raise Exception("Invalid input")
        except Exception as e:
            print(e)

    y = binomial(swap_to_percent(2), x)
    print("Chance to roll, given a {}% chance, within {} rolls: {}".format(2, x, y))

    multi_roll(x, limited_check)
