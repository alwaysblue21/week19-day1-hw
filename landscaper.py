game_data = {
    "money": 0,
}

## You are starting a landscaping business, but all you have are your teeth.
## Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.
def use_teeth():
    user_input = int(input("""
                        Would you like to cut lawns today and make $1 today?
                        [1] Yes! Make $1!
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 1
        print(f"You now have a total of ${game_data['money']}")
        use_teeth()

    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_teeth()
    
    # if (game_data['money'] >= 5):
    #     rusty_scissors = int(input("""
    #                             Would you like to buy a pair of rusty scissors for $5?
    #                             [1] Yes! I will buy!
    #                             [2] Nope! I dont need one yet!
    #     """))

    #     if (rusty_scissors == 1):
    #         game_data["money"] -= 5
    #         print(f"You bought a pair of rusty scissors! Now you can make $5 per day with a pair of rusty scissors! You now have a total of ${game_data['money']}")

    #         with_rusty_scissors = int(input("""
    #                                     Would you like to work today with a pair of rusty scissors?
    #                                     [1] Yes! Make $5!
    #                                     [2] Nope! Maybe Tmr!
    #         """))

    #         if (with_rusty_scissors == 1):
    #             game_data["money"] += 5
    #             print(f"You now have a total of ${game_data['money']}")

    #         if (with_rusty_scissors == 2):
    #             print(f"See you Tmr! You now have a total of ${game_data['money']}")

    #     if (rusty_scissors == 2):
    #         print(f"You will make more money with a pair of rusty scissors..., You now have a total of ${game_data['money']}")

use_teeth()