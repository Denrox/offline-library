# nRF52 OTA Firmware Updates

nRF52 devices from RAK are able to accept OTA firmware updates from a mobile device over bluetooth. Older T-Echo bootloaders do not have OTA support.

> **Caution:**
>
>
> OTA firmware updates come with an increased risk of failure. If the update process fails, your device will be left in a non-working state and require physical access for intervention.
>

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
  ]}>

**android**

## Android

> **Info:**
>
> For OTA-capable devices, the Meshtastic Android app can perform OTA updates itself — connect to your device over Bluetooth, then go to **Advanced → Firmware Update** and select a release. (The **Firmware Update** entry only appears for OTA-capable devices.) No third-party DFU app is required. The instructions below use a third-party app instead, which can help when the in-app update fails or for troubleshooting.

> **Info:**
>
> As of this writing, the current Android release of the nRF DFU app (v2.3.0) is not compatible with Meshtastic firmware updates. Please use the instructions below for updating via OTA with the nRF Connect App.

OTA firmware updates are available for Android using an older release of the more advanced nRF Connect App **version 4.24.3** which is available for download from the Nordic Semiconductor GitHub page.

1. Download the firmware release you wish to install from the Meshtastic Download Page or Meshtastic GitHub.
2. Unzip the firmware folder
3. Open the nRF Connect App and select CONNECT on your device from the SCANNER tab
4. If the top right corner of the interface that is shown says DISCONNECT, proceed to step 5, if it says CONNECT, select CONNECT
5. Select the DFU icon from the top-right of the screen
6. Select OK after verifying that "Distribution Packet (ZIP)" is selected
7. Select the correct device firmware file (will end with -ota.zip)
8. The update will start automatically (this will be slow)
9. Once the update is complete, the device will reboot automatically

**apple**

## Apple

> **Info:**
>
> The Meshtastic iOS/iPadOS app can perform OTA updates itself — connect to your device over Bluetooth, then go to **Settings → Firmware Updates**. No third-party DFU app is required. The instructions below use a third-party app instead, which can help when the in-app update fails or for troubleshooting.

OTA firmware updates are available on iOS & iPadOS using the nRF Device Firmware Update App available through the Apple App Store

1. Download the firmware release you wish to install from the Meshtastic Download Page, Meshtastic GitHub, or via the iOS or iPadOS app.
2. Unzip the firmware folder
3. Open the nRF DFU App and select the correct device firmware file (will end with -ota.zip)
4. Connect to your device
5. Upload the firmware

The iPhone's auto-lock feature could potentially interrupt the Bluetooth firmware upload. To avoid this, occasionally tap on your screen, or temporarily set the auto-lock to "Never" during the upload process to ensure that the phone stays awake and the upload completes without interruption.

If the update fails, you may find that adjusting the packet settings can help:

1. In settings, enable "**Packets Receipt Notification**". 
2. Change "**Number of Packets**" to a lower value. Some users report success with "5".

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52/ota. GPL-3.0 (Meshtastic documentation).*
