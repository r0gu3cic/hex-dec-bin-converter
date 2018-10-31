# hex='f'
# print('This is hexadecimal: '+hex)
# dec=int(hex, base=16)
# print('This is decimal: '+str(dec))
# binary=bin(dec)[2:]
# print('This is binary: '+str(binary))

def hexToDec(hex):
    dec=int(hex, base=16)
    return dec

def binToDec(bin):
    dec=int(bin,base=2)
    return dec

def hexToBin(hex):
    binary=bin(int(hex, base=16))[2:]
    return binary

def decToBin(dec):
    binary=bin(int(dec))[2:]
    return binary

def decToHex(dec):
    hexa=hex(int(dec))[2:]
    return hexa

def binToHex(bin):
    dec=binToDec(bin)
    hexa=decToHex(dec)
    return hexa

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
        dec=binToDec(num)
        print('Your number converted to decimal: '+str(dec))
        hex=binToHex(num)
        print('Your number converted to hexadecimal: '+str(hex))
        break
    elif choice=='2':
        num=input('Input your decimal number: ')
        binary=decToBin(num)
        print('Your number converted to binary: '+str(binary))
        hex=decToHex(num)
        print('Your number converted to hexadecimal: '+str(hex))
        break
    elif choice=='3':
        num=input('Input your hexadecimal number: ')
        binary=hexToBin(num)
        print('Your number converted to binary: '+str(binary))
        dec=hexToDec(num)
        print('Your number converted to decimal: '+str(dec))
        break
