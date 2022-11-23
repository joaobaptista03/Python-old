import time

print("Hi! Welcome to the BMR Calculator! This program was created by: ")
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
input("The Basal Metabolic Rate is the amount of energy the body needs per day, being completely still. To find out the daily calorie need, you need to add the rest of the calories spent throughout the day to the Basal Metabolic Rate. (ENTER to Continue) ")
print("---------------------------------------------------------------------------------------------------------------------")

# Lines 26, 30 and 34 ask the user to enter their gender, age and whether pounds or kilograms are used as a weight measure.

time.sleep(1)

gender = input("Are you biologically male (M) or female (F) ? - ")
        
time.sleep(1)
        
age = float(input("How old are you? (If you want to know your exact age (23.88147783418265), you can find out in the Exact Age Calculator!) - "))
        
time.sleep(1)
        
unit_w = str(input("In your country, do you use kilograms or pounds as a measure of weight? (Write kg for kilograms or lbs for pounds!) - "))
        
time.sleep(1)

# This block of code prompts the user to enter their weight
# If it is in pounds, it automatically converts to kilograms
if unit_w in ("lbs","Lbs","lBs","lbS","LBs","lBS","LBS"):
    weight_lbs = float(input("So what's your weight in pounds? (Example: 124.1 - Use a period, not a comma!) - "))
    weight = float(weight_lbs * 0.45359237)

if unit_w in ("kg","Kg","kG","KG"):
    weight = float(input("So what's your weight in kilograms? (Example: 55.9 - Use a period, not a comma!) - "))
        
time.sleep(1)
        
# This line of code asks the user whether to use meters or feet and inches as a measure of length
unit_h = str(input("And... In your country, do you use meters or feet and inches as a measure of length? (Write m for meters or f/i for feet and inches!) - "))
        
time.sleep(1)
        
# This block of code prompts the user to enter their height
# If it is in feet and inches, it automatically converts to meters
if unit_h in ("f/i","F/i","f/I","F/I","fi","Fi","fI","FI"):
    height_f = int(input("Hmmmm... Now tell me your height! (Only feet, we'll ask you about inches later!) (Example: If you measure 6'5'', write 6, no decimals!) - " ))
    time.sleep(1)
    height_i = int(input("And now, as I said, tell me the inches! (Only the inches!) (Example: If you measure 6'5'', write 5, without decimals!) - " ))
    height = float(((height_i * 0.0254) + (height_f * 0.3048))*100)
        
if unit_h in ("m","M"):
    height = float(input("Hummm... Now tell me your height in meters! (Example: 166) - "))


# Este bloco de código calcula o BMR
if gender in ("man","Man","MAN","Male","male","MALE","m","M"):
    bmr = (13.397*weight + 4.799*height - 5.677*age + 88.362)
        
if gender in ("f","F","female","Female","FEMALE","girl","Girl","GIRL"):
    bmr = (9.247*weight + 3.098*height - 4.33*age + 447.593)
        
time.sleep(1)
        
print("---------------------------------------------------------------------------------------------------------------------")
        
print("Hmmmm... let me think...")
        
time.sleep(2)
        
print("Your Basal Metabolic Rate is " + str(bmr) + " !")
        
time.sleep(2)
    
print("---------------------------------------------------------------------------------------------------------------------")
        
input("Did you like it? Thanks for using this program! follow me on twitter: @tugauga ")
        
time.sleep(60)