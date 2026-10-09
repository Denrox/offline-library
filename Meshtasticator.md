# Meshtasticator

**Meshtasticator** is a discrete-event and interactive simulator that replicates the radio section of the device software. It helps evaluate the performance of various scenarios and the scalability of the protocol. The **Meshtasticator** simulator can be found on GitHub.

## Discrete-Event Simulator

The discrete-event simulator models the radio section of the device software to analyze its behavior. It can assess the performance of specific scenarios and the scalability of the protocol.

### Getting Started

For step-by-step instructions on how to use the discrete-event simulator, see the [discrete-event simulator usage guide](Discrete%20Event%20Simulator%20Usage%20Guide.md).

### Simulation Insights

After each simulation, the tool plots node placements and schedules the timing for overlapping messages sent during the simulation.

The simulator allows network analysis using different parameter sets. For example, below are the results of 100 simulations, each lasting 200 seconds, with varying hop limits and node counts. As expected, the average number of nodes reached per message increases with a higher hop limit.

However, this improvement comes with a trade-off in **usefulness**—the proportion of received packets containing new (non-duplicate) messages decreases as rebroadcasting increases.

## Interactive Simulator

The interactive simulator leverages the Linux-native Meshtastic application, i.e., the real device software, while emulating some hardware components, including the LoRa chip. It can also run on Windows or macOS using Docker.

### Setup Instructions

To get started with the interactive simulator, see the [interactive simulator usage guide](Interactive%20Simulator%20Usage%20Guide.md).

### Debugging and Visualization

This simulator facilitates debugging multiple communicating nodes without needing physical devices.

  

Additionally, because the simulator has an 'oracle view' of the network, it provides insights into the routes taken by messages.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/software/meshtasticator/meshtasticator. GPL-3.0 (Meshtastic documentation).*
