# LILYGO® TTGO Lora Devices (lora)

Further information on the LILYGO® LoRa devices can be found on LILYGO®'s GitHub page.

**Lora T3S3**

## Lora T3S3 v1.0, v1.1 and v1.2

- **MCU**
  - ESP32-S3 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX1262
  - Semtech SX1276
  - Semtech LR1121 (Sub-GHz and LORA_24 dual band)
  - Semtech SX1280 with PA (Region LORA_24 worldwide use)
- **Frequency options**
  - 868 MHz
  - 915 MHz
  - 2.4 GHz
- **Connectors**
  - USB-C
  - Antenna: SMA antenna connector

### Features

- Built in 0.96 inch OLED display
- Power and Reset switches, Boot / User Button
- microSD connector
- No GPS

### Flashing the T3S3

To flash ESP32-S3 devices like the T3S3, you typically need to place them in Espressif's firmware download mode. Use the "1200bps reset" button in the web flasher to do this. If this method does not work for any reason, you can follow the manual process below.

> **Warning:**
>
>
> Do not proceed unless an antenna is connected to avoid possible damage to the device's radio.
>

The following process will manually place the device into the Espressif Firmware Download mode:

1. Switch off the device.
2. Connect the USB-C data cable to the device. A blue LED will illuminate while display stays black.
3. Press and hold the BOOT button to the right of the display.
4. Switch the device on.
5. After 2-3 seconds, release the BOOT button.

With the device now in the Espressif Firmware Download mode, you can proceed with flashing using one of the supported flashing methods. It's generally recommended to use the Web Flasher. You can select "Tlora T3s3 V1" from the device drop-down.

> **Note:**
>
>
> If after successfully flashing the device and the screen remains black, you may need to use the [CLI Script](Flashing%20with%20the%20CLI.md) to flash Meshtastic.
>

### Resources

- Firmware file: `firmware-tlora-t3s3-v1.xxxxxxx.bin`
- Purchase Links:
  - International
    - Lilygo

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/lilygo/lora/lora. GPL-3.0 (Meshtastic documentation).*
