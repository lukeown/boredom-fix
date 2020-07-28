import random
wheel = [
"Old School RuneScape",
"F1 2018",
"Draw",
"Mess with plants",
"Read",
"Start new video game",
"Play guitar",
"Watch a movie",
"Cook something",
"Work!"
]

do_that = "Go do that!"
bored = input("Are you bored? (y/n/spin)  ")

while bored.lower() == 'y':
    outside = (input("Is the weather nice today? (y/n)  "))
    if outside.lower() == 'y':
        print("Go outside!")
    elif outside.lower() == 'n':
        work = (input("Did you work today? (y/n)  "))
        if work.lower() == 'y':
            tired = (input("Are you tired? (y/n)  "))
            if tired.lower() == 'y':
                print("Go chill!")
            elif tired.lower() == 'n':
                projects = (input("Are there any projects you're currently working on? (y/n/not now)  "))
                if projects.lower() == 'y':
                    print(do_that)
                elif projects.lower() == 'not now':
                    challenge = (input("Are you up for a challenge? (y/n)  "))
                    if challenge.lower() == 'y':
                        print("Go practice guitar")
                    elif challenge.lower() == 'n':
                        print("Go play a video game")
                elif projects.lower() ==  'n':
                    ideas = (input("Do you have any project ideas? (y/n)  "))
                    if ideas.lower() == 'y':
                        print(do_that)
                    elif ideas.lower() == 'n':
                        inspiration = (input("Maybe you need to be inspired. Want to watch a movie or read a book? (movie/book/neither)  "))
                        if inspiration.lower() == "movie" or "book":
                            print("Go get inspired with a {}!".format(inspiration))
                        if inspiration.lower() == "neither":
                            print("You're hopeless. Go spin the wheel.\n" + random.choice(wheel))
        elif work.lower() == 'n':
            print(do_that)
elif bored.lower() == 'n':
    print("Good! Keep doing what you're doing!")
elif bored.lower() == 'spin':
    print(random.choice(wheel))
