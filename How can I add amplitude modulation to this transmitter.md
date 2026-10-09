# How can I add amplitude modulation to this transmitter?

*Tags: diy · score 13*

## Question

I recently built this circuit, and could hear a nice full quieting signal on my short-wave radio with a 7.2 megahertz crystal for the 40 meter band.

What is the simplest way I could Amplitude Modulate this signal with a microphone or computer output port so my Short wave radio could hear this signal and I could potentially make some HAM contacts?

And yes, I know AM is very rarely used, but I want to start out with this because of the complexity of sideband.

## Answer (score 11, by Phil Frost - W8II)

The first AM transmitters were made by hacking the power supplies of CW transmitters. Replace the 9V battery with a variable voltage source and you have yourself an AM transmitter. Not an especially great one, but if simple is your primary concern, it can't get much simpler.

There are many ways you might do that, but if "simple" means "low parts count", then the simplest way is to put the secondary of an audio transformer in series with the 9V supply that's already there. The audio then adds or subtracts from the 9V, and bam, you are modulating the envelope.

sci-toys.com has a detailed article:

The oscillator you've already built. All you need to add is the transformer and the plug.

## Answer (score 7, by WPrecht)

Take heart, there are some diehard AM operators out there on various bands. I am not one of them, but I have seen messages about skeds and frequencies for them.

I am not really sure how you can AM that circuit specifically. I suppose you could substitute the mic input from the usual circuit with that oscillator.

A typical, simple, AM transmitter consists of a MIC pre-amp feeding into an oscillator of some kind and thence into a tuned tank circuit for matching out to the antenna. You also probably want some sort of bandpass filter in there to minimize splatter. This can be accomplished with just a pair of 2N2222A and a handful of other components. An example circuit is:

and a nice project description can be found here.

If you want something a little more advanced, you could use an op amp like the venerable 741 or the NE5532 as your audio pre-amp. Then, instead of driving the 2N2222, you could use the 74HC4060 oscillator and divider to generate a carrier at the appropriate frequency depending on your crystal's frequency. From there you'll still need a good filter to remove the remaining DC component, etc.

The circuit for doing this is:  Looks pretty cool, actually, I am tempted to warm up the soldering iron myself. The complete project description can be found here including a complete bill of goods and how to tune and test it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/756/how-can-i-add-amplitude-modulation-to-this-transmitter, by Skyler 440, Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
