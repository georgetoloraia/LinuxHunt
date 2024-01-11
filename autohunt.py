import random
import time
import subprocess

def main():
    minimal = random.randint(36893488147419103232, 73786976294838206463)
    maximum = random.randint(36893488147419103232, 73786976294838206463)
    
    minimal_hex = hex(minimal)[2:]  # Remove '0x' prefix
    maximum_hex = hex(maximum)[2:]  # Remove '0x' prefix
    
    generated = correct(minimal_hex, maximum_hex)
    create_command(generated)

def correct(minimal, maximum) -> tuple:
    if minimal > maximum:
        return maximum, minimal
    else:
        return minimal, maximum

def create_command(text):
    minimal, maximum = text
    command = f"./keynunt -m rmd160 -r {minimal}:{maximum} -f 66.rmd -R"
    
    try:
        subprocess.run(command, shell=True, check=True, timeout=4 * 60 * 60)
    except subprocess.TimeoutExpired:
        pass

if __name__ == "__main__":
    main()
