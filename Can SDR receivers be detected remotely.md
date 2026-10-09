# Can SDR receivers be detected remotely?

*Tags: software-defined-radio, oscillator, superheterodyne · score 6*

## Question

It's my understanding that active superhet receivers can be detected by looking for the emissions from the local oscillator, particularly because the LO's frequency is usually set at some fixed offset from the carrier.

Is a similar technique applicable to software-defined radios, especially if the LO is set exactly at the carrier frequency? Are there SDRs that don't have an RF LO at all to be detected?

## Accepted answer (score 12, by Phil Frost - W8II)

You might be able to detect a *regenerative* receiver. This is because this receiver topology uses positive feedback to increase the Q of the tuned circuit. If the feedback is too much it becomes an oscillator which transmits quite conspicuously.

Detecting just any huperhet receiver is a different matter. The coupling between the LO and the antenna is not deliberate as it is in a regenerative receiver.

That's not to say there aren't detectable emissions. *Anything* with an oscillator could be detected. That includes all digital electronics, and every switch mode power supply. In fact looking around me now the only electronic device I see which does not have an oscillator in it is a fish tank heater.

All these oscillators are detectable, if you know well enough what you're looking for and have enough resources. But detecting the emissions from a superhet receiver among all the noise of everything else with an oscillator in it is a challenge, to say the least.

If anything, SDRs are easier to detect. Some SDRs have at least one mixer which would have an LO. Some are direct sampling, meaning they ADC runs at such a high rate it doesn't need to down-convert the signal before sampling it. But all SDRs have an ADC, and an ADC requires a clock, which is another oscillator. Whatever is processing the digital data will undoubtedly have another clock and a plethora of other noisemakers.

## Answer (score 2, by hotpaw2)

A direct sampling SDR does not need a LO anywhere within the frequency range or tracking the signal of interest.

A processor running off of a fixed clock frequency well above twice the RF signal frequency of interest could use that clock to run an ADC and directly sample the RF signals, producing no other RF noise other than the EMI from the processor and its assorted power, IO, and memory subsystems.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17953/can-sdr-receivers-be-detected-remotely, by chrylis -cautiouslyoptimistic-, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
