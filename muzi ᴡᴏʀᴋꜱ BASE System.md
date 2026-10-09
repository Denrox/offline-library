# muzi ᴡᴏʀᴋꜱ BASE System

The BASE System is muzi ᴡᴏʀᴋꜱ' modular Meshtastic development platform, designed for performance, reliability, and ultimate flexibility. Built from experience developing thousands of devices, the BASE System features custom core modules optimized for efficiency, next-gen base boards with extensive IO, and expandability via the IO board system. Both Base Uno and Base Duo are fully supported by Meshtastic through the Backer Program.

**Base Uno**

## Base Uno

The Base Uno is the entry-level board in the BASE System, featuring the Elecrow nRFLR1262 module with the Semtech SX1262 LoRa transceiver. It provides all the core functionality of the BASE System at an affordable price point.

### Specifications

- **MCU**
  - nRF52840 (Bluetooth 5 LE)
- **LoRa Transceiver**
  - Semtech SX1262
- **QSPI Flash**
  - 2MB
- **Frequency Options**
  - 868 MHz
  - 915 MHz
- **Connectors**
  - USB-C (charging and data)
  - QWIIC / STEMMA QT (I2C)
  - 25 header pins (0.1" spacing)
  - 3-pin Molex PicoBlade (1.25mm) battery connector
- **Buttons**
  - User button
  - Reset button
- **Dimensions**
  - 42 x 32mm
  - Weight: 10g

### Features

- Flexible power options (Solar, USB, or Battery)
- Advanced battery management with BQ28185 charger IC
- Li-ion/LiPo and LFP (LiFePO4) battery support
- Powerpath with VDPM (Voltage and Dynamic Power Management)
- Voltage and thermal protection
- 8 GPIO + 2 PWR IO + UART + I2C
- Standardized M2 mounting holes
- Open source case design available

### Expandability

Unlock the full potential of your Base Duo with the [Super IO](muzi%20%E1%B4%A1%E1%B4%8F%CA%80%E1%B4%8B%EA%9C%B1%20Super%20IO.md) expansion board, adding GPS, display support, and standalone capabilities.

### Resources

- Firmware file: `firmware-muzi-base-X.X.X.xxxxxxx.uf2`
- User Guide
- Purchase Links:
  - US
    - muzi ᴡᴏʀᴋꜱ

**Base Duo**

## Base Duo

The Base Duo is the advanced board in the BASE System, featuring the Elecrow nRFLR1121 module with the Semtech LR1121 LoRa transceiver. It offers 2.4GHz LoRa support for worldwide compatibility and hardware support for increased data rates up to 12 times faster than current Short Turbo presets.

### Specifications

- **MCU**
  - nRF52840 (Bluetooth 5 LE)
- **LoRa Transceiver**
  - Semtech LR1121 (Sub-GHz and 2.4GHz)
- **QSPI Flash**
  - 8MB
- **Frequency Options**
  - 868 MHz
  - 915 MHz
  - 2.4 GHz (worldwide)
- **Connectors**
  - USB-C (charging and data)
  - QWIIC / STEMMA QT (I2C)
  - 25 header pins (0.1" spacing)
  - 3-pin Molex PicoBlade (1.25mm) battery connector
- **Buttons**
  - User button
  - Reset button
- **Dimensions**
  - 42 x 32mm
  - Weight: 10g

### Features

- 2.4GHz LoRa support for worldwide compatibility
- Hardware support for high-speed data rates
- Flexible power options (Solar, USB, or Battery)
- Advanced battery management with BQ28185 charger IC
- Li-ion/LiPo and LFP (LiFePO4) battery support
- Powerpath with VDPM (Voltage and Dynamic Power Management)
- Voltage and thermal protection
- 8 GPIO + 2 PWR IO + UART + I2C

### Expandability

Unlock the full potential of your Base Duo with the [Super IO](muzi%20%E1%B4%A1%E1%B4%8F%CA%80%E1%B4%8B%EA%9C%B1%20Super%20IO.md) expansion board, adding GPS, display support, and standalone capabilities.

### Resources

- Firmware file: `firmware-muzi-base-X.X.X.xxxxxxx.uf2`
- User Guide
- Purchase Links:
  - US
    - muzi ᴡᴏʀᴋꜱ

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/muziworks/muzi-base/muzi-base. GPL-3.0 (Meshtastic documentation).*
