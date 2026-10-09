# Getting an STM32 Device Ready to Flash

Both flashing methods need the board in the right state before you can write
firmware. The three methods below are ordered most convenient first:

- **Meshtastic Client** and **BOOT0** enter the ROM bootloader, which a
  [UART flash](Flashing%20STM32%20over%20UART.md)
  needs.
- **SWD** resets the MCU and connects to it directly for an
  [SWD flash](Flashing%20STM32%20over%20SWD.md);
  it does not use the ROM bootloader.

## Meshtastic Client

Once Meshtastic firmware is installed, the board can be rebooted into the ROM
bootloader without touching the hardware:

1. Connect to the node over USB (or BLE).
2. Run `meshtastic --enter-dfu`, or select the equivalent option in the app.

On boards whose USB serial port connects to the ROM bootloader UART, this allows
firmware upgrades over
[UART](Flashing%20STM32%20over%20UART.md) with no
extra wiring.

## BOOT0

On boards that route the BOOT0 pin to a pad, jumper, or switch:

1. Tie BOOT0 high (to 3V3).
2. Reset or power-cycle the board. It comes out of reset in the ROM bootloader.
3. Flash the firmware over
   [UART](Flashing%20STM32%20over%20UART.md).
4. Return BOOT0 to ground (or let it float if the board has a pull-down) and
   reset again to run the firmware.

> **Note:**
>
>
> Some boards, such as the Wio-E5, do not expose the BOOT0 pin; use another method.
>

## SWD

An SWD programmer such as an
ST-LINK writes firmware
straight to flash over the SWD pins. It resets and halts the MCU to do this, so
it never uses the ROM bootloader and needs neither BOOT0 nor a working Meshtastic
client. That makes it the only option for a board that is not already running
Meshtastic firmware and has no reachable BOOT0 pin. Continue at
[Flashing over SWD](Flashing%20STM32%20over%20SWD.md).

For the BOOT0 pin location, UART pins, and any board-specific steps, see the
documentation for your board.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/stm32/entering-bootloader-mode. GPL-3.0 (Meshtastic documentation).*
