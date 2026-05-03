import requests
import time

url = "https://official-joke-api.appspot.com/random_joke"

print("Welcome to the Infinite Joke Machine!")

# The "while True" loop means this will run forever (until we tell it to 'break')
while True:
    print("\nContacting the Joke API...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()

        setup = joke_data['setup']
        punchline = joke_data['punchline']

        print("-" * 20)
        print(setup)
        time.sleep(2)
        print(punchline)
        print("-" * 20)

    except requests.exceptions.RequestException as e:
        print("\nOh no, we couldn't reach the API!")
        print("Error details:", e)
        # If the internet is down, we break the loop to stop the program
        break
#  We ask the user for input.
    # .strip().lower() removes accidental spaces and makes it lowercase so 'Y' or ' y ' still works.
    again = input("\nDo you want to hear another joke? (y/n): ").strip().lower()
# 3. If they type anything other than 'y', we break the loop.
    if again != 'y':
        print("Thanks for laughing! Goodbye.")
        break