def find_string(s):

    if s.find("are") == -1:
        return False
    else:
        return True    

def startpy():

    str1 = "hey whats going on in your life"
    string = find_string(str1)
    print(string)   


if __name__ == '__main__':
    startpy()