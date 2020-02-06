#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : negatron
#   Email         : vip170706@gmail.com
#   File Name     : mp3_play.py
#   Last Modified : 2019-07-16 16:11
#   Describe      :
#
# ====================================================

import pygame
import time
import curses
from char_data import char_data

count = 0
frame_rate = 0.0333667
file_mp3 = "data/apple.mp3"

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(50, 125)

pygame.mixer.init()
track = pygame.mixer.music.load(file_mp3)
pygame.mixer.music.play()
#  time.sleep(0.4)
now = time.time()

for frame_data in char_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * frame_rate:
        pass
    stdsrc.refresh()
    count += 1

curses.endwin()
