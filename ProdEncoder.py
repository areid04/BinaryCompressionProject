# ENCODER FILE DOCUMENTATION:
# Dear Reader,
# The encoder is a fair bit lengthier than the decoder, with plenty of nested if conditionals that may apear messy at first,
# but with a macro view of the program makes complete sense!
# The code works by checking whether or not a sequence of characters is in our pre-existing "word bank"
# (see compression table for full list.)
# This is checked by first recognizing if x is a space. We then check if the next character is t, a, i, w (etc) or a letter that
# our words could potentially start with. If a match, it checks the next, and so forth. If the word bank exists it store the space and the word.
# we check for specific of sequences of chracters rather than single characters first because logically,
# if we check for "s" in the string "shush", the code would store the "s" character and not check for "sh".
# There are several print debug statements we use to check incase a loop occurs for easy debugging.
import time
def Code(fn: str) -> str:
    org_file = open(fn)
    original_str = org_file.read()
    new_string = ""
    d = 0
    x = 0 # we need to use a while loop
    q = 0 # acts as an answer to the "did we search for words yet?" and determines if our word search sequence is used.
    start_time = time.time()
    while x < len(original_str):
        print("top of loop")
        print(new_string)
        #time.sleep(0.5)
        if original_str[x] == " " and x+1 < len(original_str) and q == 0: # word after or space?
            print("1")
            if original_str[x+1] == 't' and x+2 < len(original_str): # t word
                print("1.a")
                if original_str[x+2] == 'o' and x+3 <= len(original_str):
                    print("1.a.a")
                    new_string = new_string + "11011101" # store " to "
                    d = d + 8
                    x = x + 3
                    print("to")
                    continue
                elif original_str[x+2] == 'h' and x+3 < len(original_str):
                    print("1.b")
                    if original_str[x+3] == 'e' and x+4 <= len(original_str):
                        print("1.b.a")
                        new_string = new_string + "10111111" # store " the "
                        d = d + 8
                        x = x + 4
                        continue
                    elif original_str[x+3] == 'a' and original_str[x+4] == 't' and x+5 <= len(original_str):
                        print("1.b.b")
                        new_string = new_string + "11101110" # store " that "
                        d = d + 8
                        x = x + 5

                        continue
                    elif original_str[x+3] == 'i' and original_str[x+4] == 's' and x + 5 <= len(original_str):
                        print("1.b.c")
                        new_string = new_string + "11111010" # store " this "
                        d = d + 8
                        x = x + 5
                        continue
                q = 1
                continue
            elif original_str[x+1] == 'a': # a word
                print("1.b")
                if x+2 <= len(original_str) and original_str[x+2] != 'n':
                    new_string = new_string + "11101100" # store " a "
                    d = d + 8
                    x = x + 2

                    continue
                elif original_str[x+2] == 'n':
                    if original_str[x+3] == 'd' and x+ 4 <= len(original_str):
                        new_string = new_string + "11011010" # store " and "
                        d = d + 8
                        x = x + 4

                        continue
                elif original_str[x+2] == 'r':
                    if original_str[x+3] == 'e' and x+4 <= len(original_str):
                        new_string = new_string + "11111011" # store " are "
                        d = d + 8
                        x = x + 4

                        continue
                elif original_str[x+2] == 's':
                    if x+3 <= len(original_str):
                        new_string = new_string + "11110001" # store " as "
                        d = d + 8
                        x = x + 3

                        continue
                elif original_str[x+2] == 't':
                    if x+3 <= len(original_str):
                        new_string = new_string + "11110001" # store " at "
                        d = d + 8
                        x = x + 3

                        continue
                q = 1
                continue
            elif original_str[x + 1] == 'o' and x+2 < len(original_str): # o words
                print("1.c")
                if original_str[x+2] == 'f' and x+3 <= len(original_str):
                    new_string = new_string + "11001010" # store " of "
                    d = d + 8
                    x = x + 3

                    continue
                elif original_str[x+2] == 'n' and x+3 <= len(original_str):
                    new_string = new_string + "11110110" # store " on "
                    d = d + 8
                    x = x + 3

                    continue
                elif original_str[x+2] == 'r' and x+3 <= len(original_str):
                    new_string = new_string + "11111100" # store " or "
                    d = d + 8
                    x = x + 3

                    continue
                q = 1
                continue
            elif original_str[x+1] == 'I' and x+2 <= len(original_str):
                new_string = new_string + "11111001" # store I
                d = d + 8
                x = x + 2
                continue
            elif original_str[x + 1] == 'i': #i words
                if original_str[x+2] == 'n' and x+3 <= len(original_str):
                    new_string = new_string + "11100111" # store " in "
                    d = d + 8
                    x = x + 3
                    q = 1
                    continue
                elif original_str[x+2] == 't' and x +3 <= len(original_str):
                    new_string = new_string + "11110000" # store " it "
                    d = d + 8
                    x = x + 3
                    continue
                elif original_str[x+2] == 's' and x + 3 <= len(original_str):
                    new_string = new_string + "11101101" # store " is "
                    d = d + 8
                    x = x + 3
                    continue
                q = 1
                continue
            elif original_str[x + 1] == 'f' and x+2 < len(original_str):  # f words
                print("f")
                if x + 3 < len(original_str):
                    if original_str[x+2] == 'o' and original_str[x+3] == 'r' and x +4 <= len(original_str):
                        new_string = new_string + "11101111" # store " for "
                        d = d + 8
                        x = x + 4
                        continue
                elif x + 4 < len(original_str):
                    if original_str[x+2] == 'r' and original_str[x+3] == 'o' and original_str[x+4] == 'm' and x + 5 <= len(original_str):
                        new_string = new_string + "11111110" # store " from "
                        d = d + 8
                        x = x + 5
                        continue
                else:
                    q = 1
                    continue
                q = 1
                continue
            elif original_str[x + 1] == 'w' and x+2 < len(original_str): # w words
                if original_str[x+2] == 'a' and original_str[x+3] == 's' and x+4 < len(original_str):
                    new_string = new_string + "11110010" # store " was "
                    d = d + 8
                    x = x + 4
                    continue
                elif original_str[x+2] == 'i' and original_str[x+3] == 't' and original_str[x+4] == 'h' and x+5 < len(original_str):
                    new_string = new_string + "11110011" # store " with "
                    d = d + 8
                    x = x + 5
                    continue
                q = 1
                continue
            elif original_str[x+1] == 'b' and x+2 < len(original_str): # b words
                print("1.e")
                if original_str[x+2] == 'e' and x+3 < len(original_str):
                    new_string = new_string + "11110100" # store " be "
                    d = d + 8
                    x = x + 3
                    continue
                elif original_str[x+2] == 'y' and x+3 <= len(original_str):
                    new_string = new_string + "11110101" # store " by "
                    d = d + 8
                    x = x + 3
                    continue
                else:
                    print("2.e")
                    q = 1
                    continue
                q = 1
                continue
            elif x + 4 <= len(original_str) and original_str[x+1] == 'n' and original_str[x+2] == 'o' and original_str[x+3] == 't' and x + 4 <= len(original_str): # words starting with n
                print("1.d")
                if original_str[x+2] == 'o' and original_str[x+3] == 't' and x + 4 <= len(original_str):
                    new_string = new_string + "11110111" # store " not "
                    d = d + 8
                    x = x + 4
                    continue
                else:
                    q = 1
                    continue
                continue
            elif original_str[x + 1] == 'h' and x+2 < len(original_str):  # h words
                if original_str[x+2] == 'i' and x+3 < len(original_str):
                    if original_str[x+3] == 's' and x + 4 <= len(original_str):
                        new_string = new_string + "11111101" # store " his "
                        d = d + 8
                        x = x + 4
                        continue
                elif original_str[x+2] == 'e' and x+3 <= len(original_str):
                    new_string = new_string + "11111000" # store " he "
                    d = d + 8
                    x = x + 3
                    continue
                q = 1
                continue
            else:
                new_string = new_string + "00000"
                d = d + 5
                x = x + 1
                print("space")
                continue
            q = 1
        elif original_str[x] == " ":
            new_string = new_string + "00000"
            d = d + 5
            x = x + 1
            print("space")
            q = 0
            continue
        elif original_str[x] == "A":
            new_string = new_string + "10001100"
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "t" and x+1 < len(original_str):
            if original_str[x+1] == "h" :
                new_string = new_string + "10111010" #th
                d = d + 8
                x = x + 2
                print(x)
                print("th")
                q = 0
                continue
            if original_str[x+1] == "i" :
                new_string = new_string + "11000101" #ti
                d = d + 8
                x = x + 2
                print(x)
                print("ti")
                q = 0
                continue
            if original_str[x+1] == "o" :
                new_string = new_string + "11001100" #to
                d = d + 8
                x = x + 2
                print(x)
                print("to")
                q = 0
                continue
            else:
                new_string = new_string + "00010" #t
                d = d + 5
                x = x + 1
                print(x)
                print("t")
                q = 0
                continue
        elif original_str[x] == "t":
            new_string = new_string + "00010"  # t
            d = d + 5
            x = x + 1
            print(x)
            print("t")
            q = 0
            continue
        elif original_str[x] == "h" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "10111011" #he
                d = d + 8
                x = x + 2
                print(x)
                print("he")
                q = 0
                continue
            if original_str[x+1] == "a" :
                new_string = new_string + "11010000" #ha
                d = d + 8
                x = x + 2
                print(x)
                print("ha")
                q = 0
                continue
            if original_str[x+1] == "i" :
                new_string = new_string + "11011001" #hi
                d = d + 8
                x = x + 2
                print(x)
                print("hi")
                q = 0
                continue
            else:
                new_string = new_string + "01001" #h
                d = d + 5
                x = x + 1
                print(x)
                print("h")
                q = 0
                continue
        elif original_str[x] == "h":
            new_string = new_string + "01001"  # h
            d = d + 5
            x = x + 1
            print(x)
            print("h")
            q = 0
            continue
        elif original_str[x] == "i" and x+1 < len(original_str):
            if original_str[x+1] == "n" :
                new_string = new_string + "10111100" #in
                d = d + 8
                x = x + 2
                print(x)
                print("in")
                q = 0
                continue
            if original_str[x+1] == "t" :
                new_string = new_string + "11000111" #it
                d = d + 8
                x = x + 2
                print(x)
                print("it")
                q = 0
                continue
            if original_str[x+1] == "o" :
                new_string = new_string + "11010011" #io
                d = d + 8
                x = x + 2
                print(x)
                print("io")
                q = 0
                continue
            if original_str[x+1] == "c" :
                new_string = new_string + "11011110" #ic
                d = d + 8
                x = x + 2
                print(x)
                print("ic")
                q = 0
                continue
            else:
                new_string = new_string + "00101" #i
                d = d + 5
                x = x + 1
                print(x)
                print("i")
                q = 0
                continue
        elif original_str[x] == "i":
            new_string = new_string + "00101"  # i
            d = d + 5
            x = x + 1
            print(x)
            print("i")
            q = 0
            continue
        elif original_str[x] == "e" and x+1 < len(original_str):
            if original_str[x+1] == "r" :
                new_string = new_string + "10111101" #er
                d = d + 8
                x = x + 2
                print(x)
                print("er")
                q = 0
                continue
            if original_str[x+1] == "n" :
                new_string = new_string + "11000011" #en
                d = d + 8
                x = x + 2
                print(x)
                print("en")
                q = 0
                continue
            if original_str[x+1] == "s" :
                new_string = new_string + "11000110" #es
                d = d + 8
                x = x + 2
                print(x)
                print("es")
                q = 0
                continue
            if original_str[x+1] == "a" :
                new_string = new_string + "11100000" #ea
                d = d + 8
                x = x + 2
                print(x)
                print("ea")
                q = 0
                continue
            else:
                new_string = new_string + "00001" #e
                d = d + 5
                x = x + 1
                print(x)
                print("e")
                q = 0
                continue
        elif original_str[x] == "e":
            new_string = new_string + "00001"  # e
            d = d + 5
            x = x + 1
            print(x)
            print("e")
            q = 0
            continue
        elif original_str[x] == "a" and x+1 < len(original_str):
            if original_str[x+1] == "n" :
                new_string = new_string + "10111110" #an
                d = d + 8
                x = x + 2
                print(x)
                print("an")
                q = 0
                continue
            if original_str[x+1] == "t" :
                new_string = new_string + "11000010" #at
                d = d + 8
                x = x + 2
                print(x)
                print("at")
                q = 0
                continue
            if original_str[x+1] == "l" :
                new_string = new_string + "11001000" #al
                d = d + 8
                x = x + 2
                print(x)
                print("al")
                q = 0
                continue
            if original_str[x+1] == "r" :
                new_string = new_string + "11001001" #ar
                d = d + 8
                x = x + 2
                print(x)
                print("ar")
                q = 0
                continue
            if original_str[x+1] == "s" :
                new_string = new_string + "11010001" #as
                d = d + 8
                x = x + 2
                print(x)
                print("as")
                q = 0
                continue
            else:
                new_string = new_string + "00011" #a
                d = d + 5
                x = x + 1
                print(x)
                print("a")
                q = 0
                continue
        elif original_str[x] == "a":
            new_string = new_string + "00011"  # a
            d = d + 5
            x = x + 1
            print(x)
            print("a")
            q = 0
            continue
        elif original_str[x] == "r" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11000000" #re
                d = d + 8
                x = x + 2
                print(x)
                print("re")
                q = 0
                continue
            if original_str[x+1] == "i" :
                new_string = new_string + "11011011" #ri
                d = d + 8
                x = x + 2
                print(x)
                print("ri")
                q = 0
                continue
            if original_str[x+1] == "o" :
                new_string = new_string + "11011100" #ro
                d = d + 8
                x = x + 2
                print(x)
                print("ro")
                q = 0
                continue
            if original_str[x+1] == "a" :
                new_string = new_string + "11100001" # ra
                d = d + 8
                x = x + 2
                print(x)
                print("ra")
                q = 0
                continue
            else:
                new_string = new_string + "01000" #r
                d = d + 5
                x = x + 1
                print(x)
                print("r")
                q = 0
                continue
        elif original_str[x] == "r":
            new_string = new_string + "01000"  # r
            d = d + 5
            x = x + 1
            print(x)
            print("r")
            q = 0
            continue
        elif original_str[x] == "o" and x+1 < len(original_str):
            if original_str[x+1] == "n" :
                new_string = new_string + "11000001" #on
                d = d + 8
                x = x + 2
                print(x)
                print("on")
                q = 0
                continue
            if original_str[x+1] == "u" :
                new_string = new_string + "11010010" #ou
                d = d + 8
                x = x + 2
                print(x)
                print("ou")
                q = 0
                continue
            if original_str[x+1] == "m" :
                new_string = new_string + "11101010" #om
                d = d + 8
                x = x + 2
                print(x)
                print("om")
                q = 0
                continue
            else:
                new_string = new_string + "00100" #o
                d = d + 5
                x = x + 1
                print(x)
                print("o")
                q = 0
                continue
        elif original_str[x] == "o":
            new_string = new_string + "00100"  # o
            d = d + 5
            x = x + 1
            print(x)
            print("o")
            q = 0
            continue
        elif original_str[x] == "n" and x+1 < len(original_str):
            if original_str[x+1] == "d" :
                new_string = new_string + "11000100" #nd
                d = d + 8
                x = x + 2
                print(x)
                print("nd")
                q = 0
                continue
            elif original_str[x+1] == "t":
                new_string = new_string + "11001101" #nt
                d = d + 8
                x = x + 2
                print(x)
                print("nt")
                q = 0
                continue
            elif original_str[x+1] == "g":
                new_string = new_string + "11001110" #ng
                d = d + 8
                x = x + 2
                print(x)
                print("ng")
                q = 0
                continue
            elif original_str[x+1] == "e":
                new_string = new_string + "11011111" #ne
                d = d + 8
                x = x + 2
                print(x)
                print("ne")
                q = 0
                continue
            else:
                new_string = new_string + "00110" #n
                d = d + 5
                x = x + 1
                print(x)
                print("n")
                q = 0
                continue
        elif original_str[x] == "n":
            new_string = new_string + "00110"  # e
            d = d + 5
            x = x + 1
            print(x)
            print("n")
            q = 0
            continue
        elif original_str[x] == "s" and x+1 < len(original_str):
            if original_str[x+1] == "t" :
                new_string = new_string + "11001011" #st
                d = d + 8
                x = x + 2
                print(x)
                print("st")
                q = 0
                continue
            elif original_str[x+1] == "e" :
                new_string = new_string + "11001111" #se
                d = d + 8
                x = x + 2
                print(x)
                print("se")
                q = 0
                continue
            elif original_str[x+1] == "i" :
                new_string = new_string + "11101001" #si
                d = d + 8
                x = x + 2
                print(x)
                print("si")
                q = 0
                continue
            else:
                new_string = new_string + "00111" #s
                d = d + 5
                x = x + 1
                print(x)
                print("s")
                q = 0
                continue
        elif original_str[x] == "s":
            new_string = new_string + "00111"  # s
            d = d + 5
            x = x + 1
            print(x)
            print("s")
            q = 0
            continue
        elif original_str[x] == "l" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11010100" #le
                d = d + 8
                x = x + 2
                print(x)
                print("le")
                q = 0
                continue
            elif original_str[x+1] == "i" :
                new_string = new_string + "11100011" #li
                d = d + 8
                x = x + 2
                print(x)
                print("li")
                q = 0
                continue
            elif original_str[x+1] == "l" :
                new_string = new_string + "11100101" #ll
                d = d + 8
                x = x + 2
                print(x)
                print("ll")
                q = 0
                continue
            else:
                new_string = new_string + "01011" #l
                d = d + 5
                x = x + 1
                print(x)
                print("l")
                q = 0
                continue
        elif original_str[x] == "l":
            new_string = new_string + "01011"  # l
            d = d + 5
            x = x + 1
            print(x)
            print("l")
            q = 0
            continue
        elif original_str[x] == "v" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11010101" #ve
                d = d + 8
                x = x + 2
                print(x)
                print("ve")
                q = 0
                continue
            else:
                new_string = new_string + "10000110" #v
                d = d + 8
                x = x + 1
                print(x)
                print("v")
                q = 0
                continue
        elif original_str[x] == "v":
            new_string = new_string + "10000110"  # v
            d = d + 8
            x = x + 1
            print(x)
            print("v")
            q = 0
            continue
        elif original_str[x] == "c" and x+1 < len(original_str):
            if original_str[x+1] == "o" :
                new_string = new_string + "11010110" #co
                d = d + 8
                x = x + 2
                print(x)
                print("co")
                q = 0
                continue
            elif original_str[x+1] == "e" :
                new_string = new_string + "11100010" #ce
                d = d + 8
                x = x + 2
                print(x)
                print("ce")
                q = 0
                continue
            elif original_str[x+1] == "h" :
                new_string = new_string + "11100100" #ch
                d = d + 8
                x = x + 2
                print(x)
                print("ch")
                q = 0
                continue
            else:
                new_string = new_string + "01100" #c
                d = d + 5
                x = x + 1
                print(x)
                print("c")
                q = 0
                continue
        elif original_str[x] == "c":
            new_string = new_string + "01100"  # c
            d = d + 5
            x = x + 1
            print(x)
            print("c")
            q = 0
            continue
        elif original_str[x] == "m" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11010111" #me
                d = d + 8
                x = x + 2
                print(x)
                print("me")
                q = 0
                continue
            elif original_str[x+1] == "a" :
                new_string = new_string + "11101000" #ma
                d = d + 8
                x = x + 2
                print(x)
                print("ma")
                q = 0
                continue
            else:
                new_string = new_string + "01110" #m
                d = d + 5
                x = x + 1
                print(x)
                print("m")
                q = 0
                continue
        elif original_str[x] == "m":
            new_string = new_string + "01110"  # v
            d = d + 5
            x = x + 1
            print(x)
            print("m")
            q = 0
            continue
        elif original_str[x] == "d" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11011000" #de
                d = d + 8
                x = x + 2
                print(x)
                print("de")
                q = 0
                continue
            else:
                new_string = new_string + "01010" #d
                d = d + 5
                x = x + 1
                print(x)
                print("d")
                q = 0
                continue
        elif original_str[x] == "d":
            new_string = new_string + "01010"  # d
            d = d + 5
            x = x + 1
            print(x)
            print("d")
            q = 0
            continue
        elif original_str[x] == "b" and x+1 < len(original_str):
            if original_str[x+1] == "e" :
                new_string = new_string + "11100110" #be
                d = d + 8
                x = x + 2
                print(x)
                print("be")
                q = 0
                continue
            else:
                new_string = new_string + "10000101" #b
                d = d + 8
                x = x + 1
                print(x)
                print("b")
                q = 0
                continue
        elif original_str[x] == "b":
            new_string = new_string + "10000101"  # b
            d = d + 8
            x = x + 1
            print(x)
            print("b")
            q = 0
            continue
        elif original_str[x] == "u" and x+1 < len(original_str):
            if original_str[x+1] == "r" :
                new_string = new_string + "11101011" #ur
                d = d + 8
                x = x + 2
                print(x)
                print("ur")
                q = 0
                continue
            else:
                new_string = new_string + "01101" #u
                d = d + 5
                x = x + 1
                print(x)
                print("u")
                q = 0
                continue
        elif original_str[x] == "u":
            new_string = new_string + "01101"  # b
            d = d + 5
            x = x + 1
            print(x)
            print("u")
            q = 0
            continue
        elif original_str[x] == "w":
            new_string = new_string + "01111" # w
            d = d + 5
            x = x + 1
            print("w")
            q = 0
            continue
        elif original_str[x] == "f":
            new_string = new_string + "10000000" # f
            d = d + 8
            x = x + 1
            print("f")
            q = 0
            continue
        elif original_str[x] == "y":
            new_string = new_string + "10000001" # y
            d = d + 8
            x = x + 1
            print("y")
            q = 0
            continue
        elif original_str[x] == "*":
            new_string = new_string + "10000010" # ph
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "g":
            new_string = new_string + "10000011" # g
            d = d + 8
            x = x + 1
            print("g")
            q = 0
            continue
        elif original_str[x] == "p": #
            new_string = new_string + "10000100" # p
            d = d + 8
            x = x + 1
            print("p")
            q = 0
            continue
        elif original_str[x] == "k":
            new_string = new_string + "10000111" # k
            d = d + 8
            x = x + 1
            print("k")
            q = 0
            continue
        elif original_str[x] == "x":
            new_string = new_string + "10001000" # k
            d = d + 8
            x = x + 1
            print("x")
            q = 0
            continue
        elif original_str[x] == "q":
            new_string = new_string + "10001001" # q
            d = d + 8
            x = x + 1
            print("q")
            q = 0
            continue
        elif original_str[x] == "j":
            new_string = new_string + "10001010" # j
            d = d + 8
            x = x + 1
            print("j")
            q = 0
            continue
        elif original_str[x] == "z":
            new_string = new_string + "10001011" # z
            d = d + 8
            x = x + 1
            print("z")
            q = 0
            continue
        elif original_str[x] == "B":
            new_string = new_string + "10001101" # B
            d = d + 8
            x = x + 1
            print("b")
            q = 0
            continue
        elif original_str[x] == "C":
            new_string = new_string + "10001110" # c
            d = d + 8
            x = x + 1
            print("c")
            q = 0
            continue
        elif original_str[x] == "D":
            new_string = new_string + "10001111" # D
            d = d + 8
            x = x + 1
            print("d")
            q = 0
            continue
        elif original_str[x] == "E":
            new_string = new_string + "10010000" # E
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "F":
            new_string = new_string + "10010001" # F
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "G":
            new_string = new_string + "10010010" # G
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "H":
            new_string = new_string + "10010011" # H
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "I":
            new_string = new_string + "10010100" # I
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "J":
            new_string = new_string + "10010101" # J
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "K":
            new_string = new_string + "10010110" # K
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "L":
            new_string = new_string + "10010111" # L
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "M":
            new_string = new_string + "10011000" # M
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "N":
            new_string = new_string + "10011001" # N
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "O":
            new_string = new_string + "10011010" # O
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "P":
            new_string = new_string + "10011011" # P
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "Q":
            new_string = new_string + "10011100" # Q
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "R":
            new_string = new_string + "10011101" # R
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "S":
            new_string = new_string + "10011110" # S
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "T":
            new_string = new_string + "10011111" # T
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "U":
            new_string = new_string + "10100000" # U
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "V":
            new_string = new_string + "10100001" # V
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "W":
            new_string = new_string + "10100010" # W
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "X":
            new_string = new_string + "10100011" # X
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "Y":
            new_string = new_string + "10100100" # Y
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "Z":
            new_string = new_string + "10100101" # Z
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "0":
            new_string = new_string + "10100110" # 0
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "1":
            new_string = new_string + "10100111" # 1
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "2":
            new_string = new_string + "10101000" # 2
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "3":
            new_string = new_string + "10101001" # 3
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "4":
            new_string = new_string + "10101010" # 4
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "5":
            new_string = new_string + "10101011" # 5
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "6":
            new_string = new_string + "10101100" # 6
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "7":
            new_string = new_string + "10101101" # 7
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "8":
            new_string = new_string + "10101110" # 8
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "9":
            new_string = new_string + "10101111" # 9
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == ".":
            new_string = new_string + "10110000" # .
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == ",":
            new_string = new_string + "10110001" # ,
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "-":
            new_string = new_string + "10110010" # -
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "!":
            new_string = new_string + "10110011" # !
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "'":
            new_string = new_string + "10110100" # '
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == '"':
            new_string = new_string + "10110101" # -
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == "\n":
            new_string = new_string + "10110110" # -
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == ':':
            new_string = new_string + "10110111" # :
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == ';':
            new_string = new_string + "10111000" # ;
            d = d + 8
            x = x + 1
            q = 0
            continue
        elif original_str[x] == '?':
            new_string = new_string + "10111001" # ?
            d = d + 8
            x = x + 1
            q = 0
            continue
        x = x + 1
    out = open('BinOutput.txt', 'w+')
    output = str(d) + "." + new_string
    out.write(output)
    print("--- %s seconds ---" % (time.time() - start_time))
    return str(d) + "." + new_string
