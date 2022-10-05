import random
import math
import matplotlib.pyplot as plt
from arknightsGacha import binomial, swap_to_percent


def archive_roll_count(currency):
    x = math.floor(currency / 120)
    return x

# 8/18/2022 Current Number of total Units in Game: 69 total
# 11 1* units
# 21 2* units
# 37 3* units
# gem count 24000
# 1200 for 10 roll
# 120 for single roll
def summon_sim(num_summons, rate_up, check_limited_banner):
    temp_list = ["4*", "3*", "2*", "1*"]
    fixed_list = ["4*", "3*", "2*"]
    when_three_star = []
    when_rate_up = []

    rate_up_count = 0
    three_star_count = 0
    two_star_count = 0
    one_star_count = 0

    rolls_completed = 0
    rate_up_rate = rate_up
    ssr_new_rate = 2.5 - rate_up
    wakamo_ssr_rate = 5.0 - rate_up

    if check_limited_banner is True:
        for i in range(num_summons):
            rarity_rolled = random.choices(temp_list, weights=(rate_up_rate, wakamo_ssr_rate, 18.499992, 76.500008))

            if rolls_completed % 10 == 0 and rolls_completed != 0:
                fixed_tenth_roll = random.choices(fixed_list, weights=(rate_up_rate, wakamo_ssr_rate, 95))

                if fixed_tenth_roll[0] == "4*":
                    rate_up_count += 1
                    when_rate_up.append(rolls_completed + 1)
                    break
                elif fixed_tenth_roll[0] == "3*":
                    three_star_count += 1
                    when_three_star.append(rolls_completed + 1)
                elif fixed_tenth_roll[0] == "2*":
                    two_star_count += 1
            else:
                if rarity_rolled[0] == "4*":
                    rate_up_count += 1
                    when_rate_up.append(rolls_completed + 1)
                    break
                elif rarity_rolled[0] == "3*":
                    three_star_count += 1
                    when_three_star.append(rolls_completed + 1)
                elif rarity_rolled[0] == "2*":
                    two_star_count += 1
                elif rarity_rolled[0] == "1*":
                    one_star_count += 1

            rolls_completed += 1
    else:
        for i in range(num_summons):
            rarity_rolled = random.choices(temp_list, weights=(rate_up_rate, ssr_new_rate, 18.499992, 78.999998))

            if rolls_completed % 10 == 0 and rolls_completed != 0:
                fixed_tenth_roll = random.choices(fixed_list, weights=(rate_up_rate, ssr_new_rate, 97.499997))

                if fixed_tenth_roll[0] == "4*":
                    rate_up_count += 1
                    when_rate_up.append(rolls_completed + 1)
                    break
                elif fixed_tenth_roll[0] == "3*":
                    three_star_count += 1
                    when_three_star.append(rolls_completed + 1)
                elif fixed_tenth_roll[0] == "2*":
                    two_star_count += 1
            else:
                if rarity_rolled[0] == "4*":
                    rate_up_count += 1
                    when_rate_up.append(rolls_completed + 1)
                    break
                elif rarity_rolled[0] == "3*":
                    three_star_count += 1
                    when_three_star.append(rolls_completed + 1)
                elif rarity_rolled[0] == "2*":
                    two_star_count += 1
                elif rarity_rolled[0] == "1*":
                    one_star_count += 1

            rolls_completed += 1

    print(when_rate_up)
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
        '''
            try:
                total_successes = 0
                for i in mode:
                    total_successes += mode[i]

            except Exception as e:
                print(e)

            print("Average Pull Success: ")
        '''
    plt.bar(*zip(*sorted(mode.items())))
    plt.show()


# Only checks rate up unit pulls
def multi_roll(number_of_rolls, rate_up, check_limited_banner):
    rate_up_positions = []

    summon_length = 5000
    for x in range(summon_length):
        rate_up_positions.append(summon_sim(number_of_rolls, rate_up, check_limited_banner))

    big_strip(rate_up_positions)


# removes gacha pulls that don't have a six star, [as in] removes null
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


def blue_archive_main():
    token = False
    while token is False:
        try:
            user_input1 = float(input("Enter the character rate up percent (eg 3.5): "))
            if type(user_input1) is float:
                temp = swap_to_percent(user_input1)
                token = True
        except:
            print("Need a float value")

    token = False
    while token is False:
        try:
            user_input2 = int(input("Enter amount of usable currency: "))
            if type(user_input2) is int:
                x = archive_roll_count(user_input2)
                token = True
        except Exception as e:
            print(e)

    token = False
    while token is False:
        user_input3 = input("Is this a limited banner with changed odds for 3*? Y/N: ")
        try:
            if user_input3.lower() == "yes" or user_input3.lower() == "y":
                print("Limited banner with differing odds from standard rate up")
                user_input3 = True
                token = True
            elif user_input3.lower() == "no" or user_input3.lower() == "n":
                user_input3 = False
                token = True
        except Exception as e:
            print(e)

    # .7% is the typical rate up percentage, this will need to be adjusted for the Wakamo limited banner
    y = binomial(temp, x)
    print("Chance of success, given a .7% chance, within {} rolls: {}".format(x, y))

    multi_roll(x, user_input1, user_input3)
