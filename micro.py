import speech_recognition as sr

microphone = sr.Microphone()
recognizer = sr.Recognizer()

def get_text():
    with microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print('Listening...')
            audio = recognizer.listen(microphone, 0, 3)
            print('Started recognition...')
            return recognizer.recognize_google(audio, language='ru').lower()

        except sr.WaitTimeoutError: print('Check your microphone');
        except sr.UnknownValueError: print('ValueError')
        except sr.RequestError: print('Check your internet connection')
        return ''

while True:
    print(get_text())

'''
import asyncio
import sounddevice as sd
import numpy as np

async def main():
    def callback(indata, outdata, frames, time, status):
        print ("|" * int(np.linalg.norm(indata)*10))
#        print(indata)

    with sd.Stream(callback=callback):
        await asyncio.Event().wait()

asyncio.run(main())
'''
