# PassCracker

## Overview

PassCracker is a Python tool designed for cracking MD5 hashed passwords using brute-force and dictionary attack methods. It aims to demonstrate the vulnerabilities associated with weak password hashing and the importance of strong password practices.

## Features

- **Brute-force Cracking**: Generates all possible combinations of a specified character set to find matches for a given MD5 hash.
- **Dictionary Attack**: Compares a list of common passwords against their hashed values to identify potential matches.

## Requirements

- Python 3.x
- `hashlib` (part of the Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/avilubick/PassCracker
   cd PassCracker
   ```

2. Ensure Python 3 is installed on your machine.

## Usage

### Brute-force Password Cracking

1. Open the `brute_force.py` file and set the `hash` variable to the target MD5 hash you want to crack.
2. Run the script:
   ```bash
   python brute_force.py
   ```

### Dictionary Attack

1. Prepare two text files:
   - **Reference File**: A file containing potential plaintext passwords (one per line).
   - **Password List**: A file containing the MD5 hashes you want to check against the reference file.
2. Update the script (`dictionary_attack.py`) with the paths to your files:
   - Replace `INSERT REF. FILE` with your reference file path.
   - Replace `INSERT PASSLIST` with your password list path.
   - Replace `INSERT RESULT FILE` with the desired output file path.
3. Run the script:
   ```bash
   python dictionary_attack.py
   ```

## Important Notes

- **Ethical Use**: This tool is meant for educational purposes only. Ensure you have explicit permission before attempting to crack any passwords.
- **Performance Considerations**: Brute-force methods can take a long time depending on the complexity of the passwords. Dictionary attacks are generally faster if the password exists in the provided list.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
