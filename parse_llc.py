from pwn import *

ip,port = '164.90.142.2 30184'.split(" ")
c = remote(ip, port)
c.recvuntil(b'COMMAND: ')

blacklist = ['os','exit','http','ssh']

def solver(q):
    if any(x in q for x in blacklist):
        c.sendline(b'Y')
    else:
        try:
            q = eval(q)
            if any(x in q for x in blacklist):
                c.sendline(b'Y')
            else:
                c.sendline(b'N')
        except:
            c.sendline(b'Y')

q = c.recvline().strip().decode()
solver(q)
while True:
    c.recvline()
    q = c.recvline().decode()
    print(q)
    if q.startswith("COMMAND:"):
        q = q.replace("COMMAND: ", "").strip()
        solver(q)
    else:
        print(c.recvline().decode( ))
        break
        
