# Command-line satellite tracking software

*Tags: satellites, software, gpredict · score 4*

## Question

Is there any software similar to Gpredict but which can be used without a GUI and can control rotor Az/EL and radio doppler shift? I'm using Linux in particular, especially Ubuntu 14.04.

Currently, I can control rotors and radio via Gpredict's interface, but it requires manually selecting the satellite and tracking it. I want to script this process — provide TLE files and satellite to track and automatically record the downlink (mainly CW beacons) so that I can track multiple satellites without issuing manual commands for each one.

Basically, I'm looking for a command-line interface to Gpredict.

## Answer (score 3, by Juancho)

Predict is the option that comes to mind. It is console based (no GUI), and provides a *server mode* where you can request data via UDP messages to a running predict server.

It uses hamlib for rotor control.

N.B.: predict *does not* provide transceiver control. You can get the current Doppler (normalized to 100MHz) via UDP queries, so you will need some extra scripting to control your transceiver having this information. I'm personally trying this out.

Predict is very stable (I've had an instance running for months).

You can install it directly from your package manager.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3799/command-line-satellite-tracking-software, by user80551, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
