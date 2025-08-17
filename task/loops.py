# 1. Numbers Divisible by 3 or 5 but not both
print("Numbers Divisible by 3 or 5 but not both")
for i in range(1, 101):
    if (i % 3 == 0) ^ (i % 5 == 0):
        print(i, end=" ")
print("\n")

# 2. Reverse Words in a Sentence (without split/reverse)
print("Reverse Words in a Sentence")
sentence = "Python is fun"
word = ""
words = []
for char in sentence:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char
if word:
    words.append(word)
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")
print("\n")

# 3. Star Diamond Pattern (n = 5)
print("Star Diamond Pattern")
n = 5
for i in range(1, n+1, 2):
    print(" " * ((n-i)//2) + "*" * i)
print()

# 4. Count Consonants in a String
print("Count Consonants in a String")
input_str = "hello world"
count = 0
vowels = "aeiouAEIOU"
for ch in input_str:
    if ch.isalpha() and ch not in vowels:
        count += 1
print(count)
print()

# 5. Number Guessing Game
print("Number Guessing Game")
secret = 8
while True:
    guess = input("Guess the number: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")
