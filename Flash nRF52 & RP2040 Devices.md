# Flash nRF52 & RP2040 Devices

## Flashing Methods for nRF52, RP2040, and RP2350 Devices

nRF52, RP2040, and RP2350 based devices have the easiest firmware upgrade process. No driver or software install is required on any platform.

### Drag & Drop
nRF52, RP2040, and RP2350 devices use the [Drag & Drop](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md) installation method to install firmware releases.

### Over-The-Air (OTA)
nRF52 devices are able to accept [OTA firmware updates](nRF52%20OTA%20Firmware%20Updates.md) from a mobile device over bluetooth.

### nRF Factory Erase
You may wish to perform a [Factory Erase](Flash%20nRF52%20RP2040%20RP2350%20Factory%20Erase.md) prior to installing firmware to clear data that may change format and location between releases.

### Convert RAK4631-R to RAK4631
If your device did not come with the Arduino bootloader you will need to [perform the conversion](Convert%20RAK4631-R%20to%20RAK4631.md).

### Use Raspberry Pi as a SWDIO Flash Tool
If your device can't be flashed through USB or Bluetooth, another option might be a [direct SWDIO connection](SWDIO%20using%20a%20Raspberry%20Pi.md).

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/flashing-nrf52-devices. GPL-3.0 (Meshtastic documentation).*
