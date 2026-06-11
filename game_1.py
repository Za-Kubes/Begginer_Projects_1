from colorama import Fore, Style

print(Fore.CYAN + "="*35)
print(Fore.YELLOW + "   Welcome to Python on Android!")
print(Fore.CYAN + "="*35 + Style.RESET_ALL)

name = input(Fore.GREEN + "\nWhat's your name? ➤ " + Style.RESET_ALL)
print(Fore.MAGENTA + f"\nHello, {name}! 🎉 You're coding from your phone!")
print(Fore.BLUE + "\nSubscribe to the channel for more awesome Python tools! 🚀")