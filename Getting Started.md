# Getting Started

## How Meshtastic Works

Meshtastic creates a mesh network where devices communicate using LoRa radio. Connect your phone or computer to a radio via Bluetooth, Wi-Fi, or USB — and communicate with others across vast distances without any internet or cell service.

## Supported Hardware

Before you begin, it's important to determine which kind of hardware you're using. Meshtastic works closely with our Partners and Backers who produce officially supported hardware. These devices are tested, documented, and recommended for the best Meshtastic experience. 

There is also a wide range of community supported hardware available; however, these devices are not officially supported by Meshtastic. Please reach out to the community via Discord for assistance.

Below you'll find examples of supported hardware organized by MCU type. Once you've identified your device, we'll walk you through verifying your data cable, flashing the firmware, and connecting and configuring your device.

## ESP32

The ESP32 chip is equipped with both Wi-Fi and Bluetooth, making it ideal for devices that need web interface access or Wi-Fi-based configuration. ESP32-S3 variants offer improved performance.

### Partner Hardware

#### Seeed Studio

[SenseCAP Indicator](SenseCAP%20Indicator.md) — 4" touchscreen driven by ESP32-S3 and RP2040 Dual-MCU

#### RAK Wireless

[RAK3312 Core module](RAK%20WisBlock%20Core%20Modules.md) — ESP32-S3-based WisBlock modular core

#### Elecrow

ThinkNode M2 — Portable ESP32-S3 device built for outdoor use

#### HELTEC®

LoRa32 V4 — ESP32-S3 board with built-in 0.96 inch OLED display

#### LILYGO®

T-Deck / T-Deck Plus / T-Deck Pro — Standalone devices with screen and keyboard

### Backer Hardware

#### B&Q Consulting

Station G2 — High power LoRa transceiver for licensed ham operation

#### M5Stack

[Cardputer Mesh Kit](M5Stack%20Cardputer%20Mesh%20Kit.md) — Pocket messaging terminal with keyboard, LoRa cap, and GNSS

## nRF52

The nRF52 chip is much more power efficient than the ESP32 chip and easier to update via UF2 bootloader, but is only equipped with Bluetooth (no Wi-Fi). Ideal for battery-powered and solar deployments.

### Partner Hardware

#### Seeed Studio

[Card Tracker T1000-E](SenseCAP%20Card%20Tracker%20T1000-E.md) — IP65-rated card-sized tracker with GPS

#### RAK Wireless

[WisMesh Tag](RAK%20WisMesh%20Tag.md) — Portable location tracker with IP66 rating

#### Elecrow

ThinkNode M3 — nRF52840 with LR1110 radio and GPS

#### HELTEC®

Mesh Node T096 — Ultra-low-power nRF52840 node with color TFT display and GNSS

#### LILYGO®

T-Echo — All-in-one unit with E-Ink screen, GPS, and battery in injection-molded case

### Backer Hardware

#### muzi ᴡᴏʀᴋꜱ

[R1 Neo](muzi%20%E1%B4%A1%E1%B4%8F%CA%80%E1%B4%8B%EA%9C%B1%20R1%20Neo.md) — Custom-designed nRF52840 device with GPS

## RP2040/RP2350

The RP2040 and RP2350 are dual-core chips developed by Raspberry Pi. Cost-effective options for DIY projects.

### Partner Hardware

#### RAK Wireless

- [RAK11310 Core module](RAK%20WisBlock%20Core%20Modules.md) — RP2040-based WisBlock modular core with SX1262

### Community Supported

- Raspberry Pi Pico + Waveshare LoRa Module (Note: **Bluetooth on the Pico W is not yet supported by Meshtastic**)

## STM32

The STM32WL from STMicroelectronics puts an Arm Cortex-M4 and a Semtech SX126x radio on one chip &mdash; the lowest part count and power draw of any Meshtastic target, with no Wi-Fi or Bluetooth.

Due to low flash memory and RAM, a number of features have been excluded from STM32WL firmware by default (specific variants may re-enable specific features).

  Features excluded from STM32WL firmware by default

- ATAK/TAK forwarding
- Codec2 audio
- MQTT
- Remote Hardware module
- Waypoints
- On-device display and menu UI
- Input peripherals (rotary encoders, trackballs, buttons/keyboards) and buzzer
- Power monitoring and power-metrics telemetry
- Timezone database
- RTTTL ringtones
- Signed-packet authenticity policy

### Community Supported

- RAK3172/RAK3372 Core module — STM32WLE5 WisBlock module for embedding into custom hardware
- [Seeed Wio-E5](Seeed%20Wio-E5.md) — STM32WLE5 wireless module, mini dev board, and dev kit
- [STMicroelectronics Nucleo-WL55JC](STMicroelectronics%20Nucleo-WL55JC.md) — Official STM32WL evaluation board with onboard ST-LINK

> **Info:**
>
>
> If your device is not listed above, please review our supported devices to determine which MCU your device has or contact us in Discord with any questions.
>

## Verify Data Cable

> **STOP! Put The Power Cable Down!:**
>
>
> Never power on the radio without attaching an antenna as doing so could damage the radio chip!
>

Prior to connecting your Meshtastic device to the computer, you should perform the following basic checks.

Some cables only provide _charging_, verify that your cable is also capable of _transferring data_ before proceeding. To check if your cable can also transfer data, try connecting it to another device (like a phone) and see if you can copy a file to or from it. If the file transfer works, then your cable is also able to transfer data and you can continue.

## Install Serial Drivers

> **Caution:**
>
>
> nRF52/RP2040/RP2350 devices typically do not require serial drivers. They use the UF2 bootloader which makes the devices appear as flash drives.  Do _NOT_ download the USB device drivers unless required to install UF2 support.
>

If you require serial drivers installed on your computer, please choose one of the options below and install it before continuing.

  
    
      
        Install ESP32 Drivers
      
    

  
      
        Install nRF52/RP2040/RP2350 Drivers
      
    
  

## Flash Firmware

After completing the previous steps, you can now flash the Meshtastic firmware onto your device. To proceed, select the appropriate device type for your device.

  
    
      
        Flash ESP32 Firmware
      
    

    
      
        Flash nRF52/RP2040/RP2350 Firmware
      
    

    
      
        Flash STM32 Firmware
      
    
  

## Connect and Configure Device

After flashing the Meshtastic firmware onto your device, you can now move on to initial configuration.

  
    Connect and Configure Device

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started. GPL-3.0 (Meshtastic documentation).*
