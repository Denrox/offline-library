# nRF52/RP2040/RP2350 Serial Drivers

## Install nRF52/RP2040/RP2350 USB to Serial Drivers

> **Caution:**
>
>
> nRF52/RP2040/RP2350 devices typically do not require serial drivers. They use the UF2 bootloader which makes the devices appear as flash drives. Do _NOT_ download the USB device drivers unless required to install UF2 support.
>

           Linux
        </>
      ),
      value: "linux",
    },
    {
      label: (
        <>
           macOS
        </>
      ),
      value: "macos",
    },
    {
      label: (
        <>
           Windows
        </>
      ),
      value: "windows",
    },
  ]}>

**linux**

#### Linux

- CH34x Driver - Linux Download

**macos**

#### macOS

> **Info:**
>
>
> With the latest versions of macOS, the USB Serial driver is built-in. If you downloaded/installed any already, please remove them.
>

##### Remove the CH34x USB Driver (macOS)

If you have already downloaded/installed the macOS WCH-IC CH340/CH341
("CH341SER_MAC") drivers via the CH34x_Install_V1.5.pkg, you will have to
Uninstall the kernel extension:

1. Unplug your device
2. Open the Terminal and run:
3. `sudo rm -rf /Library/Extensions/usbserial.kext`
4. Reboot

##### Install the CH34x Driver

- CH34x Driver- macOS Download

**windows**

#### Windows

- CH34x Driver - Windows Download

> **Important:**
>
>
> After installing the driver, make sure to reboot your computer to finish the installation process.
>
> You can also [test your serial driver installation](Test%20Serial%20Driver%20Installation.md) at this step if required.
>

### Flash Firmware

After installing the serial drivers, you can now flash the Meshtastic firmware onto your device. To proceed, select the appropriate device type for your device.

  
    Flash nRF52/RP2040/RP2350 Firmware

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/serial-drivers/nrf52. GPL-3.0 (Meshtastic documentation).*
