import random
import sys
import datetime
import itertools

check = sys.argv[1]

divider = "|=-=-=-=-=-=-=-=-=-=-=-=|"
print(divider)

# program start
program_start = datetime.datetime.now()
# time since january 1 1970
origin = datetime.datetime.utcfromtimestamp(0)


def program_time(datetime):
    """Function to get time the program took"""
    return (datetime - origin).total_seconds()


def border(content):
    return "|{:<23}|".format(content)

initial_seconds = program_time(program_start)

print(border("Check: " + check))

pw_length = 8

common_passwords = open("pw.txt", "r").read().split("\n")

chars = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#chars = list("1as")


def check_pw(check):
    for pw in common_passwords:
        if pw == check:
            print(border("Found in file!"))
            print(border("Password: " + pw))
            return True
    return False

#is_there = check_pw(check)

# cartesian product provides repetitions, while permutations does not
generator = itertools.product(chars, repeat=len(check))

if not check_pw(check):
    attempt = 0
    for password in generator:
        attempt += 1
        temp_pw = "".join(password)
        if temp_pw == check:
            print(border("Found through cracking!"))
            print(border("Password: " + temp_pw))
            print(border("Attempts: " + str(attempt)))
            break

#              Get the current time        -    initial time
print(border(str(round(program_time(datetime.datetime.now()) - initial_seconds)) + " second(s)."))
print(divider)
