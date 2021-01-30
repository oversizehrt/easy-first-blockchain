import datetime

from block import Block


def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Big Bang", "0")


def next_block(old_block):
    return Block(old_block.index + 1,
                 datetime.datetime.now(),
                 "I'm block #" + str(old_block.index + 1),
                 old_block.hash)
