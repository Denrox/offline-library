# Raspbian (32-bit) - meshtasticd

#  Raspbian (32-bit)

Raspbian (Raspberry Pi OS) packages are provided via  OpenSUSE Build Service.

> **Warning:**
>
> These builds are only suitable for 32-bit *armhf* Raspberry Pi OS installations.
>
> For **64-bit** Raspberry Pi OS installations, please use the [ Debian](Debian%20-%20meshtasticd.md) packages.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ✅     |

Supported: `trixie` (13), `bookworm` (12)

## Install

**Beta**

  **Raspbian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Raspbian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Raspbian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Raspbian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Raspbian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Raspbian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  

**Alpha**

  **Raspbian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/alpha/Raspbian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:alpha.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:alpha/Raspbian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_alpha.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Raspbian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/alpha/Raspbian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:alpha.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:alpha/Raspbian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_alpha.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  

**Daily**

  **Raspbian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/daily/Raspbian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:daily.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:daily/Raspbian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_daily.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Raspbian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" != Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) not detected, please use the Debian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/daily/Raspbian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:daily.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:daily/Raspbian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_daily.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/raspbian. GPL-3.0 (Meshtastic documentation).*
