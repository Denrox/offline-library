# Elecrow MeshStick

The MeshStick is a USB LoRa radio rather than a standalone node. It supplies the SX1262 transceiver, and a Linux host running meshtasticd supplies the processor, storage, and network. Plug it into a Raspberry Pi, a server, or a laptop.

## Specifications

- **LoRa Transceiver**
  - Semtech SX1262 (TCXO), up to 22 dBm
- **Host Interface**
  - CH341 USB-to-SPI bridge
  - USB 2.0 Type-A
- **Connectors**
  - SMA antenna connector

## Features

- Identifies itself over USB, so meshtasticd configures the radio without manual setup.
- Runs from the host's USB power, with no battery to manage.
- Open hardware: the schematic and gerbers are published.

## Resources

- Configuration file: `lora-usb-meshstick-1262.yaml`
- Setup: [MeshStick under meshtasticd](MeshStick.md)
- Purchase Links:
  - International
    - Elecrow

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/elecrow/meshstick. GPL-3.0 (Meshtastic documentation).*
