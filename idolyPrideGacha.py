import random
import math
import matplotlib.pyplot as plt
from arknightsGacha import binomial, swap_to_percent


def idoly_roll_count(currency):
    x = math.floor(currency / 300)
    ten_roll_count = 0
    for y in range(x):
        if ten_roll_count > x:
            break
        else:
            ten_roll_count += 1
    print(ten_roll_count)
    print(x)
    return x


# gem count 44000
# 2700 for 10 roll
# 300 for single roll
def summon_sim(num_summons, rate_up):
    temp_list = ["6*", "5*", "4*", "3*"]
    when_five_star = []
    when_rate_up = []

    rate_up_count = 0
    five_star_count = 0
    four_star_count = 0
    three_star_count = 0

    rolls_completed = 0
    rate_up_rate = rate_up
    ssr_new_rate = 3.5 - rate_up

    token = True
    while token:
        rarity_rolled = random.choices(temp_list, weights=(rate_up_rate, ssr_new_rate, 15, 81.5))

        if rarity_rolled[0] == "6*":
            rate_up_count += 1
            when_rate_up.append(rolls_completed + 1)
        elif rarity_rolled[0] == "5*":
            five_star_count += 1
            when_five_star.append(rolls_completed + 1)
        elif rarity_rolled[0] == "4*":
            four_star_count += 1
        elif rarity_rolled[0] == "3*":
            three_star_count += 1

        rolls_completed += 1

        if rolls_completed >= num_summons:
            token = False

    return when_rate_up


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


# Only checks six stars
def multi_roll(number_of_rolls, rate_up):
    six_star_positions = []

    summon_length = 10000
    for x in range(summon_length):
        six_star_positions.append(summon_sim(number_of_rolls, rate_up))

    big_strip(six_star_positions)


# removes gacha pulls that don't have a six star, removes null
def big_strip(all_pulled):
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


def idoly_main():
    token = False
    while token is False:
        try:
            user_input1 = float(input("Enter the character rate up percent (eg 3.5): "))
            if type(user_input1) is float:
                temp = swap_to_percent(user_input1)
                token = True
        except:
            print("Need a float")

    token = False
    while token is False:
        try:
            user_input2 = int(input("Enter amount of usable currency: "))
            if type(user_input2) is int:
                x = idoly_roll_count(user_input2)
                token = True
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
        # the catch-block does run, but nothing is printed (doesn't negatively affect the function)
        except:
            print("Yes or no, do you have any tickets")

    y = binomial(.035, x)
    print("Chance of success, given a 3.5% chance, within {} rolls: {}".format(x, y))

    multi_roll(x, temp)
