#Junester Ursora II BSIT 4-A

#University of Cebu - Banilad

#https://play.picoctf.org/users/pythons_junkaze

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: Addadshashanammu.zip.

1st. Extract the zip file, using unzip in Kali in order to not manually extracting one-by-one.

$ unzip Addadshashanammu.zip

2nd. Change the directory to the innermost folder where the file fang-of-haynekhtnamet is located.

$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku

3rd. The file command shows the file is a 64-bit Linux ELF executable. Running "./fang-of-haynekhtnamet" in the terminal executes it to get the flag

$ file fang-of-haynekhtnamet 

fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=47e898db922f38cb54ab4a08fb4e3def5a1cb6a1, not stripped

$ ./fang-of-haynekhtnamet                    
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_a00cae70}