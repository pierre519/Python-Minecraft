# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:49:00 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x-1,y-1,z)
    if a==9 or a==8:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)
   
