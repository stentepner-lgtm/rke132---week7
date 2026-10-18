import datetime
from hello import say_hello

hour = datetime.datetime.now().hour
name = input("What is your name?")


say_hello(hour, name)



