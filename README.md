**🔤 Finglish to Persian Converter (PyQt5 + API)**

A smart Finglish-to-Persian and mistyped-text converter built with Python and PyQt5.
This tool can fix Persian text typed in the wrong keyboard layout (English instead of Persian) and also convert Finglish (Persian written in Latin letters) into real Persian script using AI.

**✨ Features**

🧠 Two conversion modes:

🔹 Mistyped Text Fixer: Converts Persian text typed with an English keyboard (e.g. salam → سلام, fhv → سلام).

🔹 Finglish to Persian: Uses an AI API to translate Finglish sentences into real Persian.

🪟 Modern PyQt5 GUI

🔡 Bidirectional text areas (Right-to-Left for Persian)

⚡ Instant conversion with buttons

💬 Error handling for network and API requests

**🧩 How It Works**
1. Mistyped Conversion

Maps each English key to its corresponding Persian letter based on a standard Persian keyboard layout.
Example:

Input: "fhv"
Output: "سلام"

2. Finglish Conversion (via API)

Sends your Finglish text to a Google AI Studio (Gemini) endpoint to generate accurate Persian translation.
(You must provide your own API key.)

🖥️ Interface Overview
Button	Function
تبدیل فینگلیش	Converts Finglish text to Persian (via AI API)
تبدیل متن بهم‌ریخته	Converts mistyped Persian text from English layout
Input Box	Type or paste your text
Output Box	Shows converted Persian text
**⚙️ Requirements**

Python 3.8 or higher

PyQt5

Requests

Install dependencies:

pip install PyQt5 requests

**📦 Installation & Usage**

Clone the repository:

git clone https://github.com/Mobina14/finglish-converter.git
cd finglish-converter


Run the app:

python finglish_converter.py


Type or paste your text, then click:

“تبدیل فینگلیش” for AI translation

“تبدیل متن بهم‌ریخته” for keyboard layout correction

**⚙️ Project Structure**
finglish-converter/
│
├── finglish_converter.py     # Main Python file
└── README.md                 # Documentation


**🧠 Technical Notes**
Component	Description
Framework	PyQt5
API	Google AI Studio (Gemini API)
Offline Mode	Mistyped-text conversion
Online Mode	Finglish → Persian via HTTP POST
Text Direction	RTL for Persian output
Error Handling	API timeout, connection errors, empty responses
🚀 Future Improvements

✅ Add history and undo/redo

🌐 Support for multiple AI translation providers

💾 Save converted text to file

🌓 Add dark/light mode

**🧑‍💻 Author**

Mobina RZ
📍 Mashhad, Iran
💡 Focused on AI-based educational and language tools

