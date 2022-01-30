import hashlib
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)
h = hashlib.sha256('a'.encode('utf-8'))
print(h.hexdigest())