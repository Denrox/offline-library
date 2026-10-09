# Radio Configuration

There are several config sections in the Meshtastic firmware, these are broken out so they can be sent as small admin messages over the mesh.

|           Name           |                                                                                        Description                                                                                        |
| :----------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Bluetooth](Bluetooth%20Settings.md) |                                                          The bluetooth config options are: Enabled, Pairing Mode and Fixed PIN.                                                           |
|  [Channels](Channel%20Configuration.md)  |                                                                The channels config options are: Index, Role and Settings.                                                                 |
|    [Device](Device%20Configuration.md)    |                                                  The device config options are: Device Role, Serial Output, Debug Log and Factory Reset.                                                  |
|   [Display](Display%20Configuration.md)   |                                      The display config options are: Screen On Duration, Auto Carousel Interval, Always Point North, and GPS Format.                                      |
|      [LoRa](LoRa%20Configuration.md)      |    The LoRa config options are: Region, Modem Preset, Max Hops, Transmit Power, Bandwidth, Spread Factor, Coding Rate, Frequency Offset, Transmit Disabled and Ignore Incoming Array.     |
|   [Network](Network%20Configuration.md)   |                                               The network config options are: Wi-Fi Enabled, Wi-Fi SSID, Wi-Fi PSK, Wi-Fi Mode and NTP Server.                                                |
|  [Position](Position%20Configuration.md)  |            The position config options are: GPS Enabled, GPS Update Interval, GPS Attempt Time, Fixed Position, Smart Broadcast, Broadcast Interval and Position Packet Flags.            |
|     [Power](Power%20Configuration.md)     | The power config options are: Charge Current, Power Saving, Shutdown after losing power, ADC Multiplier Override Wait Bluetooth Interval, Light Sleep Interval and Minimum Wake Interval. |
|  [Security](Security%20Configuration.md)  |                              The security config options are: Public Key, Private Key, Admin Key, Is Managed, Serial Console, Debug Logs, and Admin Channel.                              |
|      [User](User%20Configuration.md)      |                                                            The user config options are: Long Name, Short Name, Is Licensed, and Is Unmessageable                                          |

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/radio/config. GPL-3.0 (Meshtastic documentation).*
