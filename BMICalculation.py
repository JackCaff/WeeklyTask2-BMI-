# Program will allow user to enter height in (CM) and weight in (KG) and calculate their BMI.

Weight = float(input("Enter your Weight in Kg: "))  #Allows user to enter Weight
Height = float(input("Enter your Height in Cm: "))  #Allows user to enter Height

Meters_squared = ((Height * Height) / 100) #Converts height entered in CM to Metered squared

BMI = (Weight / Meters_squared) * 100

new_BMI = round(BMI, 2) #Rounds BMI value too 2 decimals places

print("Your BMI is", new_BMI,) #Displays the users BMI 
