from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z = mc.player.getTilePos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
for i in range(10):
    for j in range(5):
        for k in range(5):
            Tree(x+i*5,y+i*j,z+i*k)