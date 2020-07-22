# Python program to translate 
# speech to text and text to speech 

#if that don't work try this : pip install pipwin 
#                              pipwin install pyaudio

import speech_recognition as sr 
import pyttsx3 
e = 'Can you please repeat that ?'
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
			
			# Using ggogle to recognize audio 
			MyText = r.recognize_google(audio2, language="en-EN") 
			MyText = MyText.lower() 

			print("Did you say "+MyText) 
			SpeakText(MyText) 
			
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		
	except sr.UnknownValueError: 
		print("I didn't understood you")
		error = e
		SpeakText(error)
