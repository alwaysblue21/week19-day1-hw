game_data = {
    "money": 0,
}

## You are starting a landscaping business, but all you have are your teeth.
## Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.
while (True):
    user_input = int(input("""
                        Would you like to cut lawns today and make $1 today?
                        [1] Yes! Make $1!
                        [2] Maybe Tmr!
    """))

    if (user_input == 1):
        game_data["money"] += 1
        print(f"You now have a total of ${game_data['money']}")

    if (user_input == 2):
        print(f"See you Tmr! You now have a total of ${game_data['money']}")

    
    
