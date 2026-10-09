# RAK WisBlock Devices

**RAK3172/RAK3372**

## RAK3172/RAK3372 - STM32WLE5

> **Info:**
>
>
> **This core module does not include BLE or Wi-Fi.**
>

- **MCU:**
  - STM32WLE5CCU6
    - Arm Cortex-M4, 256 kB flash, 64 kB RAM
- **LoRa Transceiver:**
  - STM32WL integrated sub-GHz radio (Semtech SX126x-based)
- **Frequency Options:**
  - 433 MHz
  - 470 MHz
  - 868 MHz
  - 915 MHz
  - 923 MHz
- **Connectors:**
  - U.FL/IPEX (MHF1) antenna connector for LoRa
  - On `-SM-NI` modules the connector is replaced by an RF solder pad

The **RAK3172** is a castellated SMD module for embedding an STM32WL node into a product. The **RAK3372** is the same module on a WisBlock Core form factor, and requires a [base board](RAK%20WisBlock%20Base%20Boards.md).

### Ordering information

RAK3172 part numbers follow the pattern `RAK3172[-T | -TE | -F]-<band>-SM-`.

| Field      | Value    | Meaning                                         |
| ---------- | -------- | ----------------------------------------------- |
| Oscillator | _(none)_ | 32 MHz crystal only                             |
|            | `-T`     | ±2.5 ppm TCXO, wider temperature range          |
|            | `-TE`    | ±0.5 ppm TCXO                                   |
|            | `-F`     | TCXO plus 512 kB external SPI flash             |
| Band       | `-8`     | EU868, RU864, IN865                             |
|            | `-9`     | US915, AU915, KR920, AS923                      |
|            | `-43`    | EU433                                           |
|            | `-47`    | CN470                                           |
| Antenna    | `-SM-I`  | U.FL/IPEX (MHF1) connector                      |
|            | `-SM-NI` | RF solder pad only                              |

Representative orderable variants:

| Part number       | Band  | Oscillator    | Antenna    |
| ----------------- | ----- | ------------- | ---------- |
| RAK3172-8-SM-I    | EU868 | Crystal       | IPEX       |
| RAK3172-9-SM-I    | US915 | Crystal       | IPEX       |
| RAK3172-T-8-SM-I  | EU868 | ±2.5 ppm TCXO | IPEX       |
| RAK3172-T-9-SM-NI | US915 | ±2.5 ppm TCXO | Solder pad |
| RAK3172-TE-8-SM-I | EU868 | ±0.5 ppm TCXO | IPEX       |
| RAK3172-43-SM-I   | EU433 | Crystal       | IPEX       |

Meshtastic builds with `TCXO_OPTIONAL`, so both TCXO (`-T`/`-TE`/`-F`) and crystal-only modules work. Whether a module ships with RAK's RUI3 firmware or bare LoRaWAN firmware does not matter once Meshtastic is flashed.

### Flashing

- [Flashing over SWD](Flashing%20STM32%20over%20SWD.md)
- [Flashing over UART](Flashing%20STM32%20over%20UART.md)

### Resources

- Firmware file: `firmware-rak3172-X.X.X.xxxxxxx.bin` (the RAK3372 uses the same `rak3172` firmware)
- Further information on the RAK3172 can be found on the RAK Documentation Center.
- Purchase Links:
  - International
    - RAKwireless Store

**RAK11200**

## RAK11200 - ESP32

> **Info:**
>
>
> **This core module does not contain a LoRa transceiver**, which needs to be added separately in the form of the RAK13300 LPWAN module. This occupies the IO Port of the base board.
>

- RAK11200
  - **MCU:**
    - ESP32-WROVER
      - Bluetooth 4.2
      - Wi-Fi 802.11 b/g/n
      - High power consumption (relative to nRF52)

### Flashing the RAK11200

To flash the RAK11200, you need to manually place it into Espressif’s firmware download mode. Unlike other ESP32 boards, the RAK11200 does not support automatic boot mode selection. You must force it into download mode before flashing Meshtastic.

> **Warning:**
>
>
> Do not proceed unless an antenna is connected to avoid possible damage to the device's radio.
>

The following process will manually place the device into Espressif Firmware Download mode:

1. Ensure the device is powered on and connected via USB.
2. Locate the **BOOT** pin on the J10 header of the WisBlock Base Board ([RAK19007](RAK%20WisBlock%20Base%20Boards.md) / [RAK5005-O](RAK%20WisBlock%20Base%20Boards.md)).
3. Connect **BOOT** to **GND** (the GND pin is adjacent to BOOT on the J10 header).
   
     
       Diagram
       
         
       
     
   
4. Briefly tap the reset button.

Once the device is in Espressif Firmware Download mode, you can proceed with flashing using one of the supported flashing methods. It’s generally recommended to use the Web Flasher, selecting the appropriate RAK11200 firmware.

> **Note:**
>
>
> If the device does not enter download mode, double-check the BOOT to GND connection before attempting again.
>

### Resources

- Firmware file: `firmware-rak11200-X.X.X.xxxxxxx.bin`
- Further information on the RAK11200 can be found on the RAK Documentation Center.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/community-supported/rakwireless/wisblock/wisblock. GPL-3.0 (Meshtastic documentation).*
