# ESP32 Serial Drivers

## Install ESP32 USB to Serial Drivers

You may need to install a driver from Silicon Labs for the CP210X USB to UART bridge

Some newer boards may require the CH9102 (CH340/CH341) Driver.

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

- CP210X USB to UART bridge - Download
- CH9102 Driver - Linux Download

**macos**

#### macOS

- CP210X USB to UART bridge - Download
- CH9102 Driver - macOS Download

**windows**

#### Windows

- CP210X USB to UART bridge - Download
- CH9102 Driver - Windows Download
- CH9102 Driver - Windows Download (Direct Download for Windows 7)

> **Important:**
>
>
> After installing the driver, make sure to reboot your computer to finish the installation process.
>
> You can also [test your serial driver installation](Test%20Serial%20Driver%20Installation.md) at this step if required.
>

### Flash Firmware

After installing the serial drivers, you can now flash the Meshtastic firmware onto your device. To proceed, select the appropriate device type for your device.

  
    Flash ESP32 Firmware

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/serial-drivers/esp32. GPL-3.0 (Meshtastic documentation).*
