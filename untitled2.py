from mcpi.minecraft import MInecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x-1,y,z-1,x+1,y,z+1,8)
    time.sleep(10)