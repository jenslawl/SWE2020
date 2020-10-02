from rle import encode,decode

def test_encode():
    assert encode('aa') == '2a'
    assert encode('kkkbbb') == '3k3b'
    assert encode ('') == ''
    
def test_decode():
    assert decode('2a') == 'aa'
    assert decode('3k2y') == 'kkkyy'
    assert decode('3k1y') == 'kkky'
    assert decode('4k5b1y3h') == 'kkkkbbbbbyhhh'
