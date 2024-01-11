## Ok this is a my personal game

# KeyHunt Game

## Introduction

This Python script is a personal game inspired by the [keyhunt](https://github.com/albertobsd/keyhunt) project by albertobsd. The script generates a random Decimal number with 66 bits, uses it as an argument for the `./keyhunt` program, and runs the program for 4 hours. After the time limit, a new random Decimal is generated, and the process repeats.

## Usage

### Prerequisites

- Ensure you have the `./keyhunt` program installed. You can find it in the [keyhunt repository](https://github.com/albertobsd/keyhunt).

### Running the Script

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/keyhunt-game.git
   cd keyhunt-game
   ```
2. Run the Python script:

   ```bash
   python main.py
   ```

## Customization

If you want to modify or extend the game, you can:

- Adjust the bit size of the random Decimal generated in the `main.py` script.
- Customize the command used to run `./keyhunt` in the `create_command` function.

Feel free to explore and experiment with different configurations to make the game more interesting!

## Credits

- Original code for `./keyhunt` by [albertobsd](https://github.com/albertobsd/keyhunt).

## License

This project is licensed under the [MIT License](LICENSE).

# KeyHunt Game

## Introduction

This Python script is a personal game inspired by the [keyhunt](https://github.com/albertobsd/keyhunt) project by albertobsd. The script generates a random Decimal number with 66 bits, uses it as an argument for the `./keyhunt` program, and runs the program for 4 hours. After the time limit, a new random Decimal is generated, and the process repeats.

## Usage

### Prerequisites

- Ensure you have the `./keyhunt` program installed. You can find it in the [keyhunt repository](https://github.com/albertobsd/keyhunt).

### Running the Script

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/keyhunt-game.git
   cd keyhunt-game
   ```
2. Run the Python script:

   ```bash
   python main.py
   ```

## Customization

If you want to modify or extend the game, you can:

- Adjust the bit size of the random Decimal generated in the `main.py` script.
- Customize the command used to run `./keyhunt` in the `create_command` function.

Feel free to explore and experiment with different configurations to make the game more interesting!

## Credits

- Original code for `./keyhunt` by [albertobsd](https://github.com/albertobsd/keyhunt).

## License

This project is licensed under the [MIT License](LICENSE).

- Original code creator is a albertobsd https://github.com/albertobsd/keyhunt/tree/main

### What can my idea do?

- My Python code can generate random Decimal's number in bit 66
- After generate opening keyhunt automatical.
- writing in arguments -r "generated Decimal".
- ./keyhunt -t 1 -m rmd160 -l compress -r [generated Decimal [from to]]
- I think if work 4 hours it is possible
- After 4 hours program stop and generating new random Decimal's
