# LILYGO® TTGO Lora Devices

Further information on the LILYGO® LoRa devices can be found on LILYGO®'s GitHub page.

**Lora V1**

## Lora v1

> **Warning:**
>
> Not recommended with a battery! These boards contain the wrong component in the LiPo battery charging circuit allowing the battery to be overcharged.

> **Caution:**
>
> This board is still in production but for various reasons not recommended for new purchases or for unattended installations. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX1276
- **Frequency options**
  - 915 MHz
  - 868 MHz
- **Connectors**
  - Micro USB
  - Antenna: U.FL antenna connector

### Features

- Built in 0.96 inch OLED display

### Resources

- Firmware file: `firmware-tlora-v1-X.X.X.xxxxxxx.bin`

**Lora V1.3**

## Lora v1.3

> **Warning:**
>
> Not recommended with a battery! These boards contain the wrong component in the LiPo battery charging circuit allowing the battery to be overcharged.

> **Caution:**
>
> This board is still in production but for various reasons not recommended for new purchases or for unattended installations. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX127x
- **Frequency options**
  - 915 MHz
  - 868 MHz
- **Connectors**
  - Micro USB
  - Antenna: U.FL antenna connector

### Features

- Built in 0.96 inch OLED display

### Resources

- Firmware file: `firmware-tlora_v1_3-X.X.X.xxxxxxx.bin`

**Lora V2.0**

## Lora V2.0

> **Warning:**
>
> Not recommended with a battery! These boards contain the wrong component in the LiPo battery charging circuit allowing the battery to be overcharged.

> **Caution:**
>
> This board is still in production but for various reasons not recommended for new purchases or for unattended installations. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX127x
- **Frequency options**
  - 433 MHz
  - 868 MHz
  - 915 MHz
- **Connectors**
  - Micro USB
  - Antenna: U.FL antenna connector

### Features

- Built in 0.96 inch OLED display
- Power and Reset switches
- microSD connector
- No GPS

### Resources

- Firmware file: `firmware-tlora-v2-X.X.X.xxxxxxx.bin`

**Lora V2.1-1.6**

## Lora v2.1-1.6

> **Caution:**
>
> Early versions of these boards contained the wrong component in the LiPo battery charging circuit allowing the battery to be overcharged. Boards purchased after 2021, unless the version is T3_v1.6 20180606, should not have this issue.

> **Caution:**
>
> This board is still in production but for various reasons not recommended for new purchases or for unattended installations. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX127x
- **Frequency options**
  - 433 MHz
  - 868 MHz
  - 915 MHz
  - a variant of this board has a Temperature controlled oscillator (labelled TCXO) for improved frequency stability
- **Connectors**
  - Micro USB
  - Antenna: SMA antenna connector

### Variations of identifying marks

- FCC ID: 2ASYE-T3-V1-6-1
- "T3_v1.6.1 20210104" on the board
- "T3_v1.6 20180606" on the board
- "Model T3 V1.6.1" on the FCC sticker

### Features

- Built in 0.96 inch OLED display
- Power and Reset switches
- microSD connector
- No GPS

### Resources

- Firmware file: `firmware-tlora-v2-1-1_6-X.X.X.xxxxxxx.bin`

**Lora V2.1-1.8**

## Lora v2.1-1.8

> **Caution:**
>
> This board is still in production but for various reasons not recommended for new purchases or for unattended installations. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX1280 (Region LORA_24 worldwide use)
- **Frequency options**
  - 2.4 GHz
- **Connectors**
  - USB-C
  - Antenna: SMA antenna connector

### Features

- Built in 0.96 inch OLED display
- Power and Reset switches
- microSD connector
- No GPS

### Resources

- Firmware file: `firmware-tlora-v2-1-1.8-X.X.X.xxxxxxx.bin`

**Lora V3.0**

## Lora v3.0

> **Caution:**
>
> This board is using a first generation Semtech chip and is therefore not recommended for new purchases. Firmware support is phased out. If in doubt, choose the Lora T3S3 board.

- **MCU**
  - ESP32 (Wi-Fi & Bluetooth)
- **LoRa Transceiver**
  - Semtech SX127x with TCXO for improved frequency stability
- **Frequency options**
  - 433 MHz
  - 868 MHz
  - 915 MHz
- **Connectors**
  - USB-C
  - Antenna: IPEX antenna connector

### Features

- Built in 0.96 inch OLED or 2.13 inch E-Paper display
- Power and Reset switches, User Button
- microSD connector
- Solar panel and battery connector, includes solar charging circuit (CN3065)
- QWIIC for UART and I2C each
- No GPS

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/community-supported/lilygo/lora/community-tlora. GPL-3.0 (Meshtastic documentation).*
