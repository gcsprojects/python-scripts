import os
import string
import math

conversion = input("What do you want to convert to? ")

def ToFarenheight():
	GetTemp = int(input("Enter the temperature in Celcuis: "))
	temperature = (GetTemp *9/5)+32
	print ("%.1f" % temperature)

def ToCelcius():
	GetTemp = int(input("Enter the temperature in Farenheight: "))
	temperature = (GetTemp-32)*5/9
	print ("%.1f" % temperature)

if conversion == "Farenheight" or conversion == "F":
	ToFarenheight()
elif conversion == "celcius" or conversion == "C":
	ToCelcius()
