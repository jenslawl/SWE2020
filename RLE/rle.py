import time
import sys

def encode(mess):
    """ Run length endoding - konverter strenge fra 'wwwwwwbbbb' til '6w4b'"""
    
    if mess == '':
        return ''
    else:
        res = []
        old = mess[0]
        i = 0
        for c in mess:
            if c == old:
                i += 1
            else:
                res.append('%d%c' % (i,old))
                old = c
                i = 1
        res.append('%d%c' % (i,c))
        return ''.join(res)
    
def decode(mess):
    """ Run length endoding - konverter strenge fra '6w4b 'wwwwwwbbbb''"""
    res = ''
    count = 0
    for c in mess:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res += c*count
            count = 0
    return res
    
if __name__ == '__main__':
    import sys
    argv = sys.argv
    if '-e' in argv:
        filename = argv[argv.index('-e')+1]
        func = encode
    elif '-d' in argv:
        filename = argv[argv.index('-d')+1]
        func = decode
    else:
        filename = argv[-1]
        func = lambda x: decode(encode(x))
        
    with open(filename,'r') as f:
        print(func(f.read()))

    time.sleep(1)
    exit(0)
