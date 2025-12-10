# Evernight Lonely Dance ESP8266

This project demonstrates how to animate a GIF on a NodeMCU ESP‑12E board with a 128x64 SH1106 OLED display.  
It combines a Python preprocessing step to extract GIF frames and an Arduino sketch to render them on the OLED.

---

## 🎬 Demo Preview

![Evernight Honkai GIF](https://github.com/TheTechTiger/EvernightLonelyDanceESP8266/blob/master/evernight-honkai.gif?raw=true)

---

## 📂 Repository Structure
- `gif2frames.py` → Python script to convert GIFs into individual frames.
- `EvernightLonelyDance.ino` → Arduino sketch for NodeMCU ESP‑12E.
- `Evernight.h` → Header file containing converted frame bitmaps.
- `evernight-honkai.gif` → Example input GIF.
- `evernight-honkai_frames/` → Output folder containing extracted frames.

---

## 🛠 Requirements

### Python side
- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (`pip install pillow`)

### Arduino side
- NodeMCU ESP‑12E (ESP8266)
- SH1106 OLED display (128x64)
- [Adafruit SH110X library](https://github.com/adafruit/Adafruit_SH110X)

---

## ⚙️ Workflow

1. **Install Pillow**
   ```bash
   pip install pillow
   ```

2. **Convert GIF to frames**
   ```bash
   python gif2frames.py
   ```
   This saves all frames from `evernight-honkai.gif` into `./evernight-honkai_frames/`.

3. **Convert frames to C arrays**
   - Upload the PNG frames to [Image2CPP](https://javl.github.io/image2cpp/).
   - Resize frames to fit the OLED (128x64).
   - Export as a header file (`gifname.h`).

4. **Include the header in Arduino sketch**
   - Place the generated `gifname.h` in your Arduino project.
   - The sketch `EvernightLonelyDance.ino` references this header.

5. **Upload to ESP8266**
   - Connect your NodeMCU ESP‑12E.
   - Upload the sketch via Arduino IDE.

---

## 📌 Notes
- Frame delay (`delay(10)`) can be adjusted for smoother or faster playback.
- Ensure all frames are resized to **128x64** before converting to C arrays.
- Large GIFs may exceed flash memory limits; optimize by reducing frame count or resolution.

---

## 🔗 Repository
[EvernightLonelyDanceESP8266](https://github.com/TheTechTiger/EvernightLonelyDanceESP8266/)
