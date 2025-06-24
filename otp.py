# OTP Simulation
import random

otp = random.randint(1000,9999)
print(otp)

attempts = 3
while attempts:
    user_otp = int(input("Enter OTP: "))
    if len(str(user_otp))<4:
        print("OTP Must be 4 Digit Number Only")
    if otp == user_otp:
        print("Correct OTP")
        break
    attempts = attempts-1
else:
    print("Maximum attempts done, try after 24 Hours")    



    
