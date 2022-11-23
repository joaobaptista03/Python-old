import datetime
import time

print("---------------------------------------------------------------------------------------------------------------------")

print("Hi! Welcome to Exact Age Calculator! This program was created by: ")
print("")
print("                                                           |--------------------------------------------------------|")
print("                                                           |                                                        |")
print("                                                           |    -------               ---------     |---------      |")
print("                                                           |       |      |       |   |             |        |      |")
print("                                                           |       |      |       |   |             |        |      |")
print("                                                           |       |      |       |   |     ----|   |--------|      |")
print("                                                           |       |      |       |   |         |   |        |      |")
print("                                                           |       |      ---------   -----------   |        |      |")
print("                                                           |                                                        |")
print("                                                           |  © TUGA 2020                                @tugauga   |")
print("                                                           |--------------------------------------------------------|")
print("")
time.sleep(2)
print("---------------------------------------------------------------------------------------------------------------------")
print("Well, let's go!")

time.sleep(1)

# This block of code asks the user to enter their date and time of birth
year_born = int(input("In what year were you born? (Ex.: 2003): "))
month_born = int(input("Nice, now tell me the month! (Ex.: 11): "))
day_born = int(input("Hum.. And in what day? (Ex.: 24): "))
hour_born = int(input("Almost there... hour? (Write just the hour - in a 24h format) (Ex.: 15): "))
min_born = int(input("And finally, in what minute? (Ex.: 43): "))        

# This block of code puts the date of birth in a "birthday" variable, it also calculates the user's age in that year
# and the age he is (already with time) in an "age" variable
birthday = datetime.datetime(year_born,month_born,day_born,hour_born,min_born)
turn_age = str(int(datetime.datetime.now().year) - int(year_born))
age = str(datetime.datetime.now() - birthday).replace(",", " and")

# This line of code calculates the user's age in decimal
year_age = str(float(age[0:age.index("d")-1]) / 365.25 + (int(age[14:age.index(":")]) / 8766) + (int(age[age.index(":")+1:age.index(":")+3]) / 210384) + (int(age[age.index(":")+4:age.index(":")+6]) / 12623040) + (int(age[age.index(":")+7:age.index(":")+13]) / 12623040000000))
        
print("---------------------------------------------------------------------------------------------------------------------")
        
time.sleep(1)

# The rest of the code is to print the results
print("Hum....")
        
time.sleep(1)
     
input("So this is your date of birth, right? - " + str(birthday) + " - (ENTER to confirm) - ")
      
time.sleep(1)
        
input("And... you'll be " + turn_age + " this year, right? - (ENTER to confirm) - ")
        
print("---------------------------------------------------------------------------------------------------------------------")
        
time.sleep(1)
        
print("Humm...")
        
time.sleep(1)
        
print("You are " + year_age + " years old!")
        
time.sleep(2)
        
print("Now I will tell you how many days you are exactly! Let me just think a little...")
        
time.sleep(3)
       
print("You are alive for exactly " + age + " hours!")
       
time.sleep(3)
        
print("---------------------------------------------------------------------------------------------------------------------")
        
input("Did you like it? Thanks for using this program! follow me on twitter: @tugauga ")
        
time.sleep(60)