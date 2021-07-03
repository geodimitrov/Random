
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, listeners):
        listeners_count = 0

        for l in listeners:
            if l.lower() not in self.listeners:
                self.listeners.append(l.lower())
                listeners_count += 1

        return listeners_count


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
print(mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']))
print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))
