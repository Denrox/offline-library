# Fedora - meshtasticd

#  Fedora

Fedora packages are provided via  Fedora COPR.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ✅     |

Supported: Fedora `44`, Fedora `43`

## Install

**Beta**

  ```shell
  # Add Meshtastic COPR repo
  sudo dnf copr enable @meshtastic/beta
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

**Alpha**

  ```shell
  # Add Meshtastic COPR repo
  sudo dnf copr enable @meshtastic/alpha
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

**Daily**

  ```shell
  # Add Meshtastic COPR repo
  sudo dnf copr enable @meshtastic/daily
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/fedora. GPL-3.0 (Meshtastic documentation).*
