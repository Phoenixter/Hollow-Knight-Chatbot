import random

message = input("Knight stares at you silently... ")
palekingcounton = False
palekingcount = 0
while True:
    if palekingcounton:
        if palekingcount == 0:
            input("<Knight> No cost too great... ")
            palekingcount += 1
        if palekingcount == 1:
            input("<Knight> No mind to think... ")
            palekingcount += 1
        if palekingcount == 2:
            input("<Knight> No will to break... ")
            palekingcount += 1
        if palekingcount == 3:
            input("<Knight> No voice to cry suffering... ")
            palekingcount += 1
        if palekingcount == 4:
            message = input("<Knight> No... ")
            palekingcount = 0
            palekingcounton = False
    elif message.find("hornet") > -1:
        message = input("<Hornet> shaw? ")
    elif message.find("hollow knight") > -1:
        message = input("Knight walks... ")
    elif message.find("king") > -1 and random.randint(0, 5) == 1 or message.find("pale") > -1 and random.randint(0, 5) == 1 or message.find("abyss") > -1 and random.randint(0, 5) == 1 or message.find("birthplace") > -1 and random.randint(0, 5) == 1:
        input("<Knight> ...... ")
        palekingcounton = True
    else:
        message = input("<Knight> ... \n<You> ")
    
    







