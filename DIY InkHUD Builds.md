# DIY InkHUD Builds

## DIY Presets

Tried-and-tested hardware combinations, with pre-made configurations.

### Supported Hardware

#### Base Device

- Heltec Mesh Node T114
- NRF52 Pro-micro DIY

#### Display Module

- WeAct Studio 1.54" B&W
- WeAct Studio 2.13" B&W (2025 Revision)
- WeAct Studio 2.9" B&W
- WeAct Studio 4.2" B&W

### Firmware

Although configurations for these devices are provided, you will still need to build the Meshtastic firmware.

#### Building With Visual Studio Code

First, set up the build environment, then:

1. Open the PlatformIO Project Tasks pane

2. Select the environment which matches your node hardware
   - `heltec-mesh-node-t114-inkhud`
   - `nrf52_promicro_diy-inkhud`

3. Run the Build task which matches your display model
   

4. Once build is complete, find the generated .uf2 file at `./pio/build/<environment>/firmware.uf2`
   

#### Building with Platformio CLI

Execute `pio run -e <environment> -t <build task>`, where:

`<environment>`

- `heltec-mesh-node-t114-inkhud`
- `nrf52_promicro_diy-inkhud`

`<build task>`

- `build_weact_154`
- `build_weact_213`
- `build_weact_290`
- `build_weact_420`

Then find the generated .uf2 file at `./pio/build/<environment>/firmware.uf2`

### Installation

Install the generated .uf2 file to device using the [drag and drop method](Drag%20%26%20Drop%20nRF52%2C%20RP2040%2C%20%26%20RP2350%20Firmware%20Updates.md).

### Wiring

#### Heltec Mesh Node T114

| E-Ink Module | Heltec Mesh Node T114 |
| ------------ | --------------------- |
| VCC          | VCC                   |
| GND          | GND                   |
| SDA          | 0.08                  |
| SCL          | 0.07                  |
| CS           | 1.12                  |
| D/C          | 1.14                  |
| RES          | 0.05                  |
| BUSY         | 1.15                  |

#### NRF52 Pro-micro DIY

| E-Ink Module | Pro-micro |
| ------------ | --------- |
| VCC          | VCC       |
| GND          | GND       |
| SDA          | 1.15      |
| SCL          | 1.11      |
| CS           | 1.07      |
| D/C          | 1.02      |
| RES          | 1.01      |
| BUSY         | 1.06      |

## Other Hardware

Using InkHUD on hardware beyond the standard DIY presets will require manual customization of the firmware.
No specific support can be given here; only a general overview.

**Check for a Display Driver**

InkHUD relies on custom display drivers.
These are located in `/src/graphics/niche/Drivers/EInk/`.
Choose a display which is already supported; otherwise, you will have to write the driver yourself, which requires some specialist knowledge.

**Clone and Modify an Existing InkHUD Variant**

The general instructions for building with custom hardware apply here.
In addition to modifying the `variant.h` file, you should also modify `nicheGraphics.h`,
which is responsible for InkHUD's per-variant configuration.

---

*Source: Meshtastic documentation, https://meshtastic.org/docs/configuration/device-uis/inkhud/diy-builds. GPL-3.0 (Meshtastic documentation).*
