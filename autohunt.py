''' Idea George Toloraia'''

import random
import time
import subprocess

def main():
    minimal = random.randint(36893488147419103232, 73786976294838206463)
    maximum = random.randint(36893488147419103232, 73786976294838206463)
    generated = recorect(minimal, maximum)
    gotocomand = Create_Command(generated)

def recorect(minimal, maximum) -> int:
    if minimal > maximum:
        return maximum, minimal
    else:
        return minimal, maximum
    
def Create_Command(text):
    minimal, maximum = text
    command = f"./keynunt -m rmd160 -r {minimal}:{maximum} -f 66.rmd -R"
    
    subprocess.run(command, shell=True, check = True)

    time.sleep(4 * 60 * 60)

    stop = f"^c"
    subprocess.run(stop)

    continue main()

if __name__ == "__main__":
    main()

