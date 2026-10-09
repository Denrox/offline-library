# Web Client Overview

Meshtastic Web is a Meshtastic client that runs directly in your browser.
There are two ways of accessing the app:

1. A hosted version located at client.meshtastic.org.
2. Hosting it yourself.

## Compatibility

The application will work in all major browsers, but specific functionality is limited in some cases. For the best experience we recommend using a Chromium based browser such as Google Chrome or Microsoft Edge.

### HTTP

This method of connecting is limited to esp32 devices.

> **Caution:**
>
>
> When using the hosted version of the application, all traffic must be served over HTTPS.
> Meshtastic nodes generate self-signed certificates, and you must inform your browser that you wish to trust the aforementioned certificate.
> This can be done by first accessing your node directly via your browser: `https://NODE_IP_ADDRESS/` replacing `NODE_IP_ADDRESS` with the IP address of your node.
> This can be found on the screen of the device, via your router's DHCP lease page or serial console.
>

You can accessing your device over HTTP after you set up your [Network Connection](Network%20Configuration.md)

### Bluetooth

Bluetooth support is governed by the availability of the Web Bluetooth API as illustrated below. Support is primarily available in Chromium based browsers.

### Serial (USB)

The method with the least platform support, which uses the Web Serial API, allows us to connect directly to a Meshtastic node over USB and access it from directly within your browser.

## Self Hosting

The source code for the WebUI can be found on our GitHub

Instructions for building and running the project can be found in the repo's readme.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/software/web-client. GPL-3.0 (Meshtastic documentation).*
