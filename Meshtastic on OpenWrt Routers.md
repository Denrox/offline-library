# Meshtastic on OpenWrt Routers

> **Warning:**
>
> Please submit any issues at meshtastic/openwrt, rather than the primary `firmware` project.

This page outlines the setup of Meshtastic on OpenWrt routers, utilizing the openwrt-repo.

## Prerequisites and Hardware Compatibility

Before proceeding with the setup, ensure the device meets the following requirements:

### Tested Devices

- OpenWrt One
- Raspberry Pi 3/4/5

### Hardware Compatibility

- \>2MB free flash storage.
- An unused USB port, or SPI interface.

Meshtastic OpenWrt packages are built for **every** CPU architecture supported by OpenWrt.

### Supported OpenWrt versions

- `SNAPSHOT` (`main`)
- `25.12` (stable)
- `24.10` (oldstable)
- `23.05` (legacy)
- `22.03` (legacy)

## Installation

### Installing Meshtasticd on OpenWrt

#### OpenWrt 24.10 (stable)

Connect to the router via SSH (ex: `ssh root@192.168.1.1`)

1. Add the Meshtastic OpenWrt repository

2. Install meshtasticd

```sh
opkg install meshtasticd
# Optional: install meshtasticd web interface
opkg install meshtasticd-web
```

`meshtasticd` can also be installed from the LuCI web interface, after the repo has been added.

#### OpenWrt `SNAPSHOT`

Ensure your router is running the latest `SNAPSHOT` version of OpenWrt, or install it from https://firmware-selector.openwrt.org/

Connect to the router via SSH (ex: `ssh root@192.168.1.1`)

1. Add the Meshtastic OpenWrt repository

2. Install meshtasticd

```sh
apk add meshtasticd
# Optional: install meshtasticd web interface
apk add meshtasticd-web
```

`meshtasticd` can also be installed from the LuCI web interface, after the repo has been added.

## Configuration

### Meshtasticd Configuration

See [meshtasticd configuration](Usage%20-%20meshtasticd.md)

### Persistence

- The persistent .proto db files of the portduino version of meshtasticd are stored under: `/srv/meshtasticd/.portduino/default/prefs/`.

## Using meshtasticd

### Start/Stop

Upon installing meshtasticd on your router, an init script is automatically created, and set to `auto-start` upon reboot.

The following commands can be used to control the meshtastic service:

```shell
/etc/init.d/meshtasticd status
/etc/init.d/meshtasticd start
/etc/init.d/meshtasticd stop
/etc/init.d/meshtasticd restart
```

### View Logs

meshtasticd logs are sent to OpenWrt syslog.

```shell
logread
```

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/meshtasticd/openwrt/openwrt. GPL-3.0 (Meshtastic documentation).*
