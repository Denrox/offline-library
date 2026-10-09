# HELTEC® Plug&Play Sensors

**Capsule V3.0**

## Heltec Capsule Sensor Rev. 3.0

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
  - Magnetic suction interface
  - Antenna:
    - Dedicated 2.4 GHz SMT antenna for Wi-Fi/Bluetooth
    - Dedicated SMT antenna for LoRa

### How to upload firmware

> **Info:**
>
> Capsule Sensor V3 uses WirelessBoot mode to upload firmware, exchange information, and print logs through Wi-Fi.
> That is, whether you update the firmware locally or via the Web, You need to get the device into WirelessBoot state first.

Refer to this link for how to upload firmware for Capsule Sensor V3: **Wireless Boot**.

### Touch button/Physical button differences

> **Warning:**
>
> Because the touch button is easy to accidentally activate while close to metal or in your pocket, Heltec has discontinued production of this version. However, a small number of samples have entered the market.

- Button differences
  
- Other hardware differences
  1. Removal of FDG6322C (a dual N & P channel FET) from the physical-button version.
  2. Antenna filter values physical-button version (L11 = 1.8pF, C15 = 2.7nH, C24 = 1.8pF) align more closely with ESP32-S3 reference design than touch-button version (L11 = 1.6nH, C15 = 6.9pF, C24 = 2.4pF).

### Features

- Meshtastic preinstalled.
- Built-in battery.
- Sensor replaceable.

### Pin

- Connector:
  - Model name: DF12NB(3.0)-10DS-0.5V(51)
  - Pin:
    
- More pin definitions please refer Schematic Diagram

### Resources

- Firmware file: `firmware-heltec_capsule_sensor_v3-X.X.X.xxxxxx.bin`
- Purchase links
  - International
    - Heltec
    - AliExpress

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/community-supported/heltec-automation/sensor/heltec-sensors. GPL-3.0 (Meshtastic documentation).*
