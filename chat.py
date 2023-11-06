import random
import json
import threading
import pyautogui
import requests
import sys
import torch
import webbrowser
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from googlesearch import search

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "PEGASUS"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag == "questions":
                    return random.choice(intent['responses'])
                elif tag == "questions1":
                    return random.choice(intent['responses'])
                elif tag == "questions2":
                    return random.choice(intent['responses'])
                elif tag == "questions3":
                    return random.choice(intent['responses'])
                elif tag == "questions4":
                    return random.choice(intent['responses'])
                elif tag == "questions5":
                    return random.choice(intent['responses'])
                elif tag == "questions6":
                    return random.choice(intent['responses'])
                elif tag == "questions7":
                    return random.choice(intent['responses'])
                elif tag == "questions8":
                    return random.choice(intent['responses'])
                elif tag == "questions9":
                    return random.choice(intent['responses'])
                elif tag == "questions10":
                    return random.choice(intent['responses'])
                elif tag == "questions11":
                    return random.choice(intent['responses'])
                elif tag == "questions12":
                    return random.choice(intent['responses'])
                elif tag == "questions13":
                    return random.choice(intent['responses'])
                elif tag == "greeting2":
                    return random.choice(intent['responses'])
                elif tag == "questions15":
                    return random.choice(intent['responses'])
                elif tag == "questions16":
                    return random.choice(intent['responses'])
                elif tag == "questions17":
                    return random.choice(intent['responses'])
                elif tag == "depression":
                    return random.choice(intent['responses'])
                elif tag == "questions14":
                    def shree(sentence):
                        li = sentence
                        sen=""
                        url = "www.google.com"
                        a = ["search","song","hear","play","i","want","to","this"]
                        for i in li :
                            if i not in a :
                                sen+=i
                        for j in search(sen,tld="co.in",num=2,stop=1,pause=1):
                            w=webbrowser.open_new(j)

                    t9 = threading.Timer(1.0, shree(sentence))
                    t9.start()
                    return random.choice(intent['responses'])


                elif tag == "happy":
                    spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD"

                    def dev():
                        w = webbrowser.open_new(spotify_link)


                    t = threading.Timer(10.0, dev)
                    t.start()


                    def devi():
                        num_clicks = 1
                        delay = 1.0

                        x_coord = 335
                        y_coord = 23

                        for i in range(num_clicks):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x_coord, y_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(delay)

                    t = threading.Timer(11.0, devi)
                    t.start()

                    def debu():
                        x1_coord = 535
                        y2_coord = 600
                        for i in range(1):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x1_coord, y2_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(0.0)

                    t1 = threading.Timer(19.0, debu)
                    t1.start()
                    return random.choice(intent['responses'])
                elif tag == "sad":
                    spotify_link = "https://open.spotify.com/track/4BiPsAV070dg3eLSVf727A?si=e1aa89a7c000473d"

                    def dev():
                        w = webbrowser.open_new(spotify_link)


                    t = threading.Timer(10.0, dev)
                    t.start()


                    def devi():
                        num_clicks = 1
                        delay = 1.0


                        x_coord = 335
                        y_coord = 23

                        for i in range(num_clicks):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x_coord, y_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(delay)
                    t = threading.Timer(11.0, devi)
                    t.start()
                    def debu() :
                        x1_coord = 535
                        y2_coord = 630
                        for i in range(1):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x1_coord, y2_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(0.0)

                    t1 = threading.Timer(18.0, debu)
                    t1.start()
                    return random.choice(intent['responses'])
                elif tag == "greeting" :
                    return random.choice(intent['responses'])
                elif tag == "questions" :
                    return random.choice(intent['responses'])
                elif tag == "brokeup":
                    spotify_link = "https://open.spotify.com/playlist/5JQZqEJlkEhLeqdPi2wHkG?si=083a8ac7ad024f2f"

                    def dev():
                        w = webbrowser.open_new(spotify_link)


                    t = threading.Timer(10.0, dev)
                    t.start()


                    def devi():
                        num_clicks = 1
                        delay = 1.0


                        x_coord = 335
                        y_coord = 23

                        for i in range(num_clicks):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x_coord, y_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(delay)
                    t = threading.Timer(11.0, devi)
                    t.start()
                    def debu() :
                        x1_coord = 535
                        y2_coord = 600
                        for i in range(1):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x1_coord, y2_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(0.0)

                    t1 = threading.Timer(18.0, debu)
                    t1.start()
                    return random.choice(intent['responses'])
                elif tag == "motivation":
                    spotify_link = "https://open.spotify.com/playlist/3CNcHUp9CmM5EjEoZZlgr3"

                    def dev():
                        w = webbrowser.open_new(spotify_link)

                    t = threading.Timer(10.0, dev)
                    t.start()


                    def devi():
                        num_clicks = 1
                        delay = 1.0


                        x_coord = 335
                        y_coord = 23

                        for i in range(num_clicks):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x_coord, y_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(delay)
                    t = threading.Timer(11.0, devi)
                    t.start()
                    def debu() :
                        x1_coord = 535
                        y2_coord = 600
                        for i in range(1):
                            # pyautogui.FAILSAFE(False)
                            pyautogui.click(x1_coord, y2_coord)
                            # pyautogui.sleep(delay
                            pyautogui.sleep(0.0)

                    t1 = threading.Timer(18.0, debu)
                    t1.start()
                    return random.choice(intent['responses'])
    else:
        return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

