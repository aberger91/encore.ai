#!/usr/bin/python3

import os
import sys
import json
import pylyrics3 as pyl

def download_artist_lyrics(argv):
    os.mkdir(argv)
    lyrics = pyl.get_artist_lyrics(argv)
    f = open('../data/' + argv + '.txt', 'w')
    json.dump(lyrics, f)

def save_artist_lyric_files(argv):
    f = json.loads(open('../data/' + argv + '.txt', 'r').read())
    for k,v in f.items():
        with open('../data/' + argv + '/' + k + '.txt.', 'w') as song:
            song.write(v)

if __name__ == '__main__':
    argv = sys.argv[1]
    download_artist_lyrics(argv)
    save_artist_lyric_files(argv)

