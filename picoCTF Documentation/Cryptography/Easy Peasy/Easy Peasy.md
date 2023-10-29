#Junester Ursora II BSIT 4-A

#University of Cebu - Banilad

#https://play.picoctf.org/users/pythons_junkaze

1st. A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})

This Python script uses the 'pwn' library to exploit a service. The service encrypts a flag using a XOR pad of length 50000, which would be secure if not for a wrap-around vulnerability. 

By triggering a wrap-around, the known input is re-encrypted with the same XOR values. This lets us calculate the XOR key by comparing the known input with the encrypted output. 
With the XOR key, we can decrypt the encrypted flag. The script efficiently automates this process, sending data to trigger the wrap-around and recover the flag, making it vulnerable to attack.

To use the pwn library, install the following:

//pip install --upgrade pip

//pip install pwntools

2nd. Run the Easy Peasy.py, the MAX_CHUNK = 50000 enables an instant decrpytion of flag since it is the same values of the XOR pad.

//python3 Easy\ Peasy.py

[+] Opening connection to mercury.picoctf.net on port 11188: Done

[*] Flag: 551e6c4c5e55644b56566d1b5100153d4004026a4b52066b4a5556383d4b0007

[+] Causing wrap-around: Done

[+] The flag: b'7904ff830f1c5bba8f763707247ba3e1'
