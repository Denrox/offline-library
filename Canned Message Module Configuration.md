# Canned Message Module Configuration

The Canned Message Module will allow you to send messages to the mesh network from the device without using the phone app. You can predefine text messages to choose from.

The canned message module config options are: Enabled, Send Bell, Messages, Input Source, Rotary Encoder Enabled, Up Down Encoder Enabled, Input Broker Pin A, Input Broker Pin B, Input Broker Pin Press, Input Broker Event Clockwise, Input Broker Event Counter Clockwise, and Input Broker Event Press. Canned Message config uses an admin message sending a `ConfigModule.CannedMessage` protobuf.

  

## Canned Message Module Config Values

### Enabled

Enables the canned message module.

### Send Bell

Sends a bell character with each message.

The [External Notification Module](External%20Notification%20Module%20Configuration.md) can be set up to beep when a new message arrives.
This module can also be configured to beep only when a message contains the bell character.

### Messages

The list of pre-set messages as configured by the user. Messages should be separated by pipes `|`. The total byte count for the message list can be up to 200 bytes

### Input Source

Input event sources accepted by the canned message module.

|      Value      |                             Description                              |
| :-------------: | :------------------------------------------------------------------: |
|     `_any`      | Default. Allows any peripheral input device connected to the device. |
|    `rotEnc1`    |                         Basic Rotary Encoder                         |
|  `upDownEnc1`   |     Up Down Encoder (use this also for RAK14006 Rotary Encoder)      |
| `scanAndSelect` |              Single push-button (short and long press)               |
|    `cardkb`     |           M5 Stack CardKB (this covers RAK14004 Keymatrix)           |
|   `serialkb`    |                        Chatter serial keypad                         |

### Rotary Encoder Enabled

Enable the default rotary encoder.

### Up Down Encoder Enabled

Enable the up / down encoder.

### Input Broker Pin A

GPIO Pin Value (1-39) For encoder port A

### Input Broker Pin B

GPIO Pin Value (1-39) For encoder port B

### Input Broker Pin Press

GPIO Pin Value (1-39) For encoder Press port

### Input Broker Event Clockwise

Generate the rotary clockwise event.

### Input Broker Event Counter Clockwise

Generate the rotary counter clockwise event.

### Input Broker Event Press

Generate input event on Press of this kind.

## Canned Message Module Config Client Availability

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
    {
      label: (
        <>
           CLI
        </>
      ),
      value: "cli",
    },
    {
      label: (
        <>
           Web
        </>
      ),
      value: "web",
    },
  ]}>

**android**

### Android

> **Info:**
>
>
> Canned Message Config options are available for Android.
>
> 1. Open the Meshtastic App
> 2. Navigate to: **Settings > Canned Message**
>

**apple**

### Apple

> **Info:**
>
> All canned message module config options are available on iOS, iPadOS and macOS at Settings > Module Configuration > Canned Messages.

**cli**

### CLI

> **Info:**
>
>
> All canned message module config options are available in the python CLI.
>

Example commands are below:

|                Setting                 |             Acceptable Values             |           Default           |
| :------------------------------------: | :---------------------------------------: | :-------------------------: |
|         canned_message.enabled         |              `true`, `false`              |           `false`           |
|        canned_message.send_bell        |              `true`, `false`              |           `false`           |
|   canned_message.allow_input_source    | `rotEnc1`, `_any`, `upDownEnc1`, `cardkb` |           `_any`            |
|          --set-canned-message          |                 `string`                  | `""` (separate using pipes) |
|  canned_message.inputbroker_event_cw   |             `InputEventChar`              |        (not defined)        |
|  canned_message.inputbroker_event_ccw  |             `InputEventChar`              |        (not defined)        |
| canned_message.inputbroker_event_press |             `InputEventChar`              |        (not defined)        |
|    canned_message.inputbroker_pin_a    |                 `integer`                 |        (not defined)        |
|    canned_message.inputbroker_pin_b    |                 `integer`                 |        (not defined)        |
|  canned_message.inputbroker_pin_press  |                 `integer`                 |        (not defined)        |

> **Tip:**
>
>
> Because the device will reboot after each command is sent via CLI, it is recommended when setting multiple values in a config section that commands be chained together as one.
>
> ```shell title="Example:"
> meshtastic --set canned_message.enabled true --set canned_message.send_bell true
> ```
>

```shell title="Enable/Disable the Canned Message Module"
meshtastic --set canned_message.enabled true
meshtastic --set canned_message.enabled false
```

```shell title="Enable/Disable send bell character"
meshtastic --set canned_message.send_bell true
meshtastic --set canned_message.send_bell false
```

```shell title="Set Messages"
meshtastic --set-canned-message "I need an alpinist!|Call Me|Roger Roger|Keep Calm|On my way"
```

```shell title="Set Input Source"
meshtastic --set canned_message.allow_input_source "_any"
meshtastic --set canned_message.allow_input_source "rotEnc1"
```

```shell title="Enable/Disable rotary1"
meshtastic --set canned_message.rotary1_enabled 1
```

```shell title="Set/Unset Encoder Pin A"
meshtastic --set canned_message.inputbroker_pin_a 17
meshtastic --set canned_message.inputbroker_pin_a 0
```

```shell title="Set/Unset Encoder Pin B"
meshtastic --set canned_message.inputbroker_pin_b 39
meshtastic --set canned_message.inputbroker_pin_b 0
```

```shell title="Set/Unset Encoder Pin Press"
meshtastic --set canned_message.inputbroker_pin_press 21
meshtastic --set canned_message.inputbroker_pin_press 0
```

```shell title="Set/Unset Input Broker CW Event"
meshtastic --set canned_message.inputbroker_event_cw UP
meshtastic --set canned_message.inputbroker_event_cw ""
```

```shell title="Set/Unset Input Broker CCW Event"
meshtastic --set canned_message.inputbroker_event_ccw DOWN
meshtastic --set canned_message.inputbroker_event_ccw ""
```

```shell title="Set/Unset Input Broker Press Event"
meshtastic --set canned_message.inputbroker_event_press SELECT
meshtastic --set canned_message.inputbroker_event_press ""
```

**web**

### Web

> **Info:**
>
> All canned message module config options are available in the Web UI.

> **Warning:**
>
> GPIO access is fundamentally dangerous because invalid options can physically damage or destroy your hardware. Ensure that you fully understand the schematic for your particular device before trying this as we do not offer a warranty. Use at your own risk.
>
> This module requires attaching a peripheral accessory to your device. It will not work without one.

## Hardware

To navigate through messages and select one, you will require some hardware attached to your device. Currently, the module is tested with a generic rotary encoder, an up/down/select 3 button logic and several I2C Keyboards. Further input methods will be added in the future.

### I2C Keymatrix

This is tested with the RAK14004 Keyboard. A keypress will immediately send the message attached to the button number. Buttons are numbered from upper left to lower right on the keypanels. So pressing the upper left button will send the first message. The second button will send the second message and so on.

**Caveat:** the RAK 3x4 keymatrix is missing the 4th button row while scanning, so you have to skip every 4th message slot. Button 1 sends message 1 and button 4 will send message 5
Example: 1|2|3||5|6|7||9|10|11||13|14|15 - the slots 4,8 and 12 cannot be used.

### CardKB

The CardKB is fully supported in freetext mode and select mode. Use UP/DOWN/ENTER to select a predefined message and send it. For a freetext message, just type it in and press ENTER to send it.

If you don't want to broadcast your freetext message, you can use the CardKB to send it to a specific node. Just press TAB and select the target node with the LEFT/RIGHT keys. The message will be sent to the node with the matching name and node number. The target node will be remembered for your next message.

### 3 Button up/down and RAK rotary encoder

Just use UP/DOWN/ENTER to select a predefined message and send it.

### Scan and Select

Use a single push-button to select and send predefined messages.

#### Setup

- Connect a normally-open push-button between ground and a GPIO pin of your choice
- Configure the canned messages module
  - Set Input Source to `scanAndSelect`
  - Set Input Broker Pin Press to your chosen GPIO
  - Define a list of pre-set messages

#### Usage

- Short press: scroll through messages
- Long press: send the currently highlighted message to your primary channel

### Rotary encoder

Meshtastic supports hardwired rotary encoders as input devices.

You will need a generic rotary encoder. The types listed below has five legs where two is dedicated to a "press" action, but any other types will likely do the job. You can also use a three-legged version, where the "press" action should be wired from an independent switch.

- Amazon link
- Amazon.DE link
- Aliexpress link1
- Aliexpress link2
- Aliexpress link3

Connect your rotary encoder as follows. The rotary encoder has two rows of legs. One of the rows contains two legs, the other contains three legs. Bottom side view:

```text
  B o --- o PRESS
GND o | |
  A o --- o GND
```

The two legs is to sense the press action (or push). Connect one of the two to GROUND and the other to a GPIO pin. (No matter which one goes where.) Let's call this connected ports 'PRESS'.

The three legs is to sense the rotation action. Connect the middle leg to GROUND and the ones on the side to GPIO pins. Let's call these ports 'A' and 'B', according to the scheme below.

```text
A   --||
GND --||]========
B   --||
```

Recommended GPIO pins for connecting a rotary encoder.

- TTGO LoRa V1:
  - A - GPIO-22
  - B - GPIO-23
  - PRESS - GPIO-21

There is a reference case 3D-design utilizing the rotary encoder for TTGO LoRa V1:
Case for TTGO-ESP32-LORA-OLED-v1.0 with rotary encoder

## Examples

- Attach a compatible peripheral device. Take note of the GPIO numbers you use, as they will be used in the following step.

> **Note:**
>
> Replace each `GPIO` (x3) below with the GPIO numbers from your hardware setup.

```shell title="Canned Message Module - Required Rotary Encoder Module Settings"
meshtastic --set canned_message.inputbroker_pin_a GPIO
meshtastic --set canned_message.inputbroker_pin_b GPIO
meshtastic --set canned_message.inputbroker_pin_press GPIO
meshtastic --set canned_message.inputbroker_event_cw UP
meshtastic --set canned_message.inputbroker_event_ccw DOWN
meshtastic --set canned_message.inputbroker_event_press SELECT
meshtastic --set canned_message.rotary1_enabled True
```

That's it! With a functioning and enabled rotary encoder, you're ready to begin configuring the Canned Message Module.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/module/canned-message. GPL-3.0 (Meshtastic documentation).*
