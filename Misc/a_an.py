''' 
GOAL:
Decide if a/an should be placed before adjectives.
Sort and print a list alphabetically.
'''

# List vowels, split into separate letters. Could also be done with an array.
vowels =  "a,e,i,o,u,y"
vowels.split(',')

# List adjectives, sort in reverse alphabetical order
adjectives = ['omnipotent', 'happy', 'adventurous', 'sneaky', 'curious', 'promiscuous', 'audacious']
adjectives.sort(reverse=True)

for adjective in adjectives:
  # Use ternary operator to insert a/an
  a_an = "an" if adjective[0] in vowels else "a"
  
  # List some facts about the world's greatest teddybear.
  fact = f"Tiberius is {a_an} {adjective} teddybear."
  print(fact)