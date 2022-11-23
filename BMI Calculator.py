import time
import sys

print("Hi! Welcome to the BMI Calculator! This program was created by: ")
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

next_ans = input("Do not take this test if you have very developed muscles, if you are pregnant or if you are elderly! Do you want to continue? (Y/N) - ")

time.sleep(1)

# This block of code prompts the user to enter whether to use meters or feet and inches as length measurements,
# then asking for your height (if your height is given in feet and inches, it automatically converts to meters)

# Este bloco de código pede ao utilizador, se pretender avançar, que digite se utiliza kilogramas ou libras como medidas de peso
if next_ans in ("y","Y","yes","Yes","yES","yeS","YEs","yES","YES"):
    unit_w = str(input("In your country, do you use kilograms or pounds as a measure of weight? (Write kg for kilograms or lbs for pounds!) - "))
    time.sleep(1)
else: quit()

# This block of code prompts the user to enter their weight
# (if your weight is given in pounds, it automatically converts to kilograms)
if unit_w in ("lbs","Lbs","lBs","lbS","LBs","lBS","LBS"):
    weight_lbs = float(input("So what's your weight in pounds? (Example: 124.1 - Uses a period, not a comma!) - "))
    weight = float(weight_lbs * 0.45359237)

if unit_w in ("kg","Kg","kG","KG"):
    weight = float(input("So what's your weight in kilograms? (Example: 74.2 - Use a period, not a comma!) - "))
    time.sleep(1)

# This block of code asks the user whether to use meters or feet and inches as a measure of length
unit_h = str(input("And... In your country, do you use meters or feet and inches as a measure of length? (Write m for meters or f/i for feet and inches!) - "))

time.sleep(1)

# This block of code prompts the user to enter their height
# If it is in feet and inches, it automatically converts to meters
if unit_h in ("f/i","F/i","f/I","F/I","fi","Fi","fI","FI"):
    height_f = int(input("Hmmmm... Now tell me your height! (Only feet, we'll ask you about inches later!) (Example: If you are 6'5'', write 6, no decimals!) - " ))
    time.sleep(1)
    height_i = int(input("And now, as I said, tell me the inches! (Inches only!) (Example: If you measure 6'5'', write 5, without decimals!) - " ))
    height = (height_i * 0.0254) + (height_f * 0.3048)
    time.sleep(1)

if unit_h in ("m","M"):
    height = float(input("Hummm... Now tell me your height in meters! (Example: 1.66 - Uses a period, not a comma!) - "))

# This block of code evaluates the BMI and stores it in the bmi_r variable
bmi = float(weight / (height * height))

if bmi < 18.5:
    bmi_r = "Oops, looks like you're underweight! "
if bmi >= 18.5 and bmi < 24.9:
    bmi_r = "Perfect, you're a normal weight! "
if bmi >= 24.9 and bmi < 29.9:
    bmi_r = "Oops, it sounds like you're pre-obese, my advice is: try to lose some weight! "
if bmi >= 29.9 and bmi < 34.9:
    bmi_r = "Whoops, looks like you're Obese - Class I, my advice is: try to lose some weight! "
if bmi >= 34.9 and bmi < 39.9:
    bmi_r = "Whoops, looks like you're Obese - Class II, my advice is: try to lose some weight! "
if bmi >= 39.9:
    bmi_r = "Whoops, looks like you're Obese - Class III, my advice is: try to lose some weight! "
time.sleep(1)
            
print("---------------------------------------------------------------------------------------------------------------------")
            
print("I'll tell you now your BMI! Let me just think for a moment... ")
            
time.sleep(2)
            
print("Your BMI is " + str(bmi) + "! " + str(bmi_r) + " ")
            
time.sleep(2)
            
print("---------------------------------------------------------------------------------------------------------------------")
            
input("Did you like it? Thank you for using this program! Follow me on twitter: @tugauga ")
            
time.sleep(60)