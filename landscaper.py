game_data = {
    "money": 0,
}

## upgrade_rusty_scissors
def buy_rusty_scissors():
    user_input = int(input("""
                        Would you like to buy a pair of rusty scissors for $5?
                        [1] Yes! I will buy!
                        [2] No thank you!
    """))

    if (user_input == 1):
        game_data["money"] -= 5
        print(f"You bought rusty scissors! With a pair of rusty scissors, you can make $5 per day! You now have a total of ${game_data['money']}")
        use_rusty_scissors()

    if  (user_input == 2):
        print(f"You will make more money with a pair of rusty scissors...., You now have a total of ${game_data['money']}")
        use_teeth()


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
        if (game_data["money"] >= 5):
            buy_rusty_scissors()
        use_teeth()

    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_teeth()


def use_rusty_scissors():
    user_input = int(input("""
                        Would you like to cut lawns today and make $5 today?
                        [1] Yes! Make $5~
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 5
        print(f"You now have a total of ${game_data['money']}")
        use_rusty_scissors()
    
    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_rusty_scissors()

use_teeth()