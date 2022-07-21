import zlib, base64
file1=open('compressd.txt','r')
text=file1.read()
file1.close()

code = zlib.decompress(base64.b64decode(text))
code=code.decode('utf-8')

f=open('dcompressed.txt','w')
f.write(code)
f.close()