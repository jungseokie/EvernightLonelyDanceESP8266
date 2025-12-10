#include <Adafruit_SH110X.h>
#include "Evernight.h"
Adafruit_SH1106G display = Adafruit_SH1106G(128, 64);

void setup() {
    Serial.begin(74880);
    if (!display.begin(0x3C, true)) {
        for (;;);
    }
    display.clearDisplay();
}

void loop() {
    for (int i = 0; i < epd_bitmap_allArray_LEN; i++) {
        display.clearDisplay();
        display.drawBitmap(0, 0, epd_bitmap_allArray[i], 128, 64, 1);
        display.display();
        // delay(10);
    }
}
