# DASH LOGIC - 24/7 Discord Voice & Status Bot

[Türkçe Açıklama İçin Tıklayın](#türkçe)

An advanced, lightweight, and professional Python-based Discord bot designed to keep your account connected to a specific voice channel 24/7 and set a custom activity status. Perfect for maintaining presence, activity badges, or simple custom statuses.

## 🚀 Features

- **24/7 Voice Presence**: Joins a voice channel and stays connected indefinitely.
- **Auto Reconnect**: Automatically reconnects if kicked out of the channel or disconnected due to network issues.
- **Custom Status**: Set a custom English activity status (e.g., "Chilling...", "Listening to Spotify") shown on your profile.
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
   ```
2. Run the script:
   ```bash
   python main.py
   ```

---

## 🔑 How to get Details?

### 1. How to get Discord Token
> [!WARNING]
> Never share your account token with anyone.

1. Open Discord in your Web Browser (Chrome, Firefox, etc.) and log in.
2. Press `F12` or `Ctrl + Shift + I` to open Developer Tools.
3. Go to the **Network** tab.
4. Type `messages` or `/api` in the search filter box.
5. Click on any request that appears (e.g., a channel message request) and scroll down to the **Request Headers** section on the right.
6. Copy the value next to `Authorization`. This is your token!

### 2. How to get Voice Channel ID
1. Open Discord Settings -> Advanced.
2. Enable **Developer Mode**.
3. Right-click on the voice channel you want to join.
4. Click **Copy Channel ID**.

---

## ⚠️ Disclaimer
Automating user accounts (Self-botting) is against Discord's Terms of Service. Use this tool at your own risk. The author is not responsible for any account suspensions.

---

<a id="türkçe"></a>

# 🇹🇷 Türkçe Açıklama

Hesabınızı 7/24 ses kanalında tutan ve profilinize özel durum (Custom Status) ayarlayan profesyonel Python tabanlı Discord botu.

## 🚀 Özellikler

- **7/24 Ses Aktifliği**: Belirttiğiniz ses kanalına girer ve 7/24 aktif kalır.
- **Otomatik Yeniden Bağlanma**: Ses kanalından atılırsanız veya internet koparsa 5 saniye içinde tekrar bağlanır.
- **Özel Durum Ayarı**: Profilinizde gözükecek İngilizce/Türkçe durum yazısını ayarlar.
- **Kolay Kurulum**: Bilgiler girilmemişse konsol üzerinden interaktif olarak sorar ve `config.json` dosyasına kaydeder.
- **DASH LOGIC ASCII Tasarımı**: Açılışta şık bir "DASH LOGIC" ASCII tasarımı gösterir.
- **Çökme Koruması**: `start.bat` sayesinde bot kapansa bile otomatik olarak yeniden başlar.

## 🛠️ Kurulum ve Çalıştırma

### Gereksinimler
- Bilgisayarınızda Python 3.8 veya üzeri bir sürümün kurulu olması gerekir.

### Kolay Kurulum (Windows)
1. `install.bat` dosyasına çift tıklayarak gerekli kütüphaneleri yükleyin.
2. `start.bat` dosyasına çift tıklayarak botu çalıştırın.
3. İlk açılışta sizden sırasıyla **Token**, **Ses Kanalı ID'si** ve **Özel Durum** bilgilerini isteyecek ve kaydedecektir.

---

## 📝 Lisans
Bu proje [MIT](LICENSE) lisansı ile korunmaktadır.
