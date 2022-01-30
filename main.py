from block import Block
block = Block("Flintin Vellara")
block.mine(23)
print(block.hash.hexdigest())
print(block.nonce)
print(block.data)
