teddybear_facts = [
  'Tiberius is a marvelous teddybear',
  'Tiberius loves to go on humble adventures',
  'Tiberius\' favorite color is banana-cerulean',
  'Tiberius starts his day with an omnipotent cup of coffee',
  'Tiberius describes himself as playful and capricious'
]

sent_messages = []

def send_messages(messages):
  ''' Move all messages to new list, sent_messages '''
  while messages:
    send = messages.pop()
    sent_messages.append(send)

# Copy original list
new_facts = teddybear_facts[:]

# Move all facts from copied list to new list
send_messages(new_facts)

# Print lists to show that the original list has retained its messages
print(f"First list: {teddybear_facts}")
print(f"Second list: {sent_messages}")


