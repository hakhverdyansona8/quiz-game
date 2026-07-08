print("--- Welcome to the Quiz ---")
score = 0

# Question 1
ans1 = input("1. What is the name of the text type in Python (str/int/float)? ").lower().strip()
if ans1 == "str":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was 'str'")

# Question 2
ans2 = input("2. Which symbol is used to start a comment in Python? ").lower().strip()
if ans2 == "#":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '#'")

# Question 3
ans3 = input("3. What is 2 to the power of 3 (2**3)? ").lower().strip()
if ans3 == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '8'")

# Question 4
ans4 = input("4. What type will type(5/2) return in Python? ").lower().strip()
if ans4 == "float":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was 'float'")

# Question 5
ans5 = input("5. What is 5 squared (5²)? ").lower().strip()
if ans5 == "25":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '25'")

# Question 6
ans6 = input("6. What is the square root of 144 (√144)? ").lower().strip()
if ans6 == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '12'")

# Question 7
ans7 = input("7. What will type('hello') return (str/int/float)? ").lower().strip()
if ans7 == "str":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was 'str'")

# Question 8
# Fixed: Checked against lowercase "false" since .lower() is used
ans8 = input("8. What is the value of bool(0) (True/False/0/Error)? ").lower().strip()
if ans8 == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was 'False'")

# Question 9
ans9 = input("9. What is the least common multiple (LCM) of 7 and 9? ").lower().strip()
if ans9 == "63":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '63'")
    
# Question 10
ans10 = input("10. Which number is a prime number (21/33/29/45)? ").lower().strip()
if ans10 == "29":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '29'")

# Question 11
ans11 = input("11. What is 2 to the power of 4 (2**4)? ").lower().strip()
if ans11 == "16":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '16'")

# Question 12
ans12 = input("12. What is the smallest prime number? ").lower().strip()
if ans12 == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '2'")

# Question 13
ans13 = input("13. What is the sum of angles in a triangle (in degrees)? ").lower().strip()
if ans13 == "180":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was '180'")


print(f"\nQuiz finished! Your score: {score} / 13")
if 10 <= score <= 13:
    print("Excellent job!")
elif 5 <= score < 10:
    print("Not bad, but you can do better!")
else:
    print("You need to review the material.")