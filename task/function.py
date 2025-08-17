# 1. Unique Elements Function
def unique_elements(lst):
	unique = []
	for item in lst:
		if item not in unique:
			unique.append(item)
	print(unique)
print("Unique Elements Function")
unique_elements([1, 2, 2, 3, 4, 1, 5])

# 2. List Rotation
def rotate_list(lst, k):
	n = len(lst)
	if n == 0:
		print(lst)
		return
	k = k % n
	print(lst[-k:] + lst[:-k])
print("\nList Rotation")
rotate_list([1, 2, 3, 4, 5], 2)

# 3. Find Longest Word
def longest_word(sentence):
	words = sentence.split()
	longest = ''
	for word in words:
		if len(word) > len(longest):
			longest = word
	print(longest)
print("\nFind Longest Word")
longest_word("Python is an amazing programming language")

# 4. Sum of Digits Function
def sum_of_digits(num):
	num = abs(num)
	total = 0
	for digit in str(num):
		total += int(digit)
	print(total)
print("\nSum of Digits Function")
sum_of_digits(12345)

# 5. Character Frequency Counter
def char_frequency(s):
	freq = {}
	for char in s:
		freq[char] = freq.get(char, 0) + 1
	print(freq)
print("\nCharacter Frequency Counter")
char_frequency("hello")