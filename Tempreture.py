#Write a Python program to convert temperatures to and from celsius, fahrenheit. 

#Formula : c/5 = f-32/9  - where c = temperature in celsius and f = temperature in fahrenheit ]

#Expected Output :

#60°C is 140 in Fahrenheit 

#45°F is 7 in Celsius

#Input temperature

temperature = input("Input temperature in (Use C to represent Celsius and F to represent Fahrenheit)")
degree = int(temperature[:-1])
convert = temperature[-1]


#convert to Fahrenheit

if convert.upper() == "C":

result = int(round((9 * degree) / 5 + 32))

convert = "Fahrenheit"

#convert to Celsius

elif convert.upper() == "F":

result = int(round((degree - 32) * 5 / 9))

convert = "Celsius"

#Error

else:

print("Use the Correct representations e.g 20F 0r 10C ")

quit()


#Output Results

print(temperature,"converted to", convert, "=", result, "degrees", convert)