# MeshCore

- MeshCore
- Original authors Scott Powell and Liam Cottle
- Developer MeshCore community
- Written in C++
- Operating system Embedded systems
- Platform LoRa-enabled hardware
- Type Mesh networking
- License MIT License
- Website meshcore.io
- Repository

- github.com/meshcore-dev/MeshCore

**MeshCore** is a [LoRa](LoRa.md)-based mesh networking protocol and software project created by Scott Powell in 2024. It is designed for low power off-the-grid text communication, therefore not depending on cellular networks. The software is published under the MIT License.

MeshCore is often compared to [Meshtastic](Meshtastic.md), another LoRa-based mesh networking protocol. Meshtastic utilizes member roles, to define the intended purpose of each node, but it largely relies on broadcast-style message flooding to increase range and chances of successful delivery, at the cost of bandwidth utilization. MeshCore also employs flood broadcasts for all public channels, but enforces node roles more, emphasizing structured routing roles and store-and-forward mechanisms to reduce bandwidth utilization, at the cost of multi-hop range and coverage. This differentiation results in different scalability and energy-consumption characteristics between the two.

### Characteristics

MeshCore allows LoRa-enabled embedded devices to form self-organizing mesh networks in which messages can be relayed across multiple intermediate nodes. The project emphasizes low power consumption, scalability, and structured routing roles, distinguishing it from broadcast-based LoRa mesh systems.

MeshCore is designed to run on microcontroller-based hardware equipped with LoRa transceivers, including boards based on the ESP32 platform. Commonly used devices include Heltec LoRa32 and LilyGo LoRa development boards. Devices operate in unlicensed ISM frequency bands such as 868 MHz and 915 MHz, depending on regional regulations. In 2025 LILYGO brought out the first Meshcore smartphone: T-Display P4.

The software consists of firmware flashed onto supported devices and optional companion applications used for configuration and messaging.

#### Features

- Decentralized architecture: nodes communicate peer-to-peer without centralized servers.
- Multi-hop routing: messages can traverse multiple relay nodes to extend range.
- Low-power operation: optimized for battery-powered embedded devices using LoRa radios.
- Encryption support: optional end-to-end encryption mechanisms are available (as described in project documentation).
- Role-based nodes: includes companion nodes, repeaters, and room servers to structure network behavior.

#### Limitations

- Low data throughput: LoRa modulation supports only low-bandwidth text or telemetry data.
- Environmental constraints: range and reliability are affected by terrain, obstacles, and antenna placement.
- Setup complexity: reviewers have noted fragmented documentation and a steep learning curve for new users.
- Regulatory constraints: operation is subject to regional ISM band regulations and transmit power limits.
- Setup style: MeshCore is based more on fixed infrastructure. This means that instead of all devices contributing to the mesh network, only repeaters can act as mesh nodes, retransmitting data. This makes it more difficult for messages to be sent over long distances, but could also be considered a feature in areas of high radio density. Each message is being repeated fewer times by fewer nodes, resulting in less packet collisions and errors in places where the radio band is heavily utilized.

---

*Source: Wikipedia, MeshCore (https://en.wikipedia.org/wiki/MeshCore), by Wikipedia contributors, CC BY-SA 4.0.*
