# RAK WisBlock Screens

There are currently two different screens supported by the RAK WisBlock system:

**OLED Display**

## RAK1921 OLED Display

The RAK1921 OLED display is a 0.96 inch monochrome display.

- 0.96 inch OLED display
- Resolution 128 x 64 pixels
- I2C interface

This item requires soldering.
Similar modules are widely available from other suppliers, but do check the boards as some have the VDD and GND pins swapped round. This will prevent directly soldering the display to the baseboard. The preferred order is VDD, GND, SCL, SDA.
If pin ordering on the OLED board are swapped, there are some tricks to allow either reconfiguring the pins of the OLED via soldered jumpers, or by carefully soldering wire for those pins that are out-of-sequence. The final option is to use longer wires between the board and display, which permits re-ordering the wires as required.

### Resources

- RAK Documentation Center
- Purchase Links:
  - US
    - Rokland
    - muzi ᴡᴏʀᴋꜱ
  - International
    - RAKwireless
    - RAKwireless AliExpress

**E-Ink Display**

## RAK14000 E-Ink Display

The RAK14000 EPD module is an ultra low power E-Ink display with three user buttons.

- 2.13 inch black and white E-Ink display
- Three button module
- Resolution 212 x 104 pixels
- Occupies the IO Port of a Wisblock Base

Please note only the white-black display is supported at this time, the white-black-red display may work, but is not supported.

### Resources

- Firmware for 5005 with RAK14000 e-paper: `firmware-rak4631_eink-X.X.X.xxxxxxx.uf2`
- RAK Documentation Center
- Purchase Links:
  - US
    - Rokland
  - International
    - RAKwireless
    - RAKwireless AliExpress

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/screens. GPL-3.0 (Meshtastic documentation).*
