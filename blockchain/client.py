import binascii
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

"""
The client should be able to send money from his wallet to another known person.
Similarly, the client should be able to accept money from a third party. 
For spending money, the client would create a transaction specifying the sender’s name and the amount to be paid. 
For receiving money, the client will provide his identity to the third party − essentially a sender of the money. 
We do not store the balance amount of money the client holds in his wallet. 
During a transaction, we will compute the actual balance to ensure that the client has sufficient balance to make the payment.
"""


class Client:

    def __init__(self):
        self._private_key = RSA.generate(1024, Crypto.Random.new().read)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
