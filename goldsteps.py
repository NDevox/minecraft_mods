import mcpi.minecraft as minecraft
import mcpi.block as block

import time


mc = minecraft.Minecraft.create()

mc.postToChat("Hello, World!")

def goldsteps():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.GRASS.id:
        mc.setBlock(pos.x,pos.y-1,pos.z, block.GOLD_BLOCK.id)

while True:
    time.sleep(0.25)
    goldsteps()
