# Network Configuration

The Network config options are: NTP Server, Wi-Fi Enabled, Wi-Fi SSID, Wi-Fi PSK, Ethernet Enabled, IPv4 Networking Mode, Static Address rsyslog Server, and Protocol Flags. Network config uses an admin message sending a `Config.Network` protobuf.

> **Info:**
>
> Enabling Wi-Fi will disable Bluetooth. Only one connection method will work at a time.

ESP32 devices have the ability to connect to Wi-Fi as a client. SoftAP mode is not supported by the Meshtastic firmware.

## Network Config Values

### NTP Server

The NTP server used if IP networking is available.

Set to `meshtastic.pool.ntp.org` by default. (Max Length: 32)

### Wi-Fi Enabled

Enables or Disables Wi-Fi.

Set to `false` (Disabled) by default.

### Wi-Fi SSID

This is your Wi-Fi Network's SSID.

Empty `""` by default. (Case Sensitive, Max Length: 32)

### Wi-Fi PSK

This is your Wi-Fi Network's password.

Empty `""` by default. (Case Sensitive, Max Length: 64)

> **Warning:**
>
> Setting Wi-Fi credentials, or performing any other local administration, over an untrusted Wi-Fi network exposes that traffic to the network. See Local Administration Over Wi-Fi for the trust-boundary details.

### Ethernet Enabled

Enables or Disables Ethernet.

Set to `false` (Disabled) by default.

### IPv4 Networking Mode

Set to `DHCP` by default. Change to `STATIC` to use a static IP address. Applies to both Ethernet and Wi-Fi.

### IPv4 Static Address configuration

Contains IP, Gateway, Subnet, and DNS server for a static configuration if selected in Networking Mode.

### Rsyslog Server

To configure an rsyslog Server and Port. Default logging facility is `user`.

### Protocol Flags

Defines which auxiliary network protocols are used to send packets. Values are stored as a bit field of boolean configuration options (bitwise OR of ProtocolFlags).

|     Value     |                        Description                         |
| :-----------: | :--------------------------------------------------------: |
| NO_BROADCAST  |     Do not broadcast packets over any network protocol     |
| UDP_BROADCAST | Enable broadcasting packets via UDP over the local network |

> **Tip:**
>
> The first time your device restarts after enabling Wi-Fi or Ethernet, it will take an additional 20-30 seconds to boot. This is to generate self-signed SSL keys. The keys will be saved for future reuse.

## Network Config Client Availability

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
>
> Network Config options are available for Android.
>
> 1. Open the Meshtastic App
> 2. Navigate to: **Settings >  Network**
>

**apple**

### Apple

> **Info:**
>
>
> All Network config options are available on iOS, iPadOS and macOS at Settings > Device Configuration > Network.
>

**cli**

### CLI

> **Info:**
>
>
> All Network config options are available in the python CLI.
>

|       Setting        | Acceptable Values |          Default          |
| :------------------: | :---------------: | :-----------------------: |
|  network.ntp_server  |      string       | `meshtastic.pool.ntp.org` |
| network.wifi_enabled |  `true`, `false`  |          `false`          |
|  network.wifi_ssid   |      string       |           `""`            |
|   network.wifi_psk   |      string       |           `""`            |
| network.eth_enabled  |  `true`, `false`  |          `false`          |
| network.address_mode | `DHCP`, `STATIC`  |          `DHCP`           |

> **Tip:**
>
>
> Because the device will reboot after each command is sent via CLI, it is recommended when setting multiple values in a config section that commands be chained together as one.
>
> ```shell title="Example:"
> meshtastic --set network.wifi_enabled true --set network.wifi_ssid "my network" --set network.wifi_psk mypassword
> ```
>

```shell title="Set NTP Server"
meshtastic --set network.ntp_server "meshtastic.pool.ntp.org"
```

```shell title="Enable / Disable Wi-Fi"
meshtastic --set network.wifi_enabled true
meshtastic --set network.wifi_enabled false
```

```shell title="Set Wi-Fi SSID"

meshtastic --set network.wifi_ssid mynetwork
// With spaces
meshtastic --set network.wifi_ssid "my network"
```

```shell title="Set Wi-Fi password"
meshtastic --set network.wifi_psk mypassword
// With spaces
meshtastic --set network.wifi_psk "my password"
```

**web**

### Web

> **Info:**
>
> All Network config options are available in the Web UI.

## Examples

### Wi-Fi Client

With `network.wifi_ssid` & `network.wifi_psk` populated, the device will know to connect to your network. Make sure you are in range of your Wi-Fi and it is a 2.4GHz-only network. If you have a single Meshtastic device on your local network it's easy to connect to your device with DNS `http://meshtastic.local`. If you have multiple Meshtastic devices you will need to connect using their respective IP addresses.

### Disable Wi-Fi

To disable Wi-Fi completely, set `network.wifi_enabled` to `false`.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/radio/network. GPL-3.0 (Meshtastic documentation).*
