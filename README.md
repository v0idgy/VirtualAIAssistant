🌟 Overview
-----------

G-One is a versatile AI personal assistant built with Python, designed to make your daily digital interactions smoother and more efficient through voice commands. From fetching information and opening applications to answering complex queries and providing real-time weather updates, G-One aims to be your go-to companion for hands-free computing.

Say goodbye to typing and hello to the future of interaction! G-One is still in its early stages (version 1.0), but it's ready to serve you with a growing set of functionalities.

✨ Features
----------

* **Voice Activation:** Wakes up to the command "G One" (or "Jivan").

* **Intelligent Greetings:** Greets you based on the time of day (Good Morning, Good Afternoon, Good Evening).

* **Web Browsing:** Opens popular websites like YouTube, Google, GitHub, and Gmail.

* **Wikipedia Search:** Summarizes information directly from Wikipedia.

* **Location Finder:** Uses Google Maps to locate places based on your voice command.

* **Time Teller:** Informs you of the current time.

* **ChatGPT Integration:** Leverages the power of OpenAI's GPT for conversational queries and information retrieval.

* **Weather Updates:** Provides current temperature, humidity, and weather descriptions for any city using the OpenWeatherMap API.

* **News Headlines:** Fetches top headlines from Times of India.

* **Wolfram Alpha Integration:** Answers computational and geographical questions using Wolfram Alpha.

* **Self-Awareness:** Can introduce itself and tell you who created it.

* **System Commands:** Allows logging off your PC (with a prompt).

🚀 Installation
---------------

Follow these steps to get G-One up and running on your local machine.

### Prerequisites

* Python 3.x (recommended 3.8+)

* pip (Python package installer)

### Setup Steps

1. git clone <https://github.com/v0idgy/virtualaiassistant.git> && cd virtualaiassistant

2. python -m venv venv

    * .\\venv\\Scripts\\activate

    * source venv/bin/activate

3. pip install SpeechRecognition pyttsx3 wikipedia webbrowser requests wolframalpha pyChatGPT openai

    * **Note for pyttsx3 and SpeechRecognition:**

        * pyttsx3 typically requires a speech synthesis engine on your system (like SAPI5 on Windows).

        * SpeechRecognition might require PyAudio for microphone input. If you face issues on Windows, you might need to install pyaudio manually with a pre-compiled wheel from [Unofficial Windows Binaries for Python Extensions](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio). For other OS, ensure your system has PortAudio installed.

### 🔑 API Keys Setup

G-One leverages several external APIs for enhanced functionality. You'll need to obtain API keys for some features and set them as environment variables.

1. **OpenAI Session Token (for ChatGPT):**

    * Go to [ChatGPT](https://chat.openai.com/chat) and log in.

    * Open your browser's developer tools (usually F12).

    * Navigate to the "Application" or "Storage" tab, then "Cookies".

    * Find the cookie named \_\_Secure-next-auth.session-token. Copy its value.

    * Set this as an environment variable:

        * set OPENAI\_SESSION\_TOKEN="your\_session\_token\_here"

        * $env:OPENAI\_SESSION\_TOKEN="your\_session\_token\_here"

        * export OPENAI\_SESSION\_TOKEN="your\_session\_token\_here"

    * **Important:** This session token can expire, requiring you to update the environment variable periodically.

2. **OpenWeatherMap API Key (for Weather):**

    * Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api).

    * Once logged in, go to the "API keys" tab to generate or find your key.

    * Set this as an environment variable:

        * set WEATHER\_API\_KEY="your\_openweathermap\_api\_key\_here"

        * $env:WEATHER\_API\_KEY="your\_openweathermap\_api\_key\_here"

        * export WEATHER\_API\_KEY="your\_openweathermap\_api\_key\_here"

3. \# In your code, replace:app\_id="63TGXXXXXXXXXX" # <--- REPLACE THIS WITH YOUR WOLFRAM ALPHA APP IDclient = wolframalpha.Client('63TGQXXXXXXXXXXXXXXX') # <--- AND THISA more secure approach would be:# Inside your scriptimport os# ...# app\_id = os.getenv("WOLFRAM\_ALPHA\_APP\_ID")# client = wolframalpha.Client(app\_id)and then setting the environment variable WOLFRAM\_ALPHA\_APP\_ID.

    * Go to [Wolfram Alpha Developer Portal](https://developer.wolframalpha.com/portal/apisignup.html) and sign up/log in.

    * Register a new application to get an App ID.

    * Directly paste the App ID into the app\_id variable in the code (it's currently hardcoded as "63TGXXXXXXXXXXXXXXXX"). **It is highly recommended to replace this with your own ID or manage it as an environment variable for security.**

Remember to restart your terminal or IDE after setting environment variables for them to take effect.

▶️ Usage
--------

To start your personal assistant, simply run the Python script:


G-One will greet you and then start listening for commands.

### Supported Commands

Here are some of the commands G-One understands:

* "G One" or "Jivan" (to activate/greet)

* "good bye", "bye", "ok bye", "stop" (to shut down G-One)

* "wikipedia \[your query\]" (e.g., "wikipedia Albert Einstein")

* "open youtube"

* "open github"

* "open google"

* "open gmail"

* "chatgpt" or "GPT" or "open ai" (G-One will then ask for your query)

* "weather" (G-One will then ask for the city name)

* "time"

* "who i am"

* "how are you"

* "who are you" or "what can you do" or "what's your name"

* "who made you" or "who created you" or "who discovered you"

* "open stack overflow"

* "news"

* "search \[your query\]" (e.g., "search Python programming")

* "who is \[person/thing\]" or "what is \[concept\]" (for Wolfram Alpha queries)

* "where is \[location\]" (e.g., "where is Taj Mahal")

* "log off" or "sign out"

🚧 Known Issues / Future Enhancements
-------------------------------------

* **ChatGPT Session Token Expiration:** The pyChatGPT library relies on a session token which can expire, leading to the ChatGPT functionality breaking. An alternative using OpenAI's official API key (if available) would be more robust.

* **Error Handling:** More robust error handling for network issues, API key failures, and unrecognized commands could improve user experience.

* **Modularity:** Breaking down the main loop into more functions or a class would make the code more organized and easier to maintain.

* **Camera Feature:** The camera capture feature is commented out. If ecapture is intended, it needs to be installed and properly integrated.

* **Wake Word Accuracy:** Improve wake word detection for better responsiveness.

* **Voice Variety:** Explore options for different voice types or accents.

🤝 Contributing
---------------

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/YourFeature).

3. Make your changes.

4. Commit your changes (git commit -m 'Add new feature').

5. Push to the branch (git push origin feature/YourFeature).

6. Open a Pull Request.

📄 License
----------

This project is licensed under the MIT License - see the LICENSE file for details (if you create one, otherwise state no specific license).

🙏 Acknowledgements
-------------------

* **Gourav Yadav (v0idgy)** - The original creator of G-One.

* Inspired by various AI assistant tutorials and open-source projects.

* Libraries: SpeechRecognition, pyttsx3, wikipedia, webbrowser, requests, wolframalpha, pyChatGPT, openai.
