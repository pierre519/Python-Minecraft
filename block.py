# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:29:50 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,7)
mc.setBlock(x+1,y,z,7)
mc.setBlock(x+2,y,z,7)
mc.setBlock(x,y,z+1,7)
mc.setBlock(x,y,z+2,7)
mc.setBlock(x+1,y,z+2,7)
mc.setBlock(x+2,y,z+2,7)
mc.setBlock(x+2,y,z+1,7)