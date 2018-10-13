import p2

cipher_1_list = p2.read_cipher_file("../ciphertexts/ct1.hex")
cipher_2_list = p2.read_cipher_file("../ciphertexts/ct2.hex")
cipher_3_list = p2.read_cipher_file("../ciphertexts/ct3.hex")
cipher_4_list = p2.read_cipher_file("../ciphertexts/ct4.hex")
cipher_5_list = p2.read_cipher_file("../ciphertexts/ct5.hex")
cipher_6_list = p2.read_cipher_file("../ciphertexts/ct6.hex")

xor_13_list = p2.xor_cipher_lists(cipher_1_list, cipher_3_list)
xor_25_list = p2.xor_cipher_lists(cipher_2_list, cipher_5_list)
xor_46_list = p2.xor_cipher_lists(cipher_4_list, cipher_6_list)

p2.xor_word_index(xor_13_list, " the ")
p2.xor_word_index(xor_25_list, " the ")
p2.xor_word_index(xor_46_list, " the ")

p2.interpreter_xor(xor_13_list, " the ", 0)
p2.interpreter_xor(xor_25_list, " the ", 0)
p2.interpreter_xor(xor_46_list, " the ", 0)

p2.xor_word_index(xor_13_list, "LADY MACBETH: I still have the smell of blood on my hand. All the perfumes of Arabia couldn\'t make my little hand smell better.")
p2.xor_word_index(xor_13_list, "Plato: \"We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.\"")

p2.xor_word_index(xor_25_list, "Steve Rogers: [looks at Helicarrier] It seems to be powered by some sort of electricity!\nTony Stark: ...well, you\'re not wrong.")
p2.xor_word_index(xor_25_list, "/bin/bash\n\nenv x=\'() { :;}; echo vulnerable\' bash -c \"echo this is a test\"\n\nenv X=\'() { (a)=>\\\' bash -c \"echo date\"; cat echo\n\n")

p2.xor_word_index(xor_46_list, "The players gonna play, play, play \nAnd the haters gonna hate, hate, hate \nBaby I\'m just gonna shake, shake, shake \nI shake it off")
p2.xor_word_index(xor_46_list, "We few, we happy few, we band of brothers\nFor he to-day that sheds his blood with me\nShall be my brother\nbe he neer so vile, \n")
