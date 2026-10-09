# Yaesu FT-450D CW from computer - DATA and CAT connectors

*Tags: cw, yaesu, remote-control, ft-450d, computer-aided-transceiver · score 3*

## Question

**Yaesu FT-450D Transceiver**

- USB-to-DB9 cable installed to the CAT interface
- Computer runs the ADMS-450 channel-programming program fine.
- Computer can run the PCC remote-control program fine.

DATA connector has these pins:

And the cable looks like this:

- DATA connector is attached to the computer's audio in/out jacks
- Computer can record receive-audio fine.

**The Operator's Manual shows an external TNC for RTTY and PSK, wired like this**:

So I admit to being a bit confused as I thought the data cable would be all that would be necessary to use software digital modes from the laptop. Now I see that the PTT line is n/c.

It does function as a very good analog interface, and makes good recordings.

The goal is to use the laptop as a CW keyboard and memory keyer.

Perhaps the simplest option would be to use the **Keyer** jack directly with a Python program on a RPi3B from the junk box.

If it is possible to do it with the existing connections that would be best.

In searching around with Google there seems to be very little information about doing this.

**QUESTION: How to use the FT-450D for CW from the computer?**

How do you key the carrier remotely? Is it possible to use the CAT interface to send CW?

## Accepted answer (score 4, by Phil Frost - W8II)

The "data" cable you picture provides only audio in and out. Some other device, like a TNC or a computer, must provide the modulation and demodulation to provide any data capability.

Additionally, the cable picture does not expose the PTT connection on the data port, so with that cable alone there's no way for the computer to key the transmitter.

However, you do say you have a "USB-to-DB9 cable" installed. Yaesu calls this the CAT port. You can use this connection to key the transmitter, as well as control most other functions of the radio such as frequency, mode, and so on.

It sounds like all you need to do is configure your CW keyer software to use the CAT interface to control the radio.

How this is done depends on the software, but any reasonably modern software like fldigi or Ham Radio Deluxe does have the capability. Look through the setup menus and you should be able to find it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10351/yaesu-ft-450d-cw-from-computer-data-and-cat-connectors, by SDsolar, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
