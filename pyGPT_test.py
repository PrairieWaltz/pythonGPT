from pygpt4all import GPT4All_J
import colorama
from colorama import Fore, Style

print(Fore.WHITE + Style.BRIGHT)
userQ = input(
    "\nWhat can I help you with? Ask me anything: ")
print('\nOk got it. This can take a few minutes so please be patient.\n')

print(Fore.GREEN)
print('#############...fancy computer stuff here...################')
model = GPT4All_J('./ggml-gpt4all-j-v1.3-groovy.bin')
print('############################################################')

print(Fore.WHITE,
      "\nI'm working on an answer now...please be patient")

while True:
    try:
        for token in model.generate(userQ):
            print(token, end='', flush=True)
        uerQ = input(
            f'\nKeep the conversation going with a new prompt or enter ctl + c to quit: ')
    except KeyboardInterrupt:
        break
