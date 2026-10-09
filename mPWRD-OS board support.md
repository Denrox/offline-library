# mPWRD-OS board support

mPWRD-OS publishes a separate image for each board it supports. Boards differ in how you reach them for first-time setup, and several ship with onboard storage that has to be cleared before an mPWRD-OS image boots.

## Supported boards

| Board | Chipset | Status | `meshtasticd` | Setup methods | Preparation |
| --- | --- | --- | --- | --- | --- |
| Raspberry Pi (64-bit) | BCM2711 | Supported | Beta | Ethernet, Bluetooth | None |
| EByte ECB41-PGE | RK3506G | Supported | Beta | Ethernet | Erase flash |
| Luckfox Lyra Plus | RK3506G | Supported | Beta | Ethernet | Erase flash |
| Luckfox Lyra Ultra W | RK3506B | Supported | Beta | Ethernet, Wi-Fi | Write to eMMC |
| Luckfox Lyra Zero W | RK3506B | Supported | Beta | Wi-Fi | Erase flash |
| ForLinx OK3506-S12 | RK3506J | Supported | Beta | Ethernet | Erase flash |
| Luckfox Pico Max | RV1106G | Supported | Beta | Ethernet | Erase flash |
| Luckfox Pico Mini | RV1103G | Supported | Beta | Ethernet | Erase flash |
| OnionIOT Omega4 | RV1103B | Planned | | Ethernet | |
| Generic x86_64 UEFI | UEFI | In development | Beta | SSH, VM console | |

Ethernet setup means reaching the board over SSH once it joins your network. Bluetooth and Wi-Fi setup are covered in [Provisioning](mPWRD-OS%20provisioning.md), and both preparation steps in [Rockchip flashing](Rockchip%20flashing.md).

The project lists the Waveshare Pico-LoRa-SX1262 HAT as working without manual configuration on the Luckfox Lyra Plus and Luckfox Pico Max. Radio recommendations and known hardware limitations are covered in meshtasticd hardware.

## Raspberry Pi (64-bit)

Images labeled `Rpi4b` run on every 64-bit Raspberry Pi model. That covers the 3, Zero 2, and CM3; the 4, Pi400, and CM4; and the 5, Pi500, and CM5. The Pi 1, Pi Zero 1, and Pi 2 are not supported.

This board needs no preparation. Set it up over Ethernet and SSH, or over Bluetooth as described in [Provisioning](mPWRD-OS%20provisioning.md). Radio HATs that support HAT+ autoconfiguration are detected without further setup.

## EByte ECB41-PGE

This board has onboard NAND flash that must be erased before mPWRD-OS runs on it. Follow [Erase flash](Rockchip%20flashing.md) first.

Set it up over Ethernet and SSH. The board uses the standard Pi HAT interface.

## Luckfox Lyra Plus

This section covers the Luckfox Lyra as well as the Lyra Plus.

The Lyra Plus and the Lyra B have onboard NAND flash that must be erased before mPWRD-OS runs on them, so follow [Erase flash](Rockchip%20flashing.md) first. The plain Lyra does not need it.

Set it up over Ethernet and SSH.

## Luckfox Lyra Ultra W

This board has onboard eMMC, so the image is written straight to it rather than to a microSD card. Follow [Write an image to eMMC](Rockchip%20flashing.md).

Set it up over Ethernet and SSH, or over Wi-Fi as described in [Provisioning](mPWRD-OS%20provisioning.md). The wehooper4 Luckfox Ultra HAT works without manual configuration.

## Luckfox Lyra Zero W

This board has onboard NAND flash that must be erased before mPWRD-OS runs on it. Follow [Erase flash](Rockchip%20flashing.md) first.

The board has no Ethernet port, so set it up over Wi-Fi as described in [Provisioning](mPWRD-OS%20provisioning.md). It uses the standard Pi HAT interface.

## ForLinx OK3506-S12

This board has onboard NAND flash that must be erased before mPWRD-OS runs on it. Follow [Erase flash](Rockchip%20flashing.md) first.

Set it up over Ethernet and SSH. The board uses the standard Pi HAT interface.

## Luckfox Pico Max

This board has onboard NAND flash that must be erased before mPWRD-OS runs on it. Follow [Erase flash](Rockchip%20flashing.md) first.

Set it up over Ethernet and SSH.

## Luckfox Pico Mini

The Luckfox Pico Mini A has onboard NAND flash that must be erased before mPWRD-OS runs on it. Follow [Erase flash](Rockchip%20flashing.md) first.

Set it up over Ethernet and SSH. The femtofox carrier board works without manual configuration.

## OnionIOT Omega4

Support for this board is planned. No image is published for it.

## Generic x86_64 UEFI

This image exists for development and testing rather than for deploying a node. Set it up over SSH or a virtual machine console.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/software/mpwrd-os/board-support. GPL-3.0 (Meshtastic documentation).*
