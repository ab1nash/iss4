import random
PLAIN_TEXT_LEN = 8


def valid_binary_str(key):  # USED
    for i in key:
        if i not in {"0", "1"}:
            return 0
    return 1


def simencrypt(plaintext, key):  # USED all tests are done beforehand so no condition check
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += str(int(plaintext[i]) ^ int(key[i]))
    return ciphertext


def simdecrypt(ciphertext, key):  # USED all tests are done beforehand so no condition check
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += str(int(ciphertext[i]) ^ int(key[i]))
    return plaintext


def Vernam_RandSequence(l):  # USED
    ret = ""
    for _ in range(l):
        ret += str(random.randint(0, 1))
    return ret


def makeEqualProbability(seq):
    eq_seq = ""
    for i in seq:
        if i == "0":
            eq_seq += "01"
        else:
            eq_seq += "10"
    return eq_seq


def simulation_key_gen(plaintext, ciphertext):
    keylen = max(len(plaintext), len(ciphertext))
    key = equalProbabilitySequence(keylen)
    return key


def equalProbabilitySequence(length):
    randomSeq = Vernam_RandSequence(length)
    equalProbSeq = makeEqualProbability(randomSeq)
    return equalProbSeq[:length]


def resize_key(key):
    key = (key * (PLAIN_TEXT_LEN//len(key) + 4))[:PLAIN_TEXT_LEN]
    return key


def encrypt(plaintext, key, encryption_technique):
    key = resize_key(key)
    cipher_text = ""
    for i in range(PLAIN_TEXT_LEN):
        if(encryption_technique[i] == "0"):
            cipher_text += str(int(plaintext[i]) ^ int(key[i]))
        else:
            cipher_text += str(int(plaintext[i]) & int(key[i]))
    return cipher_text


def check_key(key):  # WAIT I"LL USE THIS
    if (key == ""):
        print("Enter a new key with p=0.5")
        return 0
    zero = 0
    one = 0
    for i in key:
        if (i == "0"):
            zero += 1
        elif (i == "1"):
            one += 1
        else:
            print("Invalid key. The entered key should be binary.")
    if(zero == one):
        print("Correct key! You may now proceed.")
    else:
        print("Invalid key. p should be 0.5")


def next_binary_num(binary_num):
    index = 0
    length = len(binary_num)
    # replace the first "0" with "1"
    if (index < length) and (binary_num[index] == "0"):
        binary_num = "1" + binary_num[1:]
        return binary_num
    # toggle all 1's
    while (index < length) and (binary_num[index] == "1"):
        temp_binary_num = ""
        if (index > 0):
            temp_binary_num += binary_num[:index]
        temp_binary_num += "0"
        if (index+1 < length):
            temp_binary_num += binary_num[index+1:]
        binary_num = temp_binary_num
        index += 1
    # toggle next 0
    if (index < length):
        temp_binary_num = ""
        temp_binary_num += binary_num[:index] + "1"
        if (index+1 < length):
            temp_binary_num += binary_num[index+1:]
        binary_num = temp_binary_num
    return binary_num


def generate_all_pairs(key, encryption_technique):
    key = resize_key(key)
    all_tuples = ""
    binary_num = "00000000"
    possible_plain_text = 2**PLAIN_TEXT_LEN
    for _ in range(possible_plain_text):
        binary_num = next_binary_num(binary_num)
        crypted_text = encrypt(binary_num, key, encryption_technique)
        all_tuples += (binary_num + " , " + crypted_text + "\n")
    return all_tuples


def checkAnswer(yesno, m1, m2, key, encryption_technique):
    if (yesno == 'yes'):
        return "This is not correct, Please try again!"
    key = resize_key(key)
    c1 = encrypt(m1, key, encryption_technique)
    c2 = encrypt(m2, key, encryption_technique)
    if(c1 == c2):
        return "This is correct!!"
    else:
        return "This is not correct, Please try again!"
