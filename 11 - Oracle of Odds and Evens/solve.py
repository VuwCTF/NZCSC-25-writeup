from pwn import *

n = 5790334653455970971903620873436845793829158579895897066887269765695772559686113004662274698943115108890286490469235581376490897198019248877081523754458791
e = 65537
c = 3774131772357215682697513098930388907740038637280361749113689599665002638364729930669248462231522898930869595442743730985378394146481866110093136625161785

p = remote('ctf.nzcsc.org.nz', 40025)

lb = 0
ub = n

p.recvuntil(b"> ")
for i in range(1, 512):
    ciphertext = c * pow(pow(2, i), e, n) % n
    log.info("Calculating " + str(pow(2,i)) + "m")

    odds = 0
    evens = 0

    for _ in range(0, 11):
        p.sendline(bytes(str(ciphertext), encoding='utf-8'))
        r = p.recvuntil((b'0', b'1'))
        if r.endswith(b'0'):
            # even
            evens += 1
        elif r.endswith(b'1'):
            # odd
            odds += 1
        else:
            raise ValueError

    log.info("Evens: " + str(evens) + " Odds: " + str(odds))

    if evens > odds:
        ub = (ub + lb) // 2
    else: 
        lb = (ub + lb) // 2

    p.recvuntil(b'> ')
    p.sendline(b'NEXT_BOUND')
    p.recvuntil(b'> ')
    log.info("Sending UB as " + str(bytes(str(ub), encoding="utf-8")))
    p.sendline(bytes(str(ub), encoding="utf-8"))

p.interactive()