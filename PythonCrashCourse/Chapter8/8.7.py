music = {}

def make_album(artist_name, album_title, tracks=None):
  ''' Build a dictionary describing a music album '''
  music['Artist'] = artist_name
  music['Album'] = album_title
  if tracks:
    music['Tracks'] = tracks
  return music

the_beatles = make_album("The Beatles", "Revolver")
print(the_beatles)

the_streets = make_album("Mike Skinner / The Streets", "Original Pirate Material")
print(the_streets)

father_john_misty = make_album("Joshua Tillman / Father John Misty", "Pure Comedy")
print(father_john_misty)

# Include tracks
graveyard = make_album("Graveyard", "Lights Out", 9)
print(graveyard)

the_cure = make_album("The Cure", "Japanese Whispers", 8)
print(the_cure)