# Dash Logic - 24/7 Discord Voice & Status Bot

An advanced, lightweight, and professional Python-based Discord bot designed to keep your account connected to a specific voice channel 24/7 and set a custom activity status. Perfect for maintaining presence, activity badges, or simple custom statuses.

## 🚀 Features

- **24/7 Voice Presence**: Joins a voice channel and stays connected indefinitely.
- **Auto Reconnect**: Automatically reconnects if kicked out of the channel or disconnected due to network issues.
- **Custom Status**: Set a custom activity status (e.g., "Chilling...", "Listening to Spotify") shown on your profile.
- **Interactive Setup**: If no config is found, the CLI will guide you to set up your Token and Voice Channel ID.
- **DASH LOGIC ASCII Art**: Starts with a beautiful cyan terminal banner.
- **Crash Protection**: Windows startup script (`start.bat`) automatically restarts the bot if it crashes.

---

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.8 or higher installed on your PC.

### Fast Setup (Windows)
1. Double-click `install.bat` to install all necessary dependencies.
2. Double-click `start.bat` to run the bot.
3. The console will ask for your **Token**, **Voice Channel ID**, and **Custom Status** on first run, and save them to `config.json`.

### Manual Setup (All OS)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
