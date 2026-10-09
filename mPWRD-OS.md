# mPWRD-OS

mPWRD-OS is a Linux distribution for single-board computers that pairs Armbian with Meshtastic. Its images are based on Debian 13 `trixie` and ship with meshtasticd and the [Meshtastic Python CLI](Meshtastic%20Python%20CLI%20Guide.md) already installed, so the node software is ready to configure as soon as the board boots. Images and source are published at mPWRD-OS/mPWRD-OS.

## What's included

| Component | Purpose |
| --- | --- |
| Debian 13 `trixie` | Base system, built with the Armbian userpatches framework |
| meshtasticd | Runs the Meshtastic node firmware on the board |
| [Meshtastic Python CLI](Meshtastic%20Python%20CLI%20Guide.md) | Configures the node from a shell |
| contact | Terminal client for reading and sending messages |
| mpwrd-menu | Menu-driven setup for system and Meshtastic settings |
| Wi-Fi provisioning | Sends Wi-Fi credentials to a board that has no network connection yet |

## Supported boards

| Chipset | Board | Status | `meshtasticd` |
| --- | --- | --- | --- |
| BCM2711 | [Raspberry Pi (64-bit)](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RK3506G | [EByte ECB41-PGE](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RK3506G | [Luckfox Lyra Plus](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RK3506B | [Luckfox Lyra Ultra W](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RK3506B | [Luckfox Lyra Zero W](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RK3506J | [ForLinx OK3506-S12](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RV1106G | [Luckfox Pico Max](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RV1103G | [Luckfox Pico Mini](mPWRD-OS%20board%20support.md) | Supported | Beta |
| RV1103B | [OnionIOT Omega4](mPWRD-OS%20board%20support.md) | Planned | |
| UEFI | [Generic x86_64 UEFI](mPWRD-OS%20board%20support.md) | In development | Beta |

Several boards ship with onboard storage that has to be cleared before an mPWRD-OS image boots. [Board support](mPWRD-OS%20board%20support.md) covers the setup method and the preparation each board needs.

## Install and set up

1. Download the image for your board from the mPWRD-OS releases page.
2. Prepare the board if it needs it. Boards with onboard NAND flash or eMMC are handled in [Rockchip flashing](Rockchip%20flashing.md).
3. Write the image to a microSD card with balenaEtcher or a similar tool, then power on the board. Check that the image is the one built for your board and that the selected drive is the card, because writing erases everything on the target.
4. Connect to the board. Boards with an Ethernet port are reachable over SSH once they join your network, and boards without one take the Bluetooth or hotspot route described in [Provisioning](mPWRD-OS%20provisioning.md).
5. Log in as `root` with the password `1234`. The first login prompts for a new password.
6. Run `mpwrd-menu` to set your region, configure the radio, and change system settings.

   ```shell
   mpwrd-menu
   ```

## Building your own image

The repository is an Armbian userpatches overlay, so images are compiled by armbian/build with mPWRD-OS checked out as `userpatches`. Each board has its own configuration file in the repository. The repository README carries the commands.

## Getting help

Bug reports and feature requests for mPWRD-OS belong in the project's issue tracker.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/software/mpwrd-os/mpwrd-os. GPL-3.0 (Meshtastic documentation).*
