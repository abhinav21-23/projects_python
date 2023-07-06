import pyttsx3
if __name__=='__main__':
    print("Welcome to RoboSpeaker created by Abhinav")
    pyttsx3.speak("Welcome to RoboSpeaker created by Abhinav")
    while True:
        print("Enter what you want me to speak: ", end="")
        pyttsx3.speak("Enter what you want me to speak: ")
        x = input()
        if x=='q':
            pyttsx3.speak("bye bye friend, meet you next time")
            break
        else:
            pyttsx3.speak(x)
        
