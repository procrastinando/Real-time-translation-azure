import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
SPEECH_REGION = 'japaneast'

source_lang = "en-US"
target_language="es"

speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
speech_translation_config.speech_recognition_language=source_lang
speech_translation_config.add_target_language(target_language)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

while True:
    result = translation_recognizer.recognize_once_async().get()
    print(result.translations[target_language])
