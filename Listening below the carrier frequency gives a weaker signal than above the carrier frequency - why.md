# Listening below the carrier frequency gives a weaker signal than above the carrier frequency - why?

*Tags: transceiver, cw · score 4*

## Question

I have a 20m CW transceiver with an option for a wide or a narrow filter. When the narrow filter is selected, a crystal ladder filter is used in the intermediate frequency filter, between two mixers. When the wide filter is selected, this crystal filter is bypassed and there exists a direct link (that is, only a capacitor) between the two mixers.

I use the wide filter to search for signals by rapidly increasing frequency from 14.000MHz to 14.075MHz. When I found a good signal, I tune it to have the right pitch, and switch to the narrow filter to have less noise and other signals.

There are two frequencies I can tune into to find this pitch that is convenient to listen on, with a difference of about twice the pitch frequency.

I noticed that when I use the lower frequency, when I switch to the narrow filter, the signal is weaker than when using the higher frequency, to the point that only very clear signals can be copied. Can this be explained theoretically, and will this happen with any transceiver, or is it more likely that this is specific to this transceiver?

My explanation would be that the higher frequency, yielding a stronger signal on the narrow filter, is the carrier frequency. The other frequency would be the carrier minus twice the pitch frequency, which is then much weakened by the crystal filter. If the filter is bypassed though, the next mixer outputs both the sum and the complement of its inputs, so the two signals are equally strong. Is this correct?

The RX module is from KD1JV's ATS 3B. I'm not sure if there's copyright on it, but the idea is quite straightforward: RF enters the first mixer, an NE602, together with the output of a DDS. Then the output of the mixer passes through the (4.9152MHz) crystal ladder filter (or not) and goes to the next mixer, a second NE602, together with the output of a controllable oscillator (with a trimmer cap), to adjust the pitch.

## Accepted answer (score 3, by Kevin Reid AG6YO)

The behavior you see is completely expected with the receiver design you describe.

Without either additional filtering or quadrature signals, the output of a mixer always contains both the sum and difference of the input frequencies. Therefore, the receiver you have described processes the signal as follows (all variable names are made up and probably nonstandard):


Assume there is an input signal at frequency $X$ (as well as other signals that aren't the one you're tuning to).


Your DDS VFO produces a reference signal at $Y$ which, when properly tuned, is approximately $X - I$ (where $I$ is the intermediate frequency of 4.9152 MHz).


First mixer combines these signals to $X+Y$ and $\lvert X-Y\rvert$. $X+Y$ is far out of band (~18 MHz for your description) and either there is a low-pass filter to remove it (which doesn't need to be particularly sharp) or it can just be disregarded because it won't be made audible by later stages (I'm not sure). $X-Y$ is approximately $I$.


Crystal filter at frequency $I$ removes everything not close to $I$, thus selecting the signal of interest $X-Y$.


Second oscillator (BFO) produces a reference signal at frequency $I + P$ where $P$ is the pitch you actually hear.


Second mixer combines these signals to $X-Y+(I+P)$ and $\lvert X-Y-(I+P)\rvert$. The first is at RF, the second is at audio frequencies, so only the second will be reproduced by the speaker.

Now work out the consequences of this. Suppose you're tuned exactly on frequency: $Y = X - I$. Then the output of the second mixer is $$ \lvert X-Y-(I+P)\rvert = \lvert X-(X-I)-(I+P)\rvert = \lvert I-(I+P)\rvert = \lvert -P\rvert = P $$ so you hear the pitch the BFO is set for. If $Y$ is a little bit different then the pitch is a little bit different — all of these frequency changes are *linear*.

Suppose you're instead tuned $2P$ too low: $Y = X - I - 2P$. Then the output of the second mixer is $$ \lvert X-Y-(I+P)\rvert = \lvert X-(X-I-2P)-(I+P)\rvert = \lvert I+2P-(I+P)\rvert = \lvert P\rvert = P $$

That is, you hear the same pitch. However, since $X - Y$ is farther from $I$ in this case, the crystal filter will attenuate it much more. If the crystal filter is bypassed, this effect does not occur and the two cases are symmetric.

What you have can be described as a *double-sideband (DSB)* receiver, which is a SSB receiver without the filtering that selects between USB and LSB. When you add the crystal filter, it's like a lower-sideband SSB phone receiver, except that a SSB receiver would have a wider filter for the 3 kHz voice bandwidth rather than a narrow filter trying to select a single CW signal, and the VFO is calibrated so that it shows $Y \pm P$ (plus or minus depending on selected sideband) instead of $Y$.

If you were to tune your receiver to a SSB phone (voice) signal, then (assuming the VFO & filters go that high and there's enough audio bandwidth to hear anything intelligible at all) you would hear a difference between the two frequencies: using the higher frequency (lower sideband reception), the spectrum will be reversed (garbled voice) whereas the lower frequency will preserve the spectrum and sound reasonable (if overly filtered).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3542/listening-below-the-carrier-frequency-gives-a-weaker-signal-than-above-the-car, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
