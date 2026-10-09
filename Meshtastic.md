# Meshtastic

Meshtastic

A LILYGO TTGO T-Beam running in client mode on battery power

- International standard Based on [LoRa](LoRa.md), Bluetooth, Wi-Fi
- Compatible hardware Supports ESP32, nRF52840 and others
- Typically 2–5 km (1.2–3.1 mi), upwards of 100 km (62 mi) possible via mesh 331 km (206 mi) Community range record.
- Website meshtastic.org

**Meshtastic** is a [LoRa](LoRa.md)-based mesh networking protocol and software platform. The main goal of the project is enabling low-power, long-range communication over ISM radio bands. It transmits at power levels which do not require a license to use. It is designed around exchanging text messages and data in off-grid environments, with potential applications in IoT projects where a decentralized communication system is needed without existing infrastructure.

Meshtastic uses [LoRa](LoRa.md) peer to peer (P2P), a long-range radio protocol, to form a mesh network by rebroadcasting messages to extend communication reach. Each device can connect with a single phone, enabling messaging in off-grid areas, making it useful for not only messages, but also data transmission.

Meshtastic was created by Kevin Hester in early 2020 as a solution for communication during hobbies where reliable internet access is unavailable. The project operates as a grassroots, community-driven endeavor with established local communities, maintaining a strong DIY ethos. The software is open source, with hundreds of contributors participating in its development.

### Use cases and applications

Meshtastic has found applications in various scenarios where traditional communication infrastructure is unavailable or unreliable. The Mars Society, a nonprofit advocating for Mars exploration, uses Meshtastic T-Echo radios for communication during analog astronaut missions in remote areas. These expeditions can last weeks in locations with little cellular or Wi-Fi connectivity, where communication is critical for safety due to risks such as heat stroke and distance from medical facilities.

Other common use cases include hiking in remote areas, communication during natural disasters, and maintaining contact in areas with internet censorship. Some municipalities are exploring the deployment of Meshtastic networks as backup communication systems to protect communities during natural disasters. The system's optional location-tracking capabilities allow users to monitor community members without relying on data-intensive commercial applications.

### Limitations

The system requires line-of-sight communication between devices, meaning obstructions such as buildings, trees, hills, or mountains can prevent successful mesh network connections. Network reliability depends on having multiple Meshtastic nodes in the operational area.

The system is limited to text messaging and cannot serve as an internet replacement, though messages can include emojis. Bandwidth limitations can cause network congestion when many users attempt to communicate simultaneously. This was demonstrated at the 2024 Hamvention in Dayton, Ohio, where the network crashed after excessive traffic from a single user's MQTT bridge overwhelmed the system. In response, developers created specialized firmware for large events, allowing between 2,000 and 2,500 nodes to operate simultaneously at conferences such as DEF CON. The event version makes use of "Short Turbo" mode, for quicker broadcast bursts, and limits rebroadcasting.

### Hardware

Meshtastic uses hardware development boards, based on micro controllers like ESP32 and nRF52840, that support LoRa and BLE communication technologies, and optionally, GNSS receivers and WiFi transceivers. These devices enable seamless mobile app connectivity via Bluetooth or Wi-Fi, allowing long-range message retransmission across a mesh network using LoRa transceivers. This setup is ideal for developing communicators that do not rely on conventional infrastructure.

Supported hardware includes devices from manufacturers such as RAK Wireless, Heltec Automation, LilyGo, and Seeed Studio, among others. The project maintains an official compatibility list distinguishing between actively supported devices and those with community-maintained support.

Commercial purpose-built Meshtastic boards, kits and complete devices are available.

### Roles

The behavior of each node on the mesh network is determined largely by its declared role. This role is set on each node, by the user (or based on default configuration). All roles allow for the sending and receiving of messages, but differentiate other factors, including the rebroadcast of other users' messages, and the amount and type of telemetry it sends automatically.

#### Client

The "client" role is considered the best for typical devices and typical users. The client role is set by default, and will cause the node to operate using settings which are considered optimal for the average user. It will announce itself to its neighbors, and send telemetry. Under this role, it will also rebroadcast messages which have not been resent by a neighbor.

#### Client_mute

The "client mute" role is similar to client, except it will not attempt to rebroadcast the messages of others. When a user has more than one node, this role should typically be applied to the additional nodes. Multiple nodes in the same place, using the client role, risk causing the messages of other users reach a dead-end, impairing message propagation through the network. Typically, a small node in the user's pocket, will not provide a significant benefit to the overall network's reach and coverage. Therefore, they are typically set to client mute.

#### Client_hidden

The "client hidden" role is less commonly used, but can be best for niche situations. This directs the node to only broadcast when it must. Telemetry is not automatically sent, and messages from others users are not rebroadcast. This can be useful when battery power must be preserved to the greatest extent possible.

#### Client_base

The "client base" role operates much as client, but prioritizes rebroadcasting messages from other nodes which the user has marked as "favorite." If a user has a well-positioned node, such as on their roof or in a tree, this role is recommended for that device. This will ensure their messages (such as from a pocket node), get retransmitted by that "best available" local radio.

#### Tracker

The tracker role is exactly what the name suggests. This is intended for devices with the primary purpose of broadcasting their GPS locations, like off-grid AirTags. Location broadcasts are prioritized over all others.

#### Lost and found

This is a special purpose role, intended for the recovery of lost devices. In the case of trackers, this also means locating the item it is tracking. This is a noisy role intended for use only in unusual circumstances. The node broadcasts its GPS location as messages, on the public channel, to help with recovery efforts.

#### Sensor

As the name suggests, this role is intended for devices set up with the purpose of collecting data, such at weather stations. Telemetry transmissions are prioritized above all others.

#### TAK and TAK_TRACKER

These are special purpose roles for ATAK (tactical) system communication. "TAK tracker" is comparable to the "tracker" role, prioritizing the transmission of location telemetry.

#### Repeater

This role is for infrastructure devices. Under this configuration, all messages received will be rebroadcast one time. The repeater itself will not appear on other users' node lists. A Repeater will rebroadcast each message in the first "contention window," before most other devices. This preempts a client's rebroadcast, for example.

#### Router

This role is also for infrastructure devices, and operates similarly to a repeater. However, there will be sightly more overhead traffic, as the router announces itself to other users, and provides telemetry. It will therefore appear on other users' node lists. A Router will rebroadcast each message in the first "contention window," before most other devices. This preempts a client's rebroadcast, for example.

#### Router_late

Somewhat similar to the "router" role, devices operating under this configuration will rebroadcast all messages received one time, but not immediately. The rebroadcast will occur in the last "contention window," after all other nodes have helped propagate the message through the network. This mode is intended to help fill coverage gaps, without taking priority in the process. These devices will also announce themselves to other users, thus appearing in node lists.

---

*Source: Wikipedia, Meshtastic (https://en.wikipedia.org/wiki/Meshtastic), by Wikipedia contributors, CC BY-SA 4.0.*
