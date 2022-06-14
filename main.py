import module1 # User Defined Module
import os
text_file = open("Output.txt", "w")
text_file.write(module1.greetings("Puneet"))
text_file.close()
