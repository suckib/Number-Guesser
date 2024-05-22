print("welcome to my quiz")

playing = input("DO you wanna play? ")

if playing.lower() != "yes":
    quit()

print("OK, let's play")
point = 0

answer = input("What CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    point += 1
else:
    print("Incorrect!")

answer = input("What GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    point += 1
else:
    print("Incorrect!")

answer = input("What RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    point += 1
else:
    print("Incorrect!")

answer = input("What ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    point += 1
else:
    print("Incorrect!")

answer = input("What gg stands for? ")
if answer.lower() == "good game":
    print('Correct!')
    point += 1
else:
    print("Incorrect!")

print("you get " + str(point)+ " points for correct answer")
print("your corect answer is " + str((point / 5) * 100) + "%")