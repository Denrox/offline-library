# Flash nRF52/RP2040/RP2350 Factory Erase

Meshtastic uses the littlefs library to store configuration, logs, and other data in the internal flash of nRF52, RP2040, & RP2350 devices. Updating the firmware does _not_ erase this additional data, which can cause issues when the format and location of data changes between releases.

> **Info:**
>
> You may now use the Meshtastic Web Flasher to Factory Erase your nRF52, RP2040, or RP2350-based devices. Visit the flasher, select your board, and click the trash can icon to the right of the Flash button. This will open a dialogue to begin the erase procedure.
>
> Alternatively, follow the instructions below.

### nRF52

Every nRF52 device runs a small program called the bootloader before Meshtastic itself starts. It is what shows up as a USB drive in [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md), and it installs whatever `.uf2` file you copy onto that drive. Newer Meshtastic bootloaders can factory erase the device by themselves; older ones need a separate erase firmware. The steps below start the same way and then branch depending on which bootloader your device has.

To reset the flash storage on your nRF52 board:

1. Download and unzip the latest firmware from Meshtastic Downloads.
2. Connect your device to your computer with a USB data cable.
3. Put the device into [bootloader mode](Entering%20Bootloader%20Mode%20on%20nRF52%20Devices.md). On most devices, double-press the reset button.
4. Notice a new drive will be mounted on your computer (Windows, Mac, or Linux)
5. Open this drive and you should see three files: `CURRENT.UF2`, `INDEX.HTM`, and `INFO_UF2.TXT`
6. Open the `INFO_UF2.TXT` file with a text editor. If it contains a line starting with `Factory-Erase:`, continue with Bootloader factory erase. If there is no such line, continue with Older bootloaders.

#### Bootloader factory erase

1. Download meshtastic_factory_erase.uf2 (attached to every Meshtastic nRF52 bootloader release from OTAFIX 2.4 on). One file works for every nRF52 board, so there is no SoftDevice version to match.
2. Copy it onto the drive.
3. About half a second after the copy finishes, the drive disappears. A couple of seconds later it comes back. That is the erase done: no serial connection or command line is needed. (If you eject the drive instead, the device resets immediately.)
4. Either copy the firmware `.uf2` for your device from the firmware you unzipped at the start onto the drive, or just unplug the device. The firmware that was already installed is kept and starts as if the device were brand new.

The erase clears everything Meshtastic stores on the device: its settings, its encryption keys, its Bluetooth pairings, and its node database (the list of other Meshtastic devices, or nodes, it has heard from). The bootloader and the installed firmware are left untouched.

#### Older bootloaders

Bootloaders without a `Factory-Erase:` line in `INFO_UF2.TXT`, which includes every bootloader before OTAFIX 2.4 and the stock bootloaders many boards ship with, silently ignore `meshtastic_factory_erase.uf2`. Use the erase firmware included with each Meshtastic release instead:

1. In `INFO_UF2.TXT`, note the `SoftDevice` value (the version of the device's built-in Bluetooth software).
2. Find the file included in the downloaded firmware matching your softdevice major version number (7.x.x or 6.x.x). Either use `Meshtastic_nRF52_factory_erase_v3_S140_7.3.0.uf2` or `Meshtastic_nRF52_factory_erase_v3_S140_6.1.0.uf2` and copy it onto the new drive. The device should reboot.
3. With the [Meshtastic CLI](Meshtastic%20Python%20CLI%20Guide.md) installed, open your Terminal/Console and enter the command: `meshtastic --noproto`.
4. You should see the message: `Formatting... Done`.

> **Warning:**
>
> The erase file must match your SoftDevice version: the wrong one can overwrite part of the SoftDevice and leave the device needing a hardware programmer to recover. If you copied `meshtastic_factory_erase.uf2` and nothing happened, your bootloader does not support it yet: use the preceding steps, or [update the bootloader](How%20to%20Update%20or%20Recover%20the%20Bootloader%20on%20nRF52%20Devices%20to%20the%20Latest%20Version.md) first and check `INFO_UF2.TXT` again.

Once the device has been erased, you can proceed to install the latest Meshtastic firmware on a clean storage filesystem by clicking the link below.

### RP2040

To reset the flash storage on your RP2040 board:

1. Download flash_nuke.uf2 to your computer.
2. Press the BOOTSEL button and while keeping it pressed, connect it to your computer via a USB cable.
3. The board should now appear as a mass storage device on your computer with the label RPI-RP2.
4. Copy the flash_nuke.uf2 file to the device.
5. The board will now restart and the flash memory will be erased.

Once the device has been erased, you can proceed to install the latest Meshtastic firmware on a clean storage filesystem by clicking the link below.

  
    Flash nRF52/RP2040/RP2350 Firmware

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/nrf52-erase. GPL-3.0 (Meshtastic documentation).*
