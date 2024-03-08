#this program converts from any numbering system to another

while True:   #to repeat the program all over again

# function to display the numbering system menu1
    def numbering_system_menu1():
        print("** Numbering System Converter **")
        print()
        print("A) Insert a new number ")
        print("B) Exit program ")
        result1 =input("Please enter your choice (A/B): ").upper()

        if result1 == "A":
            pass
        elif result1 == "B":
            exit("Exiting program. ")
        else:
            print("** Please select a valid choice **")
            numbering_system_menu1()


    numbering_system_menu1()

    def get_number():
        global number
        number = input("please insert a number: ").upper()
        print()
        return number
    number = get_number()


#function to display the numbering system menu2
    def numbering_system_menu2():
        print()
        print("** Please select the base you want to convert from **")
        print()
        print("A) Decimal")
        print("B) Binary")
        print("C) octal")
        print("D) hexadecimal")
        result2 = input("Please enter your choice (A/B/C/D): ").upper()

        if result2 == "A" or result2 == "B" or result2 == "C" or result2 == "D":
            pass
        else:
            print("** Please select a valid choice **")
            numbering_system_menu2()

        valid_string = '0123456789ABCDEF'

#check if number is decimal
        if result2 == "A":
            true = 0
            false = 0
            for digit in number:
                if digit in valid_string[:10]:
                    true += 1
                else:
                    false += 1
            if true != len(number):
                print("Error: ",number," is not a valid number in base 10. Please enter a valid number. ")
                numbering_system_menu1()
                get_number()
                numbering_system_menu2()
            if true == len(number):
                pass

#check if number is binary
        if result2 == "B":
            true = 0
            false = 0
            for digit in number:
                if digit in valid_string[:2]:
                    true += 1
                else:
                    false += 1
            if true != len(number):
                print("Error: ",number," is not a valid number in base 2. Please enter a valid number. ")
                numbering_system_menu1()
                get_number()
                numbering_system_menu2()
            if true == len(number):
                pass

#check if number is octal
        if result2 == "C":
            true = 0
            false = 0
            for digit in number:
                if digit in valid_string[:8]:
                    true += 1
                else:
                    false += 1
            if true != len(number):
                print("Error: ",number," is not a valid number in base 8. Please enter a valid number. ")
                numbering_system_menu1()
                get_number()
                numbering_system_menu2()
            if true == len(number):
                pass

#check if number is hexadecimal
        if result2 == "D":
            true = 0
            false = 0
            for digit in number:
                if digit in valid_string[:16]:
                    true += 1
                else:
                    false += 1
            if true != len(number):
                print("Error: ",number," is not a valid number in base 16. Please enter a valid number. ")
                numbering_system_menu1()
                get_number()
                numbering_system_menu2()
            if true == len(number):
                pass

        return result2
    result2 = numbering_system_menu2()

#function to display the numbering system menu3
    def numbering_system_menu3():
        print()
        print("** Please select the base you want to convert a number to **")
        print()
        print("A) Decimal")
        print("B) Binary")
        print("C) octal")
        print("D) hexadecimal")
        result3 = input("Please enter your choice (A/B/C/D): ").upper()

        if result3 == "A" or result3 == "B" or result3 == "C" or result3 == "D":
            pass
        else:
            print("** Please select a valid choice **")
            numbering_system_menu3()

        return result3
    result3 = numbering_system_menu3()


#function to convert from decimal to binary
    def decimal_to_binary(num):
        x = int(num)
        if x > 1:
            decimal_to_binary(x//2)
        print(x % 2,end = '')

#function to convert decimal to octal
    def decimal_to_octal(num):
        x = int(num)
        if x > 1:
            decimal_to_octal(x//8)
        print(x % 8,end = '')

#function to convert decimal to hexadecimal
    def decimal_to_hexadecimal(num):
        x = int(num)
        if x > 1:
            decimal_to_hexadecimal(x//16)
        if x % 16 == 10:
            print("A",end = '')

        if x % 16 == 11:
            print("B",end = '')

        if x % 16 == 12:
            print("C",end = '')

        if x % 16 == 13:
            print("D",end = '')

        if x % 16 == 14:
            print("E",end = '')

        if x % 16 == 15:
            print("F",end = '')

        if x % 16 < 10:
            print(x % 16,end='')

#function to convert binary to decimal
    def binary_to_decimal(num):
        s = 0
        power = len(num) - 1
        i = 0

        for digit in num:
            s = s + int(num[i])*(2**power)
            i += 1
            power -= 1
        print(s)

#function to convert binary to octal in two steps
    def binary_to_octal(num):
#step1: convert binary to decimal

        s = 0
        power = len(num) - 1
        i = 0

        for digit in num:
            s = s + int(num[i])*(2**power)
            i += 1
            power -= 1

#step2: convert decimal to octal
        def decimal_to_octal(num):
            if num > 1:
                decimal_to_octal(num//8)
            print(num % 8,end = '')

        decimal_to_octal(s)

#funcion to convert binary to hexadecimal in two steps
    def binary_to_hexadecimal(num):
#step1: convert binary to decimal
        s = 0
        power = len(num) - 1
        i = 0

        for digit in num:
            s = s + int(num[i])*(2**power)
            i += 1
            power -= 1

#step2: convert decimal to hexadecimal
        def decimal_to_hexadecimal(num):
            x = int(num)
            if x > 1:
                decimal_to_hexadecimal(x//16)
            if x % 16 == 10:

                print("A",end = '')
            if x % 16 == 11:

                print("B",end = '')
            if x % 16 == 12:

                print("C",end = '')
            if x % 16 == 13:

                print("D",end = '')
            if x % 16 == 14:

                print("E",end = '')
            if x % 16 == 15:

                print("F",end = '')
            if x % 16 < 10:
                print(x % 16,end='')
        decimal_to_hexadecimal(s)

#function to convert octal to binary in two steps
    def octal_to_binary(num):
#step1: convert from octal to decimal
        s = 0
        power = len(num) - 1
        i = 0
        for digit in num:
            s = s + int(num[i])*(8**power)
            i += 1
            power -= 1

#step2: convert from decimal to binary
        def decimal_to_binary(num):
            x = int(num)
            if x > 1:
                decimal_to_binary(x//2)
            print(x % 2,end = '')

        decimal_to_binary(s)

#function to convert octal to decimal
    def octal_to_decimal(num):
        s = 0
        power = len(num) - 1
        i = 0

        for digit in num:
            s = s + int(num[i])*(8**power)
            i += 1
            power -= 1
        print(s)

#function to convert octal to hexadecimal in two steps
    def octal_to_hexadecimal(num):
#step1: convert octal to decimal
        s = 0
        power = len(num) - 1
        i = 0

        for digit in num:
            s = s + int(num[i])*(8**power)
            i += 1
            power -= 1

#step2: convert decimal to hexadecimal
        def decimal_to_hexadecimal(num):
            x = int(num)
            if x > 1:
                decimal_to_hexadecimal(x//16)
            if x % 16 == 10:
                print("A",end = '')

            if x % 16 == 11:
                print("B",end = '')

            if x % 16 == 12:
                print("C",end = '')

            if x % 16 == 13:
                print("D",end = '')

            if x % 16 == 14:
                print("E",end = '')

            if x % 16 == 15:
                print("F",end = '')

            if x % 16 < 10:
                print(x % 16,end='')

        decimal_to_hexadecimal(s)

#function to convert hexadecimal to binary in two steps
    def hexadecimal_to_binary(num):
#step1: conver from hexadecimal to decimal
        hex_char = "0123456789ABCDEF"
        decimal = 0
        for digit in num:
            decimal = decimal * 16 + hex_char.index(digit)

#step2: convert from decimal to binary

        def decimal_to_binary(num):
            x = int(num)
            if x > 1:
                decimal_to_binary(x//2)
            print(x % 2,end = '')

        decimal_to_binary(decimal)

#function to convert hexadecimal to decimal
    def hexadecimal_to_decimal(num):
        hex_char = "0123456789ABCDEF"
        decimal = 0
        for digit in num:
            decimal = decimal * 16 + hex_char.index(digit)
        print(decimal)

#function to convert hexadecimal to octal in two steps
    def hexadecimal_to_octal(num):

#step1: convert hexadecimal to decimal
        hex_char = "0123456789ABCDEF"
        decimal = 0
        for digit in num:
            decimal = decimal * 16 + hex_char.index(digit)

#step2: convert decimal to octal
        def decimal_to_octal(num):
            x = int(num)
            if x > 1:
                decimal_to_octal(x//8)
            print(x % 8,end = '')

        decimal_to_octal(decimal)

#recall decimal_to_binary function to convert from decimal to binary
    if result2 == "A" and result3 == "B":
        print("Result: ",end="")
        decimal_to_binary(number)
        print()
#recall decimal_to_octal function to convert from decimal to octal
    if result2 == "A" and result3 == "C":
        print("Result: ",end="")
        decimal_to_octal(number)
        print()
#recall decimal_to_hexadecimal function to convert from decimal to hexadecimal
    if result2 == "A" and result3 == "D":
        print("Result: ",end="")
        decimal_to_hexadecimal(number)
        print()
#recall binary_to_decimal function to convert from binary to decimal
    if result2 == "B" and result3 == "A":
        print("Result: ",end="")
        binary_to_decimal(number)
        print()
#recall binary_to_octal function to convert from binary to octal
    if result2 == "B" and result3 == "C":
        print("Result: ",end="")
        binary_to_octal(number)
        print()
#recall binary_to_hexadecimal function to convert from binary to hexadecimal
    if result2 == "B" and result3 == "D":
        print("Result: ",end="")
        binary_to_hexadecimal(number)
        print()
#recall octal_to_decimal function to convert from octal to decimal
    if result2 == "C" and result3 == "A":
        print("Result: ",end="")
        octal_to_decimal(number)
        print()
#recall octal_to_binary function to convert from octal to binary
    if result2 == "C" and result3 == "B":
        print("Result: ",end="")
        octal_to_binary(number)
        print()
#recall octal_to_hexadecimal function to convert from octal to hexadecimal
    if result2 == "C" and result3 == "D":
        print("Result: ",end="")
        octal_to_hexadecimal(number)
        print()
#recall hexadecimal_to_decimal function to convert from hexadecimal to decimal
    if result2 == "D" and result3 == "A":
        print("Result: ",end="")
        hexadecimal_to_decimal(number)
        print()
#recall hexadecimal_to_binary function to convert from hexadecimal to binary
    if result2 == "D" and result3 == "B":
        print("Result: ",end="")
        hexadecimal_to_binary(number)
        print()
#recall hexadecimal_to_octal function to convert from hexadecimal to octal
    if result2 == "D" and result3 == "C":
        print("Result: ",end="")
        hexadecimal_to_octal(number)
        print()
