# SenseCAP MeshTracker X1

The SenseCAP MeshTracker X1 is a card-sized IP66-rated tracker for Meshtastic, built on the Nordic nRF52840 and a Semtech LR2021 transceiver. Dual-band GNSS and a five-day battery suit it to asset tracking and field use, and it has no screen.

## Specifications

- **MCU**
  - Nordic nRF52840 (Bluetooth 5.0 LE)
- **LoRa Transceiver**
  - Semtech LR2021
- **Frequency options**
  - 863 - 928 MHz
- **Navigation Module**
  - Dual-band GNSS
- **Battery Capacity**
  - Rechargeable lithium battery, 1100 mAh
- **Connectors**
  - USB-C

## Features

- Up to five days of battery life.
- IP66-rated enclosure.
- Vibration motor for alerts.
- Barometric pressure sensor.
- User button and RGB status LED. There's no reset button.
- No screen, so the device is configured from a client.

## Flashing

The MeshTracker X1 has one button and no reset button, so the double-press that reaches bootloader mode on most nRF52 devices doesn't apply. This needs the Meshtastic OTAFIX bootloader 2.5 or later.

1. Connect the device to your computer with a USB data cable.
2. Press and hold the button to power the device on, and keep holding it for 3 seconds.
3. The device mounts as a USB drive a few seconds later.
4. Copy the firmware `.uf2` file onto the drive, as described in [Drag & Drop](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md).

To leave bootloader mode without flashing, eject the drive.

On an earlier bootloader, or to skip the button entirely, connect the device over USB and run `meshtastic --enter-dfu`. [Entering bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md) covers every method.

## Resources

- Firmware file: `firmware-seeed_mesh_tracker_X1-X.X.X.xxxxxxx.uf2`
- Purchase Links:
  - International
    - Seeed Studio Online Store

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/seeed-studio/sensecap/meshtracker-x1. GPL-3.0 (Meshtastic documentation).*
