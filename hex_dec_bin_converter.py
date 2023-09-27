#!/usr/bin/env python3

def hex_to_dec(hex):
    dec=int(hex, base=16)
    return dec

def bin_to_dec(bin):
    dec=int(bin,base=2)
    return dec

def hex_to_bin(hex):
    binary=bin(int(hex, base=16))[2:]
    return binary

def dec_to_bin(dec):
    binary=bin(int(dec))[2:]
    return binary

def dec_to_hex(dec):
    hex_result=hex(int(dec))[2:]
    return hex_result

def bin_to_hex(bin):
    dec=bin_to_dec(bin)
    hex_result=dec_to_hex(dec)
    return hex_result

###MAIN###
print('''This is simple numerical system converter used to convert hexadecimal,
decimal or binary number to hexadecimal, decimal or binary number''')
while True:
    choice=input('''What number type you need to convert?
1-Binary
2-Decimal
3-Hexadecimal
Choice: ''')
    if choice not in ['1','2','3']:
        continue
    elif choice=='1':
        num=input('Input your binary number: ')
        dec=bin_to_dec(num)
        print('Your number converted to decimal: '+str(dec))
        hex=bin_to_hex(num)
        print('Your number converted to hexadecimal: '+str(hex))
        break
    elif choice=='2':
        num=input('Input your decimal number: ')
        binary=dec_to_bin(num)
        print('Your number converted to binary: '+str(binary))
        hex=dec_to_hex(num)
        print('Your number converted to hexadecimal: '+str(hex))
        break
    elif choice=='3':
        num=input('Input your hexadecimal number: ')
        binary=hex_to_bin(num)
        print('Your number converted to binary: '+str(binary))
        dec=hex_to_dec(num)
        print('Your number converted to decimal: '+str(dec))
        break
