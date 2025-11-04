from os import system
import subprocess

while True:
    push = input('Do you want to push it after every modifire?(y/n)(default:y): ').lower()
    if push == '' or push == 'y':
        push = True
        break
    elif push == "n":
        push = False
        break
    else:
        print('Answer only with y or n.')

init = input('Do you want to init?(y/n)(default:y): ').lower()
if init == '' or init == 'y':
    system('git init')
def safe_run(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {command}")
        print(f"Details: {e}")

def main():
    while True:
        change = input("Whats your changes?: ")
        safe_run('git add .')
        safe_run(f'git commit -m "{change}"')
        if push:
            safe_run('git pull')
            safe_run('git push')
main()
