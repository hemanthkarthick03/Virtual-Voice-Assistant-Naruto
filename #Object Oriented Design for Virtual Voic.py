# Object Oriented Design for Virtual Voice Assistant - Naruto (Jan 2024)

import mysql.connector
import speech_recognition as sr
import pyttsx3
import datetime
import time
import subprocess
import wolframalpha
import requests
import json
import spotipy
import webbrowser
import platform
import random
import pygetwindow as gw
import PyDictionary as dic
import wikipedia
import screen_brightness_control as sbc
import cv2
import mediapipe as mp
from bs4 import BeautifulSoup
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np


class VirtualAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.newVoiceRate = 160
        self.engine.setProperty('rate', self.newVoiceRate)
        self.r = sr.Recognizer()
        self.client = wolframalpha.Client('R2K75H-7ELALHR35X')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def wish_me(self):
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good Morning Buddy"
        elif 12 <= hour < 15:
            greeting = "Good Afternoon Homie"
        elif 15 <= hour < 20:
            greeting = "Good Evening Homie"
        else:
            greeting = "Hello Homie"

        print("\n\t\t\t\t\t\tHello 👋 ", greeting, "\n")
        print("-------------------------------------------------------------------------------------")
        self.speak(f"Hello {greeting}")

    def take_command(self):
        with sr.Microphone() as source:
            print("\n🎤  🎙  Hearing  🎙  🎤\n")
            audio = self.r.listen(source)

            try:
                statement = self.r.recognize_google(audio, language='en-in')
                print(f"Hemanth Karthick 😎 ~ {statement}\n")

            except Exception:
                print(
                    "[# Microphone Error] ---  Sorry 😅 ! Say that again please !!!\n")
                print(
                    "-------------------------------------------------------------------------------------")
                self.speak("Pardon me, please say that again")
                return "None"
        return statement

    def run_virtual_assistant(self):
        print("-------------------------------------------------------------------------------------")
        self.speak("Loading your Virtual Assistant Uzumaki Narutho")
        self.wish_me()

        while True:
            sentence = random.choice(["How can I help you now, mate?",
                                      "Say what I can do for you?",
                                      "Do you want me to help you pick something?",
                                      "What can I do for you?", ""])
            self.speak(sentence)
            statement = self.take_command().lower()
            if statement == 0:
                continue

            if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement \
                    or "end" in statement or "mood" in statement or "tata" in statement:
                print(
                    'Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bye')
                print(
                    "-------------------------------------------------------------------------------------")
                self.speak(
                    'Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bai')
                break

            elif "wikipedia" in statement:
                self.speak('Searching in Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=2)
                self.speak("According to Wikipedia")
                print(
                    "------------------------------------------------------------------")
                print(results)
                print(
                    "-------------------------------------------------------------------------------------")
                self.speak(results)

            # Add other functionalities similarly

            time.sleep(3)


if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run_virtual_assistant()
