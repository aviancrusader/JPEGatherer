from arknightsGacha import *
from blueArchiveGacha import *
from idolyPrideGacha import *

def runner():
    token = False
    while token is False:
        user_input = input("Select which gacha to simulate:"
                       "\n1: Arknights\n2: Idoly Pride\n3: Blue Archive"
                       "\n===============================\n")
        try:
            if user_input == "1" or user_input.lower() == "arknights":
                arknights_main()
                token = True
            elif user_input == "2" or user_input.lower() == "idoly pride" or user_input.lower() == "idolypride" \
                    or user_input.lower() == "idoly":
                idoly_main()
                token = True
            elif user_input == "3" or user_input.lower() == "blue archive" \
                or user_input.lower() == "bluearchive" or user_input.lower() == "archive":
                blue_archive_main()
                token = True

        except:
            print("Invalid input")

runner()