#!/usr/bin/python

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    songs = map(int,raw_input().split())
    k = int(raw_input())-1
    uj = songs[k]
    songs.sort()
    print songs.index(uj)+1
