# Two-Apes, GitHub
import random, string
amount = int(input('TWO-APES | (all the codes are unchecked) How many Nitro codes do you want to be generated?: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
