"""
Exercise 3.7. Read command line input for the formula (1.1). Modify the program listed in Exercise 3.6 such that v0 and t are read from the command line. Name of program file: ball_cml.py.
"""
import sys
try:
    v0 = eval(sys.argv[1])
except IndexError:
    v0 = eval(raw_input("v0=?\n"))

try:
    t = eval(sys.argv[2])
except IndexError:
    t = eval(raw_input("t=?\n"))

g = 9.81
y = v0*t - 0.5*g*t**2
print y
