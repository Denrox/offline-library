# alinco dr-635T receive squelch will not open in DCS mode

*Tags: tone-squelch · score 3*

## Question

Newbie here with a question:

I have programmed my Alinco DR-635T for use with a variety of local repeaters. Half of these are opened with CTCSS codes and the rest with DCS codes. When monitoring any of the CTCSS repeater frequencies, the Tx/Rx diode lights up and shows Rx and I can hear static, repeater traffic and repeater ID transmissions. When I key my transmitter, the diode lights up for Tx and I can hit the repeaters and hear the repeater squelch closure after I stop transmitting, so all is OK with talking to the CTCSS repeaters and hearing their responses.

But when I am tuned to any of the DCS repeater frequencies (all in the same Peak Radio Service Oregon network, all using the same DCS code 023, which is set on my 635) the following things happen:

The Tx/Rx indicator diode goes OUT and the audio is silenced (no static with the squelch setting wide open). The S-meter jumps around and pops up to +9 when someone else opens the repeater but at no time does the squelch on my radio open, nor does the Rx diode light up.

When I key transmit, the Tx diode lights up and when I watch the S-meter, I can see it hold at +9 for one second after I switch to Rx, indicating that I did hit the repeater and it then gave me the normal squelch closure tail, but then there is no audio and the Rx light never comes on. Then I watch the S-meter jump up to +9, indicating that someone out there heard my transmission through the repeater and is trying to answer, but the Rx diode stays dark and there is no audio- while the S-meter is at +9. Then they sign off, the S-meter drops down- and the Rx diode stays out and the audio stays off.

It is as if the 635's squelch is always closed when I am in DCS mode, and here is the puzzle: I successfully programmed the radio over a year ago and it worked properly on both CTCSS and DCS repeaters, but I did not use it again until just now. Did the radio's memory fail while it sat idle? If so, how could it remember everything else except opening the Rx squelch while monitoring a DCS repeater frequency? Please help! I am new to this business and do not know what to do.

## Accepted answer (score 1, by rclocher3)

I too have an Alinco radio with a channel set for a Peak Radio Association repeater, which uses the same CDCSS (DCS) code. I just tried, and I was able to key up my local PRA repeater and hear its call sign back.

My radio is not yet supported by CHIRP, so I had to use the Alinco software to program the radio. For that channel I have encode set to D023N (that's how the software shows it), which I interpret to mean "digital code 023 normal", as opposed to D023I, which would be "digital code 023 inverse". Decode is set to None for that channel.

Perhaps you have decode set to something other than None for that channel in your radio, which I'd think would be incorrect. As I understand, most repeaters don't encode their output, so if you were to have decode set to something other than None for a repeater, then you wouldn't hear any of the repeater's output.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17990/alinco-dr-635t-receive-squelch-will-not-open-in-dcs-mode, by niels nielsen, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
