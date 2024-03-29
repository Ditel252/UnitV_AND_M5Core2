#include <Arduino.h>
#include <M5Core2.h>
#include <LovyanGFX.h>
#include <LGFX_AUTODETECT.hpp>

uint32_t readDataImageSize;
uint8_t *readData;

static LGFX lcd;

void setup(){
    M5.begin(true, true, false);

    Serial2.begin(2000000, SERIAL_8N1, 14, 13);

    lcd.init();
    lcd.clearDisplay(WHITE);
    lcd.setTextColor(BLACK);
    lcd.setTextSize(1);
    lcd.setCursor(0, 0);
    lcd.println("Program Start");

    readData = (uint8_t *)malloc(sizeof(uint8_t) * 153600);
}


void loop(){
    if(Serial2.available()){
        int readDataSize = Serial2.readBytes(readData, 4);

        if(readDataSize == 4){
            if(*(readData + 0) == 0xA0){
                readDataImageSize = (*(readData + 1) << 16) | (*(readData + 2) << 8) | (*(readData + 3) << 0);

                Serial2.readBytes(readData, readDataImageSize);

                lcd.drawJpg(readData, readDataImageSize, 0, 0, 320, 240, 0, 0, ::JPEG_DIV_NONE);
            }
        }
    }
}