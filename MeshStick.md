# MeshStick

The MeshStick is a CH341 USB-to-SPI LoRa radio with a Semtech SX1262 transceiver, sold assembled by Elecrow and also published as open hardware you can build yourself.

### Features

- Semtech SX1262 with TCXO, up to 22 dBm
- Identifies itself over USB, so meshtasticd selects the right configuration automatically
- USB 2.0 Type-A plug, with an SMA connector for the LoRa antenna

### Configuration

Select `lora-usb-meshstick-1262.yaml` from the available configuration files. Copy it from `/etc/meshtasticd/available.d` into `/etc/meshtasticd/config.d`, as described in [Usage](Usage%20-%20meshtasticd.md).

### Purchase Links

Elecrow

### Schematic

MeshStick information and gerbers are available on GitHub.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/hardware/radios/usb/meshstick. GPL-3.0 (Meshtastic documentation).*
