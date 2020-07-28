# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:48:44 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=6
while t<100:
    mc.postToChat("hi")
    t=t+5