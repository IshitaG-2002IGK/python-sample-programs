
def eliminate_spaces(my_string):

    eliminate_spaces = my_string.strip()

    
    return eliminate_spaces 
    
def startpy():

    str1 = "\n        i love pizza and pasta"
    my_string_1= eliminate_spaces(str1)   
    print(my_string_1)

if __name__ == '__main__':
    startpy()