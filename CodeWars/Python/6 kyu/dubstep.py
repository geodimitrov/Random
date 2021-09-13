def song_decoder(song):
    return ' '.join(el for el in song.split('WUB') if el)