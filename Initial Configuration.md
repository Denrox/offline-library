# Initial Configuration

## Supported Clients per Connection Type

Depending on your connection, some configuration options are not fully supported. Find out which client is best for your type of connection.

           Serial
        </>
      ),
      value: "serial",
    },
    {
      label: (
        <>
           Bluetooth
        </>
      ),
      value: "ble",
    },
    {
      label: (
        <>
           Network
        </>
      ),
      value: "network",
    },
  ]}>

**serial**

### Serial

- [Python CLI](Meshtastic%20Python%20CLI%20Guide.md)
- Web Client
- [Android App](User%20Guide.md)

**ble**

### Bluetooth

- [Android App](User%20Guide.md)
- Web Client

**network**

### Network

> **Info:**
>
> Connecting over network is only supported on ESP32 devices.

- Web Client
- [Android App](User%20Guide.md)
- [iOS App](User%20Guide%20%28user%29.md)
- [Python CLI](Meshtastic%20Python%20CLI%20Guide.md)

## Set Regional Settings

In order to start communicating over the mesh, you must set your region. This setting controls which frequency range your device uses and should be set according to your regional location.

           Android
        </>
      ),
      value: "android",
    },
    {
      label: (
        <>
           Apple
        </>
      ),
      value: "apple",
    },
    {
      label: (
        <>
           CLI
        </>
      ),
      value: "cli",
    },
    {
      label: (
        <>
           Web
        </>
      ),
      value: "web",
    },
  ]}>

**android**

### Android

1. Follow the [setup and usage instructions](User%20Guide.md) for [Meshtastic Android](Android%20App.md).
2. Open the app, connect to the device from your phone over USB Serial or Bluetooth.
3. Once paired and connected, Click **SET YOUR REGION** under the connected device card. or navigate to **Settings > LoRa**.
4. Select the region from the list according to your regional location. Click **Send**

**apple**

### Apple

> **Info:**
>
> Configuration of Region, Modem Preset and Hop Limit is available on iOS, iPadOS and macOS at Settings > Radio Configuration > LoRa.

**cli**

### CLI

1. Install [Meshtastic PythonCLI](Meshtastic%20Python%20CLI%20installation.md)
   ```sh
   pip3 install --upgrade pytap2
   pip3 install --upgrade meshtastic
   ```
2. Run the following command, replacing `` with the region code listed above according to your regional location.
   ```sh
   meshtastic --set lora.region <REGION-CODE>
   ```

**web**

### Web

1. Open the Meshtastic Web interface: client.meshtastic.org
2. Navigate to the **LoRa** menu.
3. Under **Regional Settings**, set your **Region** according to your regional location.
4. Click **Save**.

### Region Codes

| Region Code  |          Description           | Frequency Range (MHz) | Duty Cycle (%) | Power Limit (dBm) |
|:------------:|:------------------------------:|:---------------------:|:--------------:|:-----------------:|
|   `UNSET`    |             Unset              |          N/A          |      N/A       |        N/A        |
|     `US`     |         United States          |     902.0 - 928.0     |      100       |        30         |
|   `EU_433`   |     European Union 433 MHz      |     433.0 - 434.0     |       10       |        10         |
|   `EU_868`   |     European Union 868 MHz      |    869.4 - 869.65     |       10       |        27         |
|   `EU_866`   |     European Union 866 MHz      |     865.6 - 867.6     |    2.5 / 10    |        27         |
|  `EU_N_868`  | European Union 868 MHz (Narrow) |    869.4 - 869.65     |       10       |        27         |
|     `CN`     |             China              |     470.0 - 510.0     |      100       |        19         |
|     `JP`     |             Japan              |     920.5 - 923.5     |      100       |        13         |
|    `ANZ`     |    Australia & New Zealand     |     915.0 - 928.0     |      100       |        30         |
|  `ANZ_433`   |    Australia & New Zealand     |    433.05 - 434.79    |      100       |        14         |
|     `KR`     |             Korea              |     920.0 - 923.0     |      100       |        23         |
|     `TW`     |             Taiwan             |     920.0 - 925.0     |      100       |        27         |
|     `RU`     |             Russia             |     868.7 - 869.2     |      100       |        20         |
|     `IN`     |             India              |     865.0 - 867.0     |      100       |        30         |
|   `NZ_865`   |       New Zealand 865 MHz       |     864.0 - 868.0     |      100       |        36         |
|     `TH`     |            Thailand            |     920.0 - 925.0     |       10       |        27         |
|   `UA_433`   |         Ukraine 433 MHz         |     433.0 - 434.7     |       10       |        10         |
|   `MY_433`   |        Malaysia 433 MHz         |     433.0 - 435.0     |      100       |        20         |
|   `MY_919`   |        Malaysia 919 MHz         |     919.0 - 924.0     |      100       |        27         |
|   `SG_923`   |        Singapore 923 MHz        |     917.0 - 925.0     |      100       |        20         |
|   `KZ_433`   |       Kazakhstan 433 MHz       |   433.075 - 434.775   |      100       |        10         |
|   `KZ_863`   |       Kazakhstan 863 MHz       |     863.0 - 868.0     |      100       |        30         |
|   `BR_902`   |         Brazil 902 MHz          |     902.0 - 907.5     |      100       |        30         |
|   `PH_433`   |       Philippines 433 MHz       |     433.0 - 434.7     |      100       |        10         |
|   `PH_868`   |       Philippines 868 MHz       |     868.0 - 869.4     |      100       |        14         |
|   `PH_915`   |       Philippines 915 MHz       |     915.0 - 918.0     |      100       |        24         |
|   `NP_865`   |          Nepal 865 MHz          |     865.0 - 868.0     |      100       |        30         |
|  `ITU1_2M`   |    ITU Region 1 Amateur 2m     |     144.0 - 146.0     |      100       |        30         |
|  `ITU2_2M`   |    ITU Region 2 Amateur 2m     |     144.0 - 148.0     |      100       |        30         |
|  `ITU3_2M`   |    ITU Region 3 Amateur 2m     |     144.0 - 148.0     |      100       |        30         |
| `ITU2_125CM` |   ITU Region 2 Amateur 1.25m   |     220.0 - 225.0     |      100       |        30         |
| `ITU1_70CM`  |   ITU Region 1 Amateur 70cm    |     430.0 - 440.0     |      100       |        30         |
| `ITU2_70CM`  |   ITU Region 2 Amateur 70cm    |     420.0 - 450.0     |      100       |        30         |
| `ITU3_70CM`  |   ITU Region 3 Amateur 70cm    |     430.0 - 450.0     |      100       |        30         |
|  `LORA_24`   |     2.4 GHz band worldwide     |    2400.0 - 2483.5    |      100       |        10         |

`EU_433` and `EU_868` are limited to a 10% duty cycle, calculated every minute over a rolling hour. A node that reaches the limit stops transmitting until it's allowed again. `EU_866` is limited to 2.5%, or 10% for a node in the `ROUTER` or `ROUTER_LATE` role.

`EU_868`, `EU_866`, and `EU_N_868` cover the same European band with different channel plans, and each accepts only its own presets. Selecting a preset that belongs to one of the others switches the region to it.

The `ITU1_*`, `ITU2_*`, and `ITU3_*` regions are amateur radio allocations and can only be selected in [licensed mode](User%20Configuration.md). **Do not use them without an amateur radio license.** Review the [privileges and restrictions](FAQs.md) of operating under an amateur license first: encryption is not permitted, and you must transmit your call sign.

The listed power limit is the ceiling the firmware applies, not your national limit. Some countries do not allocate the full range shown, for example 220–222 MHz in the USA and Canada. Check your national band plan before transmitting.

Refer to [LoRa Region by Country](LoRa%20Region%20by%20Country.md) for a more comprehensive list.

## Continue Configuration

Now that you have set the LoRa region on your device, you can continue with configuring any additional configs to suit your needs.

  
    Device Configuration

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/initial-config. GPL-3.0 (Meshtastic documentation).*
