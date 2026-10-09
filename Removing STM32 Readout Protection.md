# Removing STM32 Readout Protection

Some boards, such as the Wio-E5, ship with flash readout protection (RDP level 1)
enabled.
STM32CubeProgrammer
connects but cannot read, verify, or write flash. Removing the protection clears
it but erases the whole chip, including the factory firmware.

> **Warning:**
>
>
> Removing RDP mass-erases the chip and resets the MCU. On a board whose BOOT0 pin
> is not reachable, such as the Wio-E5, remove RDP
> [over SWD](Flashing%20STM32%20over%20SWD.md),
> connecting **under reset** (`mode=UR`, or **Connect Under Reset** in the GUI) so
> the programmer keeps control after the erase. With the firmware erased and no
> BOOT0 pin, nothing can re-enter the ROM bootloader for a UART connection.
>

## GUI &mdash; STM32CubeProgrammer

1. Connect over SWD with **Connect Under Reset**. Only on a board that exposes
   BOOT0 can you instead connect over UART with the board in the
   [ROM bootloader](Getting%20an%20STM32%20Device%20Ready%20to%20Flash.md).
2. Choose **Read Unprotect (MCU)** from the target menu.
3. Wait for the mass erase to finish, then reconnect.
4. Flash the Meshtastic firmware as described in
   [Flashing over SWD](Flashing%20STM32%20over%20SWD.md),
   or [Flashing over UART](Flashing%20STM32%20over%20UART.md)
   after re-entering the ROM bootloader with BOOT0.

## CLI &mdash; STM32CubeProgrammer

STM32CubeProgrammer's `-rdu` (read unprotect) removes RDP and mass-erases the
chip. Over SWD, connecting under reset:

```shell
STM32_Programmer_CLI -c port=SWD mode=UR -rdu
```

`mode=UR` needs the programmer's nRST line wired to the board; see
[Flashing over SWD](Flashing%20STM32%20over%20SWD.md)
for the `mode=HOTPLUG` fallback. On a board that exposes BOOT0, you can instead
run `-rdu` over the UART bootloader, then use BOOT0 to re-enter the bootloader
and flash firmware:

```shell
STM32_Programmer_CLI -c port=/dev/ttyUSB0 br=115200 -rdu
```

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/stm32/removing-readout-protection. GPL-3.0 (Meshtastic documentation).*
