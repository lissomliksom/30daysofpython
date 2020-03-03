guest_list = ['Mahatma Ghandi', 'Martin Luther King Jr', 'Barack Obama', 'Richard Feynman']
message = "you are invited to dinner"
print(guest_list[0], message)
print(guest_list[1], message)
print(guest_list[2], message)
print(guest_list[3], message)

#One guest can't make it. Replace him in list.
print(f"\nUnfortunately, {guest_list[2]} can't make it")
guest_list[2] = 'Marcus Aurelius'

print("\nNew guest list:")
print(guest_list[0], message)
print(guest_list[1], message)
print(guest_list[2], message)
print(guest_list[3], message)

print("\nDear guests, I just found a bigger dinner table. More guests will be joining us.")

#Add guest to beginning of list
guest_list.insert(0, 'John Lennon')

#Add another guest to middle of list
guest_list.insert(3, 'Elvis')

#Add another guest to end of list
guest_list.append('Jimi Hendrix')

revised_message = "Welcome to my big dinner party,"
print(revised_message, guest_list[0])
print(revised_message, guest_list[1])
print(revised_message, guest_list[2])
print(revised_message, guest_list[3])
print(revised_message, guest_list[4])
print(revised_message, guest_list[5])
print(revised_message, guest_list[6])

#Remove all but two guests (in a terrible way) using pop()
print("\nUnfortunately, my new table didn't arrive. I only have room for two guests")
removed_guest = guest_list.pop()
print(f"I'm terribly sorry, but you'll have to stay home {removed_guest}")
removed_guest = guest_list.pop()
print(f"I'm terribly sorry, but you'll have to stay home {removed_guest}")
removed_guest = guest_list.pop()
print(f"I'm terribly sorry, but you'll have to stay home {removed_guest}")
removed_guest = guest_list.pop()
print(f"I'm terribly sorry, but you'll have to stay home {removed_guest}")
removed_guest = guest_list.pop()
print(f"I'm terribly sorry, but you'll have to stay home {removed_guest}")

last_message = "You're still invited,"
print(last_message, guest_list[0])
print(last_message, guest_list[1])

#Remove the last two guests using del. Notice that after deleting [0], the only remaining guest is now in the [0]-position
del guest_list[0]
del guest_list[0]

#Print empty guest list
print(guest_list)