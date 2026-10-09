# Flash STM32 Devices

## Flashing Methods for STM32 Devices

Flashing an STM32WL board takes two steps: get the board ready to flash, then
write the firmware. A UART flash uses the chip's built-in ROM bootloader; an SWD
programmer writes to flash directly. Meshtastic firmware for STM32WL targets is
distributed as `firmware-<target>-X.X.X.xxxxxxx.bin` and flashed to `0x08000000`;
the `.elf` in the same release also works with
STM32CubeProgrammer.

For the BOOT0 pin location, UART pins, and any board-specific steps, see the
documentation for your board.

### Getting the Board Ready to Flash

STM32WL has no USB DFU mode. For a UART flash, the
[ROM bootloader can be entered](Getting%20an%20STM32%20Device%20Ready%20to%20Flash.md)
from a Meshtastic client or with the BOOT0 pin. For an SWD flash, the programmer
resets and connects to the board itself.

### Flashing from Web Flasher

Browser-based flashing is a work-in-progress and not available for STM32 targets yet.

### Flashing over UART

A USB-TTL serial adapter can
[flash STM32WL over UART](Flashing%20STM32%20over%20UART.md)
without an SWD programmer, once the board is in the ROM bootloader.

### Flashing over SWD

An SWD programmer such as an ST-LINK
[writes firmware straight to flash over the SWD pins](Flashing%20STM32%20over%20SWD.md),
without using BOOT0 or the ROM bootloader.

### Flashing over USB

STM32WL has no USB peripheral, so there is no USB DFU mode. A UART flash (through
the ROM bootloader) and an SWD flash are the only options.

Any USB port connects to an internal USB-to-UART bridge and can be used for UART
flashing, unless that bridge is not wired to a bootloader UART. On the Wio-E5 it
is not, though two jumper wires can bridge it to one; see the
[Wio-E5 page](Seeed%20Wio-E5.md).

### Removing Readout Protection

Some boards, such as the Wio-E5, ship with flash readout protection enabled.
STM32CubeProgrammer connects but cannot read or write flash until
[readout protection is removed](Removing%20STM32%20Readout%20Protection.md).

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/stm32/flashing-stm32-devices. GPL-3.0 (Meshtastic documentation).*
