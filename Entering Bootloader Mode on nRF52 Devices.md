# Entering Bootloader Mode on nRF52 Devices

Every nRF52 device runs a small program called the bootloader before the firmware starts. In bootloader mode, also called DFU mode, the device mounts on your computer as a USB drive and installs whatever `.uf2` file is copied onto it. [Drag & Drop](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md), [Factory Erase](Flash%20nRF52%20RP2040%20RP2350%20Factory%20Erase.md), and [Update nRF52 Bootloader](How%20to%20Update%20or%20Recover%20the%20Bootloader%20on%20nRF52%20Devices%20to%20the%20Latest%20Version.md) all start here. The methods are ordered most convenient first.

## Reset button

Most nRF52 devices enter bootloader mode when you double-press the reset button within about half a second. Press the reset button once to leave it without flashing.

## Meshtastic client

Once Meshtastic firmware is installed, the device can be rebooted into bootloader mode from a client without touching a button. Connect the device over USB and run:

```shell
meshtastic --enter-dfu
```

The device reboots into bootloader mode and mounts the drive. The Android client's [USB File Transfer](Firmware%20Updates.md) option does the same over a USB connection.

## Devices with a single button

The SenseCAP Card Tracker T1000-E and SenseCAP MeshTracker X1 have one button and no reset button, so the double-press doesn't apply. On the Meshtastic OTAFIX bootloader 2.5 or later, connect the USB cable, then hold the button while the device starts and keep holding it for 3 seconds. The drive appears a few seconds later. A short press while the device starts, or a hold while the firmware is running, doesn't reach the bootloader. The steps are on each device page: [Card Tracker T1000-E](SenseCAP%20Card%20Tracker%20T1000-E.md) and [MeshTracker X1](SenseCAP%20MeshTracker%20X1.md).

To leave bootloader mode without flashing, eject the drive. Unplugging doesn't leave bootloader mode: the device stays in it on battery, and plugging it back in only mounts the drive again.

A T1000-E on an OTAFIX bootloader before 2.5 has no button path into the bootloader, and ejecting the drive doesn't leave it, so use the Meshtastic client method and copy a firmware file to get out.

## Checking your bootloader version

`INFO_UF2.TXT` on the mounted drive names the bootloader version, and from OTAFIX 2.4 on carries a `Factory-Erase:` line. [Update nRF52 Bootloader](How%20to%20Update%20or%20Recover%20the%20Bootloader%20on%20nRF52%20Devices%20to%20the%20Latest%20Version.md) covers moving to a newer one.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/entering-bootloader-mode. GPL-3.0 (Meshtastic documentation).*
