import pyttsx3 #Importing the Library 

def voice_func(): #Function for your code
    voice=pyttsx3.init() #Initializing the library
    speech=input("Text:")  #Taking the input from the user
    voice.say(speech) #Passing the input to the library
    #If we want the function to just return a default voice, 
    #we can just skip speech and 
    #pass the default voice text into the 
    #voice.say function 
    #SO whenever the function is called, a voice is generated
    return voice.runAndWait() #Running the function and waiting for the output

voice_func()