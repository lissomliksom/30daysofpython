def make_album(artist_name, album_title, tracks=None):
  ''' Build a dictionary describing a music album '''
  music['Artist'] = artist_name
  music['Album'] = album_title
  if tracks:
    music['Tracks'] = tracks
  return music

# Allow users to input info about albums.
while True:
  print("\nInsert artist, album and tracks(optional).")
  print("Enter 'q' at any time to quit.")

  # Start with an empty list every time to avoid conflicts with None-value
  music = {}

  artist = input("Artist name: ")
  if artist == 'q':
    break

  album = input("Album name: ")
  if album == 'q':
    break

  tracks = input("Tracks (optional): ")
  if tracks == 'q':
    break

  insert_info = make_album(artist, album, tracks)
  print(music)