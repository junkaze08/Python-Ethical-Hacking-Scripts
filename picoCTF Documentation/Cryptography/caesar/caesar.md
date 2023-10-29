#Junester Ursora II BSIT 4-A
#University of Cebu - Banilad
#https://play.picoctf.org/users/pythons_junkaze

1st Decrypt this message. there is a downloaded file without file extension. ciphertext
In windows, rename the file from ciphertext to cipher.txt

The output inside the txt file is: picoCTF{gvswwmrkxlivyfmgsrhnrisegl}

We already know that it is the flag but it is encrypted.

2nd Using this decoder online https://www.dcode.fr/caesar-cipher I am able to decode the caesar cipher but also noticing the Shifts
Caesar Cipher in context is a substitution cipher that shifts letters in a message to make it unreadable if intercepted.
So I've noticed on the 4th shift a recognizable string and that is the flag!

picoCTF{crossingtherubicondjneoach}