# Would it be feasible to set up a SSB or AM 2 meter repeater?

*Tags: repeater, ssb, am · score 4*

## Question

Would it be feasible to set up a SSB or AM 2 meter repeater? I want to set up an AllStar full duplex node and like the idea of AM because stations can double without issues. SSB works for weaker signals and it takes up less bandwidth. The circuitry is also way simpler. Just set up a PL tone on the repeater so interference does not get through.

Would it work?

## Answer (score 8, by Kevin Reid AG6YO)

(This is a purely theoretical answer; I have no experience in repeater building. Sorry.)

The components of a repeater are:

- an antenna,
- a duplexer,
- a transmitter and a receiver,
- and a repeater controller.

The antenna and duplexer are passive devices and aren't affected by what modulation you're using. The repeater controller is on the audio side of the radios, not the RF side. So there is no fundamental reason this can't work.

However, using a CTCSS tone together with SSB modulation would not work. This is because SSB causes an audio frequency shift if the transmitter and receiver are not exactly on frequency (as they never are), so the tone sent by a user of the repeater will not be recognized by the repeater controller unless the tuning is exact to within a few Hz.

(With AM, the carrier provides the frequency reference. With FM, as normal VHF repeaters use, the audio frequency is not related to the RF frequency.)

There are various other coded squelch (*selective calling*) systems available, some of which *might* do better than CTCSS, but many of them are only a burst at the beginning of the transmission and thus assume the signal has a carrier which the repeater can use to know when to *stop* repeating, which is not true of SSB.

Incidentally, there *are* existing repeaters, of a sort, which can use SSB/AM. There is a device called a linear translator, or linear transponder, which is *completely* mode-independent: it receives a certain band, frequency shifts it to another band, amplifies, and retransmits it.

These systems can be used with any mode you care to transmit at them. The cost is that since they are not demodulating, they don't have any sort of intelligent handling of the signal (such as tone squelch, timeout, etc.).

Linear transponders are most often found on amateur radio *satellites* (those that do not carry FM repeaters instead). Because the satellite has very limited power available, it is polite to use SSB, CW, or other power-efficient modes as opposed to AM or FM.

## Answer (score 3, by user5755)

I find the idea of an SSB repeater quite challenging. A repeater has noteworthy the function of allowing communication between points which are mutually inaccessible along the direct line. A repeater has not the function of giving the word (the channel) to one sole participant a time (sic!). I greatly prefer the convivial chat in SSB on the HF bands to the scholarly sequenced conversation in FM on 2m and above! Therefore, the SSB repeater would just be a continuously operating frequency translator, installed at a high place, which takes in a first, lower frequency band, e.g. a 12kHz channel at 434MHz, and gives it out, transposed and amplified, in a higher frequency band, e.g. at 439MHz. For putting this in place, two problems must be solved: 1) to achieve an amplification of 90dB without feed-back, and 2) to achieve steep (rectangular!) channel filtering to avoid crosstalk. The solution to the problem is in the combination of a digital I/Q receiver at the first, lower frequency, e.g. based on the Realtek RTL2832U chip, with digital filtering, amplification and processing to isolate the 12kHz baseband signal, and reemitting the baseband signal at the second, higher frequency with the help of an I/Q switching modulator, followed by a HF amplification stage.

The advantages of passing through the baseband are a) the distribution of the necessary gain stages between three different frequency levels, reducing possible internal feedback problems, and b) the ease of realizing a very steep and phase-linear filter window for the 12kHz channel.

The advantages of digital signal processing are the ease of realizing time-delayed phase-linear FIR filters and the total avoidance of external feedback by an appropriate combination of time-delay between input and output signal, and high-pass filter cutting off all low-frequency signals beyond the time delay of the signal processing chain.

Input and output frequency may be in the same, or preferably in different bands.The operation on the repeater is as ordinary operation, but in duplex.The repeater processes any type of analog or digital input signal and any type of modulation to the frequency-translated output.

Remains the question whether such repeaters are admissible after all, because they work in continuous operation, monopolizing one channel (the emission channel) from the band.However, this might be worth the value of providing a real chatting option in SSB or CW via a repeater. Furthermore, if there is no activity on the input channel, the output is silent, too.

In any case, HAM radio is an experimental discipline, and this would certainly be a field of new experience, which is worth the effort!

## Answer (score 2, by Mike)

Rotorua branch 33 of NZART 2m linear repeater is still operational and has been for more than 20 years. It is a solar powered repeater and situated on a high point overlooking Rotorua Town. Output is 144.350MHz with a plus 600 shift.

More details of it can be found here  
http://www.amalgamate2000.com/radio-hobbies/radio/Rotorualinear.htm

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3680/would-it-be-feasible-to-set-up-a-ssb-or-am-2-meter-repeater, by Skyler 440, Kevin Reid AG6YO, user5755, Mike. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
