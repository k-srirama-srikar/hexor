# Hexor
A program to encode text into hex or decode hex to text by using One-Time-Pad

## One Time Pad
The One Time Pad is a symmetric cipher, i.e., there is a secret key shared between the two parties who are communicating, was developed by Gilbert Vernam back in 1917. 
<br>Although the idea is seemingly quite simple, it is quite secure and the proof of same is written below...
<br><p>c := E(k,m) = k $\oplus$ m</p>
<p> D(k,c) = k $\oplus$ c </p>
