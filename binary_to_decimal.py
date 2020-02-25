def bin2dec(binary):
    binary1 = int(binary)
    i, decimal = 0, 0
    while (binary1 != 0):
        dec = binary1 % 10
        decimal =decimal + dec * ( 2 ** i)
        binary1 = binary1 // 10 # dzielenie bez reszty
        i = i+1
    return decimal