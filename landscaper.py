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

## upgrade_old-timey push lawnmower for $25
def buy_old_timey_push_lawnmower():
    user_input = int(input("""
                        Would you like to buy an old-timey push lawnmower for $25
                        [1] Yes! I will buy!
                        [2] No thank you!
    """))

    if (user_input == 1):
        game_data["money"] -= 25
        print(f"You bought an old-timey push lawnmower! With an an old-timey push lawnmower you can make $50 per day! You now have a total of ${game_data['money']}")
        use_old_timey_push_lawnmower()

    if  (user_input == 2):
        print(f"You will make more money with an old-timey push lawnmower...., You now have a total of ${game_data['money']}")
        use_rusty_scissors()


## upgrade_a fancy battery-powered lawnmower for $250
def buy_fancy_battery_powered_lawnmower():
    user_input = int(input("""
                        Would you like to buy a fancy battery-powered lawnmower for $250
                        [1] Yes! I will buy!
                        [2] No thank you!
    """))

    if (user_input == 1):
        game_data["money"] -= 250
        print(f"You bought a fancy battery-powered lawnmower! With a fancy battery-powered lawnmower you can make $100 per day! You now have a total of ${game_data['money']}")
        use_fancy_battery_powered_lawnmower()

    if  (user_input == 2):
        print(f"You will make more money with a fancy battery-powered lawnmower...., You now have a total of ${game_data['money']}")
        use_old_timey_push_lawnmower()


## upgrade_hire a team of starving students for $500
def hire_a_team_of_starving_students():
    user_input = int(input("""
                        Would you like to hire a team of starving students for $500
                        [1] Yes! I will hire them!
                        [2] No thank you!
    """))

    if (user_input == 1):
        game_data["money"] -= 500
        print(f"You hired a team of starving students for $500! With a team of starving students you can make $250 per day! You now have a total of ${game_data['money']}")
        hired_a_team_of_starving_students()

    if  (user_input == 2):
        print(f"You will make more money with a fancy battery-powered lawnmower...., You now have a total of ${game_data['money']}")
        use_fancy_battery_powered_lawnmower()


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
        if (game_data["money"] >= 25):
            buy_old_timey_push_lawnmower()
        use_rusty_scissors()
    
    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_rusty_scissors()


def use_old_timey_push_lawnmower():
    user_input = int(input("""
                        Would you like to cut lawns today and make $50 today?
                        [1] Yes! Make $50~
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 50
        print(f"You now have a total of ${game_data['money']}")
        if (game_data["money"] >= 250):
            buy_fancy_battery_powered_lawnmower()
        use_old_timey_push_lawnmower()

    
    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_old_timey_push_lawnmower()


def use_fancy_battery_powered_lawnmower():
    user_input = int(input("""
                        Would you like to cut lawns today and make $100 today?
                        [1] Yes! Make $100~
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 100
        print(f"You now have a total of ${game_data['money']}")
        if (game_data["money"] >= 500):
            hire_a_team_of_starving_students()
        use_fancy_battery_powered_lawnmower()

    
    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        use_fancy_battery_powered_lawnmower()



def hired_a_team_of_starving_students():
    user_input = int(input("""
                        Would you like to cut lawns today and make $250 today?
                        [1] Yes! Make $250~
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 250
        print(f"You now have a total of ${game_data['money']}")
        
        hired_a_team_of_starving_students()

    
    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")
        hired_a_team_of_starving_students()

use_teeth()