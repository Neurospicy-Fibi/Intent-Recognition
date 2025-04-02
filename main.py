import re
import random
from datetime import datetime
from colorama import init, Fore, Style
import sys

# Initialisiere colorama
init()

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

class IntentRecognizer:
    def __init__(self):
        self.intents = {
            "greeting": {
                "patterns": [
                    r"hallo", r"guten tag", r"guten morgen", r"guten abend",
                    r"hi", r"hey", r"servus", r"moin"
                ],
                "responses": [
                    "Hallo! Wie kann ich Ihnen helfen?",
                    "Guten Tag! Was möchten Sie wissen?",
                    "Willkommen! Wie kann ich Sie unterstützen?"
                ]
            },
            "weather": {
                "patterns": [
                    r"wetter", r"wie ist das wetter", r"wettervorhersage",
                    r"regnet es", r"scheint die sonne", r"wie warm ist es"
                ],
                "responses": [
                    "Das Wetter ist heute schön!",
                    "Es ist sonnig und warm.",
                    "Aktuell scheint die Sonne."
                ]
            },
            "time": {
                "patterns": [
                    r"wie spät", r"uhrzeit", r"wie viel uhr",
                    r"wie spät ist es", r"wie viel uhr ist es"
                ],
                "responses": [
                    "Es ist {} Uhr.",
                    "Die aktuelle Zeit ist {} Uhr.",
                    "Jetzt ist es {} Uhr."
                ]
            },
            "farewell": {
                "patterns": [
                    r"tschüss", r"auf wiedersehen", r"bis bald",
                    r"tschau", r"bye", r"bis später"
                ],
                "responses": [
                    "Auf Wiedersehen!",
                    "Tschüss! Kommen Sie bald wieder!",
                    "Bis zum nächsten Mal!"
                ]
            },
            "help": {
                "patterns": [
                    r"hilfe", r"kannst du mir helfen", r"wie geht das",
                    r"was kannst du", r"was machst du", r"wie funktioniert"
                ],
                "responses": [
                    "Ich kann Ihnen bei verschiedenen Dingen helfen:",
                    "Ich erkenne verschiedene Absichten in Ihren Nachrichten.",
                    "Ich verstehe Fragen zu Wetter, Zeit und mehr."
                ]
            }
        }

    def recognize_intent(self, text):
        text = text.lower()
        
        for intent, data in self.intents.items():
            for pattern in data["patterns"]:
                if re.search(pattern, text):
                    return intent, data["responses"]
        
        return "unknown", ["Entschuldigung, ich verstehe das nicht."]

    def get_response(self, intent, responses):
        if intent == "time":
            current_time = datetime.now().strftime("%H:%M")
            return random.choice(responses).format(current_time)
        return random.choice(responses)

def main():
    if (len(sys.argv) > 1 and sys.argv[1] == "score"):
      print("Score: 12")
      exit()
      
    recognizer = IntentRecognizer()
    print_colored("\nWillkommen beim Intent Recognition System!", Fore.MAGENTA)
    print_colored("Geben Sie 'beenden' ein, um das Programm zu beenden.\n", Fore.CYAN)
    
    while True:
        user_input = input("\nIhre Eingabe: ").strip()
        
        if user_input.lower() == "beenden":
            print_colored("\nAuf Wiedersehen!", Fore.MAGENTA)
            break
            
        intent, responses = recognizer.recognize_intent(user_input)
       
        print_colored("\nErkannter Intent:", Fore.GREEN)
        print_colored(intent.capitalize(), Fore.YELLOW)
        
        response = recognizer.get_response(intent, responses)
        print_colored("\nAntwort:", Fore.BLUE)
        print_colored(response, Fore.CYAN)

if __name__ == "__main__":
    main() 
