# Docker - meshtasticd

#  Docker

Docker containers are provided via  DockerHub.

**Debian:**

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ❌     |
| 🌐 [Web][WebClient]      | ✅     |

**Alpine:**

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ❌     |
| 🌐 [Web][WebClient]      | ❌     |

Supported platforms: `linux/amd64`, `linux/arm64`, `linux/arm/v7`, `linux/riscv64`

## Pull

**Beta**

  Debian
  ```shell
  docker pull meshtastic/meshtasticd:beta-debian
  ```
  Alpine
  ```shell
  docker pull meshtastic/meshtasticd:beta-alpine
  ```
  

**Alpha**

  Debian
  ```shell
  docker pull meshtastic/meshtasticd:alpha-debian
  ```
  Alpine
  ```shell
  docker pull meshtastic/meshtasticd:alpha-alpine
  ```
  

**Daily**

  Debian
  ```shell
  docker pull meshtastic/meshtasticd:daily-debian
  ```
  Alpine
  ```shell
  docker pull meshtastic/meshtasticd:daily-alpine
  ```
  

See: [Docker Usage](Usage%20-%20meshtasticd.md)

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/docker. GPL-3.0 (Meshtastic documentation).*
