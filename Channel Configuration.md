# Channel Configuration

The Channels config options are: Index, Roles, and Settings. Channel config uses an admin message sending a `Channel` protobuf which also consists of a `ChannelSettings` or `ModuleSettings` protobuf.

> **Info:**
>
> **Channel Settings** (as described on this page) should not be confused with [Modem Preset Settings](LoRa%20Configuration.md)
>
> [Modem Preset Settings](LoRa%20Configuration.md) contain the modem configuration (frequency settings, spreading factor, bandwidth, etc.) used for the LoRa radio. These settings are identical for all channels and can **not** be unique per channel.
>
> **Channel Settings** contain information for segregating message groups, configuring optional encryption, and enabling or disabling messaging over internet gateways. These settings **are** unique and configurable per channel.

## Channel Config Values

### Index

The channel index begins at 0 and ends at 7.

_Indexing_ cannot be modified.

| Index | Channel | Default Role |          Purpose          |
| :---: | :-----: | :----------: | :-----------------------: |
|   0   |    1    |  `PRIMARY`   | Used as `default` channel |
|   1   |    2    |  `DISABLED`  |       User defined        |
|   2   |    3    |  `DISABLED`  |       User defined        |
|   3   |    4    |  `DISABLED`  |       User defined        |
|   4   |    5    |  `DISABLED`  |       User defined        |
|   5   |    6    |  `DISABLED`  |       User defined        |
|   6   |    7    |  `DISABLED`  |       User defined        |
|   7   |    8    |  `DISABLED`  |       User defined        |

> **Note:**
>
> You can **not** have `DISABLED` channels in-between active channels such as `PRIMARY` and `SECONDARY`. Active channels must be consecutive.

### Role

Each channel is assigned one of 3 roles:

1. `PRIMARY` or `1`
   - This is the first channel that is created for you on initial setup.
   - Only one primary channel can exist and cannot be disabled.
   - By default, periodic broadcasts like position and telemetry are sent over this channel.
2. `SECONDARY` or `2`
   - Can modify the encryption key (PSK).
3. `DISABLED` or `0`
   - The channel is no longer available for use.
   - The channel settings are set to default.

> **Note:**
>
> While you can have a different PRIMARY channel and communicate over SECONDARY channels with the same Name & PSK, a hash of the PRIMARY channel's name sets the LoRa frequency slot, which determines the actual frequency you are transmitting on in the band.
> To ensure devices with different PRIMARY channel name transmit on the same frequency, you must explicitly set the LoRa frequency slot.

## Channel Settings Values

The Channel Settings options are: Name, PSK, Use AEAD, Downlink Enabled, Uplink Enabled, and Mute. Channel settings are embedded in the `Channel` protobuf as a `ChannelSettings` protobuf and sent as an admin message.

### Name

A short identifier for the channel. _(< 12 bytes)_

| Reserved Name  |                                                                                                                 Purpose                                                                                                                  |
| :------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `""` (default) |                                                                               If left empty on the Primary channel, this designates the `default` channel.                                                                               |
|    `admin`     | On Secondary channels, the name `admin`, in any letter case, designates the `admin` channel used to administer nodes over the mesh. It works only when [Admin Channel Enabled](Security%20Configuration.md) is on. Note that this is a Legacy feature, see [Remote Admin](Remote%20Node%20Administration.md) for details. |

> **Note:**
>
>
> Matching channel names are required in order to communicate on the same channel with other devices. Example: If your device is using the channel name `LongFast` the device you are attempting to communicate with must also have a channel named `LongFast`.
>

### PSK

The encryption key used for private channels.

Hex byte `0x01` for the Primary `default` channel.

Must be either 0 bytes (no crypto), 16 bytes (AES128), or 32 bytes (AES256).

> **Note:**
>
>
> Matching PSKs are required in order to communicate on the same channel with other devices. Example: If your device is using a channel with the default PSK of `AQ==` the device you are attempting to communicate with must also have a matching channel with the same PSK.
>

### Use AEAD

On firmware 2.8.1 and later, `use_aead` switches the channel from AES-CTR to authenticated encryption, AES-CCM. Each packet carries a 12-byte tag, and nodes reject any packet that was altered or forged by someone without the key.

Every node on the channel must turn it on. Nodes with it on and nodes with it off can't read each other's messages on that channel, even with the same name and PSK. The setting needs a PSK, is experimental, and is off by default.

### Downlink Enabled

If enabled, messages captured from a **public** internet gateway will be forwarded to the local mesh.

Set to `false` by default for all channels.

### Uplink Enabled

If enabled, messages from the mesh will be sent to the **public** internet through any node's configured gateway.

Set to `false` by default for all channels.

## Channel Config Client Availability

## Channel Module Settings

The channel module settings options are: Is muted and position precision. Channel module settings are embedded in the Channel protobuf as a ModuleSettings protobuf and sent as an admin message.

### Is Muted
If enabled, the `is_muted` setting silences invocation of the `ExternalNotificationModule` when messages are received over the specified channel(s). UI notifications such as `"New Message From []"` are also blocked from popup.

Set to `false` by default for all channels.

Control the channel's notification behaviour.

```shell title="Toggle is_muted on the PRIMARY channel"
meshtastic --ch-set module_settings.is_muted true --ch-index 0
meshtastic --ch-set module_settings.is_muted false --ch-index 0
```

### Position Precision

The `position_precision` setting allows control of the level of precision for location data that is sent over a particular channel. This can be useful for privacy reasons, where obfuscating the exact location may be desired when sending position data over certain channels.

The `position_precision` value is an integer between 0 and 32:

- A value of 0 means that location data is never sent over the given channel.
- A value of 32 means that location data is sent with full precision.
- On a channel whose key is public, which means no key, the default key, or any single-byte key, the firmware limits precision to 15 bits.
- Values in between indicate the number of bits of precision to be sent, which correspond to a position precision from the table below.
- The public MQTT server filters out precise positions.

| Precision bits | Metric  |  Imperial  |
| :------------: | :-----: | :--------: |
|       10       | 23.3 km | 14.5 miles |
|       11       | 11.7 km | 7.3 miles  |
|       12       | 5.8 km  | 3.6 miles  |
|       13       | 2.9 km  | 1.8 miles  |
|       14       | 1.5 km  | 4787 feet  |
|       15       |  729 m  | 2392 feet  |
|       16       |  364 m  | 1194 feet  |
|       17       |  182 m  |  597 feet  |
|       18       |  91 m   |  299 feet  |
|       19       |  45 m   |  148 feet  |

The client applications have implemented different levels of precision giving the user a practical range to choose from. Setting across the full range of integers can be done via the Python CLI. See Setting Position Precision for examples on setting different levels of precision using CLI.

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
> All Channel config options are available for Android.
>
> 1. Open the Meshtastic App
> 2. Navigate to: **Settings > Channels**
>

**apple**

### Apple

> **Info:**
>
>
> A channel editor is available on the iOS, iPadOS and macOS applications at Settings > Radio Configuration > Channels.
>

**cli**

### CLI

> **Info:**
>
> All Channel config options are available in the python CLI. Example commands are below:

> **Tip:**
>
>
> Because the device will reboot after each command is sent via CLI, it is recommended when setting multiple values in a config section that commands be chained together as one.
>
> ```shell title="Example:"
> meshtastic --ch-set name "My Channel" --ch-set psk random --ch-set uplink_enabled true --ch-index 4
> ```
>

#### Name

```shell title="Set channel name for the PRIMARY channel"
# without spaces
meshtastic --ch-set name MyChannel --ch-index 0
# with spaces
meshtastic --ch-set name "My Channel" --ch-index 0
```

#### PSK

If you use Meshtastic for exchanging messages you don't want other people to see, `random` is the setting you should use. Selecting `default` or any of the `simple` values from the following table will use publicly known encryption keys. They're shipped with Meshtastic source code and thus, anyone can listen to messages encrypted by them. They're great for testing and public channels.

|        Setting         |                                       Behavior                                        |
| :--------------------: | :-----------------------------------------------------------------------------------: |
|         `none`         |                                  Disable Encryption                                   |
|       `default`        |                   Default Encryption (use the weak encryption key)                    |
|        `random`        | Generate a secure 256-bit encryption key. Use this setting for private communication. |
| `simple0`- `simple254` |                      Uses a single byte encoding for encryption                       |

```shell title="Set encryption to default on PRIMARY channel"
meshtastic --ch-set psk default --ch-index 0
```

```shell title="Set encryption to random on PRIMARY channel"
meshtastic --ch-set psk random --ch-index 0
```

```shell title="Set encryption to single byte  on PRIMARY channel"
meshtastic --ch-set psk simple15 --ch-index 0
```

```shell title="Set encryption to your own key on PRIMARY channel"
meshtastic --ch-set psk 0x1a1a1a1a2b2b2b2b1a1a1a1a2b2b2b2b1a1a1a1a2b2b2b2b1a1a1a1a2b2b2b2b --ch-index 0
```

```shell title="Set encryption to your own key on PRIMARY channel (Base64 encoded)"
meshtastic --ch-set psk base64:puavdd7vtYJh8NUVWgxbsoG2u9Sdqc54YvMLs+KNcMA= --ch-index 0
```

> **Tip:**
>
> Use this to copy and paste the `base64` encoded (single channel) key from the meshtastic --info command. Please don't use the omnibus (all channels) code here, it is not a valid key.

```shell title="Disable encryption on PRIMARY channel"
meshtastic --ch-set psk none --ch-index 0
```

#### Uplink / Downlink

For configuring gateways, please see [MQTT](MQTT%20Module%20Configuration.md)

```shell title="Enable/Disable Uplink on PRIMARY channel"
meshtastic --ch-set uplink_enabled true --ch-index 0
meshtastic --ch-set uplink_enabled false --ch-index 0
```

```shell title="Enable/Disable Downlink on SECONDARY channel"
meshtastic --ch-set downlink_enabled true --ch-index 1
meshtastic --ch-set downlink_enabled false --ch-index 5
```

#### Setting Position Precision

> **Info:**
>
>
> This is a per-channel setting. The `--ch-index` parameter must be specified to set the position precision for a specific channel, e.g., `--ch-index 0` for the primary channel or `--ch-index 1` for the secondary channel 1.
>

```shell title="Set position precision to 13 bits (approx ±3 km)"
meshtastic --ch-set module_settings.position_precision 13 --ch-index 0
```

```shell title="Set position precision to full precision (32 bits)"
meshtastic --ch-set module_settings.position_precision 32 --ch-index 1
```

**web**

### Web

> **Info:**
>
> All Channel config options are available in the Web UI.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/radio/channels. GPL-3.0 (Meshtastic documentation).*
