# Raspberry Pi

### Raspberry Pi Pico / Pico 2

Fast versatile boards using the RP2040 and RP2350 microcontrollers.

| Name                               | MCU      | LoRa (external module required) | Wi-Fi | BT | GPS |
| :--------------------------------- | :------- | :------------------------------ | :--: | :-: | :-: |
| Raspberry Pi Pico       | RP2040   | SX1276 / SX1262 (external)     | NO  | NO | ADD-ON[^3] |
| Raspberry Pi Pico W     | RP2040   | SX1276 / SX1262 (external)     | YES[^1] | NO[^2] | ADD-ON[^3] |
| Raspberry Pi Pico 2     | RP2350   | SX1276 / SX1262 (external)     | NO  | NO | ADD-ON[^3] |
| Raspberry Pi Pico 2 W   | RP2350   | SX1276 / SX1262 (external)     | YES[^1] | NO[^2] | ADD-ON[^3] |

[^1]: 2.4GHz 802.11 b/g/n Wi-Fi is available only on the **W variants** (Pico W and Pico 2 W). Meshtastic supports Wi-Fi on Pico W and Pico 2 W (no web server or HTTP API).

[^2]: Pico W and Pico 2 W include Bluetooth hardware (Bluetooth 5.2 on Pico 2 W), but BLE is not currently supported by Meshtastic.

[^3]: Meshtastic supports external UART GPS modules. Examples of tested modules are listed in the Meshtastic GPS compatibility spreadsheet.

For the popular Linux Single Board Computer series, see [Raspberry Pi (meshtasticd)](Raspberry%20Pi%20%28Linux%29.md).

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/raspberrypi/raspberry-pi. GPL-3.0 (Meshtastic documentation).*
