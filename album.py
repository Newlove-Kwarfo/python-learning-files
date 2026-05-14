"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information.
Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album
"""


def make_album(artist_name, album_title, number_of_songs=None):
    album = {'Artist name' : artist_name, 'Album title' : album_title}
    if number_of_songs:
        album['Number of Songs: '] = number_of_songs
    return album

"""
album1 = make_album('John', 'Cube', 5)
print(album1)
album2 = make_album('Joanna', 'Divine')
print(album2)
album3 = make_album('Skz', 'Oddinary', 6)
print(album3)
"""

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

while True:
    print('\nEnter q at any point in time to exit')
    artist = input('Enter the name of the artist here: ')
    if artist == 'q' or artist == 'Q':
        break

    title = input('Enter the title of their album here: ')
    if title == 'q' or title == 'Q':
        break

    album = make_album(artist, title)
    print(album)