# DIY SA612 + RTL-SDR HF receiver: good on laptop, but huge wideband noise on Raspberry Pi

*Tags: software-defined-radio, rfi, rtl-sdr, mixer · score 8*

## Question

I recently built a SA612 mixer for HF reception. I used an USB-frequency oscilator to shift the incoming frequency up by 28.8 MHz.

I used a random wire antenna outside my balcony and connected it to the center-pin of a car antenna mount, and used a long coax to guide the signal in the room to my DIY low-pass filter, then connected it to my DIY SA612 mixer, and its output to my RTL-SDR, and finally connected everything to my battery-powered laptop.

The reception was not the best, but its performance just allowed me to be able to pick up a lot of the high-power shortwave and mediumwave radio stations with low distortion, I was pretty satisfied with my device (although I was unable to hear anything from any amateur radio bands due to its limited dynamic range facing these strong stations).

However, sitting inside the balcony on a tiny seat with a laptop is extremely uncomfortable, so I decided to hook up my Raspberry Pi for remote operation. Unfortunately, as soon as I connect my SDR to my Raspberry Pi, huge wideband noise is received all over the spectrum, killing MW and HF beyond recognition! I'm using the mediumwave as an example, but HF is also the case as well (note: this is upconverted signal, the actual IF is around 30 MHz).

There must be a strong interference that was driving the SA612 to saturation. Initially, I thought the noise was coming from the switiched-mode power supply, so I powered the Raspberry Pi from a benchtop linear power supply, and I also powered the SA612 mixer from a 9-volt battery instead. See the following block diagram.

But it had little effect. Although number of spurious interference was somewhat reduced, but the SA612 is still being overdriven, and I still see "machine-gun" like interference at fixed intervals, some are sweeping back and forth around its carrier like a wobbulator. Also, the noise floor of the signal of the entire band kept moving up and down.

And strangely, if I power my SA612 via Raspberry Pi and use the RTL-SDR on my laptop, I see almost no interference. I also tried listening to the radio on my laptop while running an Ethernet speed test on the Raspberry Pi, but I see nothing at all.

And I finally found if I disconnect the coax input of my SA612 mixer, almost all the interference would be gone.

So my best guess of the situation is that the interference was generated inside the Raspberry Pi, its internal USB bus, or the Ethernet, and the EMI was traveling across the ground/shield, and/or somewhat the signal was being picked up at the input side of the mixer. Another possibility is that the Raspberry Pi has switched-mode power supply of its own to generate the 3.3 V and 1.8 V rails, perhaps this is the source of the interference.

Is it a correct conclusion? And what can do I to fix the interference?

### Edit 1

I realized that my benchtop power supply was actually a switched-mode power supply, oops... And I did more experiments.

1.

Charging the laptop while listening to the radio can completely wipe out MW and HF using its own power supply. Although my benchtop supply was a switched-mode power supply, but I expect better performance.


Laptop + Battery: Clean spectrum.


Laptop + OEM power supply: "Ultra-wideband" interference at MW and HF.


Laptop + benchtop power supply: Wideband interference at MW and HF below and around 5 MHz, but the interference is weaker at 7 MHz and 10 MHz.


Laptop + unpowered benchtop power supply: strong interference at MW. But low interference at HF.


Laptop + unplugged benchtop power supply: No interference.

2.

Using an old transformer and a LDO, I made my own linear power supply to power the Raspberry Pi.


Raspberry Pi + DIY linear power supply: mild interference at MW, but strong interference across HF.


Raspberry Pi + additional 1:1 isolation transformer + DIY linear power supply: low interference at MW, but strong interference across HF.

#### Conclusion

It doesn't change the conclusion of my original question, it seems the Raspberry Pi was responsible for most interference. But conducted EMI from the powerlines was also a culprit.

I'll try isolating the ground plane between RTL-SDR and SA612 using an RF transformer to see if it improves its immunity of EMI/RFI.

### Edit 2

I tried to use 10+ ferrite to chock every single cables, but it has absolutely no effect on reducing interference, the machine guns are still everywhere. And I'm already using a metal chassis on the Pi (*although I doubt it's effective as a shield since the case is painted and all the screw holes on the Pi doesn't have exposed copper to ground*).

I think the problem is that my SA612 mixer has poor immunity (built on a copper board with dead-bug construction). Better filtering and shielding for the mixer is probably the only potential solution to the problem.

## Accepted answer (score 3, by 比尔盖子)

I believe my problem is created by common-mode noise. I redesigned my homemade SA612 mixer. I isolated the antenna ground from the mixer ground, and I also isolated the mixer ground from the output RTL-SDR ground, and now the problem is fixed.

Here's how I solved the problem. Since I only have very limited knowledge of electronics and radio, it may contain error, corrections and suggestions of improvement of this answer is welcomed.

### Identify the Noise Sources

From the first observations, we can draw several educated guesses about the sources of the noise.

Unfortunately, as soon as I connect my SDR to my Raspberry Pi, huge wideband noise is received all over the spectrum

- The radio works well on a laptop, but receives huge wideband noise on a Raspberry Pi.

So I powered the Raspberry Pi from a benchtop linear power supply, But it had little effect. Although number of spurious interference was somewhat reduced, but the SA612 is still being overdriven, and I still see "machine-gun" like interference at fixed intervals.

- Using different power sources does make a difference, and somewhat reduce the noise on the spectrum, but not much.

It indicates that the noise was certainly coming from external sources, and it's likely that the noise was coupled by conduction, not radiation.

### Identify how the noise is coupled into the receiver

And strangely, if I power my SA612 via Raspberry Pi and use the RTL-SDR on my laptop, I see almost no interference.

- The noise is not detected when the SA612 mixer frontend is connected to the Raspberry Pi, which is our suspected noise source. It means the noise was not coupled into the system by its power supply.

I also tried listening to the radio on my laptop while running an Ethernet speed test on the Raspberry Pi, but I see nothing at all.

- The noise is not detected by the SDR if the laptop is used, even if the radio is at the same physical location, which indicates the noise was not coupled into the system by radiation.

And I finally found if I disconnect the coax input of my SA612 mixer, almost all the interference would be gone.

- This is a critical observation: Disconnecting the antenna input makes the noise to disappear immediately, which means the noise must have found a way to travel all the way from the SDR to the mixer frontend, it's possible that the problem is created by common-mode noise.

And from the block diagram...

The only conductive path is the coax cables, which connects the input of the mixer, output of the mixer, and the input of the RTL-SDR together.

### Hypothesis

So the hypothesis is that the EMI was traveling across the ground/shield, and finally being picked up at the input side of the mixer.

### Mixer

Here's how the mixer was designed.

An input balun transformer converts the single-ended signal from the antenna to a balanced signal, the incoming signal is mixed with an externally injected local oscillator, and the balanced output to converted back to a single-ended signal and connected to the RTL-SDR receiver. The baluns used were Mini-Circuit ADT16-1T, which is a high-performance RF transformer, combined with a double-balanced mixer, we should have a reasonable common-mode rejection and port isolation. Thus, the noise is unlikely to travel across the system through the ports.

However, the input, output, and the mixer are all connected to a common ground plane. Naturally, it becomes our suspect.

Another warning sign is the use of a random-wire antenna - the coax shield and any ground connected directly to it becomes the counterpoise of the antenna. The antenna is extremely vulnerable to interference if common-mode current is not suppressed.

### Redesign

The solution is to cut the conductive path between the input and output. The input transformer and output transformer should only be connected to the coax, but not be tied to common ground. Although separating the ground plane into pieces is normally not recommended, I believe it should work to solve the specific problem in my case.

On a single-layer PCB, I used three copper fills.

After etching and soldering the board, the mediumwave and shortwave spectrum are crystal clear now!

## Answer (score 2, by AF7SJ)

It looks to me like you've put a lot of effort into tracking this down. I believe you are on the right track as far as the Pi creating a lot of broadband noise. But I'm wondering if you've tried putting the SDR on a extension USB cable so that you can move it as far from the Pi as possible?

I've found that getting farther from a noise source helps a lot.

If you are feeding the SDR via a external antenna that is fed by coax, you could embed the SDR in a all metal project box (grounded), that has the coax passing on on one side for the antenna input, and a USB extension cord running to the Pi.

Best of luck!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15714/diy-sa612-rtl-sdr-hf-receiver-good-on-laptop-but-huge-wideband-noise-on-raspbe, by 比尔盖子, AF7SJ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
