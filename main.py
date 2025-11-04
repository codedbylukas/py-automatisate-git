from os import system

push = input('Do you want to push it after every modifire?(y/n)(default:y): ').lower()
if push == '' or push == 'y':
    push = True
else:
    push = False

init = input('Do you want to init?(y/n)(default:y): ').lower()
if init == '' or init == 'y':
    system('git init')

def main():
    while True:
        change = input("Whats your changes?: ")
        system('git add .')
        system(f'git commit -m "{change}"')
        if push:
            system('git pull')
            system('git push')
main()
