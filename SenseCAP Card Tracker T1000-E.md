# SenseCAP Card Tracker T1000-E

SenseCAP T1000-E is a high-performance tracker designed for Meshtastic. As small as a credit card, effortlessly fitting in your pocket or attaching to your assets. It embeds Semtech's LR1110, Nordic's nRF52840, and Mediatek's AG3335 GPS module, providing Meshtastic users with a high-precision, low-power positioning and communication solution.

> **[Note]:**
>
> Currently, LR1110 radios are unable to receive Meshtastic packets from the older SX127x radios, it requires a breaking change to fix this. Transmitting works and when hopping through an SX126x radio, you can still receive packets from SX127x radios.

### Specifications

- **MCU**
  - Nordic nRF52840 (supports Bluetooth)
- **LoRa Transceiver**
  - Semtech LR1110
- **Frequency options**
  - 865-928 MHz
- **Navigation Module**
  - Mediatek AG3335 GPS chip
- **Battery Capacity**
  - Rechargeable lithium battery, 700mAh
- **Charging**
  - USB magnetic charging cable

### Features

- **Button and Buzzer**: For user interaction and alerts.
- **Pogo Pins**: Four pins for USB, DFU, serial logging, and charging.
- **Rugged Build**: IP65 rated, waterproof and durable for various environments.

### Functionality

- **User/Program Button (face):**
  - **Long press:** Will signal the device to shutdown after 5 seconds.
  - **Double press:** Sends an adhoc ping of the device's position to the network.
  - **Triple press:** Enables/Disables the GPS Module on demand.
  - **Quadruple press:** Temporarily mute or unmute device.
  - **Hold while the device starts:** Enters bootloader mode for a firmware update. See Flashing.

### Flashing

The T1000-E has one button and no reset button, so the double-press that reaches bootloader mode on most nRF52 devices doesn't apply. This needs the Meshtastic OTAFIX bootloader 2.5 or later.

1. Connect the device to your computer with a USB data cable.
2. Press and hold the button to power the device on, and keep holding it for 3 seconds.
3. The device mounts as a USB drive a few seconds later.
4. Copy the firmware `.uf2` file onto the drive, as described in [Drag & Drop](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md).

To leave bootloader mode without flashing, eject the drive.

On the bootloader Seeed ships, the button doesn't reach bootloader mode. Follow Seeed's T1000-E guide to enter it, or [update the bootloader](How%20to%20Update%20or%20Recover%20the%20Bootloader%20on%20nRF52%20Devices%20to%20the%20Latest%20Version.md) first. To skip the button entirely on any bootloader, connect the device over USB and run `meshtastic --enter-dfu`. [Entering bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md) covers every method.

### Resources

- Firmware file: `firmware-tracker-t1000-e-X.X.X.xxxxxxx.uf2`
- Purchase Links:
  - International:
    - Seeed Studio Online Store
    - Seeed Studio Aliexpress Official Store
    - Seeed Studio Amazon Official Store
- User Guide

#### Images

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/seeed-studio/sensecap/card-tracker. GPL-3.0 (Meshtastic documentation).*
