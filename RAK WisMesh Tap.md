# RAK WisMesh Tap

**WisMesh Tap**

## WisMesh Tap

The WisMesh TAP is a Meshtastic device equipped with a touch screen featuring an on-screen keyboard that's built on the WisBlock RAK19007 Base Board and RAK4631 nRF52 core module in an IP65-rated enclosure. This makes it perfect for reliable off-grid communication during activities like exploring, hiking, or testing other remotely deployed devices, all without needing a phone.

- **Base Board**
  - [RAK19007](RAK%20WisBlock%20Base%20Boards.md)
- **MCU**
  - [RAK4631 (nRF52840)](RAK%20WisBlock%20Core%20Modules.md)
    - Bluetooth BLE 5.0
    - Very low power consumption
- **LoRa Transceiver:**
  - SX1262
- **Frequency Options:**
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - USB-C
  - SMA

### Features

- 320 x 240 TFT touch screen
- 3200 mAh rechargeable battery
- GNSS location module onboard ([RAK12500](RAK%20WisBlock%20Supported%20Peripherals.md))
- External RAK Blade 2.3 dBi LoRa antenna
- Internal bluetooth antenna
- Versatile- use as a portable handheld or pick a mounting solution

### Resources

- Firmware file: `firmware-rak_wismeshtap-X.X.X.xxxxxxx.uf2`
- Further information on the WisMesh TAP can be found on the RAK Documentation Center.
- Purchase Links:
  - US
    - Rokland - US915 Mhz
  - International
    - RAKwireless Store
    - RAKwireless AliExpress

**WisMesh Tap V2**

## WisMesh Tap V2

The WisMesh Tap V2 is the ESP32-S3 successor to the WisMesh Tap, built on the RAK3312 WisBlock Core module. It keeps the 320 x 240 TFT touchscreen and on-screen keyboard of the original while adding support for the Meshtastic UI (MUI), an SD-card map function, a buzzer, and an onboard accelerometer for a fully standalone, phone-free experience.

- **MCU**
  - [RAK3312 (ESP32-S3)](RAK%20WisBlock%20Core%20Modules.md)
    - 2.4GHz Wi-Fi b/g/n
    - Bluetooth BLE
- **LoRa Transceiver:**
  - Semtech SX1262
- **Frequency Options:**
  - 868 MHz
  - 915 MHz
- **Connectors:**
  - USB-C
  - SMA

### Features

- 320 x 240 TFT touch screen with on-screen keyboard
- Meshtastic UI (MUI) support
- microSD card slot (used for the MUI map function)
- Buzzer for incoming-message notifications
- Onboard GNSS location module and 3-axis accelerometer
- 3200 mAh rechargeable battery
- IP65-rated enclosure

### Resources

- Firmware file: `firmware-rak_wismesh_tap_v2-X.X.X.xxxxxxx.bin`
- Further information on the WisMesh Tap V2 can be found on the RAK Documentation Center.
- Purchase Links:
  - International
    - RAKwireless Store

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wismesh/tap. GPL-3.0 (Meshtastic documentation).*
