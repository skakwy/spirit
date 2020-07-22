# Python program to translate 
# speech to text and text to speech 
# pip install speechrecognition
# linux : sudo apt-get install python3-pyaudio
# pip install pyaudio
# pip install pyttsx3
import wikipedia
import speech_recognition as sr 
import pyttsx3
passch = 0 # check if passwort is on
e = 'Can you repeat that please ?'
test = ''
# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to 
# speech 
def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	
	
# Loop infinitely for user to 
# speak 
while(1):	 
	
	# Exception handling to handle 
	# exceptions at the runtime 
	try: 
		
		# use the microphone as source for input. 
		with sr.Microphone() as source2: 
			
			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2) 
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			#check what the user said you can basicly change this to everything you want. btw. you use google to regonize the voice 
			if r.recognize_google(audio2,) == 'hey spirit' :
                                #answer after check
				test = "yes"
				SpeakText(test)
		
			MyText = 'test' 
			 
			 
			
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		
	except sr.UnknownValueError: 
		print("I didn't understood you")
		error = e
		SpeakText(error) 
