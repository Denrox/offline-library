# What "test transmissions" are allowed above 51MHz?

*Tags: united-states, legal, band-plan · score 12*

## Question

The ARRL's band plan chart includes the following text in its legend:

Test transmissions are authorized above 51 MHz, except for 219-220 MHz

What FCC regulation is this referring to?

Aren't *all* ham bands available for transmitter testing and other experimental communications? What sort of "test" transmissions are allowed above this frequency but not below? (And is the cutoff really at 51 MHz, not 50.1 MHz?)

## Accepted answer (score 3, by WA9ZZZ)

A "test" mode transmission is basically an unmodulated carrier. Below 51.0 MHz, the FCC regs would like you to not leave a dead carrier on indefinitely. Above 51.0 you can do that for whatever reason (as long as you identify).

One common use for unmodulated carrier is full duplex operation. Nobody seems to do this anymore (that I know of). It is easy to do cross band with one station transmitting on 6m (above 51 MHz) and the other on 2m. If one or both stations leave their carrier on when not talking it is an unmodulated signal and not allowed below 51.0 MHz.

The 51.0 MHz cutoff has been around for quite a while. I find it in 12.111(h) which includes in frequencies and emissions: "51.0 to 54.0 Mc using type A0 emission". This from 1962. Also, "52.5 to 54.0 Mc using types F0,..."

## Answer (score 12, by natevw - AF7TB)

This is indeed in the FCC regulations. In Part 97, section 305 regarding "Authorized Emission Types" there is the following chart which lists two relevant subbands, see in the VHF group the 6m row and the  Do ditto right below it:

Tracing our way outwards from there, we find:

- 47 CFR §97.305(c) is the heart of the FCC regulation on which the ARRL legend note is based.
- Limited testing **is permitted** on all amateur-allocated frequencies, and experimental digital modes are also cautiously permitted within the HF bands (i.e. below the frequency in question). In the HF bands, there are a number of technical and discretionary restrictions that can apply to data emissions.
- At 51 MHz and above there is basically no **technical** restriction on emission types within the amateur allocations. Advance the radio art! (You still can't "obscure your meaning" or avoid good amateur practice, of course.)
- Yes, 51.0 MHz is really the cutoff. (There's actually a specific bandwidth restriction that "hangs on" up through the 2m band, but the ARRL chart's summary is accurate enough.)

These answers are explored in more detail below.

Let's zero in on the difference between 50.1–51.0 MHz range vs. the 51.0-54.0 MHz range.* The first frequencies allow emissions of type "MCW, phone, image, RTTY, data" whereas the second allow all that and "…, test". This must be exactly what the ARRL chart is referring to. So **yes, 51 MHz is the correct boundary** for where "test" emissions may occur.

What *is* a "test" emission type? The definitions section of Part 97 says this:

**Test.** Emissions containing no information having the designators with N as the third symbol. Test does not include pulse emissions with no information or modulation unless pulse emissions are also authorized in the frequency band

But to expand on that a bit, the table above also has a "standards" column which lists only (2), (5) for the 50.1–51 MHz subband, but (2), (5), (8) for the 51.0–54.0 MHz portion [see updates below — this column is a red herring re. "test" emissions]. The definitions of these standards are given in § 97.301(f) within numbered paragraphs.

The first applicable standard the two subbands here have in common is a general rule regarding allowable bandwidth:

(2) No non-phone emission shall exceed the bandwidth of a communications quality phone emission of the same modulation type. The total bandwidth of an independent sideband emission (having B as the first symbol), or a multiplexed image and phone emission, shall not exceed that of a communications quality A3E emission.

So for 6m (and 2m and 1.25m) one needs to limit data transmissions so they fit within the same bandwidth as a phone transmission would use. (Note how this paragraph (2) is not applicable on 73cm and above.)

It's the next two standards that distinguish between what might be considered "data" and "test" signals.

**UPDATE**: I'm leaving the discussion below largely intact because it does at least detail a **different** expansion of signal authorizations above the same 51 MHz cut-off. But see other update note below.

DataBasic data would be:

(5) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 19.6 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. The authorized bandwidth is 20 kHz.

Looks like we need to unpack this further! This standard refers to §97.309(a) and §97.309(b) to define what exactly counts as "data" in here. I won't paste those entire sections here, but in summary they allow:

- Baudot, AMTOR, ASCII, and "any technique whose technical characteristics have been documented publicly" (a)
- "an unspecified digital code", provided it's exchanged with a country which has agreed to such things, and **not** "for the purpose of obscuring the meaning of any communication", and assuming the FCC hasn't given more specific instructions against it. (b)

That's already pretty broad!

For the standard which seems to apply to "test" signals, we findThere's additional data privileges that start here too:

(8) A RTTY or data emission having designators with A, B, C, D, E, F, G, H, J or R as the first symbol; 1, 2, 7, 9 or X as the second symbol; and D or W as the third symbol is also authorized.

To understand this paragraph we actually have to jump out of Part 97 and in to Part 2 of the FCC's 47 CFR to learn their definitions of "Emission, modulation and transmission characteristics". If you do so, you'll find that there's not much that all those letters and numbers leave out. (For the life of me [I can't figure out what the "E" modulation type is](What%20is%20emissions%20designator%20E%20when%20used%20as%20a%20type%20of%20modulation.md), but the others cover AM/SSB/FM/PM for any sort of baseband signal for any sort information….)

Note that this paragraph (8) standard is much broader definition than the overall "test" definition above, in that the third symbol is pretty much a wildcard, rather than the "no information" N symbol that test emissions in general are restricted to.

**UPDATE**: thanks to WA9ZZZ's answer I know think it's clear that the paragraph (8) standard has **nothing to do with** the "test" emissions **also** allowed starting at 51 MHz. (Case in point: note how the 23 cm and 13 cm band rows in the table have the same three Standards listed in that column, but one has "pulse" and the other doesn't in the "Emission types" column! Those columns aren't tied as closely as I originally assumed.)

Covering that general case, §97.305(b) says:

A station may transmit a test emission on any frequency authorized to the control operator for brief periods for experimental purposes, except that no pulse modulation emission may be transmitted on any frequency where pulse is not specifically authorized and no SS modulation emission may be transmitted on any frequency where SS is not specifically authorized.

To re-summarize the deep-dive above, I think the distinction is that:

- You can perform **brief** tests carrying no information, **anywhere**. (I would expect that combination of "good amateur practice" with the "no information" designation means one wouldn't ever splatter a fat AM/FM "test" signal over a CW-only portion of a band.)
- You have relatively broad leeway in many "data" portions of authorized bands to experiment with new modes and protocols. (Some restrictions may apply, see store for details, void in Quebec, etc. etc.)
- At 51.0 MHz and above, you have almost /carte blanche/ as far as permitted signal types for this broader class of "paragraph 8" emissions within the ham allocations, subject in the VHF bands to the bandwidth limitations of 97.307(f)2, and only to common decency in the UHF bands (by §97.307(a)) as far as I can tell.
- [new point] You *also* are allowed to emit **sustained** test transmissions — i.e. unmodulated and implicitly no-information signals — starting at this 51 MHz line and basically on up [excepting the 2m CW-only slice].

I now believe this last [new] point is what the ARRL's language is referring to on their band chart — *sustained* (rather than brief) "test" transmissions. In other words "dead air" can be transmitted at 51 MHz on up — subject of course to the ever-present station identification requirements. (See WA9ZZZ's answer for examples of when this might be useful.)

*You might wonder why the the 50–50.1 MHz portion of the 6m allocation is missing from the §97.305 chart. I believe this is covered instead by the table in §97.301 revealing the 6m allocation as the full 50–54 MHz (in ITU regions 2 and 3 at least), coupled with §97.305(a) which states:

Except as specified elsewhere in this part, an amateur station may transmit a CW emission on any frequency authorized to the control operator.

(Or, having read through this entire answer, you might have *lost* all sense of wonder, entirely ;-)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6967/what-test-transmissions-are-allowed-above-51mhz, by natevw - AF7TB, WA9ZZZ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
