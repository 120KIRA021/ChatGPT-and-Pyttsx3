import openai
import pyttsx3
from tok import GTP#импорт переменной с ключом

class GPT:
    def __init__(self):
        openai.api_key = GTP
        self.__messages = []

    def request(self, task):
        self.__messages.append({'role': 'user', 'content': task})
        print("Отправлено...")
        answer = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages=self.__messages
        )
        self.__messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content


if __name__ == '__main__':
    assist = GPT()
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty("voice", "ru")
    tts.setProperty('rate', 150)
    for voice in voices:
        if voice.name == "Victoria":#Конкретный голос
            tts.setProperty("voice", voice.id)

    while True:
        data = input('>>>')
        response = assist.request(data)
        print(f'GPT answer: {response}')
        tts.say(response)
        tts.runAndWait()
