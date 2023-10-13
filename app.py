# CONVERSION FUNCTIONS

def bin_to_dec(bin_str):
    #Convert a binary string to its decimal representation.
    return sum(int(bit) * (2 ** i) for i, bit in enumerate(reversed(bin_str)))


def dec_to_bin(dec_num):
    #Convert a decimal number to its binary string representation.
    binary = []
    while dec_num:
        binary.append(str(dec_num % 2))
        dec_num //= 2
    return ''.join(reversed(binary)).rjust(8, '0')


# MATH FUNCTIONS

def bin_add(bin_str_1, bin_str_2):
    #Add two binary numbers.
    max_len = max(len(bin_str_1), len(bin_str_2))
    carry, result = 0, []

    for b1, b2 in zip(bin_str_1.rjust(max_len, '0'), bin_str_2.rjust(max_len, '0')):
        total = carry + int(b1) + int(b2)
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.insert(0, '1')

    return ''.join(result)


def bin_sub(bin_str_1, bin_str_2):
    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_str_1 = bin_str_1.rjust(max_len, '0')
    bin_str_2 = bin_str_2.rjust(max_len, '0')

    if bin_str_1 < bin_str_2:
        return "Error: Negative result"

    borrow, result = 0, []
    for b1, b2 in zip(bin_str_1, bin_str_2):
        bit_sub = int(b1) - int(b2) - borrow
        if bit_sub < 0:
            borrow = 1
            result.append('1')
        else:
            borrow = 0
            result.append(str(bit_sub))

    return ''.join(result).lstrip('0') or '0'



def bin_mul(bin_str_1, bin_str_2):
    #Multiply two binary numbers.
    return ''.join([bin_add(bin_str_1 + '0' * i, '0' * len(bin_str_2)) for i, bit in enumerate(reversed(bin_str_2)) if bit == '1'])


def bin_div(bin_str_1, bin_str_2):
    if bin_str_2 == '0':
        return "Error: Division by Zero"

    result = ''
    remainder = '0'
    for bit in bin_str_1:
        remainder = remainder + bit  # append bit
        remainder = remainder.lstrip('0')  # remove leading zeros

        if remainder >= bin_str_2: 
            remainder = bin_sub(remainder, bin_str_2)  # subtract divisor
            result = result + '1'  # append 1 to quotient
        else:
            result = result + '0'  # append 0 to quotient

    return result.lstrip('0') or '0'


# MAIN MENU FUNCTION

def menu():
    ACTIONS = {
        'b': ("Binary Number (8-digits)", bin_to_dec),
        'd': ("Decimal Number (0-255)", lambda x: dec_to_bin(int(x))),
        'a': ("first binary number", "second binary number", bin_add),
        's': ("first binary number", "second binary number", bin_sub),
        'm': ("first binary number", "second binary number", bin_mul),
        'i': ("first binary number", "second binary number", bin_div),
    }

    while True:
        print("\n*** Binary Calculator ***\n" + "-" * 42)
        print("(B)inary to Decimal Conversion")
        print("(D)ecimal to Binary Conversion")
        print("(A)dd two Binary Numbers")
        print("(S)ubtract two Binary Numbers")
        print("(M)ultiply two Binary Numbers")
        print("D(i)vide two Binary Numbers")
        print("(Q)uit")

        choice = input(">> ").lower()

        if choice == 'q':
            print("\nGoodbye!")
            break
        elif choice in ACTIONS:
            inputs = [input(f"\nEnter {prompt} : ") for prompt in ACTIONS[choice][:-1]]
            print("=", ACTIONS[choice][-1](*inputs))
        else:
            print("\nInvalid choice!")

menu()
