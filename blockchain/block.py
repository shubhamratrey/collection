import hashlib


class Block:

    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def sha256(self, message):
        return hashlib.sha256(message.encode('ascii')).hexdigest()

    def mine(self, message, difficulty=1):
        assert difficulty >= 1
        prefix = '1' * difficulty
        for i in range(1000):
            digest = Block.sha256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                print("after " + str(i) + " iterations found nonce: " + digest)
            return digest
