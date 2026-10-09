# Devices | Supported Hardware Overview

## Supported Devices

Meshtastic firmware can be installed on a wide range of development boards. The list below provides a brief comparison of currently supported hardware.

### Which board should I choose?

While all the boards listed on this page will run Meshtastic and mesh with each other, some current community favorites are:

- RAK Meshtastic Start Kit: [RAK19007](RAK%20WisBlock%20Base%20Boards.md)+[RAK4631](RAK%20WisBlock%20Core%20Modules.md)
- [Seeed Card Tracker T1000-E](SenseCAP%20Card%20Tracker%20T1000-E.md)
- [Seeed Wio Tracker L1](Seeed%20Wio%20Tracker%20L1.md)
- Heltec Mesh Node T114
- Nano G2 Ultra
- Station G2
- LILYGO LoRa T3-S3

Please do your research and choose the board that meets your needs (or maybe already have in a bin somewhere).

> **Info:**
>
>
> - We **strongly** recommend choosing devices equipped with the newer Semtech SX126x or LR11xx series, as they offer improved performance and better compatibility than the SX127x series.
> - nRF52-based devices use less power than ESP32-based devices and are therefore generally preferred for solar and handset applications.
> - ESP32-based devices require more power to operate but are typically lower-cost alternatives that do perform well when using house power, or for handsets that only require a day or two of runtime, and for applications that require Wi-Fi connectivity or more RAM.
>

## RAK®

### Wisblock

Modular hardware system with Base, Core and Peripheral modules including the low-power and solar ready nRF52840-based Meshtastic Starter Kit (19007 & 4631).

[**WisBlock Core Modules**](RAK%20WisBlock%20Core%20Modules.md)

| Name                                                             | MCU      | Radio  | Wi-Fi | BT  |  GPS   |
| :--------------------------------------------------------------- | :------- | :----- | :--: | :-: | :----: |
| [RAK4631](RAK%20WisBlock%20Core%20Modules.md)   | nRF52840 | SX1262 |  NO  | 5.0 | ADD-ON |
| [RAK11310](RAK%20WisBlock%20Core%20Modules.md) | RP2040   | SX1262 |  NO  | NO  | ADD-ON |
| [RAK3312](RAK%20WisBlock%20Core%20Modules.md)   | ESP32-S3 | SX1262 | YES  | 5.0 | ADD-ON |

[**Base Boards**](RAK%20WisBlock%20Base%20Boards.md)

| Name                                                              | Type                                 |
| ----------------------------------------------------------------- | ------------------------------------ |
| [RAK5005-O](RAK%20WisBlock%20Base%20Boards.md) | WisBlock Base Board (End Of life).   |
| [RAK19007](RAK%20WisBlock%20Base%20Boards.md)   | WisBlock Base Board (2nd Generation) |
| [RAK19003](RAK%20WisBlock%20Base%20Boards.md)   | WisBlock Mini Base Board.            |
| [RAK19001](RAK%20WisBlock%20Base%20Boards.md)   | WisBlock Dual IO Base Board.         |

[**WisBlock Peripherals**](RAK%20WisBlock%20Supported%20Peripherals.md)

| Name                                                                              | Type                            |
| --------------------------------------------------------------------------------- | ------------------------------- |
| [RAK1910](RAK%20WisBlock%20Supported%20Peripherals.md)                     | GPS                             |
| [RAK12500](RAK%20WisBlock%20Supported%20Peripherals.md)                    | GPS                             |
| [RAK18001](RAK%20WisBlock%20Supported%20Peripherals.md)                 | Buzzer                          |
| [RAK13002](RAK%20WisBlock%20Supported%20Peripherals.md)                     | IO Module                       |
| RAK14001                                                                          | RGB LED                         |
| [RAK12002](RAK%20WisBlock%20Supported%20Peripherals.md)                    | Real Time Clock                 |
| [RAK1901](RAK%20WisBlock%20Supported%20Peripherals.md) | Temperature and Humidity Sensor |
| [RAK1902](RAK%20WisBlock%20Supported%20Peripherals.md) | Barometric Pressure Sensor      |
| [RAK1906](RAK%20WisBlock%20Supported%20Peripherals.md) | Environment Sensor              |
| RAK12013                                                                          | Radar Sensor                    |
| RAK13800                                                                          | Ethernet Module                 |

[**WisBlock Displays**](RAK%20WisBlock%20Screens.md)

| Name                                                         | Type                    | Resolution |
| ------------------------------------------------------------ | ----------------------- | ---------- |
| [RAK1921](RAK%20WisBlock%20Screens.md)   | 0.96 inch OLED          | 128x64px   |
| [RAK14000](RAK%20WisBlock%20Screens.md) | 2.13 inch E-Ink display | 212x104px  |

### WisMesh

| Name                                                                                      | MCU      | Radio       | Wi-Fi | BT  |  GPS   |
| :---------------------------------------------------------------------------------------- | :------- | :---------- | :--: | :-: | :----: |
| [WisMesh Pocket V2](RAK%20WisMesh%20Pocket%20Devices.md)                       | nRF52840 | SX1262      |  NO  | 5.0 |  YES   |
| [WisMesh Pocket Mini](RAK%20WisMesh%20Pocket%20Devices.md)                  | nRF52840 | SX1262      |  NO  | 5.0 |   NO   |
| [WisMesh Tag](RAK%20WisMesh%20Tag.md)                                             | nRF52840 | SX1262      |  NO  | 5.0 |  YES   |
| [WisMesh TAP](RAK%20WisMesh%20Tap.md)                                         | nRF52840 | SX1262      |  NO  | 5.0 |  YES   |
| [WisMesh Tap V2](RAK%20WisMesh%20Tap.md)                                      | ESP32-S3 | SX1262      | YES  | 5.0 |  YES   |
| [WisMesh Board ONE](RAK%20WisMesh%20Board%20ONE.md)                                 | nRF52840 | SX1262      |  NO  | 5.0 | ADD-ON |
| [WisMesh 1W Booster](RAK%20WisMesh%201W%20Booster%20Starter%20Kit.md)                                   | nRF52840 | SX1262 (1W) |  NO  | 5.0 | ADD-ON |
| [WisMesh Repeater](RAK%20WisMesh%20Repeater%20Devices.md)                    | nRF52840 | SX1262      |  NO  | 5.0 | ADD-ON |
| [WisMesh Repeater Mini](RAK%20WisMesh%20Repeater%20Devices.md)          | nRF52840 | SX1262      |  NO  | 5.0 | ADD-ON |
| [WisMesh Ethernet MQTT Gateway](RAK%20WisMesh%20Gateway.md) | nRF52840 | SX1262      |  NO  | 5.0 | ADD-ON |
| [WisMesh Wi-Fi MQTT Gateway](RAK%20WisMesh%20Gateway.md)         | ESP32    | SX1262      | YES  | 5.0 | ADD-ON |

## LILYGO®

### T-Beam

Boards complete with GPS, 18650 battery holder, and optional screen.

| Name                                            | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :---------------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| T-Beam S3-Core | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| T-BeamSUPREME | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| T-Beam 1W   | ESP32-S3 | SX1262 (1W) | 2.4GHz b/g/n | 5.0 | YES |

### T-Echo

All-in-one unit with E-Ink screen, GPS and battery in injection-molded case. Features the low-power nRF52840 for long battery life.

| Name                                                | MCU      | Radio  | Wi-Fi | BT  | GPS |
| :-------------------------------------------------- | :------- | :----- | :--: | :-: | :-: |
| T-Echo              | nRF52840 | SX1262 |  NO  | 5.0 | YES |
| T-Echo Plus    | nRF52840 | SX1262 |  NO  | 5.0 | YES |

### LoRa

Inexpensive basic ESP32-based boards.

| Name                                             | MCU      | Radio                                   |     Wi-Fi     | BT  | GPS |
| :----------------------------------------------- | :------- | :-------------------------------------- | :----------: | :-: | :-: |
| LoRa32 T3-S3 V1.0 | ESP32-S3 | SX1262SX1276SX1280LR1121 | 2.4GHz b/g/n | 5.0 | NO  |

### T-Deck

Standalone device with screen and keyboard

| Name                                            | MCU         | Radio  | Wi-Fi | BT  | GPS |
| :---------------------------------------------- | :---------- | :----- | :--: | :-: | :-: |
| T-Deck         | ESP32-S3FN8 | SX1262 | YES  | 5.0 | NO  |
| T-Deck Plus    | ESP32-S3FN8 | SX1262 | YES  | 5.0 | YES |
| T-Deck Pro | ESP32-S3FN8 | SX1262 | YES  | 5.0 | YES |

### T-Lora Pager

Standalone device with screen and keyboard.

| Name                                                     | MCU      | Radio  | Wi-Fi | BT  | GPS |
| :------------------------------------------------------- | :------- | :----- | :--: | :-: | :-: |
| T-Lora Pager | ESP32-S3 | LR1121 | YES  | 5.0 | YES |

### Mini ePaper S3

Compact e-ink node that takes an 18350 cell, supplied without a battery.

| Name                                          | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :-------------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| Mini ePaper S3       | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

### T5 E-Paper S3 Pro

Large touch e-ink display with 16 grayscale levels. V2 adds a GNSS receiver.

| Name                                                        | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :---------------------------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| T5 E-Paper S3 Pro V2    | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| T5 E-Paper S3 Pro V1    | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

### T-LoRa C6

Compact, low-cost board with an internal PCB antenna.

| Name                                | MCU       | Radio  |     Wi-Fi     |  BT   | GPS |
| :---------------------------------- | :-------- | :----- | :----------: | :---: | :-: |
| T-LoRa C6      | ESP32-C6  | SX1262 | 2.4GHz b/g/n | 5.0\* | NO  |

\* The Meshtastic firmware does not support Bluetooth on ESP32-C6 modules.

### T-Watch

Wearable node with a touch screen, haptics, speaker, and microphone.

| Name                                                          | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :------------------------------------------------------------ | :------- | :----- | :----------: | :-: | :-: |
| T-Watch S3 Plus    | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| T-Watch S3              | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

## HELTEC®

### LoRa 32

Inexpensive basic ESP32-based boards.

| Name                                                                                | MCU         | Radio  |     Wi-Fi     | BT  | GPS |
| :---------------------------------------------------------------------------------- | :---------- | :----- | :----------: | :-: | :-: |
| LoRa32 V4                                  | ESP32-S3R2  | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| LoRa32 V4-R8                            | ESP32-S3R8  | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| LoRa32 V3/3.1                              | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| Wireless Stick Lite V3 | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| Wireless Tracker v1.0            | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| Wireless Tracker v1.1            | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| Wireless Tracker V2                | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| Wireless Paper v1.0                | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| Wireless Paper v1.1                | ESP32-S3FN8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

### Vision Master

Versatile ESP32-S3-based boards E-Ink development boards.

| Name                                                                               | MCU        | Radio  |     Wi-Fi     | BT  | GPS |
| :--------------------------------------------------------------------------------- | :--------- | :----- | :----------: | :-: | :-: |
| Vision Master E213 | ESP32-S3R8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| Vision Master E290 | ESP32-S3R8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| Vision Master T190 | ESP32-S3R8 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

### Mesh Node

| Name                                                            | MCU      | Radio  | Wi-Fi | BT  |   GPS    |
| --------------------------------------------------------------- | :------- | :----- | :--- | :-: | :------: |
| Mesh Node T114 | nRF52840 | SX1262 | NO   | 5.0 | OPTIONAL |
| Mesh Node T096 | nRF52840 | SX1262 | NO   | 5.0 | YES |
| Mesh Node T1 | nRF52840 | SX1262 | NO   | 5.0 | YES |

### MeshPocket

Compact device with QI2 wireless charging and integrated Meshtastic.

| Name                                                     | MCU      | Radio  | Wi-Fi | BT  | GPS |
| :------------------------------------------------------- | :------- | :----- | :--: | :-: | :-: |
| MeshPocket | nRF52840 | SX1262 |  NO  | 5.0 | NO  |

### HT-CT62

Tiny ESP32-C3 + SX1262 surface-mount module for DIY Meshtastic nodes.

| Name                                   | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| HT-CT62   | ESP32-C3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

## Seeed Studio

### SenseCAP

The SenseCAP product line offers a comprehensive range of solutions for both hobbyists and industrial users, featuring the T1000-E card tracker, an IP65-rated, ready-to-go Meshtastic handheld device, the Indicator with a 4-inch touchscreen driven by ESP32-S3 and RP2040 Dual-MCU, and the Solar Node, a solar-powered device designed for long-term outdoor deployment. These devices are designed to be user-friendly, with pre-flashed Meshtastic firmware for easy setup and operation.

| Name                                                          | MCU           | Radio  | Wi-Fi         | BT  | GPS      |
| ------------------------------------------------------------- | ------------- | ------ | ------------ | --- | -------- |
| [Card Tracker T1000-E](SenseCAP%20Card%20Tracker%20T1000-E.md) | nRF52840      | LR1110 | NO           | 5.1 | YES      |
| [SenseCAP Indicator](SenseCAP%20Indicator.md)      | ESP32, RP2040 | SX1262 | 2.4GHz b/g/n | 5.0 | OPTIONAL |
| [SenseCAP Solar Node](Seeed%20SenseCAP%20Solar%20Node.md)    | nRF52840      | SX1262 | NO           | 5.0 | OPTIONAL |
| [MeshTracker X1](SenseCAP%20MeshTracker%20X1.md)     | nRF52840      | LR2021 | NO           | 5.0 | YES      |

### Wio Series

A lineup of development boards and modules for hobbyists and prototyping, with a variety of MCU and sensor options. Most models are intended for integration into custom projects, while the Tracker L1 has a "Pro" variant that is available as a ready-to-go handheld device with a pre-installed case and battery.

| Name                                                                                         | MCU      | Radio      | Wi-Fi | BT  |   GPS    |
| :------------------------------------------------------------------------------------------- | :------- | :--------- | :--: | :-: | :------: |
| [Wio Tracker L1](Seeed%20Wio%20Tracker%20L1.md)                                       | nRF52840 | SX1262     |  NO  | 5.0 |   YES    |
| [XIAO nRF52840 & Wio-SX1262 Kit](Seeed%20Wio-SX1262%20Series.md) | nRF52840 | Wio-SX1262 |  NO  | 5.0 | OPTIONAL |
| [XIAO ESP32-S3 & Wio-SX1262 Kit](Seeed%20Wio-SX1262%20Series.md) | ESP32-S3 | Wio-SX1262 | 2.4GHz b/g/n | 5.0 | OPTIONAL |

## B&Q Consulting

### Nano Series

Portable and durable devices designed for Meshtastic.

| Name                                                       | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :--------------------------------------------------------- | :------- | :----- | :--: | :-: | :-: |
| Nano G2 Ultra | nRF52840 | SX1262 |  NO  | 5.0 | YES |

### Station Series

High power LoRa transceiver designed for Meshtastic licensed ham operation.

| Name                                               | MCU              | Radio  |     Wi-Fi     | BT  |   GPS    |
| :------------------------------------------------- | :--------------- | :----- | :----------: | :-: | :------: |
| Station G2 | ESP32-S3 WROOM-1 | SX1262 | 2.4GHz b/g/n | 5.0 | OPTIONAL |

## Elecrow

### ThinkNode Series

| Name                                                     | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :------------------------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| ThinkNode M1 | nRF52840 | SX1262 |      NO      | 5.0 | YES |
| ThinkNode M2 | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| ThinkNode M3 | nRF52840 | LR1110 |      NO      | 5.0 | YES |
| ThinkNode M4 | nRF52840 | LR1110 |      NO      | 5.4 | YES |
| ThinkNode M5 | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |
| ThinkNode M6 | nRF52840 | SX1262 |      NO      | 5.4 | YES |
| ThinkNode M7 | ESP32-S3 | LR1110 | 2.4GHz b/g/n | 5.0 | NO  |
| ThinkNode M9 | ESP32-S3 | LR1110 | 2.4GHz b/g/n | 5.0 | YES |

### CrowPanel Advance Series

| Name                                                       | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :--------------------------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| CrowPanel 2.4/2.8/3.5/4.3/5.0/7.0" | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |

### [MeshStick](Elecrow%20MeshStick.md)

A USB LoRa radio rather than a node: it supplies the SX1262 transceiver, and a Linux host running meshtasticd supplies everything else. Up to 22 dBm over a CH341 USB-to-SPI bridge, with an SMA antenna connector.

## muzi ᴡᴏʀᴋꜱ

### [R1 Neo](muzi%20%E1%B4%A1%E1%B4%8F%CA%80%E1%B4%8B%EA%9C%B1%20R1%20Neo.md)

Compact and rugged device with built-in GPS, RTC, and buzzer.

| Name                          | MCU      | Radio  | Wi-Fi | BT  | GPS |
| :---------------------------- | :------- | :----- | :--: | :-: | :-: |
| [R1 Neo](muzi%20%E1%B4%A1%E1%B4%8F%CA%80%E1%B4%8B%EA%9C%B1%20R1%20Neo.md) | nRF52840 | SX1262 |  NO  | 5.0 | YES |

### BASE System

Modular development platform with custom core modules and expandable IO.

| Name                                                    | MCU      | Radio  | Wi-Fi | BT  | GPS |
| :------------------------------------------------------ | :------- | :----- | :--: | :-: | :-: |
| Base Uno | nRF52840 | SX1262 |  NO  | 5.0 |  NO |
| Base Duo | nRF52840 | LR1121 |  NO  | 5.0 |  NO |

## M5Stack

Compact, ready-to-use LoRa nodes from M5Stack.

| Name                                       | MCU      | Radio  |     Wi-Fi     | BT  | GPS |
| :----------------------------------------- | :------- | :----- | :----------: | :-: | :-: |
| [Unit C6L](M5Stack%20Unit%20C6L.md)            | ESP32-C6 | SX1262 | 2.4GHz b/g/n | 5.0 | NO  |
| [Cardputer Mesh Kit](M5Stack%20Cardputer%20Mesh%20Kit.md) | ESP32-S3 | SX1262 | 2.4GHz b/g/n | 5.0 | YES |

## Raspberry Pi

### Raspberry Pi Pico

Fast versatile boards using the RP2040.

| Name                                    | MCU    | Radio  |     Wi-Fi     |      BT       | GPS |
| :-------------------------------------- | :----- | :----- | :----------: | :-----------: | :-: |
| Raspberry Pi Pico | RP2040 | SX1262 | 2.4GHz b/g/n | not supported | NO  |

[**Pico Peripherals**](Raspberry%20Pi%20Pico%20Supported%20Peripherals.md)
SSD1306 OLED Display
SH1106 OLED Display
CardKB Keyboard

### Linux

Meshtastic also supports using a MacOS/Linux device as a 'node' through our platform, meshtasticd.
For full information, please see our meshtasticd documentation.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/devices. GPL-3.0 (Meshtastic documentation).*
