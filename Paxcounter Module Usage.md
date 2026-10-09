# Paxcounter Module Usage

The Paxcounter module counts the number of people passing by a specific area by scanning for Wi-Fi and BLE MAC addresses. It is commonly used in retail stores, museums, and other public spaces to monitor foot traffic and gather valuable data for analysis.

In order to use this module, make sure your devices have firmware version 2.2.17 or higher.

> **Info:**
>
> This module can only be used with ESP32 devices. To operate the Paxcounter Module, it is mandatory to switch off both Wi-Fi and Bluetooth in your Network and Bluetooth settings.

## Paxcounter Module Config Values

### Enabled

Whether the Module is enabled.

### Update Interval

The interval in seconds of how often we can send a message to the mesh when a state change is detected.

## Paxcounter Module Client Availability

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

> **Info:**
>
> Paxcounter Config options are available for Android.
>
> 1. Open the Meshtastic App
> 2. Navigate to: **Settings >  Paxcounter**
>

**apple**

### Apple

> **Info:**
>
>
> All Paxcounter config options are available on iOS, iPadOS and macOS at Settings > Module Configuration > Paxcounter.
>

**cli**

### CLI

> **Info:**
>
>
> All Paxcounter Module config options are available in the python CLI version 2.2.16 and higher.
>

Example commands are below:

```shell title="Enable/Disable the Paxcounter Module"
meshtastic --set paxcounter.enabled true
meshtastic --set paxcounter.enabled false
```

```shell title="Set the Minimum Broadcast Interval to 900 seconds"
meshtastic --set paxcounter.paxcounter_update_interval 900
```

```shell title="Get the Paxcounter Module Configuration"
meshtastic --get paxcounter
```

**web**

### Web

> **Info:**
>
>
> All Paxcounter module config options are available in the Web UI.
>

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/module/paxcounter. GPL-3.0 (Meshtastic documentation).*
