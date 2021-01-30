import life_of_block
import random


blockchain = [life_of_block.create_genesis_block()]
previous_block = blockchain[0]


num_of_blocks_until_the_end_of_the_world = random.randint(3,20)

for generation in range(0, num_of_blocks_until_the_end_of_the_world):
    new_block = life_of_block.next_block(previous_block)
    blockchain.append(new_block)
    previous_block = new_block

    print(f"New block #{format(new_block.index)} " +
          "has been added to the blockchain.")
    print(f"Hash: {format(new_block.hash)}\n")
