# HELTEC® LoRa 32

**LoRa32 V4**

## V4

> **Info:**
>
> A newer **V4-R8** variant is also available, which uses the **ESP32-S3R8** chip and has a different pinout and firmware. If your board has the ESP32-S3R8, use the V4-R8 tab instead.

- **MCU:**
  - ESP32-S3R2 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Integrated antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa

### Features

- Built in 0.96 inch OLED display
- High power option: 28±1dBm
- Optimized lithium battery management
- Form factor and pin compatibility with V3/V3.1
- 1.25-2Pin solar interface
- 1.25-8Pin GNSS interface

### Pin Map

### Resources

- Firmware file: `firmware-heltec-v4-X.X.X.xxxxxxx.bin`
- Purchase links
  - US
    - Rokland
  - International
    - Heltec
    - Hexaspot

**LoRa32 V4-R8**

## V4-R8

> **Caution:**
>
> The **V4-R8** is a separate hardware variant from the original V4. It uses the **ESP32-S3R8** chip with a different pinout and requires its own firmware. Do not flash the original `firmware-heltec-v4-*` firmware on a V4-R8 board.

- **MCU:**
  - ESP32-S3R8 (Wi-Fi & Bluetooth)
- **Flash:**
  - 16 MB external
- **PSRAM:**
  - 8 MB
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Integrated antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa
  - SH1.25-2Pin solar panel interface
  - SH1.25-8Pin GNSS interface

### Features

- Built in 0.96 inch OLED display (OLED variant) or TFT display (TFT variant)
- High power option: 28±1dBm
- Optimized lithium battery management
- 8 MB PSRAM for maps and more complex UI
- Similar physical form factor to the V4, but the pinout is not compatible

### Pin Map

Image Source: Heltec

### Resources

- Firmware files:
  - OLED: `firmware-heltec-v4-r8-oled-X.X.X.xxxxxxx.bin`
  - TFT: `firmware-heltec-v4-r8-tft-X.X.X.xxxxxxx.bin`
- Use the latest Meshtastic firmware (2.7.25 or newer). In the Web Flasher, select **Heltec LoRa32 V4-R8**.
- Purchase links
  - International
    - Heltec

**LoRa32 V3/V3.1**

## V3/V3.1

::::info
This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

> **Caution:**
>
> Be careful when interacting with the USB-C port. This device does not have ESD protection for the CP2102 USB to UART bridge chip.

::::

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 433 MHz
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Dedicated 2.4 GHz metal spring antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa

### V3.1 differences

Firmware remains the same as V3 below. Compare schematics: V3.0_V3_Schematic_Diagram.pdf>) and V3.1_V3.1_Schematic_Diagram.pdf>). Key differences:

- Removal of FDG6322C (a dual N & P channel FET) from the V3.1 power supply.
- Antenna filter values in V3.1 (L11 = 1.8pF, C15 = 2.7nH, C24 = 1.8pF) align more closely with ESP32-S3 reference design than V3.0 (L11 = 1.6nH, C15 = 6.9pF, C24 = 2.4pF).

### Features

- Built in 0.96 inch OLED display
- User and Reset Buttons
- No GPS

### Meshtastic I2C Definitions

- SDA: GPIO41
- SCL: GPIO42

### Pin Map

Image Source: Heltec_V3.png>)

### Resources

- Firmware file: `firmware-heltec-v3-X.X.X.xxxxxxx.bin`
- Purchase links
  - US
    - muzi ᴡᴏʀᴋꜱ
    - Rokland
  - International
    - Heltec
    - AliExpress
    - Hexaspot

**Wireless Stick Lite V3**

## Wireless Stick Lite V3

> **Info:**
>
> This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 433 - 510 MHz
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Dedicated 2.4 GHz stamped metal antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa (next to the V3 icon)

### Features

- No display.
- User and Reset Buttons
- Additional GPIO availability
- No GPS

### Meshtastic I2C Definitions

- SDA: GPIO41
- SCL: GPIO42

### Pin Map

Image Source: Heltec

Image Source: Heltec

There are two antenna connectors. You need to connect the LoRa antenna while the Wi-Fi antenna is optional.

### Resources

- Firmware file: `firmware-heltec-wsl-v3-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - US
    - Rokland
  - International
    - Heltec
    - AliExpress
- From Heltec
  - Documentation (docs.heltec.org)
  - Schematic Diagram (PDF)
  - LoRa Node Development Kit (PDF).pdf>)

**Wireless Tracker v1.0**

## Wireless Tracker v1.0

> **Info:**
>
> This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Dedicated 2.4 GHz metal spring antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa and GNSS

### Features

- Onboard 0.96-inch LCD display
- User and Reset Buttons

### Flashing

To flash ESP32-S3 devices like the Wireless Tracker, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this. If this method does not work for any reason, you can follow the manual process below.

> **Warning:**
>
>
> Do not proceed unless an antenna is connected to avoid possible damage to the device's radio.
>

The following process will manually place the device into the Espressif Firmware Download mode:

1. Unplug the device.
2. Press and hold the USER button.
3. Plug device in.
4. After 2-3 seconds, release the USER button.

With the device now in the Espressif Firmware Download mode, you can proceed with flashing using one of the supported flashing methods. It's generally recommended to use the Web Flasher. You can select "Heltec Wireless Tracker" from the device drop-down.

### Pin Map

Image Source: Heltec

### Resources

- Firmware file: `firmware-heltec-wireless-tracker-V1-0-X.X.X.xxxxxxx.bin`

> **Note:**
>
>
> Heltec revised the Wireless Tracker schematics and released a V1.1, most devices being sold are now V1.1.
>

**Wireless Tracker v1.1**

## Wireless Tracker v1.1

> **Info:**
>
> This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - Dedicated 2.4 GHz metal spring antenna for Wi-Fi/Bluetooth
    - U.FL/IPEX antenna connector for LoRa and GNSS

### Features

- Onboard 0.96-inch LCD display
- User and Reset Buttons

### Flashing

To flash ESP32-S3 devices like the Wireless Tracker, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this. If this method does not work for any reason, you can follow the manual process below.

> **Warning:**
>
>
> Do not proceed unless an antenna is connected to avoid possible damage to the device's radio.
>

The following process will manually place the device into the Espressif Firmware Download mode:

1. Unplug the device.
2. Press and hold the USER button.
3. Plug device in.
4. After 2-3 seconds, release the USER button.

With the device now in the Espressif Firmware Download mode, you can proceed with flashing using one of the supported flashing methods. It's generally recommended to use the Web Flasher. You can select "Heltec Wireless Tracker" from the device drop-down.

### Meshtastic I2C Definitions

- SDA: GPIO45
- SCL: GPIO46

### Pin Map

Image Source: Heltec

### Resources

- Firmware file: `firmware-heltec-wireless-tracker-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - US
    - Rokland
  - International
    - Heltec
    - AliExpress

**Wireless Tracker V2**

## Wireless Tracker V2

The Wireless Tracker V2 is the revised version of Heltec's Wireless Tracker, built on the ESP32-S3 with a high-power (28±1 dBm) SX1262 LoRa radio, a dual-band UC6580 GNSS, and a 0.96-inch color TFT display, plus battery and solar power management.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262 (up to 28±1 dBm)
- **Frequency Options:**
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Navigation Module:**
  - UC6580 dual-band GNSS (GPS, GLONASS, BDS, Galileo, NAVIC, QZSS)
- **Connectors:**
  - USB-C
  - Antenna:
    - U.FL/IPEX antenna connector for LoRa
    - Integrated antenna for Wi-Fi/Bluetooth

### Features

- Onboard 0.96-inch color TFT display (160 x 80).
- Dual-band UC6580 GNSS.
- High-power SX1262 LoRa radio (up to 28±1 dBm).
- Battery and solar smart power management.

### Flashing

To flash ESP32-S3 devices like the Wireless Tracker, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this.

### Resources

- Firmware file: `firmware-heltec-wireless-tracker-v2-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - International
    - Heltec

**Wireless Paper v1.0**

## Wireless Paper V1.0

> **Info:**
>
> **The Wireless Paper V1.0 is listed as "Wireless Paper V1.0" in the firmware files and on the web flasher.**
>
> This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 433 MHz
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - U.FL/IPEX antenna connector for LoRa
    - Integrated 2.4 GHz PCB antenna

### Features

- Onboard 2.13-inch black and white E-Ink display screen
- User and Reset switches
- No GPS

### Resources

- Firmware file: `firmware-heltec-wireless-paper-v1_0-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - International
    - Heltec
    - AliExpress

**Wireless Paper v1.1**

## Wireless Paper V1.1

> **Info:**
>
> **The Wireless Paper V1.1 is listed as "Wireless Paper" in the firmware files and on the web flasher.**
>
> This device may have issues charging a connected battery if utilizing a USB-C to USB-C cable. It's recommended to use a USB-A to USB-C cable.

- **MCU:**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth)
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 433 MHz
  - 470 - 510 MHz
  - 863 - 870 MHz
  - 902 - 928 MHz
- **Connectors:**
  - USB-C
  - Antenna:
    - U.FL/IPEX antenna connector for LoRa
    - Integrated 2.4 GHz PCB antenna

### Features

- Onboard 2.13-inch black and white E-Ink display screen
- User and Reset switches
- No GPS

### Resources

- Firmware file: `firmware-heltec-wireless-paper-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - US
    - Rokland
  - International
    - Heltec
    - AliExpress

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/heltec-automation/lora32/lora32. GPL-3.0 (Meshtastic documentation).*
