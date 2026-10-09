# Test Serial Driver Installation

### Test Serial Driver Installation

You can verify that you have a proper data cable (rather than a charge-only type cable) and that the appropriate drivers for your system are installed by performing the following test:

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

1. Connect your Meshtastic device to your USB port
2. Open a **Terminal** and enter the following command:

   ```shell
   lsusb
   ```

3. You should see something like:

   ```shell
   ID xxxx:xxxx Silicon Labs CP210x UART Bridge
   # or
   ID xxxx:xxxx QinHeng Electronics USB Single Serial
   # or
   ID xxxx:xxxx Adafruit WisCore RAK4631 Board
   ```

**macos**

#### macOS

1. Navigate to `Apple Menu  > About This Mac > More Info > System Report... > Hardware > USB`.
2. You should see similar to one of the following entries:

- `CP210X USB to UART Bridge Controller`
- `CH9102 USB to UART Bridge Controller`
- `WisCore RAK4631 Board`
- `USB Single Serial`

**windows**

#### Windows

1. Navigate to `Device Manager > Ports (COM & LPT)`
2. You should see similar to one of the following entries:

- `Silicon Labs CP210X USB to UART Bridge (COM5)`
- `Silicon Labs CH9102 USB to UART Bridge (COM5)`
- `USB-Enhanced-SERIAL CH9102 (COM5)`
- `USB Serial Device (COM5)`

> **Info:**
>
>
> If you are unable to see your device:
>
> - Make sure that your cable is not only for charging but also for [data transfer](Getting%20Started.md).
> - It's possible that you need to reinstall the USB serial driver.
>

## Flash Firmware

After completing the previous steps, you can now flash the Meshtastic firmware onto your device. To proceed, select the appropriate device type for your device.

  
    
      
        Flash ESP32 Firmware
      
    

  
      
        Flash nRF52/RP2040/RP2350 Firmware

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/serial-drivers/test-serial-driver-installation. GPL-3.0 (Meshtastic documentation).*
