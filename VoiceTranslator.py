import googletrans
import speech_recognition
import gtts
import pygame  # Import pygame instead of playsound

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Speak Now")

    recognizer.adjust_for_ambient_noise(source)
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="en")
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text, dest="hi")
print(translation.text)

converted_audio = gtts.gTTS(translation.text, lang="hi")
converted_audio.save("hello.mp3")

# Use pygame to play the audio
pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.mixer.quit()
