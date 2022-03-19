#Question 1: Ryerson letter grade
def ryerson_letter_grades(pct):
 if pct <= 49:
  return 'F'
 if pct <= 52:
   return 'D-'
 if pct <= 56:
   return 'D'
 if pct <= 59:
   return 'D+'
 if pct <= 62:
   return 'C-'
 if pct <= 66:
   return 'C'
 if pct <= 69:
   return 'C+'
 if pct <= 72:
   return 'B-'
 if pct <= 76:
   return 'B'
 if pct <= 79:
   return 'B+'
 if pct <= 84:
   return 'A-'
 if pct <= 89:
   return 'A'
 else:
   return 'A+'

#Question 2: Even the odds
def only_odd_digits(n):
  if_odd = True
  for a in str(n):
    if int(a) % 2 == 0:
      if_odd = False
  return if_odd

#Question 3: Ascending list
def is_ascending(items):
  if_ascending = True 
  for b in range(0,len(items)-1):
    if items[b] <= items[b-1]:
      if_ascending = False
  return if_ascending

#Question 4: Riffle shuffle kerfuffle
def riffle(items, out = True):
  result = []
  out = True
  first_half = items[:len(items)//2]
  second_half = items[len(items)//2:]
  for i in range (0,len(items)//2):
     result = result + [first_half[i]] + [second_half[i]]
  return result

#Question 5: Cyclops numbers
def is_cyclops(n):
  cyclops = True
  first_half = str(n)[:(len(str(n))-1)//2]
  second_half = str(n)[(len(str(n))+1)//2:]
  if len(str(n)) % 2 == 0:
   cyclops = False
  for i in range(0,(len(str(n))-1) // 2):
     if first_half[i] == 0 or second_half[i] == 0:
      cyclops = False
  else:
    if str(n)[(len(str(n))-1) // 2] != '0':
      cyclops = False
  return cyclops

#Question 6: Domino Cycle
def domino_cycle(tiles):
  domino = False
  if len(tiles) == 0:
    domino = True
  if len(tiles) == 1 and tiles[0][0] == tiles[0][1]:
    domino = True
  if len(tiles) == 2 and tiles[0][1] == tiles[1][0] and tiles[0][0] == tiles[1][1]:
    domino = True
  for i in range (0,len(tiles)-2):
    if tiles[i][1] == tiles[i+1][0] and tiles[i+1][1] == tiles[i+2][0] and tiles[0][0] == tiles[len(tiles)-1][1]:
     domino = True
  return domino

#Question 7: Count dominators
def count_dominators(items):
  count = 1
  if len(items) == 0:
    count = 0
  if len(items) == 1:
    count = 1
  for i in range (0, len(items)-1):
    if items[i] > max(items[i+1:]):
      count = count + 1
  return count

#Question 8: Try a spatula
def pancake_scramble(text):
  first = ''
  last = ''
  for i in range (0, len(text)):
    if i % 2 == 0:
     first = first + text[i]
    if i % 2 != 0:
      last = last + text[i]
  return first[::-1] + last

#Question 9: Fail while daring greatly
def josephus(n, k):
  circle = list(range(1, n+1))
  dead = []
  index = 0
  while len(circle):
    index = (index-1+k) % len(circle)
    person = circle[index]
    circle.remove(person)
    dead.append(person)
  return dead
  
#Question 10: Crack the crag
def crag_score(dice):
  if dice[0] == dice[1] == dice[2]:
    return 25
  if dice[0] == dice[1] or dice[0] == dice[2] or dice[1] == dice[2]:
    if dice[0] + dice[1] + dice[2] == 13:
      return 50
    else:
      if dice.count(max(dice)) == 2:
        return max(dice)*2
      elif dice.count(min(dice)) == 2:
        return min(dice)*2
  if dice[0]+ dice[1] + dice[2] == 13:
    return 26
  if 1 in dice and 2 in dice and 3 in dice:
    return 20
  if 4 in dice and 5 in dice and 6 in dice:
    return 20
  if 1 in dice and 3 in dice and 5 in dice:
    return 20
  if 2 in dice and 4 in dice and 6 in dice:
    return 20
  else:
    return max(dice)
