# C-11: Oracle of Odds and Evens
> A digital oracle guards a coveted prize, its knowledge locked behind RSA encryption. It offers only the faintest clues about a hidden message – the evenness or oddness of decrypted data. However, this oracle is known for its playful deceit, as its pronouncements are not always truthful. Success demands more than just uncovering the secret; you must meticulously document each step of your binary pursuit, proving you've truly mastered its game of whispers and shadows.  
 Connect over TCP using netcat or a similar program to solve: `nc ctf.nzcsc.org.nz 40025`

*Unfortunately due to the nature of this challenge we are unable to archive it.*
Connecting to the server gives us the following task:
```
Welcome to the Oracle of Odds and Evens - The Deceptive Edition! (512-bit Variant)

The game has changed. The oracle is... temperamental. And we demand precision.

Public Modulus N: 5790334653455970971903620873436845793829158579895897066887269765695772559686113004662274698943115108890286490469235581376490897198019248877081523754458791
Public Exponent E: 65537
Ciphertext C (integer): 3774131772357215682697513098930388907740038637280361749113689599665002638364729930669248462231522898930869595442743730985378394146481866110093136625161785

Oracle Interaction:
- Send an integer (a ciphertext you want to test) on a new line.
- The oracle will decrypt it and return its parity:
  '0' if the decrypted plaintext is EVEN.
  '1' if the decrypted plaintext is ODD.
- WARNING: The oracle has a 10% chance of returning the INCORRECT parity.
  You may need to query strategically for important decisions.

Submission Protocol:
- You do NOT submit the final decrypted message value.
- Instead, you must submit the sequence of an *upper bound* for the plaintext
  at each of the 511 iterations of your binary search decryption.
- After the initial welcome, the server will prompt you for each bound sequentially.
- If your entire trace of 511 upper bounds matches our expected path, you win the flag.
(A generous query limit is in place, but repeated, identical queries for the same bound decision are expected.)
```
This is a challenge involving what is known as a parity oracle. I used an [article by ENOENT](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-3/) which was extremely helpful. I will summarise the basic logic but this article and the others are excellent for a deeper understanding of this attack and RSA in general.

RSA uses modular arithmetic to compute a ciphertext. The ciphertext $c$ is computed as the result of $m^e \text{ mod } n$, where $m$ is the plaintext, $e$ is a prime exponent, and $n$ is the modulus. We can send ciphertexts to the oracle and it will return whether the decrypted value is even or odd.
We must then determine the upper bound of a range of values that contain the plaintext.
Using even multiples of $m$ calculated via $c (2^e \text{ mod }n) \text{ mod } n$ we can determine whether $2m>n$, as if $2m>n$, because $2m$ is even and $n$ is odd, $2m \text{ mod } n$ will be odd. If $2m < n$, the modulus operation will not impact the value and $2m \text{ mod } n$ will be even. We can therefore create a range that shrinks for each iteration, and perform a binary search. As $\log_2(n) \approx 510.5$ we will need to perform 511 queries.

This oracle is unique in that it sometimes lies. We can get around this by simple probability. If the oracle tells the truth 90% of the time, and we want our script to get all 511 parity checks correct almost always. (it takes several minutes to run, so running it multiple times would be extra slow) Let's say we want 90% success rate. This means that $P(\text{correct parity})^{511} = 0.90$.
$P(\text{correct parity}) = \sqrt[511]{0.90} = 0.9998$
We can use the binomial distribution to model this with $p=0.9$. We must now test different numbers of trials, and find the probability that over half of them are correct.
Using odd numbers of trials is convenient as it allows for a clear majority in either odd or even parity.

| $n$ | $x$ | $P(x\ge n)$ |
| --- | --- | ----------- |
| 5   | 3   | 0.9914      |
| 7   | 4   | 0.9972      |
| 9   | 5   | 0.9991      |
| 11  | 6   | 0.9997      |
| 13  | 7   | 0.9999      |
Using 13 trials meets this level of accuracy. (although this is definitely higher than required)

We can now construct a script to calculate the bounds, such as the one in [[solve.py]].
This (after roughly 5 minutes) gives us the flag: `FLAG[FE927CB38D65A47E]`

![[11 - Oracle of Odds and Evens/flag.png]]