# Convert RAK4631-R to RAK4631

The only difference between the _RAK4631-R_ (RUI3) and the _RAK4631_ (Arduino) is the bootloader it is shipped with - the hardware is the same.

Meshtastic requires the Arduino bootloader on RAK WisBlock nRF52-based boards. The process of converting the bootloader only needs to be performed once.

Here are two ways to flash the bootloader:

## USB Device Firmware Upgrade (DFU)

1. Install Python
2. Install adafruit-nrfutil
   ```shell
   pip3 install adafruit-nrfutil
   ```
3. Download the required bootloader: RAK4631 bootloader package (.zip)
4. Connect your RAK device by USB.
5. Flash the bootloader
   ```shell
   adafruit-nrfutil --verbose dfu serial --package ./wiscore_rak4631_board_bootloader-0.4.4_s140_6.1.1.zip -p /dev/ttyACM0 -b 115200 --singlebank --touch 1200
   ```
   Note: The serial port name (`/dev/ttyACM0`) may differ depending on your operating system. Make sure to identify the correct port name for your setup.
6. Continue with the normal [flashing instructions](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md)

### Extra RUI3 Steps

If the above steps fail with errors like:

```bash
Touched serial port COM11
Opened serial port COM11
Starting DFU upgrade of type 2, SoftDevice size: 0, bootloader size: 39000, application size: 0
Sending DFU start packet
Timed out waiting for acknowledgement from device.
Failed to upgrade target. Error is: No data received on serial port. Not able to proceed.
```

You will need to follow the first part (through the `AT+BOOT` command) of the Converting RAK4631-R to RAK4631 instructions.

## Debugger

This conversion requires the use of either a DAPLink or J-Link. The most reasonably priced and available is the RAKDAP1.

1. Install Python
2. Install pyOCD
   ```shell
   pip3 install pyocd
   ```
3. Download the required bootloader: RAK4631 bootloader image (.hex)
4. Connect the RAKDAP as follows:
   
5. Flash the bootloader
   ```shell
   pyocd flash -t nrf52840 .\wiscore_rak4631_board_bootloader-0.4.4_s140_6.1.1.hex
   ```
6. Continue with the normal [flashing instructions](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md)

Alternate flashing methods.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/convert-rak4631r. GPL-3.0 (Meshtastic documentation).*
