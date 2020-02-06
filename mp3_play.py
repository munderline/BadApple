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

import time
import pygame

file_mp3 = "tyc.mp3"

pygame.mixer.init()
print("play mp3 start")
track = pygame.mixer.music.load(file_mp3)


pygame.mixer.music.play()
time.sleep(100)
pygame.mixer.music.stop()


