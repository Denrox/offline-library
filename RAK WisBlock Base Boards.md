# RAK WisBlock Base Boards

Operation requires both a base board and a core module.

**RAK5005-O**

## RAK5005-O

> **Caution:**
>
> The RAK5005-O is no longer in production. It is recommended to use the RAK19007 instead.

- RAK5005-O - The original WisBlock Base Board.
- **Slots**
  - (x1) Core Module slot
  - (x1) WisBlock IO Module slot
  - (x4) WisBlock Sensor Module slots
- **Buttons**
  - (x1) Reset Button
  - It may be possible to add a user button using the 13002 IO module.
- **Connectors**
  - JST PHR-2 connector for 3.7v LiPo battery (with charge controller)
  - JST-ZHR-2 connector for 5v solar panel (max 5.5v)
  - I2C, UART, GPIOs and analog input accessible with solder contacts
  - Micro USB port for debugging and power
- **Screen Support**
  - OLED screen support (OLED screen sold separately)

> **Note:**
>
> The RAK5005 (without the -O) is not compatible.

### Connectors Diagram

### Voltages

- JST PHR-2 connector for 3.7v LiPo battery.
  - Charge controller max charge rate is 500mAh.
  - Minimum input voltage for charging is 3.3v, maximum 4.3v.
- JST ZHR-2 connector for 5v solar panel.
  - Minimum input voltage to charge is 4.4v, maximum 5.5v.

Further information on the RAK5005-O can be found on the RAK Documentation Center.

 

**RAK19007**

## RAK19007

- RAK19007 - WisBlock Base Board (2nd Generation, an upgrade to the RAK5005-O)
- **Slots**
  - (x1) Core Module slot
  - (x1) WisBlock IO Module slot
  - (x4) WisBlock Sensor Module slots
- **Buttons**
  - (x1) Reset Button
  - To add a user button, you can utilize the AIN1 pin, which is exposed as pin 31 in the firmware.
- **Connectors**
  - JST PHR-2 connector for 3.7v LiPo battery.
  - JST ZHR-2 connector for 5v solar panel.
  - I2C, UART, BOOT and GPIOs accessible with solder contacts
  - USB-C port for debugging and power
- **Screen Support**
  - OLED screen support (OLED screen sold separately)

Further information on the RAK19007 can be found on the RAK Documentation Center.

### Connectors Diagram

### Voltages

- JST PHR-2 connector for 3.7v LiPo battery.
  - Charge controller max charge rate is 350mAh.
  - Minimum input voltage for charging is 3.3v, maximum 4.3v.
- JST ZHR-2 connector for 5v solar panel.
  - Minimum input voltage to charge is 4.4v, maximum 5.5v.

### Resources

- Purchase Links:
  - US
    - Rokland
  - International
    - RAKwireless
    - RAKwireless Starter Kit
    - RAKwireless AliExpress
    - RAKwireless AliExpress Starter Kit
    - HexaSpot

 

**RAK19003**

## RAK19003

- RAK19003 - WisBlock's Mini Base Board.
- **Slots**
  - (x1) Core Module slot
  - (x2) WisBlock Sensor Module slots
- **Buttons**
  - (x1) Reset Button
- **Connectors**
  - JST PHR-2 connector for 3.7v LiPo battery.
  - JST ZHR-2 connector for 5v solar panel.
  - I2C, UART and BOOT headers accessible with solder contacts
  - USB-C port for debugging and power
- **Screen Support**
  - OLED screen support (OLED screen sold separately)

Further information on the RAK19003 can be found on the RAK Documentation Center

### Connectors Diagram

### Voltages

- JST PHR-2 connector for 3.7v LiPo battery.
  - Charge controller max charge rate is 350mAh.
  - Minimum input voltage for charging is 3.3v, maximum 4.3v.
- JST ZHR-2 connector for 5v solar panel.
  - Minimum input voltage to charge is 4.4v, maximum 5.5v.

### Resources

- Purchase Links:
  - US
    - Rokland
  - International
    - RAKwireless
    - RAKwireless AliExpress
    - HexaSpot

**RAK19001**

## RAK19001

- RAK19001 - WisBlock's Dual IO Base Board.
- **Slots**
  - (x1) Core Module slot
  - (x2) WisBlock IO Module slot
  - (x6) WisBlock Sensor Module slots
- **Buttons**
  - (x1) Reset Button
  - (x1) User-defined push button switch
  - (x1) Battery selector switch
  - On this board the PIN for user button (IO5) is available as a solder contact on the upper header row.
- **Connectors**
  - JST PHR-2 connector for 3.7v LiPo battery (with charge controller)
  - JST ZHR-2 connector for 5v solar panel (max 5.5v)
  - Separate FGH20005-S02M2W1B connector for non-rechargeable batteries
  - I2C, SPI, UART, BOOT and GPIOs accessible with solder contacts
  - USB-C port for debugging and power
- **Screen Support**
  - OLED screen support (OLED screen sold separately)

Further information on the RAK19001 can be found on the RAK Documentation Center.

### Connectors Diagram

### Voltages

- JST PHR-2 connector for 3.7v LiPo battery.
  - Charge controller max charge rate is 500mAh.
  - Minimum input voltage for charging is 3.3v, maximum 4.3v.
- JST ZHR-2 connector for 5v solar panel.
  - Minimum input voltage to charge is 4.4v, maximum 5.5v.
- FGH20005-S02M2W1B connector for non-rechargeable battery.
  - Minimum required is 3.3v, typical 3.7v, maximum 5.5v.
  - Active battery is selected with the battery selector switch.

### Resources

- Purchase Links:
  - US
    - Rokland
  - International
    - RAKwireless
    - RAKwireless AliExpress
    - HexaSpot

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/base-board. GPL-3.0 (Meshtastic documentation).*
