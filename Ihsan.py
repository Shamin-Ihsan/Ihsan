import random
word_list = ['apple', 'table', 'green', 'dream', 'music', 'beach', 'honey', 'peace', 'Smile','Plant','Apple', 'Table', 'Green', 'Dream', 'Music', 'Beach', 'Honey', 'Peace', 'Bread', 'Never', 'Magic', 'Sunny', 'Cloud', 'Tiger', 'Fresh', 'Knife', 'Earth', 'Beach', 'Honey', 'Light', 'Queen', 'Music', 'Bliss', 'Stars', 'Honey', 'Faith', 'Awake', 'Plant', 'Bliss', 'Peace', 'Flute', 'Juicy', 'Child', 'Alarm', 'Sound', 'Brush', 'Fresh', 'Candy', 'Smile', 'World', 'Toast', 'Prize', 'Sound', 'Swarm', 'Party', 'Brush', 'Juicy', 'Flute', 'Fresh', 'World', 'Sound', 'Toxic', 'Sharp', 'Light', 'Alarm', 'Child', 'Candy', 'Party', 'Prize', 'Smile', 'Tough', 'Solid', 'Trust', 'Style', 'Error', 'Fever', 'Trust', 'Major', 'Pizza', 'Ghost', 'Hotel', 'Lodge', 'Spice', 'Peace', 'Solid', 'Style', 'Flame', 'Error', 'Trust', 'Ghost', 'Major', 'Pizza', 'Hotel', 'Spice', 'Peace', 'Flame', 'Lodge', 'Trust', 'Solid']
random_word = random.choice(word_list)        
user_word = input("Enter a 5-letter word: ")
result = ""
for i in range(len(random_word)):
    if  random_word[i].upper == user_word[i].upper:
          result += "\033[92m" + user_word[i] + "\033[0m"   #green
    elif user_word[i] in random_word:
          result += "\033[93m" + user_word[i] + "\033[0m"   #yellow
    else:
          result += "\033[91m" + user_word[i] + "\033[0m"   #red
highlighted_letters = result 
print(f"Random Word: {random_word}")
print(f"Your Word  : {highlighted_letters}") 
green=0
yellow=0
red=0
for i in result:
    if i.startswith("\033[92m"):
      green+=1
    elif i.startswith("\033[93m"):
      yellow+=1
    else:
      red+=1
if green>=3:
  print('Winner winner chicken dinner')
elif yellow>=3:
  print('Better luck next time')
elif red>=3:
  print('Arjun Kapoor does better acting than your guess ¯\_(ツ)_/¯ ')
