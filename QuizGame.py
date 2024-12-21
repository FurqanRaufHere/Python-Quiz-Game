# Computer Quiz Game
print("Welcome to my Computer Quiz Game ")
print("-" * 40)

#Introduction and start of the Game
playing = input("Do you want to play? (yes/no): ").lower()
score = 0
totalQuestions = 4

if playing != "yes":
    print("Next time Maybe, Goodbye! ")
    quit()
print("\nGreat, so let's Play :) ")

# Question 1
print("\n1. What does CPU stand for?")
answer = input("a) Central Processing Unit\nb) Central Power Unit\nc) Central Program Utility\nd) None of the above\nYour answer: ").lower()
if answer == "a" or answer == "central processing unit":
    print("Correct Answer! 🎉")
    score += 1
else:
    print("Wrong Answer! The correct answer is a) Central Processing Unit.")

# Question 2
print("\n2. Which company is known for developing the Windows operating system?")
answer = input("a) Apple\nb) Microsoft\nc) Google\nd) IBM\nYour answer: ").lower()
if answer == "b" or answer == "microsoft":
    print("Correct Answer! 🎉")
    score += 1
else:
    print("Wrong Answer! The correct answer is b) Microsoft.")

# Question 3
print("\n3. Which language is primarily used for web development and runs in the browser?")
answer = input("a) C++\nb) JavaScript\nc) Python\nd) Java\nYour answer: ").lower()
if answer == "b" or answer == "javascript":
    print("Correct Answer! 🎉")
    score += 1
else:
    print("Wrong Answer! The correct answer is b) JavaScript.")

# Question 4
print("\n4. What does GPU stand for?")
answer = input("a) Graphical Processing Unit\nb) Graphics Power Unit\nc) General Processing Utility\nd) Graphics Protocol Unit\nYour answer: ").lower()
if answer == "a" or answer == "graphical processing unit":
    print("Correct Answer! 🎉")
    score += 1
else:
    print("Wrong Answer! The correct answer is a) Graphical Processing Unit.")


# Final Score
print("\n" + "-" * 40)
print(f"You got {score} out of {totalQuestions} questions correct!")

if score == totalQuestions:
    print("Excellent, You are a Genius!")
elif score>=totalQuestions // 2:
    print("Good job! You know your stuff. ")
else:
    print("Better luck next time. Keep learning! ")

# Ending Note
print("Thanks for Playing!")

