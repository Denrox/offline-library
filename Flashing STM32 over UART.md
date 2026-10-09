# Flashing STM32 over UART

A USB-TTL serial adapter can flash STM32WL without an SWD programmer, once the
board is in the
[ROM bootloader](Getting%20an%20STM32%20Device%20Ready%20to%20Flash.md).

The ROM bootloader listens on:

- USART1 &mdash; PA9 (TX), PA10 (RX)
- USART2 &mdash; PA2 (TX), PA3 (RX)

Connect the adapter's RX to the MCU's TX and the adapter's TX to the MCU's RX,
with a common ground.

## GUI &mdash; STM32CubeProgrammer

1. Launch STM32CubeProgrammer.
2. Select the **UART** connection and the serial port of your USB-TTL adapter.
3. Put the board in the
   [ROM bootloader](Getting%20an%20STM32%20Device%20Ready%20to%20Flash.md).
4. Click **Connect**.
5. Open the `firmware-<target>-X.X.X.xxxxxxx.bin` file and confirm the start address is `0x08000000` (the default).
6. Click **Download**.

## CLI &mdash; STM32CubeProgrammer

```shell
STM32_Programmer_CLI -c port=/dev/ttyUSB0 br=115200 -w firmware-<target>-X.X.X.xxxxxxx.bin 0x08000000 -v -g 0x08000000
```

`-v` verifies the write and `-g 0x08000000` starts the firmware once it finishes.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/stm32/flashing-over-uart. GPL-3.0 (Meshtastic documentation).*
