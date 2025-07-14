# C-10: Secure Vault
> You've intercepted a suspicious executable from a cyber criminal organization. Intelligence suggests it contains a secret treasure code. Your mission is to reverse engineer the binary and extract the hidden flag.  
Connect over TCP using netcat or a similar program to solve: `nc ctf.nzcsc.org.nz 35627`  
[[rev|Download Binary Here]]

Decompiling this binary in Ghidra we can see there are a lot of `printf` and `puts` calls. 
There is a hardcoded ciphertext decrypted using a function called `xor_decrypt`, and another decrypted using `custom_decode`, and also a `printf` statement which claims to print the flag using the value `__s2`.
This variable is set by function called `build_string`.
![[build_string.png]]
*build_string()*

This function simply builds an char array consisting of the flag. Decoding this hex gives us the flag: `FLAG[23C26B6Z3A99MC5E]`.
#### Easter eggs
*This easter egg was only on the server so we were unable to archive it.*

This challenge has a lot of red herrings. We can see that the 'treasure' can be found by entering the flag itself, setting `iVar1` to true. This has the following result:
![[treasure.png]]
which is certainly interesting.

The 'encoded message' is simply ROT13 encoded giving `FLAG[notHerEFlag]`

So far we have been unable to find any meaning to the 'hint' that is decoded using XOR.