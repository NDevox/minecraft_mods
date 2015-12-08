import time

from picraft import World, Vector, Block

world = World()

world.say("connected")

def stairs_to_heaven():
    pos = world.player.tile_pos
    #print(world.player.direction)
    if world.blocks[pos + Vector(x=1)].id == 0:
        world.blocks[pos + Vector(x=1)] = Block('stone')
while True:
    time.sleep(0.05)
    stairs_to_heaven()
