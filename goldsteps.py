import time

import mcpi.block as block
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("connected")

def goldsteps():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.GRASS.id:
        mc.setBlock(pos.x,pos.y-1,pos.z, block.GOLD_BLOCK.id)

while True:
    time.sleep(0.25)
    goldsteps()
