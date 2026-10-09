# Ubuntu - meshtasticd

#  Ubuntu

Ubuntu packages are provided via  Canonical Launchpad.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ✅     |

Supported: `resolute` (26.04 LTS), `questing` (25.10), `noble` (24.04 LTS), `jammy` (22.04 LTS)

## Install

**Beta**

  ```shell
  # Install requirements for add-apt-repository
  sudo apt install software-properties-common
  # Add Meshtastic repo
  sudo add-apt-repository ppa:meshtastic/beta
  # Install meshtasticd
  sudo apt install meshtasticd
  ```
  

**Alpha**

  ```shell
  # Install requirements for add-apt-repository
  sudo apt install software-properties-common
  # Add Meshtastic repo
  sudo add-apt-repository ppa:meshtastic/alpha
  # Install meshtasticd
  sudo apt install meshtasticd
  ```
  

**Daily**

  ```shell
  # Install requirements for add-apt-repository
  sudo apt install software-properties-common
  # Add Meshtastic repo
  sudo add-apt-repository ppa:meshtastic/daily
  # Install meshtasticd
  sudo apt install meshtasticd
  ```
  

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/ubuntu. GPL-3.0 (Meshtastic documentation).*
