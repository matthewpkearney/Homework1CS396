# Matt Kearney - q3 program solution

# message data
messages = ["000d1a07263a376b111c3a07390b154606021a4c003c1043071704254c03091000",
            "0d0d19530674332a0b593b163101521f0a16541c1c210306160609384c0004151f",
            "151f0c002039356b0a172c53240c1f0345131508593a1643021d172a0519065953", 
            "0d0910533831703f0415225331071d13114300041c73040d060500331f570f1604",
            "1d48011c3f3170250a593a07250117081143170d1773170614164535041e125953",
            "000008076f233f3e091d6911354503130c17114c1c3e0702070004321f1e0f1e53",
            "181d0a182638296b2a2d195339165216001112091a27091a550100221e12155953",
            "03091a1d3b742423000b2c533145110711001c4c162145101a1f0035041e0f1e53",
            "190910112a74292e11590053340c16081143040d0073041701170b3505180f5953", 
            "030d4900273b252701593b1631091e1f450f110d0b3d4502171d10354c1e155953",
            "1a0901532b3b3e3f450d211a3e0e521100431a091c3745171a5245614c57415953"]

# find_hex -> return the hexidecimal value associated with 'word'
def find_hex(word):
    return "".join(hex(ord(char))[2:] for char in word)

# remove the x in the hex-rep
def remove_x(str, res):
    if str == "":
        return res
    if str[0] == 'x':
        return remove_x(str[1:], res)
    return remove_x(str[1:], res+ str[0] )

# XOR -> take xor of any two hex strings
def XOR(c, word):
    return hex(int(c, 16) ^ int(word, 16))[2:]

# remove -> remove the first number (unneeded padding)
def remove(word):
    return word[1:]


# To find the following strings, I used the online cribdrag resource:
# https://www.tausquared.net/pages/ctf/twotimepad
# Through cribdragging, it was found that the plaintexts of p1 and p2 were either str1 or str2


str1= "testing testing can you read this"
str2= "yep I can read you perfectly well"
p1_hex = find_hex(str1)
p2_hex = find_hex(str2)
#To understand how the above messages were revealed as P1, P2, we use cribdragging to guess words in the message XORS

c=messages
#Now that we have obtained p1, we take c1 xor'ed with all (ciphered) messages in the range c2-c11 
ciphs=[]
for i in range(1, len(c)):
    ciphs.append(remove_x(hex(int(messages[0], 16) ^ int(c[i], 16)), ""))

sized_ciphs=[]
for i in ciphs:
    if len(i)>66:
        sized_ciphs.append(remove(i))
    else: 
        sized_ciphs.append(i)

print(str1)
#to find words... 
# we will use the obtained p1 hexcode xor'd with all messages and then decode to ascii to find the messages
for i, ciph in zip(range(0,10), ciphs):
    print(bytearray.fromhex(XOR(ciph, p1_hex)).decode())
