# Flatpak - meshtasticd

#  Flatpak

Flatpaks are provided via  FlatHub.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ❌     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ❌     |

Supported platforms: `x86_64`, `aarch64`

Many distros support Flatpaks, see FlatHub Setup for help getting started.

## Install

```shell
flatpak install flathub org.meshtastic.meshtasticd
```

## Run

```shell
flatpak run org.meshtastic.meshtasticd
```

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/flatpak. GPL-3.0 (Meshtastic documentation).*
