# Hackathon Alien Project

Welcome to the Hackathon Alien Project! This project is an engaging and interactive SMS-based application designed to entertain and inform users with a range of features such as space diplomacy tips, UFO data, alien language translation, and real-time information about the International Space Station (ISS).

## Features

### 1. Diplomatic Tips & Tricks
Offers humorous and practical advice for navigating interactions in outer space. Example tips include:
* "Do not comment on their glowing eyes—it's a sensitive topic."
* "Don't touch glowing buttons, unless you enjoy space roulette."

### 2. Display UFO Data
Displays UFO sightings and data retrieved from an external API.

### 3. Klingon Translator
Translates basic text into Klingon or other alien languages (version 2 in progress).

### 4. ISS Information
Provides real-time updates about the location and status of the International Space Station (ISS).

### 5. Exit
Allows users to exit the menu gracefully.

## How It Works

### User Registration
Users register by sending their phone number and name to the system. A confirmation SMS is sent back to the user.

### Menu Interaction
Users receive a menu with options to choose from. Based on their selection, the corresponding function is triggered, and feedback is sent via SMS.

### Data Management
User and message data are stored and managed in the backend.


## Getting Started

### Prerequisites
* Python 3.9+
* Libraries: requests

### Installation

1. Clone the repository:
```bash
git clone https://github.com/masterschool-weiterbildung/hackathon-alien.git
```

2. Navigate to the project directory:
```bash
cd hackathon-alien
```

3. Install dependencies:
```bash
pip install requests
```

### Running the Application

1. Start the server (if applicable):
```bash
python main.py
```

2. Interact with the application via SMS or the terminal.