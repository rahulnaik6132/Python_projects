# text to speech Convertor
from gtts import gTTS
import os 

# Default texts
myText = "You can use your computer or Android tablet to chat with your friends     through Google Message…Important: Your Google Account is used to:"

# Type of languaue
language = "en"
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3") # Output File Name

# For System Sound Configuration
os.system("output.mp3")
