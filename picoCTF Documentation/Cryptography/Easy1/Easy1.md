#Junester Ursora II BSIT 4-A

#University of Cebu - Banilad

#https://play.picoctf.org/users/pythons_junkaze

1st. The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this "table" to solve it?.

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
    
   +----------------------------------------------------
   
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A

C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D

F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E

G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F

H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G

I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H

J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I

K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J

L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K

M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L

N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M

O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N

P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O

Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P

R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q

S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R

T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S

U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T

V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U

W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V

X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W

Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X

Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

2nd. This is a Vigenère cipher (French pronunciation: [viʒnɛːʁ]), a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key. I will manually solved it, refer on the picture Easy1.png.

It can be solved by manual:

    -Finding the row of the corresponding the letter
    
    -In the row, find the column which contains the matching ciphertext letter
    
    -The matching plaintext letter is noted at the top of the column
    
Or in CyberChef under Vigenere Cipher Decode

    https://gchq.github.io/CyberChef/

The flag is: CRYPTOISFUN
