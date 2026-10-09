# What is the use of dual VFOs?

*Tags: hf, transceiver, vfo · score 3*

## Question

What is the value of more than one VFO in an HF transceiver?

Many novice rigs only have a single crystal oscillator, and a vast number of famous classic transceivers, HF kits, and QRP rigs only have a single VFO. So more than one VFO is obviously not a requirement for successfully operating in the HF bands

So what's the typical use case and advantage of having more than one VFO? For what situations is another VFO needed, and when can one do without?

## Answer (score 5, by Mike Waters)

Dual VFOs are needed for transmitting on one frequency but listening on another. The reason why this is done is nicely explained [here](Why%20do%20some%20DX%20listen%20on%20a%20different%20frequency%20than%20they%20transmit%20on.md).

This is called operating "split" and it takes a certain amount of skill to work a DX operator working split and even more to operate split.

The reason this is done is to help manage the pileup. If too many stations are calling and the pileup becomes unmanageable it takes longer and longer to complete an exchange. This is less fun for everyone.

By working split, the DX operator keeps his transmit frequency clear so that the callers will hear him well making the exchange go more smoothly. He also has the opportunity to spread out the calling stations on several frequencies near his transmit frequency.

## Answer (score 3, by rclocher3)

For anyone new to ham radio: in the analog era, in order to listen on one frequency and transmit on another with a single HF receiver or transceiver, by flipping a switch rather than turning a knob I mean, two VFOs were needed. That generally meant two oscillators and two tuning knobs. Now that oscillators are digitally-controlled frequency synthesizers, the frequency can be easily and accurately changed in a fraction of a second. These days a "VFO" is just a few bytes of memory holding the frequency in a computer. Modern HF radios typically offer two "VFOs". They could easily offer many more; the only reason they don't is that more buttons on a front panel that is already crammed with buttons would be required. (This is true whether there is a physical front panel on the radio, or a virtual front panel created in software.)

As @MikeWaters said, the main reason for the dual VFO function is to enable operating "split", that is listening and transmitting on different frequencies. This is sometimes used because the stations in a QSO can't legally transmit on the same frequency as the DX station, but it's more commonly used in DX pileups. In a pileup, there are so many stations all trying to call a single rare DX station that the DX station can't pick individual call signs out of the howling noise of many stations all transmitting on the same frequency. So the DX station announces that they are operating split, and the calling stations spread themselves over several kilohertz, typically higher than the DX's frequency. The DX station's frequency is supposed to be left to the DX station alone.

The OP asked why transceivers have a split mode at all, rather than just using RIT or XIT. The reason is that the RIT and XIT functions are intended to solve different problems, and using them to operate split in a DX pileup would be more complicated than using the transceiver's split mode. Operating split in a pileup takes skill, timing, and fast button-pushing, and anything that makes that easier is welcome. Also, RIT and XIT are usually limited to a range of a few kilohertz in the same band, and sometimes that range isn't wide enough. Sometimes people have a cross-band QSO in which one station transmits on one band and the other station transmits on a different band; in that case, the RIT and XIT ranges *definitely* aren't enough, and split mode is the only practical way to make it work.

## Answer (score 2, by Phil Frost - W8II)

Many radios will have buttons labeled "VFO1" and "VFO2", suggesting there are two oscillators when actually there is only 1. The buttons simply store a frequency in memory which is restored at the appropriate time, not unlike the "recall" button on a TV remote. In the past, this would have actually required two oscillators since they were not digitally controlled and also not so stable.

Largely, it's a convenience. For example, you may be having a QSO when someone else starts using your frequency. By switching to the other VFO you can tune around to find a free frequency, then switch back to propose the new frequency.

Or you may use it as sort of a "memory". Perhaps you often operate FT8 and CW: one VFO can be left on the FT8 frequency, and the other in the CW portion of the band, and the buttons provide a quick means of switching between the two.

Radios that actually have two VFOs are capable of operating on two frequencies simultaneously.

Some can operate as a cross-band repeater. This may allow the operator to have a mobile station on a higher frequency which can remotely access the greater HF capabilities of the base station.

Two VFOs also allows the simultaneous monitoring of two frequencies without scanning between them. While this isn't such a common use case as it is on VHF/UHF, it does exist: there are repeaters on 10 meters in some places, and 6 meters although not technically HF is part of many HF radios, and there can be repeaters there, too.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17074/what-is-the-use-of-dual-vfos, by hotpaw2, Mike Waters, rclocher3, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
