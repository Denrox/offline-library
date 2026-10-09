# Seeed Wio-WM1100

> **[Note]:**
>
> Currently, LR1110 radios are unable to receive Meshtastic packets from the older SX127x radios, it requires a breaking change to fix this. Transmitting works and when hopping through an SX126x radio, you can still receive packets from SX127x radios.

**WM110 Dev Kit**

## Seeed Wio-WM1110 Dev Kit

> **External GPS Required:**
>
> The LR1110 GNSS functionality does not yet work. Seeed recommends at Grove - GPS (Air530).

- **MCU**
  - Nordic nRF52840
- **LoRa Transceiver**
  - Semtech LR1110
- **Frequency options**
  - 868 MHz
  - 915 MHz
  - 923 MHz
- **Navigation Module**
  - Grove GPS Air530 (Supports GPS, Beidou, Glonass, Galileo, QZSS, SBAS)
- **Connectors**
  - USB-C
  - LoRa Antenna: SMA antenna connector and U.FL/IPEX
  - GNSS Antenna: RP-SMA antenna connector U.FL/IPEX
  - NFC Antenna: U.FL/IPEX
  - GPIO
  - I2C x1
  - UART x1
  - Solar Panel
  - SWDIO

### Features

- Temperature and Humidity Sensor (SHT41)
- 3-Axis Accelerometer(LIS3DHTR)
- Reset switch, power jumpers, 2 configurable buttons
- AAA Battery x3
- Screen sold separately

### Resources

- Firmware file: `firmware-wio-sdk-wm1110-X.X.X.xxxxxxx.uf2`
- Purchase Links:
  - International
    - Seeed Studio

**Wio Tracker 1110**

## Wio Tracker 1110 Dev Kit for Meshtastic

- **MCU**
  - Nordic nRF52840 (BLE 5.3)
- **LoRa Transceiver**
  - Semtech LR1110
- **Frequency options**
  - 868 MHz
  - 915 MHz
  - 923 MHz
- **Navigation Module**
  - Semtech LR1110
- **Connectors**
  - USB-C
  - LoRa Antenna: on-board and U.FL/IPEX
  - GNSS Antenna: on-board and U.FL/IPEX
  - Grove connectors: ADC x1, I2C x1, UART x1, Digital x3

### Features

- Temperature and Humidity Sensor (SHT41)
- 3-Axis Accelerometer(LIS3DHTR)
- Reset switch, power jumpers
- Screen sold separately

### Resources

- Firmware file: `firmware-wio-tracker-wm1110-X.X.X.xxxxxxx.uf2`
- Purchase Links:
  - International
    - Seeed Studio

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/community-supported/seeed-studio/wio-series/seeed-wm1110. GPL-3.0 (Meshtastic documentation).*
