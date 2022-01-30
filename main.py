from block import Block
block = Block("Random String")
# difficulty level 19!
block.mine(19)
print(block.hash.hexdigest())
print(block.nonce)
print(block.data)
