# RAK WisMesh Gateway

The WisMesh Gateway series extends the capabilities of Meshtastic by bridging off-grid mesh networks to MQTT, or enabling real-time data exchange. Whether integrating sensor networks, linking multiple mesh regions, or expanding communication reach, these gateways provide a seamless way to connect Meshtastic to the cloud for greater flexibility and control.

**Ethernet MQTT Gateway**

## WisMesh Ethernet MQTT Gateway

The WisMesh Ethernet MQTT Gateway provides a stable and wired connection between Meshtastic networks and MQTT brokers featuring an Ethernet interface.

- **Base Board:**
  - [RAK19007](RAK%20WisBlock%20Base%20Boards.md)
- **MCU**
  - [RAK4631 (nRF52840)](RAK%20WisBlock%20Core%20Modules.md)
    - Bluetooth BLE 5.0
    - Very low power consumption
- **LoRa Transceiver:**
  - SX1262
- **Frequency Options:**
  - 864 MHz
  - 865 MHz
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - RP-SMA
  - USB-C
  - Ethernet

### Features

- Pre-assembled option with IP67 Unify Enclosure
  - Includes WisMesh Blade Antenna
- RAK13800 Ethernet Module (Requires an external power source)
  - Optional RAK19018 PoE Module

### Resources

- Firmware file: `firmware-rak4631_eth_gw-X.X.X.xxxxxxx.uf2`
- Further information on the WisMesh Ethernet MQTT Gateway can be found on the RAK Documentation Center.
- Purchase Links:
  - International
    - RAKwireless Store
    - RAKwireless AliExpress

**Wi-Fi MQTT Gateway**

## WisMesh Wi-Fi MQTT Gateway

The WisMesh Wi-Fi MQTT Gateway is a wireless solution for bridging Meshtastic networks to MQTT brokers.

- **Base Board:**
  - [RAK19007](RAK%20WisBlock%20Base%20Boards.md)
- **MCU**
  - [RAK11200 (ESP32)](RAK%20WisBlock%20Core%20Modules.md)
    - Bluetooth BLE 4.2
    - Wi-Fi 802.11 b/g/n
    - High power consumption (relative to nRF52)
- **LoRa Transceiver:**
  - SX1262 (RAK13300 LPWAN module)
    - Occupies the IO Port of the base board
- **Frequency Options:**
  - 864 MHz
  - 865 MHz
  - 868 MHz
  - 915 MHz
  - 920 MHz
  - 923 MHz
- **Connectors:**
  - RP-SMA (Enclosure only)
  - USB-C
  - M8 5-pin connector (Enclosure only)

### Features

- Wi-Fi connectivity
- Pre-assembled option with IP67 Unify Enclosure
  - Includes WisMesh Blade Antenna
  - Includes M8 Cable for 5V power

### Resources

- Firmware file: `firmware-rak11200-X.X.X.xxxxxxx.bin`
- Further information on the WisMesh Wi-Fi MQTT Gateway can be found on the RAK Documentation Center.
- Purchase Links:
  - International
    - RAKwireless Store
    - RAKwireless AliExpress

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wismesh/gateway. GPL-3.0 (Meshtastic documentation).*
