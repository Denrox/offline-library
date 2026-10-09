# Flashing with the CLI

> **Caution:**
>
> Make sure not to power the radio on without first attaching the antenna! You could damage the radio chip!

Before you flash your device start by verifying connectivity with the device being flashed. Outlined below are steps that can be taken to verify connectivity and, if necessary, to install the appropriate drivers. If you end up needing to install drivers be sure to reboot your computer afterwards to verify the installation is complete.

> **Note:**
>
> The T-Beam 0.7 board is an earlier version of the T-Beam board, and due to changes in the design in subsequent iterations this board uses a specific firmware file different from the other T-Beam boards.
>
> `firmware-tbeam0.7-X.X.X.xxxxxxx.bin` is the correct firmware. `firmware-tbeam-X.X.X.xxxxxxx.bin` is incompatible. For all other T-Beam boards review the resources section for the correct selection.

## Command Line Interface Instructions

### Install Prerequisite Software

           Linux
        </>
      ),
      value: "linux",
    },
    {
      label: (
        <>
           macOS
        </>
      ),
      value: "macos",
    },
    {
      label: (
        <>
           Windows
        </>
      ),
      value: "windows",
    },
  ]}>

**linux**

#### Linux

Check if you have `python3` and `pip` installed with the following command

```shell
python3 --version
pip3 --version
```

If `python3` is not installed, install with

```shell
sudo apt-get update
sudo apt-get install python3
```

If `pip` is not installed, install with

```shell
sudo apt-get install python3-pip
```

  

**macos**

#### macOS

macOS comes with `Python 2.7` installed, but not `pip`. The following uses Homebrew to install `python3` which includes `pip3`. On macOS you will use `pip3` instead > of `pip`.

> **Note:**
>
> Check if you have Homebrew installed with the following command
>
> ```shell
> brew -v
> ```
>
> If it's not installed, follow the instructions on the Homebrew website before continuing.

Check if you have `python3` and `pip` installed with the following command

```shell
python3 --version
pip3 --version
```

If `python3` is not installed, install with
Install Python3

```shell
brew install python3
```

Confirm `pip3` was installed alongside `python3`

```shell
pip3 -v
```

  

**windows**

#### Windows

- Download and install Python. When installing, make sure to click `Add Python X.Y to PATH`.
- Download and install Gitbash (or other appropriate shell) and run all subsequent commands from that shell.

> **Note:**
>
> Confirm installation of `python` & `pip` with the following commands.
>
> ```shell
> py --version
> ```
>
> ```shell
> pip --version
> ```
>

  

### Install `esptool`

```shell
pip3 install --upgrade esptool
```

### Confirm Communication With Chip

           Linux
        </>
      ),
      value: "linux",
    },
    {
      label: (
        <>
           macOS
        </>
      ),
      value: "macos",
    },
    {
      label: (
        <>
           Windows
        </>
      ),
      value: "windows",
    },
  ]}>

**linux**

#### Linux

> **Important:**
>
> On Linux, you may need to explicitly declare esptool as a .py script. Use `esptool.py chip_id`.

**macos**

#### macOS

> **Important:**
>
> On macOS, you may need to explicitly declare esptool as a .py script. Use `esptool.py chip_id`.

**windows**

#### Windows

> **Important:**
>
> On Windows, you must explicitly declare esptool as a .py script. Use `esptool.py chip_id`.

  

Connect the radio to your computer using a data USB cable. Confirm your device is talking to your computer using the following command:

```shell title="Command"
esptool chip-id
```

```shell title="Expected Output"
# You should see a result similar to this:
mydir$ esptool chip-id
esptool.py v2.6
Found 2 serial ports
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
MAC: 24:6f:28:b5:36:71
Uploading stub...
Running stub...
Stub running...
Warning: ESP32 has no Chip ID. Reading MAC instead.
MAC: 24:6f:28:b5:36:71
Hard resetting via RTS pin...
```

### Download Firmware

1. Head to the Meshtastic Downloads Page to download the latest firmware.
2. Scroll down to the **Firmware** section and select one of the following, depending on your preferences:

- **Download Stable**: For stable, well-tested releases.
- **Download Alpha**: For newer, experimental releases with the latest features.

3. Once redirected to the GitHub release page, scroll down to the "Assets" section and expand it. Identify the correct firmware for your device by its architecture (e.g., `firmware-esp32s3` for ESP32-S3-based devices like the Heltec V3).
4. Download the file and take note of the download location on your system (usually in your `~/Downloads` folder).

### Navigate to Firmware Directory

1. Open a terminal and navigate (`cd`) to the directory where your firmware was downloaded. The folder name typically matches the architecture and firmware version from the zip file. For example:

```shell title="Example"
cd ~/Downloads/firmware-esp32s3-X.X.X.xxxxxxx/
```

> **Note:**
>
> Make sure to replace `esp32s3` and the version number with those corresponding to the file you downloaded.

### Install/Update Firmware

Now, proceed with the instructions below for your operating system to install or update the firmware for your specific board:

> **Caution:**
>
> Be very careful to install the correct firmware file for your board. In particular, the popular 'T-BEAM' radio from TTGO is not called 'TTGO-Lora' (that is a different board). So don't install the 'TTGO-Lora' build on a TBEAM, it won't work correctly. If you flash the incorrect device firmware, it may appear to successfully complete, yet the device will usually become unresponsive, displaying a blank screen (if equipped). Attempt to flash the correct version. Please note, while these devices are quite resilient and damage is not always likely, there is a possibility of onboard radio and peripheral damage due to incorrect GPIO pin direction

           Linux
        </>
      ),
      value: "linux",
    },
    {
      label: (
        <>
           macOS
        </>
      ),
      value: "macos",
    },
    {
      label: (
        <>
           Windows
        </>
      ),
      value: "windows",
    },
  ]}>

**linux**

#### Linux

##### Install

```shell title="Command"
./device-install.sh -f firmware-BOARD-VERSION.bin
```

##### Update

```shell title="Command"
./device-update.sh -f firmware-BOARD-VERSION-update.bin
```

  

**macos**

#### macOS

##### Install

```shell title="Command"
./device-install.sh -f firmware-BOARD-VERSION.bin
```

##### Update

```shell title="Command"
./device-update.sh -f firmware-BOARD-VERSION-update.bin
```

  

**windows**

#### Windows

##### Install

```shell title="Command"
device-install.bat -f firmware-BOARD-VERSION.bin
```

##### Update

```shell title="Command"
device-update.bat -f firmware-BOARD-VERSION-update.bin
```

  

Use the `--web` option to include the embedded [Web Client](Web%20Client%20Overview.md) during installation of the firmware.

## Connect and Configure Device

After flashing the Meshtastic firmware to the device, you can proceed with the initial configuration.

  
    Connect and Configure Device

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/esp32/cli-script. GPL-3.0 (Meshtastic documentation).*
