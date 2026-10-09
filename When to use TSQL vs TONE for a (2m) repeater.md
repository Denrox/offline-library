# When to use TSQL vs TONE for a (2m) repeater?

*Tags: vhf, repeater, 2m · score 5*

## Question

I'm trying to understand when to use TSQL and when to use TONE in the configuration of a repeater. I got a repeater file to import into my radio from http://www.dstarinfo.com/repeater-list.aspx and in the file some repeaters use TSQL and some use TONE, like this:

but when I look at the source information from https://ukrepeater.net, I can't see any difference to indicate TONE should be used with one and TSQL with the other.

MB7IAT is here: https://ukrepeater.net/my_repeater.php?id=4517

and MB7IHA is here https://ukrepeater.net/my_repeater.php?id=4819

**Update**: thank you for the explanations of TSQL. It confirms what I understood so far. I guess my question then boils down, looking at the list of repeaters, how do I know a repeater will forward the tone or not? How do I know whether to enable TSQL or not for each of the almost-500 repeaters in the UK?

## Answer (score 5, by user3486184)

It almost always makes sense to use TONE. On Yaesu radios, TONE will send a CTCSS tone when you push PTT, which almost all repeaters sense. If the tone is not there, your signal doesn't get repeated. On some other radios, this is equivalent to setting TX TONE.

TSQL does two things: it sends a CTCSS tone when you push PTT, and it sets a CTCSS tone squelch value on your radio. This is equivalent to setting TX TONE *and* RX TONE on some other radios. It requires that the repeater send a CTCSS tone back to you when it transmits, otherwise your radio will keep the signal squelched.

Some repeaters don't transmit a tone back. For those repeaters, you'd never hear them if you set TSQL.

When would you use TSQL? When you *don't* want to hear something.

Usually it's when two repeaters are on the same frequency. Often repeaters that are "far enough" apart get coordinated with identical frequency pairs. When the atmosphere is just right, repeater signals travel further, and the repeaters can interfere with each other. If both repeaters send different CTCSS tones when they repeat, you can ignore one repeater by setting TSQL (or RX TONE) so you don't hear the distant repeater and only hear traffic from the nearby repeater.

You might also use TSQL with APRS. Most of the time there's no tone on APRS signals - and you don't want to hear the digital bursts anyway. However, sometimes people will key up on the APRS frequency with voice traffic - "I'm listening on APRS." You can set TSQL or RX TONE on the APRS frequency so you don't hear APRS traffic, but do hear when someone keys up with a transmit tone set. This is called Voice Alert.

In general, if you want to hear everything, use TONE only (or TX TONE). If you want to block transmissions that don't have a particular CTCSS tone, use TSQL (or RX TONE along with TX TONE) if transmit CTCSS is required.

No matter what, remember that tone squelch just blocks what you hear. You still need to be aware that the frequency may be active (the green light on most radios that shows the frequency is busy) so you don't interfere with someone else.

## Answer (score 2, by ha3flt)

I have not read the links, but it is simple.

TSQL means that your radio will transmit the preset CTCSS tone, and the received signal will be muted unless the preset CTCSS tone is present in the received signal *and* the signal is stronger than the preset squelch trigger level.

TONE means that your radio will transmit the preset CTCSS signal, but will receive any signal stronger than the preset squelch trigger level.

Setting your radio to TONE mode instead of TSQL is desirable if you do not have data for all repeaters, or if you are lazy to set/program CTCSS individually for all repeaters in an area, but want to scan repeaters, channels, etc.

If you know the tone (which you need to in order to transmit through the repeater), there is no reason not to use TSQL, as it will reduce or eliminate the reception of interference if there are other signals on the repeater's downlink frequency while it is not transmitting. Except that the others send the same CTCSS tone :-)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21397/when-to-use-tsql-vs-tone-for-a-2m-repeater, by Pablo Fernandez, user3486184, ha3flt. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
