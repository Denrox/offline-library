# LILYGO® TTGO T-Beam Devices (tbeam)

All T-beam models (with the exception of the S3-Core) have an 18650 size battery holder on the rear of the device. This is designed to the original specification of the 18650 and only fits unprotected flat top 18650 cells. Button top and protected cells are typically longer than 65mm, often approaching 70mm.

Further information on the LILYGO® T-Beam devices can be found on LILYGO®'s GitHub page.

**S3-Core**

## T-Beam S3 Core

- **MCU**
- ESP32-S3 (Wi-Fi & Bluetooth 5LE)
- **LoRa Transceiver**
  - **Semtech SX1262** (improved performance)
- **Frequency options**
  - 433 MHz
  - 868 MHz
  - 915 MHz
- **Navigation Module**
  - **NEO-M10S - GNSS receiver (supports GPS, GLONASS, Galileo, BeiDou)** (better GPS sensitivity)
  - **Quectel L76K - (supports GPS, Beidou, GLONASS)** (lower price)
- **Connectors**
  - USB-C
  - Antenna: U.FL antenna connector

### Features

- SoftRF preinstalled (flashing to Meshtastic required)
- Boot and Reset switches
- Can be used standalone without 'Supreme' daughterboard in a headless configuration

### Resources

- Firmware file: `firmware-tbeam-s3-core-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - International
    - LilyGO Store

**Supreme**

## T-Beam Supreme

- **MCU**
- ESP32-S3 (Wi-Fi & Bluetooth 5LE)
- **LoRa Transceiver**
  - **Semtech SX1262** (improved performance)
- **Frequency options**
  - 433 MHz
  - 868 MHz
  - 915 MHz
- **Navigation Module**
  - **NEO-M10S - GNSS receiver (supports GPS, GLONASS, Galileo, BeiDou)** (better GPS sensitivity)
  - **Quectel L76K - (supports GPS, Beidou, GLONASS)** (lower price)
- **Connectors**
  - USB-C
  - Antenna: U.FL antenna connector

### Features

- Includes T-Beam S3-Core Module
- SoftRF preinstalled (flashing to Meshtastic required)
- Power, Boot and Reset switches
- 1.3" OLED included
- BME280 Air pressure sensor
- QMI8658 IMU
- QMC6310 Magnetometer
- PCF8563 RTC
- Micro-SD reader (not implemented in Meshtastic)

### Flashing

To flash ESP32-S3 devices like the T-Beam Supreme, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this. If this method does not work for any reason, you can follow the manual process below.

> **Warning:**
>
>
> Do not proceed unless an antenna is connected to avoid possible damage to the device's radio.
>

The following process will manually place the device into the Espressif Firmware Download mode:

1. Unplug the device.
2. Press and hold the BOOT button.
3. Plug device in.
4. After 2-3 seconds, release the BOOT button.

With the device now in the Espressif Firmware Download mode, you can proceed with flashing using one of the supported flashing methods. It's generally recommended to use the Web Flasher. You can select "Tbeam S3 Core from the device drop-down.

### Resources

- Firmware file: `firmware-tbeam-s3-core-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - International
    - LilyGO Store
  - US
    - Rokland NEO-M10S
    - Rokland Quectel L76K

**T-Beam 1W**

## T-Beam 1W

The T-Beam 1W is a high-power ESP32-S3 LoRa board with a 1-watt (up to 32 dBm) SX1262 front end, multi-constellation GNSS, and an onboard cooling fan for sustained high-power transmit.

- **MCU**
  - ESP32-S3FN8 (Wi-Fi & Bluetooth 5 LE)
    - 16 MB flash
    - 8 MB PSRAM
- **LoRa Transceiver**
  - Semtech SX1262 with 1W power amplifier (up to 32 dBm)
- **Frequency options**
  - 868 MHz
  - 915 MHz
- **Navigation Module**
  - L76K GNSS (supports GPS, BeiDou, GLONASS, QZSS)
- **Connectors**
  - USB-C
  - Antenna connector for LoRa

### Features

- 1.3-inch SH1106 OLED display (128 x 64).
- AXP2101 power management.
- Onboard cooling fan for high-power RF transmit.
- L76K multi-constellation GNSS.

> **Warning:**
>
>
> The 1W RF stage requires a stable power supply, and the board does not charge a connected 7.4 V battery pack. Always connect an antenna before transmitting to avoid damaging the radio.
>

### Flashing

To flash ESP32-S3 devices like the T-Beam 1W, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this.

### Resources

- Firmware file: `firmware-t-beam-1w-X.X.X.xxxxxxx.bin`
- Purchase Links:
  - International
    - LilyGO Store

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/lilygo/tbeam/tbeam. GPL-3.0 (Meshtastic documentation).*
