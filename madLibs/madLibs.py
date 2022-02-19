gameCode =  input("Which game would you like to play? Please enter a number between 1 and 3: ")

def game1():
    print(f"\nWelcome to Game 1!\n")
    One= input("Adjective #1: ")
    Two= input("Adjective #2: ")
    Three = input("Adjective #3: ")
    Four = input("Adjective #4: ")
    Five = input("Articel of Clothing ")
    Six = input("Exclamation: ")
    Seven = input("Geographical Location: ")
    Eight = input("Noun: ")
    Nine = input("Part of the Body: ")
    Ten = input("Plural Noun #1: ")
    Eleven = input("Plural Noun #2: ")
    Twelve = input("Spanish Word #1: ")
    Thirteen = input("Spanish Word #2: ")


    print(f"\nBullfighting is a {One} sport which is very popular in {Seven}. A bullfighter is called a Matador, and his equipment \
consists of a long, sharp {Eight} called a {Twelve}, and a bright red {Five}. He waves his {Five} at the bull, which makes the bull \
{Two} and causes him to charge. The matador then goes through a series of {Three} maneuvers to avoid getting caught on the \
bull's {Nine}. If the matador kills the bull, the spectators yell '{Thirteen}!' and thow their {Ten} into the ring. If the bull wins, they \
yell '{Six}!' and call for another Matador. Bullfighting is a vary {Four} sport, but it will never be popular in America because \
{Eleven} is too popular!")


def game2():
    print(f"\nWelcome to Game 2!\n")
    One= input("Enter a number: ")
    Two= input("A type of game: ")
    Three = input("Adjective #1: ")
    Four = input("Adjective #2: ")
    Five = input("Adjective #3: ")
    Six = input("Adjective #4: ")
    Seven = input("Adjective #5: ")
    Eight = input("Noun: ")
    Nine = input("Another Noun: ")
    #Ten = input("Plural Noun: ")
    Eleven = input("Another Plural Noun: ")
    Twelve = input("Type of Liquid: ")
    Thirteen = input("Another Type of Liquid: ")
    
    print(f"\nSpring vacation usually falls around Easter time. The schools are closed and all the students get {One} weeks off. \
The {Three} teachers also get a vacation. There are lots of things to do during Easter vacation. Some kids loaf around and watch \
the {Eight}. Others get outside and play {Two}, while more abitious students spend their time studying their {Four} books so they \
can grow up to become {Eleven}. Little kids also color {Five} eggs. Here's how you color an egg; first mix a package of {Six} dye \
in a bowl full of {Twelve}. Then, dip a {Nine} in the bowl and rinse it off with {Thirteen}. Then, after it dries, you can paint it with a \
brush. Then show it to your friends, who will say, 'Boy what a {Seven} egg!' ")

def game3():
    print(f"\nWelcome to Game 3!\n")
    One= input("A Funny Noise: ")
    Two= input("A Person You Know: ")
    Three = input("A Place: ")
    Four = input("Adjective #1: ")
    Five = input("Adjective #2: ")
    Six = input("Adjective #3: ")
    Seven = input("Adjective #4: ")
    Eight = input("Animal #1: ")
    Nine = input("Animal #2: ")
    Ten = input("Plural Noun #1: ")
    Eleven = input("Plural Noun #2: ")
    Twelve = input("Plural Noun #3: ")
    Thirteen =input("Plural Type of Food: ")

    print(f"\nOne of the most {Four} characters in fiction is called 'Tarzan of the {Eleven}'. Tarzen was raised by a {Eight} and \
lives in a {Five} jungle in the heart of the darkest {Three}. He spends most of his time eating {Thirteen} and swinging from trees to \
{Ten}. Whenever he gets angry, he beats on his chest and says '{One}'! This is his war cry. Tarzen always dresses in {Six} shorts \
made form the skin of a {Nine}, and his best friend is a {Seven} chimpanzee named Cheetah. He is supposed to be able to speak \
to elephants and {Twelve}. In the movies, Tarzan is played by {Two}.")

def restart(gameCode):
    while True:
        key = input(f"\n Thank you for playing! Would you like to play again? (Enter y or n): ").lower()
        if key == "y":
            gameCode =  str(input("Which game would you like to play? Please enter a number between 1 and 3: "))
            break
        elif key == "n":
            print("\nOkay, good bye!")
            gameCode = "end"
            break
        else:
            print("\nI think you misstpyed!\n")
    return gameCode

while True:
# Game Loop
    if gameCode.isnumeric() == False:
        gameCode = input("Please only enter a number between 1 and 3: ")
    else:
        gameCode=int(gameCode)   
    if gameCode == 1:
        game1()
        gameCode = restart(gameCode)
    elif gameCode == 2:
        game2()
        gameCode = restart(gameCode)
    elif gameCode == 3:
        game3()
        gameCode = restart(gameCode)
    else:
        gameCode = input("Please only enter a number between 1 and 3: ")
    if gameCode == "end":
        break
