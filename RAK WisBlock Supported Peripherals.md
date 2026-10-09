# RAK WisBlock Supported Peripherals

## Antennas

### WisMesh Blade Antenna

The WisMesh Blade Antenna is available in two variants:

- 915MHz (902-928 MHz) with a max gain of 2.3 dBi and a VSWR ≤ 1.5
- 868MHz (863-870 MHz) with a max gain of 2.8 dBi and a VSWR ≤ 1.3

#### Resources

- Purchase Links:
  - International
    - RAKwireless
    - RAKwireless AliExpress

## Enclosures

### WisMesh Unify Enclosure

The WisMesh Unify enclosure is an IP65-rated outdoor enclosure designed for Meshtastic with optional solar power panels, two size variants, and flexible mounting options

#### Resources

- Purchase Links:
  - International
    - RAKwireless
    - RAKwireless AliExpress

## WisBlock Modules

**GPS Module**

### GPS Modules

#### RAK12500

The RAK12500 GPS sensor is a newer GPS module and is generally preferred.

- uBlox Zoe-M8Q GNSS receiver
- GPS, GLONASS, QZSS and BeiDou satellite support

The RAK12500 is supported on the following base boards & slots:

- RAK19007 on slot A
- RAK19003 on slot C
- RAK19001 on slot F

#### RAK1910

The RAK1910 GPS sensor is the older generation of the supported RAKwireless GPS modules and while still supported in Meshtastic it has reached EOL (End of Life) and is no longer available for purchase.

- uBlox MAX-7Q GPS module
- GPS and GLONASS satellite support

The RAK1910 is supported on the following base boards & slots:

- RAK5005-0 on slot A
- RAK19007 on slot A
- RAK19003 on slot C
- RAK19001 on slot F

#### Resources

- RAK Documentation Center
  - RAK12500
  - RAK1910
- Purchase Links:
  - International
    - RAKwireless
    - AliExpress

**Buzzer**

### Buzzer

#### RAK Buzzer

The RAK18001 Buzzer Module may be used with the External Notifications plugin. There is currently a known conflict with the buzzer if the module is placed in Slot D, although other slots should work. NOTE: Many users have complained of the RAK buzzer being very quiet as currently implemented. As of yet, there is no fix for this issue.

#### Resources

- RAK Documentation Center RAK18001
- Purchase Links:
  - International
    - RAKwireless
    - AliExpress

### Third Party Buzzer

Another option is to use a standard "passive buzzer" and a transistor (such as a 2N2222 transistor). This can be done by wiring the VCC pin to leg 1 of the transistor and the positive terminal of the buzzer to leg 3. To the central pin (2) of the transistor, connect pin RX1 on the Wisblock board. Connect the negative terminal of the buzzer to the GND pin on the Wisblock board. In settings, go to Device and set Redefine PIN_BUZZER (Buzzer GPIO) to 15. Then go to External Notification and set the module to Enabled, PWM buzzer to enabled, Alert Message Buzzer to enabled and Output Buzzer GPIO to 15. Save your settings and your buzzer should activate whenever you get an incoming message.

#### Resources

- Purchase Links:
  - International
    - Amazon: Buzzer
    - Amazon: Transistor

**Vibration**

### Vibration

To add vibration to your Wisblock device you'll need a standard 3V DC vibramotor and a transistor (such as a 2N2222 transistor). This can be done by wiring the VCC pin to leg 1 of the transistor and the positive (red) wire of the vibramotor to leg 3. To the central pin (2) of the transistor, connect pin AIN1 on the Wisblock board. Connect the negative wire (black) of the vibramotor to the GND pin on the Wisblock board. In settings, go to External Notification and set the module to Enabled, Alert Message Vibra to enabled and Output Vibra GPIO to 31. Save your settings and vibration should activate whenever you get an incoming message.

#### Resources

- Purchase Links:
  - International
    - Amazon: Vibrator
    - Amazon: Transistor

**I/O Module**

### IO Module

The RAK13002 IO Module can be used to, among other things, add a user button to the RAK base boards (excluding the RAK19003 Mini base board). It features a number of different interface options:

- 2x I2C interfaces
- 2x UART interfaces
- 1x SPI interface
- Upto 6x GPIOs
- 2x ADC interfaces
- 3.3v Power rails

There is development activity in progress to get sensors such as this added to the Meshtastic Core.

#### Resources

- RAK Documentation Center RAK13002
- Purchase Links:
  - US
    - muzi ᴡᴏʀᴋꜱ
    - Rokland
  - International
    - RAKwireless
    - AliExpress

**Environmental Sensors**

### Environmental Sensors

#### RAK1901 Temperature and Humidity Sensor

The RAK1901 Temperature and Humidity Sensor is based on the Sensirion SHTC3 module and has the following features:

- Temperature measurement (Range -40&deg;C to +125&deg;C)
- Humidity measurement (Range 0% to 100%)
- Lower power consumption

#### RAK-1902 Barometric Pressure Sensor

The RAK1902 Barometric Pressure Sensor is based on the STMicroelectronics LPS22HB module and has the following features:

- Barometer measurement (Range 260 to 1260 hPa)
- Low power consumption of 3uA
- Small form factor

#### RAK1906 Environment Sensor

The RAK1906 Environment Sensor is based on the Bosch BME680 module and has the following features:

- Temperature measurement (Range -40&deg;C to +85&deg;C)
- Humidity measurement (Range 0% to 100%)
- Barometer measurement (Range 300 to 1100 hPa)
- Air Quality measurement

#### Resources

- RAK Documentation Center
  - RAK1901
  - RAK1902
  - RAK1906
- Purchase Links:
  - US
    - Rokland RAK1901
    - Rokland RAK1902
    - Rokland RAK1906
  - International
    - RAKwireless RAK1901
    - RAKwireless RAK1902
    - RAKwireless RAK1906
    - AliExpress RAK1901
    - AliExpress RAK1902
    - AliExpress RAK1906

**RTC Module**

### RTC Module

The RAK12002 WisBlock RTC Module is a real-time-clock with a supercapacitor backup, allowing a node to maintain the correct time across reboots and for up to seven days without power. It operates on a crystal oscillator and communicates via the i2c interface. The module can be inserted into slots A, B or C (some users have reported issues with slot D) and is plug and play - no settings are required.

#### Resources

- RAK Documentation Center RAK12002
- Purchase Links:
  - US
    - Rokland
  - International
    - RAKwireless
    - AliExpress

**User Button**

### User Button

Any tactile momentary push button is compatible as long as it is wired to the correct pins, here's a sample of a Push Button

The button is recommended to be used on the following base board's exposed pins or slots :

- RAK19007 on AIN1 (Pin 31) - See supporting instructions
- RAK19001 on IO5 (Pin 37)

#### Wiring

One side of the switch should be on GND and the other on the recommended Pin per your baseboard. The pin must be configured on the node using the app, webclient or CLI.

#### Resources

For more information on the User Button functionality refer to

- [RAK WisBlock Hardware Buttons](RAK%20WisBlock%20Hardware%20Buttons.md)

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/peripherals. GPL-3.0 (Meshtastic documentation).*
