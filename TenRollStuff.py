import random

"""
Used only for arknightsGacha.py
ten_roll is to be used to simulate a ten roll that guarantees a 5* or greater.

if, by chance, a 5* or greater is not pulled by the tenth roll - then the tenth roll is automatically made to be 
5* or greater

Testing against the summon simulator on gamepress, currently seems like the rates are wrong as there are more instances
in which multiple 5* are pulled in a single 10 roll (ie: 3 5* in one 10 roll, in comparison - the gamepress sim yielded
only 1 instance in which more than 1 5* was rolled in a set of 10 10 rolls). In addition, 6* were
seen more frequently (as much as 3x more often) in comparison to the gamepress sim results

v2 update to the 10th roll check, after looking through the gamepress code it looks like they combined the rates of 
3*-5* in order to give ssr's a 98% pull rate. A quick 10 set check resulted in fewer discrepancies from the first 
10 set check using the old code, but still unsure as to the variability of it. However, much better results overall.
Ultimately will need to, unfortunately, test against the actual Arknights gacha when the time comes - note that times 
of testing will have to be spread out over the course of a year, collecting only about 4 times roughly

note: index 9 is the 10th roll, however 10th roll is also the 10th roll. Unsure as to how this is supposed to be thought
of, that is, 10th roll is denoted as such because the previous 9 rolls did not yield an ssr or greater. So for index 9
to appear, it would mean that on the 10th roll it rolled an ssr or greater without triggering the code to guarantee such
a roll.

note: include setting to switch between recording the first instance of a 6* and the first instance of a 5*
"""
def ten_roll():
    counter = 0
    temp_list = ["6*", "5*", "4*", "3*"]
    temp_list2 = ["6*", "5*"]
    first_instance_of_six_star = None

    six_star_count = 0
    five_star_count = 0
    four_star_count = 0
    three_star_count = 0

    ur_ssr_check = False
    for x in range(10):
        rarity_rolled = random.choices(temp_list, weights=(2, 8, 50, 40))

        if ur_ssr_check is False:
            if counter == 9:
                rarity_rolled = random.choices(temp_list2, weights=(2, 98))

                if rarity_rolled[0] == "6*":
                    six_star_count += 1
                    first_instance_of_six_star = "10th"
                    ur_ssr_check = True
                    break
                elif rarity_rolled[0] == "5*":
                    five_star_count += 1
                    ur_ssr_check = True
                    break

            if rarity_rolled[0] == "6*":
                six_star_count += 1
                first_instance_of_six_star = x
                ur_ssr_check = True

            elif rarity_rolled[0] == "5*":
                five_star_count += 1
                ur_ssr_check = True

            elif rarity_rolled[0] == "4*":
                four_star_count += 1

            elif rarity_rolled[0] == "3*":
                three_star_count += 1
        elif ur_ssr_check is True:
            if rarity_rolled[0] == "6*":
                six_star_count += 1

            elif rarity_rolled[0] == "5*":
                five_star_count += 1

            elif rarity_rolled[0] == "4*":
                four_star_count += 1

            elif rarity_rolled[0] == "3*":
                three_star_count += 1
        counter += 1
    return first_instance_of_six_star


# Testing multiple calls to ten_roll to see how many and when 6* (currently set to only 6*) are pulled
# within 100 10 rolls
def first6_from10roll():
    firstInstanceOfSixStar = []
    tempFirstInstance = []
    token = False
    c = 0
    while token is False:
        a = ten_roll()
        firstInstanceOfSixStar.append(a)
        c += 1
        if c == 100:
            token = True

    for x in firstInstanceOfSixStar:
        if x is not None:
            tempFirstInstance.append(x)

    instance = strip(tempFirstInstance)
    print("First instance of when a 6* was rolled, "
          "numerical values are indexes so add +1 to get the actual roll number.\n"
          "Except for 10 (not to be confused with 9)")
    print(instance)
    print("A 6* was rolled {} times out of 100 ten rolls".format(str(len(tempFirstInstance))))


# strip(instance) takes elements that are labelled "10th" and switches it from a string to an integer value
def strip(instance):
    temp = instance
    take2 = []
    for x in temp:
        if x == "10th":
            x = 10
            take2.append(x)
        else:
            take2.append(x)

    return take2
