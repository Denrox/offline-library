# Raspberry Pi Pico & Pico 2

The Raspberry Pi Pico series includes boards based on the RP2040 and RP2350 microcontrollers, designed by Raspberry Pi in the UK.

> **Info:**
>
>
> Only the Pico W has Wi-Fi/BLE capabilities. Meshtastic supports Wi-Fi on the Pico W (although no web server and HTTP API), but does not currently support BLE.

## Specifications

- **MCU:**
  - Raspberry Pi RP2040
    - Dual M0+ Core
    - 133MHz CPU Clock
  - Raspberry Pi RP2350
    - Dual Cortex-M33 / Hazard3 RISC-V Core
    - 150MHz CPU Clock
- **Connectors (On Pico):**
  - Micro-USB on Pico

> **Note:**
>
>
> Please be aware that the Raspberry Pi Pico must be used in combination with a Waveshare LoRa Module, which provides the necessary SX1262 LoRa radio. Please ensure to select the correct frequency for your region.
>

- **LoRa Transceiver (On LoRa Module):**
  - SX1262
- **Frequency Options:**
  - 410 - 525 MHz
  - 863 - 870 MHz
  - 902 - 930 MHz
- **Connectors (On LoRa Module):**
  - U.FL/IPEX antenna connector for LoRa
  - 1.25mm 2-Pin JST for battery

> **Note:**
>
>
> LoRa transmissions may interfere with the USB connection. It is recommended to place the antenna as far away from the USB port as possible.
>

### Resources

- **Firmware files:**
  - Pico (RP2040): `firmware-pico-X.X.X.xxxxxxx.uf2`
  - Pico W (RP2040): `firmware-picow-X.X.X.xxxxxxx.uf2`
  - Pico 2 (RP2350): `firmware-pico2-X.X.X.xxxxxxx.uf2`
  - Pico 2 W (RP2350): `firmware-pico2w-X.X.X.xxxxxxx.uf2`

- **Official Raspberry Pi product pages:**
  - Raspberry Pi Pico (RP2040)
  - Raspberry Pi Pico 2 (RP2350)

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/raspberrypi/pico/raspberry-pi-pico. GPL-3.0 (Meshtastic documentation).*
