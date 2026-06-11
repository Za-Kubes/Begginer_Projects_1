# A little celebration script!
import time

def celebrate():
    message = "SYNTAX HIGHLIGHTING IS BACK!"
    colors = ["\033[91m", "\033[92m", "\033[94m", "\033[95m", "\033[96m"]
    
    for i in range(5):
        for char in message:
            # This will print the message in different colors
            print(f"{colors[i % 5]}{char}", end="", flush=True)
            time.sleep(0.05)
        print("\n")

if __name__ == "__main__":
    celebrate()
    print("\033[0m" + "Now, what are we building today?")
    