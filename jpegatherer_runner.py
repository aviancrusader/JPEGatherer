from arknightsGacha import *
from idolyPrideGacha import *
from blueArchiveGacha import *


def runner():
    user_input = input("Select which gacha to simulate:"
                       "\n1: Arknights\n2: Idoly Pride\n3: Blue Archive"
                       "\n===============================\n")
    try:
        if user_input == "1" or user_input.lower() == "arknights":
            arknights_main()
        elif user_input == "2" or user_input.lower() == "idoly pride" or user_input.lower() == "idolypride" \
                or user_input.lower() == "idoly":
            idoly_main()
        elif user_input == "3" or user_input.lower() == "blue archive" \
            or user_input.lower() == "bluearchive" or user_input.lower() == "archive":
            blue_archive_main()

    except Exception as e:
        print(e)

runner()