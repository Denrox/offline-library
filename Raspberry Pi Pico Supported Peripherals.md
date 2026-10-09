# Raspberry Pi Pico Supported Peripherals

## I2C peripherals

I2C peripherals like OLED Displays (e.g. SSD1306 or SH1106) and keyboards (e.g. CardKB) can be connected to GPIO pins 4 (SDA) and 5 (SCL), which will be recognized on boot. Note that for keyboard input, the [Canned Message Module](Canned%20Message%20Module%20Configuration.md) has to be enabled and the [input source](Canned%20Message%20Module%20Configuration.md) should be specified.

## External device using Serial Module

For connecting an external device via the [Serial Module](Serial%20Module%20Configuration.md), it's recommended to use GPIO pins 8 (`serial.txd`) and 9 (`serial.rxd`).

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/raspberrypi/pico/peripherals. GPL-3.0 (Meshtastic documentation).*
