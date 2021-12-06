import os
import sys
from hashlib import md5


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

secret_key = raw_data.encode()

nonce = 1
while True:
    hash_input = secret_key + str(nonce).encode()

    if md5(hash_input).hexdigest().startswith('00000'):
        print('Found:', nonce)
        break

    if nonce % 100_000 == 0:
        print('Nonce reached', nonce)

    nonce += 1
