# Red Hat (EPEL) - meshtasticd

#  Red Hat (EPEL)

Red Hat (EPEL) packages are provided via  Fedora COPR.
Built with Red Hat's UBI.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ✅     |

Supported: EPEL `10`, EPEL `9`

CentOS Stream, Red Hat Enterprise Linux, AlmaLinux, Rocky Linux, and other EPEL-supported distributions.

## Install

**Beta**

  ```shell
  # Add Meshtastic COPR repos
  sudo dnf config-manager --set-enabled crb
  sudo dnf install epel-release
  sudo dnf copr enable @meshtastic/beta
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

**Alpha**

  ```shell
  # Add Meshtastic COPR repos
  sudo dnf config-manager --set-enabled crb
  sudo dnf install epel-release
  sudo dnf copr enable @meshtastic/alpha
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

**Daily**

  ```shell
  # Add Meshtastic COPR repos
  sudo dnf config-manager --set-enabled crb
  sudo dnf install epel-release
  sudo dnf copr enable @meshtastic/daily
  # Install meshtasticd
  sudo dnf install meshtasticd
  ```
  

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/epel. GPL-3.0 (Meshtastic documentation).*
