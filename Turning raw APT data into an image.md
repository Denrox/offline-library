# Turning raw APT data into an image

*Tags: software-defined-radio, software-development, dsp · score 3*

## Question

I apologize if this question is a little out of scope for the amateur radio stack exchange but I feel like it fit better here than over in any other forum.

I have successfully parsed raw PCM data out of a WAV file representing the signal received from one of NOAA's satellites in APT format. Since its bit rate is 16 bit I combined sequential pairs of bytes into 16 bits using simple bit shifting. I understand these values represent sampled amplitudes.

What I am trying to figure out is where to go from here. I don't really want to use a normal application as most of them are proprietary, and being a ham operator I feel like programming an APT demodulator would be a useful exercise as a rite of passage.

I've done some digging around and have read the APT specification, but it doesn't quite give any clues on what I need to do to transform the signal into the appropriate image. I've read around on other forums, and it seems I need an AM demodulator and some form of an FFT to get it to where I need to be - however I am brand new to this stuff. I come from a computer science and math background so I can definitely handle the learning curve. I'm just about through with my amateur extra exam and the knowledge in there seems have left me with little to work with in this regard. I am willing to dig in but I have to know where to start!

Can anyone provide me any resources on how I can begin to learn how to transform these signals in the raw PCM data to the images I need? . I'd really appreciate it!

## Accepted answer (score 2, by ElectroNeutrino)

The data is AM modulated on the 2.4 kHz subcarrier, with 256 different levels representing a single value from 0 to 255. It's a scanline every 1/2 second from the cameras with sync and telemetry data added to the beginning and end.

Each line is 2080 data points (words) long, so it broadcasts at 4160 baud. The sync lines at the beginning let you know when a line starts, and helps the decoder to adjust its baud rate if needed.

Channel A starts its 39 word sync with 7 square wave pulses at 1040 Hz, with each pulse being 2 words wide with 2 word spacing, and the remainder blank. Then the space and minute marker at 47 words long. Then the raw 256 value picture data. And then 45 words of telemetry data used to calibrate the range values of the sensor and determine which sensor is transmitting.

Channel B is exactly the same, except its sync is 7 pulses at 832 Hz, making its pulses 3 words wide with 2 word spacing.

Edit: Others around the web have pointed out that you can sample the audio at 9.6 kHz and get 4 samples per wave, take any two consecutive samples $x_{_1}$ and $x_{_2}$, and get the carrier amplitude with $A = \sqrt{{x_{_1}}^2 + {x_{_2}}^2}$ .

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15638/turning-raw-apt-data-into-an-image, by CL40, ElectroNeutrino. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
