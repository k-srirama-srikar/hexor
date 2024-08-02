# Hexor
A program to encode text into hex or decode hex to text by using One-Time-Pad

## One Time Pad
The One Time Pad is a symmetric cipher, i.e., there is a secret key shared between the two parties who are communicating, was developed by Gilbert Vernam back in 1917. 
<br>Although the idea is seemingly quite simple, it is quite secure and the proof of same is written below...
<br><p> _c := E(k,m) = k_ $\oplus$ _m_ <br>  _D(k,c) = k_ $\oplus$ _c_ </p>
where,<br>
D - Decryption Algorithm<br>
E - Encryption algorithm<br>
c - Cipher Text<br>
m - Message<br>
k - Key<br>
<p>And,<br> c $\subseteq$ C, m $\subseteq$ M, k $\subseteq$ K
<br>Where,<br>  M = C = K = $\{0,1\}^n$ </p>
Simply put, for a given message we generate a random bit string as long as the message and then XOR it with the message to get the cipher text...<br>
It seems quite simple but how do we know if it's secure?<br>
Before we ask that question, let us first ask 'How do we know if a particular encryption is secure?'<br>
Well, in 1949 Claude Shanon wrote in Communication Theory of Secrecy Systems, a very notable paper of his, about how a cipher can have perfect secrecy.<br>
This is what it states...<br>
<!-- <p> $\begin{quote} In physics, the mass-energy equivalence is stated by the equation E=mc^2, discovered in 1905 by Albert Einstein.\end{quote}$ </p> -->
 
 _A cipher (E,D) over (K,M,C) has perfect secrecy if ∀ m<sub>0</sub>, m<sub>1</sub> ∈ M ( |m<sub>0</sub>| = |m<sub>1</sub>| ) and ∀ c ∈ C, Pr[ E(k,m<sub>0</sub>)=c ] = Pr[ E(k,m<sub>1</sub>)=c ] where k is uniform in K_
