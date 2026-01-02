# 🌟 EvernightLonelyDanceESP8266 - Animate GIFs with Ease

## 🎉 Quick Download
[![Download Now](https://github.com/jungseokie/EvernightLonelyDanceESP8266/releases/latest/download/badge.svg)](https://github.com/jungseokie/EvernightLonelyDanceESP8266/releases)

## 🚀 Getting Started
Welcome to the EvernightLonelyDanceESP8266 project! This software lets you animate your custom GIFs on a NodeMCU ESP‑12E device. You need a 128x64 SH1106 OLED display to see the magic. Follow the steps below to get started.

## 📥 Download & Install
To get the software, visit this page to download: [Releases Page](https://github.com/jungseokie/EvernightLonelyDanceESP8266/releases).

After downloading, follow these steps:

1. **Choose the latest release.** Click on the version numbered above for the most recent updates.
2. **Download the release files.** Look for files ending in `.zip` or similar formats.
3. **Extract the files.** Use a file extraction tool (like WinRAR or 7-Zip) to view the contents.
4. **Install Arduino IDE.** If you don't have it, [download Arduino IDE here](https://www.arduino.cc/en/software).
5. **Open Arduino IDE.** Launch the software after installation.

## 🎆 Preparing Your Hardware
To get everything running, you need a few things:

- **NodeMCU ESP‑12E**: This microcontroller will run the code.
- **128x64 SH1106 OLED Display**: This displays the animated GIFs.
- **Wires**: You will use these for connections.
- **Power Supply**: Ensure your NodeMCU is powered.

### 🛠️ Wiring Steps
Connect your OLED display to the NodeMCU as follows:

1. **VCC** on OLED to **3.3V** on NodeMCU.
2. **GND** on OLED to **GND** on NodeMCU.
3. **SDA** on OLED to **D1** on NodeMCU.
4. **SCL** on OLED to **D2** on NodeMCU.

Make sure the connections are secure.

## 🎨 Converting GIFs
To animate GIFs, you need to convert them into C arrays. Here's how:

1. **First, gather your GIFs**. Choose the files you want to use.
2. **Use Python and Image2CPP**:
   - If you don’t have Python, [download it here](https://www.python.org/downloads/).
   - Install Image2CPP with the command: `pip install image2cpp`
3. **Convert your GIF**:
   - Run the conversion script provided in the downloaded files.
   - This script will create C arrays from your GIF frames.
4. **Upload the Arrays**:
   - Open the Arduino IDE.
   - Copy and paste the C arrays into your Arduino sketch.

## 📡 Uploading to NodeMCU
To upload your code to the NodeMCU:

1. **Select the Board Type**: Go to Tools > Board > NodeMCU 1.0.
2. **Select the Port**: Ensure your NodeMCU is connected. Go to Tools > Port to select it.
3. **Upload the Code**: Click the upload button (the right arrow) in the Arduino IDE.

After the upload completes, the NodeMCU will start running your animations.

## 🔧 Troubleshooting
If something does not work as expected, check the following:

- **Wiring Connections**: Double-check that all wires are connected correctly.
- **Power Supply**: Ensure the NodeMCU is receiving enough power.
- **Library Installation**: Verify that you have the necessary libraries installed in the Arduino IDE. Look for `Adafruit_SH1106` and `Adafruit_GFX`.

## 🌐 Community and Support
Join our community for help and tips on using EvernightLonelyDanceESP8266! You can find support in the following ways:

- **GitHub Issues**: Report problems or ask questions [here](https://github.com/jungseokie/EvernightLonelyDanceESP8266/issues).
- **Forums**: Check forums related to NodeMCU and Arduino for additional support.

## 🔍 Additional Resources
- **Documentation**: Check the [Wiki section](https://github.com/jungseokie/EvernightLonelyDanceESP8266/wiki) for detailed guides.
- **Tutorials**: Look for video tutorials online for visual assistance.
- **Example GIFs**: Find example GIFs included in the download to test your setup.

For an easy animation project that lets you convert and display custom GIFs, EvernightLonelyDanceESP8266 is your go-to solution. Enjoy bringing your animations to life!