# mPWRD-OS provisioning

A board with no Ethernet port needs another way onto the network the first time it boots. mPWRD-OS offers two, and which one applies depends on the board. [Board support](mPWRD-OS%20board%20support.md) lists the setup methods for each.

## Bluetooth provisioning

Raspberry Pi (64-bit) boards accept Wi-Fi credentials over Bluetooth, handled on the board by nymea-networkmanager.

The Meshtastic Flasher sends the credentials. Its Bluetooth entry appears only in a browser that supports Web Bluetooth, which in practice means a Chromium-based browser.

1. Flash the image to your board and power it on.
2. Open the Meshtastic Flasher and select **mPWRD-OS Tools**, then **BLE WiFi Provisioning**.

   

3. Select **Connect to BLE Device** and choose your board.
4. Select **Scan for Networks**, choose your network under **Available Networks**, and enter its **Password**.
5. Select **Apply**. The Flasher reports when the credentials have been applied.
6. Connect to the board over SSH.

## Web provisioning

The Luckfox Lyra Zero W and the Luckfox Lyra Ultra W start a temporary hotspot instead, served by armbian-web-config.

1. Flash the image to your board and power it on.
2. Connect a Wi-Fi capable device to the `armbiansetup` network, using the password `armbian1234`.
3. Open `http://10.42.0.1:8080`. The Armbian Setup wizard opens on its first step.

   

4. Work through the wizard's five steps: **Root**, **User**, **Locale**, **Network**, and **Advanced**.
5. Connect to the board over SSH.

The wizard sets the root password at its first step, so the default credentials do not apply to a board set up this way.

The hotspot name and password are the same on every board, so anyone in range can open the wizard on a board that has not been set up. Whoever reaches the first step sets the root password, so power on the board only where you control physical access. Do not leave it unattended before setup is complete.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/software/mpwrd-os/provisioning. GPL-3.0 (Meshtastic documentation).*
