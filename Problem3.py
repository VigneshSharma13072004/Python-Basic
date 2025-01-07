# Install an external module and use it to perform an operation of your interest 
import pyttsx3
engine = pyttsx3.init()
x = input("Enter any string you want to listen : ")
engine.say(x)
engine.runAndWait()
# here we go to terminal and using pip we install a python module