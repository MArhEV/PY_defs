def palnidrome(string):
    stringlength=len(string)
    slicedString=string[stringlength::-1]
    if slicedString == string:
        return True
    else:
        return False