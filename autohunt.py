import random
import time
import subprocess

def main():
    # Generate random values for minimal and maximum
    minimal = random.randint(36893488147419103232, 73786976294838206463)
    maximum = random.randint(36893488147419103232, 73786976294838206463)
    
    # Convert minimal and maximum to hexadecimal
    minimal_hex = hex(minimal)[2:]  # Remove '0x' prefix
    maximum_hex = hex(maximum)[2:]  # Remove '0x' prefix
    
    # Ensure minimal is less than maximum
    generated = correct(minimal_hex, maximum_hex)
    
    # Create and execute the command
    create_command(generated)

def correct(minimal, maximum) -> tuple:
    # Swap values if minimal is greater than maximum
    if minimal > maximum:
        return maximum, minimal
    else:
        return minimal, maximum

def create_command(text):
    minimal, maximum = text
    # Construct the command string
    command = f"./keynunt -m rmd160 -r {minimal}:{maximum} -f 66.rmd -R"
    
    try:
        # Run the command with a timeout of 4 hours
        subprocess.run(command, shell=True, check=True, timeout=4 * 60 * 60)
    except subprocess.TimeoutExpired:
        pass

if __name__ == "__main__":
    main()
