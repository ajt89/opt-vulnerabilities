One of the messages is code, one of the messages is song lyrics, and one of the messages is a Shakespeare quotation. The other three are other memorable phrases.

General idea:
http://jarmoc.com/blog/2013/08/12/otp/

1) Use the readCipherFile() function to read in the cipher texts as int arrays
2) Use the xorCipherArr() function to xor the int arrays from step 1 with each other resulting in a int array
3) From step 2, we have determined ct1 and ct3 go together, ct2 and ct5 go together, and ct4 and ct6 go together
4) Use the xorWordIndex() function to xor a crib at every index of the int arrays from step 2
5) Repeat step 4 until enough plain text has been found for googling

ct1.hex and ct3.hex are encrypted with the same pad

    Shakespear quote (Macbeth):
    LADY MACBETH: I still have the smell of blood on my hand. All the perfumes of Arabia couldn't make my little hand smell better.

    General quote 1(Plato Quote):
    Plato: "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light."

ct2.hex and ct5.hex are encrypted with the same pad

    General quote 2(Avengers quote):
    Steve Rogers: [looks at Helicarrier] It seems to be powered by some sort of electricity!
    Tony Stark: ...well, you're not wrong.

    Code quote:
    /bin/bash

    env x='() { :;}; echo vulnerable' bash -c "echo this is a test"

    env X='() { (a)=>\' bash -c "echo date"; cat echo

ct4.hex and ct6.hex are encrypted with the same pad

    Song quote (Shake it Off):
    The players gonna play, play, play
    And the haters gonna hate, hate, hate
    Baby I'm just gonna shake, shake, shake
    I shake it off

    General quote 3(St. Crispin's Day Speech):
    We few, we happy few, we band of brothers
    For he to-day that sheds his blood with me
    Shall be my brother
    be he ne'er so vile
