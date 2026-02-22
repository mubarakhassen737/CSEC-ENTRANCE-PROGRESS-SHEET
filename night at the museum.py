word = input().strip()

current = 'a'
moves = 0

for letter in word:
    difference = abs(ord(letter) - ord(current))
    step = min(difference, 26 - difference)
    moves += step
    current = letter

print(moves)