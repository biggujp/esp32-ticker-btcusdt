#  ESP32-ticker-btcusdt 

This repository contains the code for Ticker Price of cryptocurrency BTCUSDT from [binance](https://www.binance.com/en/binance-api) and notification to [LineNotify](https://notify-bot.line.me/en/). I do deployed on ESP32 microcontrollers used by Micropython.

## 📂 Directory Structure
    .
    ├── 📄 boot.py                          // run system file
    ├── 📄 app.py                           // Main source code file
    └── 📄 README.md

## 🔨 Config
- 1st open app.py : edit SSID and SSID_PASSWORD 

  ```sh
  SSID = "INSERT YOUR NAME WIFI"
  SSI_PASSWORD = "INSERT YOUR WIFIPASSWORD"
  ```

- 2nd Line edit : TOKEN of  LineNotify

  ```sh
  token = 'INSERT YOUR TOKEN'
  ```

Enjoy and funny :smiley:
