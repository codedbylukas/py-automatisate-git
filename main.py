from os import system

push = input('Do you want to push it after every modifire?(y/n)(default:y): ').lower()
if push == '' or push == 'y':
    push = True
    
system