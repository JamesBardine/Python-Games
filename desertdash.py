

print(input("Hello, welcome to Desert Island Dash"))

name = input ("Enter your name: ")
gender = input ("Enter your gender: ")

print(input("You are on a desert island, " + name))
sword = (input("You see a sword, type 'grab' to grab it: "))
if sword == "grab":
    print(input("You have a sword in your hand"))
    bird = (input("You see enemy bird, type 'hit' to hit it: "))
    if bird == "hit":
        print(input("You kill it in one hit with your sword"))
        print(input("You now have a dead bird rotting in your inventory, loser."))
        print(input("The end, you win, " + name + ", if you call having a dead bird rotting in your inventory winning."))
    else:
        print(input("You do not hit it, it kills you"))
        print(input("You dead"))
        print(input("The end, you lose"))
else:
   print(input("You ignore the sword"))
   enemy_bird = (input("You see enemy bird, type hit to hit it: "))
   if enemy_bird == "hit":
       print(input("You don't have sword, the bird kills you"))
       print(input("You dead"))
       print(input("You lose"))
   else:
       print(input("the bird kills you"))
       print(input("you dead"))
       print(input("you lose"))


