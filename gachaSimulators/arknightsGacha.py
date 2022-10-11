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


def summon_sim(num_summons):
    temp_list = ["6*", "5*", "4*", "3*"]
    when_six_star = []
    when_five_star = []
    default_ur = 2

    six_star_count = 0
    five_star_count = 0

    rolls_completed = 0
    ur_reset = False

    token = True
    while token:
        rarity_rolled = random.choices(temp_list, weights=(default_ur, 8, 50, 40))

        if rarity_rolled[0] == "6*":
            six_star_count += 1
            default_ur = 2
            when_six_star.append(rolls_completed + 1)
            ur_reset = True
            token = False
        elif rarity_rolled[0] == "5*":
            five_star_count += 1
            when_five_star.append(rolls_completed + 1)

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


# Only checks six stars
def multi_roll(number_of_rolls):
    six_star_positions = []

    summon_length = 7500
    for x in range(summon_length):
        six_star_positions.append(summon_sim(number_of_rolls))

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
            user_input1 = int(input("Chance to roll (as integer, not decimal): "))
            if type(user_input1) is int:
                token = True
        except:
            print("Need a number chief")

    token = False
    while token is False:
        try:
            user_input2 = int(input("Enter amount of usable currency: "))
            if type(user_input2) is int:
                x = roll_count(user_input2)
                token = True
        except:
            print("Need a number chief")

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

    y = binomial(swap_to_percent(user_input1), x)
    print("Chance to roll, given a {}% chance, within {} rolls: {}".format(user_input1, x, y))

    multi_roll(x)
