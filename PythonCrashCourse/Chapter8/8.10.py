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

send_messages(teddybear_facts)

# Print both lists to make sure the messages were moved correctly
print(f"First list: {teddybear_facts}")
print(f"Second list: {sent_messages}")


