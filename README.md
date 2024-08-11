# Hexor
A program to encode text into hex or decode hex to text by using One-Time-Pad

## One Time Pad
The One Time Pad is a symmetric cipher, i.e., there is a secret key shared between the two parties who are communicating, that was developed by Gilbert Vernam back in 1917. 
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
Simply put, for a given message we generate a random bit string as long as the message and then XOR it with the message to get the cipher text...


It seems quite simple but how do we know if it's secure?<br>
Before we ask that question, let us first ask 'How do we know if a particular encryption is secure?'<br>
Well, in 1949 Claude Shanon wrote in Communication Theory of Secrecy Systems, a very notable paper of his, about how a cipher can have perfect secrecy.<br>
This is what it states...<br>
<!-- <p> $\begin{quote} In physics, the mass-energy equivalence is stated by the equation E=mc^2, discovered in 1905 by Albert Einstein.\end{quote}$ </p> -->
 _A cipher (E,D) over (K,M,C) has perfect secrecy if ∀ m<sub>0</sub> , m<sub>1</sub> ∈ M (|m<sub>0</sub>| = |m<sub>1</sub>|) and ∀ c ∈ C, Pr[E(k,m<sub>0</sub>)=c] = Pr[E(k,m<sub>1</sub>)=c] where k is uniform in K_
<br>
i.e., given the cipher text alone, one cannot know what the message is...
<br>We can use this to prove that One Time Pad is secure in the following way,<br>
$\forall$ m,c: Pr<sub>k</sub>[E(k,m)=c] = $\frac{No.  of keys, k \in K, s.t. E(k,m)=c}{|K|}$ <br>
as Pr<sub>k</sub>[E(k,m)=c] is constant, therefore, No.  of keys, k $\in$ K, s.t. E(k,m)=c (N<sub>k</sub>), is also constant
<br> As, there is a single map between a key and the message, N<sub>k</sub>=1, this shows that One Time Pad is prefectly secure<br>
But, the major drawback of One Time Pad is that length of the key, as it is equal to message length...<br>
This is because, only the case where |K| $\geq$ |M|, can form a secure cipher...<br>
<br>
## About the program
You can download the zip file and extract the `.py` files from it.<br>
Then, run the `main.py` file.<br>
You can then encode or decode the the text as you would like...<br>
I've made the use of `os.urandom()` function in order to generate a random key<br>
Here are a few examples...<br>
```
Welcome to the Hex Encoder!
Enter E to Encode and D to Decode:e
Enter text that needs to be encoded: Hello World!
Encoded text: da52978bd767d5772fe6c8ba
Key:9237fbe7b84782185d8aac9b
```
```
Welcome to the Hex Encoder!
Enter E to Encode and D to Decode:e
Enter text that needs to be encoded: Hello World!
Encoded text: 26c7d0c5aa15166ddbf9baf
Key:6ea2bca9c53541027fd3ff8e
```
Even for the same word, we get different keys and hence different cipher texts...
<br>

