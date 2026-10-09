# Debian - meshtasticd

#  Debian

Debian packages are provided via  OpenSUSE Build Service.

| Feature                  | Status |
| ------------------------ | ------ |
| 🔌 [USB Radio][USBRadio] | ✅     |
| 🕸️ [SPI Radio][SPIRadio] | ✅     |
| 📱 [MUI][MUI]            | ✅     |
| 🌐 [Web][WebClient]      | ✅     |

Supported: `trixie` (13), `bookworm` (12)

## Install

**Beta**

  **Debian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Debian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Debian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Debian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  

**Alpha**

  **Debian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/alpha/Debian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:alpha.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:alpha/Debian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_alpha.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Debian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/alpha/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:alpha.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:alpha/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_alpha.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```
  

**Daily**

  **Debian 13 (`trixie`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/daily/Debian_13/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:daily.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:daily/Debian_13/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_daily.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Debian 12 (`bookworm`):**

  ```shell
  [[ "$(. /etc/os-release && echo $NAME)" == Raspbian* ]] && echo "ERROR: Raspberry Pi OS (32-bit) detected, please use the Raspbian repos."
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/daily/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:daily.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:daily/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_daily.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```
  

  Experimental builds

  These builds are provided without support, please **do not file issues** relating to Experimental builds.

  Experimental Support: `forky` (testing), `sid` (unstable)

  **Install Debian 14 (`forky`):**

  ```shell
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Debian_Testing/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Debian_Testing/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

  **Install Debian unstable (`sid`):**

  ```shell
  echo 'deb http://download.opensuse.org/repositories/network:/Meshtastic:/beta/Debian_Unstable/ /' | sudo tee /etc/apt/sources.list.d/network:Meshtastic:beta.list
  curl -fsSL https://download.opensuse.org/repositories/network:Meshtastic:beta/Debian_Unstable/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_Meshtastic_beta.gpg > /dev/null
  sudo apt update
  sudo apt install meshtasticd
  ```

[MUI]: /docs/configuration/device-uis/meshtasticui/
[WebClient]: /docs/software/web-client/
[USBRadio]: /docs/meshtasticd/hardware/
[SPIRadio]: /docs/meshtasticd/hardware/

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/installation/debian. GPL-3.0 (Meshtastic documentation).*
