# start with a function to create the album

def make_album(artist, album_title):
    album = {'artist': artist.title(), 'title': album_title.title()}
    return album

keepgoing = True

while keepgoing:
    artist_name = input("Please enter the name of the artist (or 'quit' to stop): ")
    if artist_name != 'quit':
        title = input("Please enter the name of the album: ")
        created_album = make_album(artist_name, title)
        print(created_album)
    else:
        keepgoing = False    
