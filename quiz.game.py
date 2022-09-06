print("welcome to my python quiz")
playing = input("do u wanna play quiz game ? ")

if playing.lower() != "yes" :
    quit()

print("Okay let's play :)")
score = 0

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct !!! ")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct !!! ")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct !!! ")
    score += 1
else:
    print("incorrect!")

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct !!! ")
    score += 1
else:
    print("incorrect!")

answer = input("what does PSU stand for? ").lower()
if answer == "power supply unit":
    print("correct !!! ")
    score += 1
else:
    print("incorrect!")

print("you got " +str(score) + "questions correct ...")
print("you got " +str((score/4)) * 100 + "%")