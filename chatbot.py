# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:01:21 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
blockType=int(input("請輸入要放的方塊ID:"))
mc.setBlockx,y,z blockType