# C-8: Signal From Sector 91
> A fragmented transmission was intercepted from an old relay — its contents layered and disguised. From what little we can reconstruct, the key was first spoken in a rhythmic tongue once used over the air. It was then compressed into something tighter, more obscure, and finally converted into raw bytes. The message itself? Secured with a method older than most passwords, and buried under two coats of obfuscation. Your job: recover the key, unwrap the message, and reveal what was so carefully hidden. [encoded_message.txt](encoded_message.txt)

This text file contains two hex strings, `encoded_key` and `encoded_flag`. 
We will first decode the key. 
Decoding from hex produces:
```
ma=CL:xXLR1t7P$k3L,<p+cC4!1t7P$k+L,<p+cC4!1t7P9Qma=CL:TXx#[yZEkLma=Ct)aC4!.4IvWiNBcfl/TXLR!&7PkLma=Ct)!{4!1t7PkL^DQJm+${4!.4nuWiNBcfl/xXwS:y5ETj0XPEt)aC4!!&7P$k3LYJm+${4!.4IvFl3LYJm+cC4!!&7P9Q^DQJm+cC4!.4IvFl+LzI.W<0#F}u1ETj0XD
```
which looks similar to the base 45 used in Challenge 5 in its use of symbols, but notably has uppercase and lowercase characters. Looking into similar encodings we find base 91. Decoding from b91 gives:
```
di di/dah dah di/di di dah/di/di di di/di di di/dah di dah dah/dah dah dah/di di dah/di di dah di/dah dah dah/di di dah/dah di/dah di di/dah/di di di di/di/dah di dah/di/dah di dah dah
```
which is morse code. It translates to `IGUESSYOUFOUNDTHEKEY`. 
Decoding the flag from hex gives `NRUK[WT639AT274UI85TU]`. 
The presence of the brackets, and the four characters beforehand suggests that a byte-level operation such as XOR is not necessary, and instead a simple Vigenère cipher with the key found above gives us the flag: `FLAG[EB639CF274AD85FA]`.