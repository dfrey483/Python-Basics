''' Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.'''

import subprocess

fun=str(input("please enter a Python function that you wish to know its documentation : "))
p = subprocess.Popen("pydoc  "+fun, stdout=subprocess.PIPE, shell=True)
print(p.stdout.read())
