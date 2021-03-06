import hashlib


class Block:

    def __init__(self, index, time_stamp, data, previous_hash):
        self.index = index
        self.time_stamp = time_stamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
        # I used .encode('utf-8') because Python 3 uses Unicode
        # but .sha256() waits for UTF-8 code
        # I did had this error:
        # TypeError: Unicode-objects must be encoded before hashing

    def hash_block(self):
        hash = hashlib.sha256()
        hash.update(str(self.index).encode('utf-8') +
                    str(self.time_stamp).encode('utf-8') +
                    str(self.data).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8'))
        return hash.hexdigest()
