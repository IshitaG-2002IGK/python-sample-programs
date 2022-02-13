'''
Created on 
Course work: 
@author: Ishita
Source:
     
     
'''

def weekday(x):
    if x == 1:
        day = "Monday"
    elif x == 2:
        day = "Tuesday"  
    elif x == 3:
        day = "Wednesday"
    elif x == 4:
        day = "Thursday"          
    elif x == 5:
        day = "Friday"
    elif x == 6:
        day = "Saturday"
    elif x == 7:
        day = "Sunday"
    else:
        day = "Incorrect day!"         
    return day   

def startpy():

    user_input = int(input("Enter a number for displaying the week"))
    week = weekday(user_input)
    print(week)   


if __name__ == '__main__':
    startpy()