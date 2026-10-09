# How to Update or Recover the Bootloader on nRF52 Devices to the Latest Version

If you're experiencing issues with updating or flashing newer versions of the Meshtastic firmware, and your nRF52 device is not running the latest bootloader version, updating the bootloader may resolve these problems.

To check which version of the bootloader your device is running, put the device into [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md). Then, open the mounted drive that appears on your computer and check the `INFO_UF2.TXT` file.

> **Info:**
>
>
> Many nRF52-based Meshtastic devices ship with, or can be upgraded to, Meshtastic's OTAFIX bootloader — a fork with faster, more reliable Bluetooth OTA updates. Its releases page lists current UF2/zip packages per board, and its README lists which boards it supports.
>

## Updating bootloader

Below are the steps to update your bootloader.

### Method 1: From the Meshtastic Android App (Easiest, if supported)

For boards OTAFIX supports, the Meshtastic Android app can flash the bootloader directly — no manual download needed. This in-app path is Android-only for now; the iOS/iPadOS app does not yet offer a bootloader upgrade, so use one of the manual methods below on Apple platforms.

1. Connect the radio over **USB/serial** (not Bluetooth).
2. Open the connected radio's configuration and go to **Advanced → Firmware Update**.
3. If an upgraded bootloader is published for your board, select **Upgrade bootloader**.
4. The app reads `INFO_UF2.TXT` from the update drive to confirm the board, then writes the bootloader image. It then asks you to select the update drive again to write the firmware image — two drive selections in total.

See the app's Firmware Updates guide for the full flow. If your board isn't listed yet, or you're not on Android, use one of the manual methods below.

### Method 2: Using the UF2 File

Depending on your device, you need to select the correct bootloader package. Below are the links to the bootloader packages:

- Lilygo T-Echo
- RAK4631
- Seeed Tracker 1000-E
- Generic Meshtastic 6.1.1 for DIY
- Generic Meshtastic 7.3.0 for DIY

1. Download the correct UF2 Bootloader File.
2. Connect your device to your computer via USB.
3. Put the device into [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md). On most devices, double-press the reset button. A T1000-E still on the bootloader Seeed ships uses the gesture in Seeed's T1000-E guide: hold the button, then connect the charging cable twice in quick succession. The device should appear as a removable drive on your computer.
4. Drag and drop the UF2 file you downloaded into the removable drive. The device will automatically update the bootloader and reset.
5. Once the device resets, the update is complete. Your device is now running the latest bootloader version and you can proceed with [flashing the firmware](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md).

### Method 3: Using adafruit-nrfutil

> **Warning:**
>
>
> Unlike uf2 uploads, adafruit-nrfutil does not check if you have the correct bootloader package for your device. If you flash the wrong bootloader, you may brick your device. Please verify the SHA256 checksum before flashing.
>

> **Info:**
>
>
> These instructions assume you have python and pip already installed. If you do not, please install the latest version of python (which includes pip) from Python.org.
>

Depending on your device, you need to select the correct bootloader package. Below are the links to the bootloader packages:

- Lilygo T-Echo SHA256: 85d8a334bbf82802d712e183f29ec5215f06786ca88914687c437aceab75d9cf
- RAK4631 SHA256: df99fee1ceb4ec77c171ec5d2529c604cd0cce891f51c15de8a32825a8a3f8c7
- Seeed Tracker 1000-E SHA256: 8c69f0d43a7aac925055451d7262682d6926d4cfb7ea8240b466dc8f16a692ba
- Generic Meshtastic 6.1.1 for DIY SHA256: ecebecea849ab79d09517dd4f6ff98de5647fe275b0b4d525501e6c29cb5a586
- Generic Meshtastic 7.3.0 for DIY SHA256: 9a38edf4e974a6f705c41b296499a4fc57682ec9bb686eecd9f3d8d02fc6ffcf

1. Open a terminal or command prompt and install adafruit-nrfutil by running:

```bash
pip install adafruit-nrfutil
```

2. Obtain the correct zip package.
3. Connect your device to your computer via USB.
4. In the terminal or command prompt, navigate to the directory where you downloaded the bootloader zip package and execute the following command, replacing /dev/ttyACM0 with the correct port for your device (Windows users might use COMx):

```bash
adafruit-nrfutil --singlebank --touch 1200 --verbose dfu serial --package <downloaded file>.zip -p /dev/ttyACM0 -b 115200
```

5. Once the process finishes, the update is complete. Your device is now running the latest bootloader version and you can proceed with [flashing the firmware](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md).

On OTAFIX 2.0 or later, flashing the bootloader package this way clears the bootloader's record of the installed firmware, so the device comes back waiting for a Bluetooth OTA update rather than starting the firmware: no USB drive and no serial port appear. That is expected, not a failure. Put the device into [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md) for the UF2 drive and copy the firmware across, or complete a [Bluetooth OTA update](nRF52%20OTA%20Firmware%20Updates.md).

### Method 4: Using a Debugger

If the above methods do not work and if the hardware supports it (i.e., has the required SWD pins), a debugger like a DAPLink or J-Link can be used to flash the bootloader directly. Refer to the [Debugger Instructions](Convert%20RAK4631-R%20to%20RAK4631.md) for an example with the RAK4631.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/update-nrf52-bootloader. GPL-3.0 (Meshtastic documentation).*
