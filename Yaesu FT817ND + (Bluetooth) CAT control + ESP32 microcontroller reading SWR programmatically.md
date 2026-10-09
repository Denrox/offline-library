# Yaesu FT817ND + (Bluetooth) CAT control + ESP32 microcontroller: reading SWR "programmatically"?

*Tags: impedance-matching, software-development, computer-aided-transceiver · score 4*

## Question

I am building a wireless control system for a *magnetic loop antenna*. The system uses an **ESP32 microcontroller** (that has Bluetooth and WiFi) that

1. automatically **drives the magloop capacitor** by means of a **DC motor**, while
2. *minimising SWR in real time*.

While "1" is easy, I failed at "2". I want to use FT817's own SWR meter, and assumed I could *programmatically read-out the LCD readings via CAT control*: this is what **Omnirig** does (if I am not mistaken).

I then got a **(CAT) Bluetooth dongle** on eBay and, using the "BluetoothSerial" Arduino library I managed to have the ESP32 and the FT817 communicating! For instance, the ESP32 can easily read (and set) mode + frequency, activate/release the PTT, and even switch ON/OFF the radio! I even managed to read out the S-Meter values (by the ad hoc CAT command).

Reading SWR programmatically, however, requires using an (undocumented) CAT command (mentioned by KA7OEI). Unfortunately, as I try that, the ESP3 gets a series of wrong numerical values, at odd with the number of "segments" on the LCD indicating SWR.

Something is wrong with my idea or with the (Arduino, C) code, whose extract is reported below:

```
#define CAT_sTX_DATA_CMD    0xBD

unsigned short int getSWR() {  
byte outByte[5] = {0x00,0x00,0x00,0x00,0x00};
outByte[4] = CAT_sTX_DATA_CMD;
long elapsed = 0;
byte reply1, reply2;
unsigned int swr;
unsigned int pwr;
String SWR;
long timeout = millis();

sendCmd(outByte, 5);

while (SerialBT.available() < 2 && elapsed < 2000) {
elapsed = millis() - timeout;
;}

reply1 = SerialBT.read();
reply2 = SerialBT.read();

pwr = (unsigned short) ((reply1 >> 4) & 0x0f);
swr = (unsigned short) (reply1 & 0x0f);
return swr;
}

void sendCmd(byte cmd[], byte len) {
for (byte i=0; i<len; i++)
SerialBT.write(cmd[i]);
}

```

Any chance that some among you has already solved the same problem? Any hints or suggestions? Do you see a problem in my getSWR() function?

## Answer (score 3, by webmarc)

it looks like the flrig folks have it sorted out.

From the flrig source file in src/rigs/yaesu/FT817.cxx:

```
static int swr_map[] = {
 0,  4,  8, 13, 25, 37, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100};
// 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14,  15

```

It's not clear to me what the mapped values actually mean, but it occurs to me that you could fire up flrig, run a trace, and actually see how it maps those values to the meter display.

Or you could also go spelunking in that code!

From the same source file just stumbled across this which should be helpful:

```
// uses undocumented command 0xBD
// returns two bytes b0 b1
// b0 PWR|SWR
// b1 ALC|MOD

int  RIG_FT817::get_power_out()
{
init_cmd();
cmd[4] = 0xBD;
int ret = waitN(2, 100, "get PWR/SWR/ALC", HEX);
getthex("get_power_out");

```
if (ret &lt; 2) return 0;

int fwdpwr = (replystr[0] &amp; 0xF0) &gt;&gt; 4;
swr = (replystr[1] &amp; 0xF0) &gt;&gt; 4;
alc = (replystr[0] &amp; 0x0F);

if (fwdpwr &gt; 8) fwdpwr = 8;
if (fwdpwr &lt; 0) fwdpwr = 0;
return pmeter_map[fwdpwr];
```

}

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20953/yaesu-ft817nd-bluetooth-cat-control-esp32-microcontroller-reading-swr-programm, by Michele, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
