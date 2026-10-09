# macOS - meshtasticd

#  macOS

MacOS packages are installed via  Homebrew.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ❌     |
| 📱 [MUI][MUI]            | ❌     |
| 🌐 [Web][WebClient]      | ❌     |

Supported MacOS: 26 `tahoe`, 15 `sequoia`

## Install

```shell
brew tap meshtastic/tap
brew trust meshtastic/tap
brew install meshtasticd
brew services start meshtasticd
```

## macOS paths

- configuration : `/opt/homebrew/etc/meshtasticd`
- log : `/opt/homebrew/var/log/meshtasticd.log`

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/macos. GPL-3.0 (Meshtastic documentation).*
