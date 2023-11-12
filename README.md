# BRUTEBRO

BRUTEBRO is a Python script designed for simulating brute force attacks on login systems. It generates random usernames and passwords, attempts to log in using a specified URL, and records the results in a CSV file.

## Features

- **Random Usernames and Passwords**: BRUTEBRO generates random usernames and passwords for each login attempt.
- **Configurable Options**: Users can customize the number of attempts, password length, delay between attempts, and more.
- **Visual Broadcast**: BRUTEBRO visually broadcasts each attempt, showing the username, password, and result on the console.

## Getting Started

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/bpike34/BRUTEBRO.git
    ```

2. **Navigate to the BRUTEBRO Directory**:

    ```bash
    cd BRUTEBRO
    ```

3. **Run BRUTEBRO**:

    ```bash
    python BRUTEBRO.py
    ```

4. **Follow the Prompts**:

    - Enter the login URL.
    - Specify the number of attempts.
    - Choose password options (length, character types).
    - Set the delay between attempts.

## Options

- **Password Character Types**:
    - Letters only
    - Numbers only
    - Symbols only
    - Letters, Numbers, and Symbols (default)

- **Password Length Options**:
    - Set a fixed password length
    - Specify a length range

- **Pre-made Usernames**:
    - Users can provide a text file with pre-made usernames.

## Example Usage

```bash
python BRUTEBRO.py
Disclaimer
This script is intended for educational purposes only. Unauthorized access to computer systems is illegal.

License
This project is licensed under the MIT License
