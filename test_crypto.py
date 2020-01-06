import pytest
from crypto import encrypt, decrypt

def test_encryption():
    org_sent = 'Ive had a really great day today I hope you did too.'
    expected = 'kxg jcf c tgcnna itgcv fca vqfca k jqrg aqw fkf vqq.'
    assert encrypt(org_sent, 2) == expected

def test_decryption_known():
    org_encrypted = 'kxg jcf c tgcnna itgcv fca vqfca k jqrg aqw fkf vqq.'
    expected = 'ive had a really great day today i hope you did too.'
    assert decrypt(org_encrypted) == expected