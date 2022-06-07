#!/usr/bin/python3

#welcome text
print("Welcome to BMI calculator ver 1.0")

#take user details
height = input("Please put in your height in meters: ")
body_weight = input("Pleas put in your weight in kilos: ")

#calculate bmi with formula weight/height ** 2

bmi = int(body_weight) / float(height) ** 2
print(f"Your Body Mass Index is: {round(bmi, 2)}")
