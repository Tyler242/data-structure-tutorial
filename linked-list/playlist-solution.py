class Song:

    def __init__(self, name) -> None:
        """
            Initialize a new song for the playlist
        """
        # name of the song
        self.name = name

        # pointers to next and previous song
        self.next = None
        self.prev = None


class Playlist:

    def __init__(self) -> None:
        """
            Initialize a new playlist
        """
        # head and tail of the playlist
        self.head = None
        self.tail = None

        # set the current song to the head
        self._curr = self.head

    def move_next(self):
        """
            Move to the next Song
        """
        # check if the playlist is empty
        if self.head is None:
            return
        # check if the current song is the tail (last song)
        if self._curr is self.tail:
            # set the current song to the head (first song)
            self._curr = self.head
        # if the current song is not the tail
        else:
            self._curr = self._curr.next

    def move_prev(self):
        """
            Move to the previous Song
        """
        # check if the playlist is empty
        if self.head is None:
            return
        # check if the current song is the head (first song)
        if self._curr is self.head:
            # set the current song to the tail (last song)
            self._curr = self.tail
        # if the current song is not the head
        else:
            self._curr = self._curr.prev

    def add(self, song):
        """
            Add a new Song to the tail
        """
        new_song = Song(song)

        # check if the playlist is empty
        if self.tail is None:
            # set the new_song as both the head and tail
            self.tail = new_song
            self.head = new_song
            self._curr = self.head

        # if the playlist is not empty
        else:
            # add the new song to the end of the playlist
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

    def remove(self):
        """
            Remove the current Song
        """
        # check if the playlist is empty
        if self.head is None:
            return

        # if the current song is the only song in the playlist
        if self.head is self.tail:
            # delete the song by setting head, tail and _curr to None
            self.head = None
            self.tail = None
            self._curr = self.head

        # if the current song is the head
        elif self._curr is self.head:
            # delete the song by removing and reseting the pointers
            self.head.next.prev = None
            self.head = self.head.next
            self._curr = self.head

        # if the current song is the tail
        elif self._curr is self.tail:
            # delete the song by removing and reseting the pointers
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self._curr = self.tail
        # if the current song is somewhere between the head and tail
        else:
            # delete the song by reseting the pointers
            self._curr.prev.next = self._curr.next
            self._curr.next.prev = self._curr.prev
            self._curr = self._curr.next

    def get_curr_song(self):
        """
            Return the current song
        """
        return self._curr


# Create a new playlist
playlist = Playlist()

# Control when the user is finished
done = False
empty = 'Playlist is empty'

while not done:
    if playlist.get_curr_song() != None:
        print(f'Current song: {playlist.get_curr_song().name}')
    else:
        print(f'Current song: {empty}')
    # Menu
    print('1. Next song')
    print('2. Previous song')
    print('3. Add song')
    print('4. Remove current song')
    print('5. Quit')
    option = int(input('> '))

    # controller
    if option == 1:
        playlist.move_next()
    elif option == 2:
        playlist.move_prev()
    elif option == 3:
        song_name = input('Please enter the song name: ')
        playlist.add(song_name)
    elif option == 4:
        playlist.remove()
    elif option == 5:
        print('Goodbye')
        done = True
