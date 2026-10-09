# Drag & Drop nRF52, RP2040, & RP2350 Firmware Updates

## Flash Firmware

> **Info:**
>
> You may now use the Meshtastic Web Flasher to download and copy firmware to your nRF52, RP2040, or RP2350-based devices. Alternatively, follow the instructions below to download and install firmware.

If you have just performed a [Factory Erase](Flash%20nRF52%20RP2040%20RP2350%20Factory%20Erase.md), your device may automatically startup in bootloader mode, and you may skip to "Copy the appropriate firmware..." for your respective device below:

### nRF52

1. Download and unzip the latest firmware from Meshtastic Downloads.
2. Connect your device to your computer with a USB data cable.
3. Put the device into [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md). On most devices, double-press the reset button.
4. Notice a new drive will be mounted on your computer (Windows, Mac, Linux, or Android).
5. Open this drive and you should see three files: `CURRENT.UF2`, `INDEX.HTM`, and `INFO_UF2.TXT`.
6. Copy the appropriate firmware file (`firmware-DEVICE_NAME-X.X.X-xxxxxxx.uf2`) from the release onto this drive.
7. Once the file has finished copying onto the drive, the device will reboot and install the Meshtastic firmware.

### RP2040
1. Download and unzip the latest firmware from Meshtastic Downloads.
2. Press the BOOTSEL button and while keeping it pressed, connect the device to your computer via a USB cable.
3. Notice a new drive will be mounted on your computer (Windows, Mac, Linux, or Android).
4. Open this drive and you should see two files: `INDEX.HTM` and `INFO_UF2.TXT`.
5. Copy the appropriate firmware file (`firmware-DEVICE_NAME-X.X.X-xxxxxxx.uf2`) from the release onto this drive.
6. Once the file has finished copying onto the drive, the device will reboot and install the Meshtastic firmware.

## Connect and Configure Device

After flashing the Meshtastic firmware to the device, you can proceed with the initial configuration.

  
    Connect and Configure Device
  

### Potential Flashing Edge Cases

> **Info:**
>
>
> Before flashing confirm that you have RAK4631 and not a RAK4631-R If this is not the case, fear not. The hardware is identical but requires [changing the bootloader](Convert%20RAK4631-R%20to%20RAK4631.md).
>

> **Info:**
>
>
> Previous versions of the Meshtastic firmware may save stale data, causing devices to get stuck in a crash loop during startup. If you experience issues when upgrading your nRF52 device from a previous version of Meshtastic, you may need to perform a full factory reset of the internal flash memory.
>
> Follow the guide to [factory erase your nRF52](Flash%20nRF52%20RP2040%20RP2350%20Factory%20Erase.md) device before continuing to flash firmware.
>

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/drag-n-drop. GPL-3.0 (Meshtastic documentation).*
