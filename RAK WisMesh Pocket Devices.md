# RAK WisMesh Pocket Devices

The WisMesh Pocket line offers compact, ready-to-use Meshtastic devices designed for seamless communication in a LoRa mesh network. Built for portability and reliability, these devices eliminate the need for assembly or configuration, providing a straightforward and efficient way to stay connected. Whether for personal use or large-scale deployments, the WisMesh Pocket series delivers versatile solutions for reliable off-grid messaging.

**Pocket V2**

## WisMesh Pocket V2

> **Info:**
>
> WisMesh Pocket V2 is an updated version of the WisMesh Pocket. It features a newly designed base board with improved voltage regulator and battery circuit to comply with the European CE requirements and uses an SMA antenna connector to comply with FCC requirements.
>
> The WisMesh Pocket V1, while still supported, is no longer available for purchase.

- **Base Board**
  - RAK19026
- **MCU**
  - RAK4630 (nRF52840)
    - Bluetooth BLE 5.0
    - Very low power consumption
- **LoRa Transceiver:**
  - SX1262
- **Frequency Options:**
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - USB-C
  - SMA

### Features

- RAK19026 WisBlock Base Board
  - Improved voltage regulator with USB over-voltage protection
  - Improved battery charger, control with NTC temperature sensors
  - Improved location of the sensor slots
- 1.3” OLED display
- GNSS location module onboard
- Acceleration sensor onboard
- 3200 mAh Rechargeable battery

### Resources

- Firmware file: `firmware-rak4631-X.X.X.xxxxxxx.uf2`
- Further information on the WisMesh Pocket V2 can be found on the RAK Documentation Center.
- Purchase Links:
  - US
    - Rokland - US915 Mhz
  - International
    - RAKwireless Store
    - RAKwireless AliExpress
    - [Hexaspot] (https://msh.to/hexaspot-wismesh-pocket-v2/)

**Pocket Mini**

## WisMesh Pocket Mini

The WisMesh Pocket Mini is an ultra-compact, lightweight Meshtastic device without a built-in display or GPS, designed for low-power, long-lasting portable mesh communication.

- **Base Board**
  - [RAK19003](RAK%20WisBlock%20Base%20Boards.md)
- **MCU**
  - [RAK4631 (nRF52840)](RAK%20WisBlock%20Core%20Modules.md)
    - Bluetooth BLE 5.0
    - Very low power consumption
- **LoRa Transceiver:**
  - SX1262
- **Frequency Options:**
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - USB-C

### Features

- On/Off switch
- 2 sensor slots
- Internal PCB Antenna for LoRa
- Internal BLE Antenna
- 1000mAh battery

### Resources

- Firmware file: `firmware-rak4631-X.X.X.xxxxxxx.uf2`
- Further information on the WisMesh Pocket Mini can be found on the RAK Documentation Center.
- Purchase Links:
  - US
    - Rokland - US915 Mhz
  - International
    - RAKwireless Store
    - RAKwireless AliExpress

**RAK19026**

## RAK19026 WisMesh Base Board

The RAK19026 WisMesh Base Board serves as the foundation for the WisMesh Pocket line and is also available separately for users who want to build their own Meshtastic device. It includes an onboard GNSS module, acceleration sensor, user button, and battery disconnect switch, providing additional built-in features while maintaining a compact and easy-to-assemble design.

### Variants

The RAK19026 is available in three variants:

- OLED Mounted with GNSS and Motion Sensor
- GNSS and Motion Sensor with Unsoldered OLED
- Without OLED with GNSS and Motion

All variants include the following features:

- **MCU**
  - RAK4630 (nRF52840)
    - Bluetooth BLE 5.0
    - Very low power consumption
- **LoRa Transceiver:**
  - SX1262
- **Frequency Options:**
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - USB-C
  - U.FL/IPEX for LoRa

### Features

- Improved voltage regulator with USB over-voltage protection
- Improved battery charger, control with NTC temperature sensors
- Improved location of the sensor slots
- GNSS location module onboard
- Acceleration sensor onboard

### Resources

- Firmware file: `firmware-rak4631-X.X.X.xxxxxxx.uf2`
- Further information on the WisMesh Base Board can be found on the RAK Documentation Center.
- Purchase Links:
  - US
    - Rokland - US915 Mhz
  - International
    - RAKwireless Store
    - RAKwireless AliExpress

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wismesh/pocket. GPL-3.0 (Meshtastic documentation).*
