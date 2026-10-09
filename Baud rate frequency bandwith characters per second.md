# Baud rate/frequency/bandwith/characters per second

*Tags: filter, noise · score 3*

## Question

I'm trying to filter a noisy serial line that comes in to a radio (mostly as a thought excercise in line filtering). The data comes in on a RS-232 line, 9600 baud, 8n1. I've found a lot of explanations, some of them contradicting each other.

Am I correct in believing that:

1.

9600 baud in our case (two states, mark or space) also means 9600 bits per second

2.

Maximum signal frequency is 9600 Hz (if pattern would be all 010101010)

3.

Using those 9600 baud, only 9600/10=960 characters per second can be send (each character needs 8 bits, plus one start and one stop bit)

4.

If I want to add ferrite beads to the input to filter for EMI, I not only need to take the maximum signal frequency into account, but also x harmonics to allow the signal to rise at a decent rate.

How do you estimate what kind of impedance at what frequency you need to still allow fast enough rise times?

## Accepted answer (score 2, by Marcus Müller)

Maximum signal frequency is 9600 Hz (if pattern would be all 010101010)

No, your 01010101… would lead to a square wave signal, and that has an infinite spectral support, with components at every odd multiple of the symbol rate, amplitude declining with the multiple. So, no, your highest frequency is *not* 9600 Hz

Using those 9600 baud, only 9600/9=1066 characters per second can be send (each character needs 8 bits, plus one parity bit)

Depends on your character encoding, parity bits, as you noticed, but also flow control – your RS232 might have separate CTS / RTS lines, but more often there's start and stop bits.

If I want to add ferrite beads to the input to filter for EMI, I not only need to take the maximum signal frequency into account, but also x harmonics to allow the signal to rise at a decent rate.

The harmonics *are* part of the signal. The question is after how many harmonics you can attenuate without killing too much signal. Rule of thumb says 5. or 7. harmonic should be enough for digital lines, but if in doubt:

The series representation of the square wave is

$$ \frac4\pi\sum\limits_{n=1,3,5,\ldots}^{\infty}\frac{2\pi n f_{symbol}t}{n} $$

so just your own discretion!

## Answer (score 4, by Glenn W9IQ)

The issue of filtering RS-232 (or any slow digital signal) is not so much the baud rate as it is the required rise and fall time of each bit.

There are two ways to quantify this rise/fall time issue: what does the RS-232 standard say or what does your RS-232 chipset and UART require? I have formulated my answer from the perspective of the former.

RS-232 control signals should maintain a rise/fall time of less than 1 ms. When operating at 19,200 baud, data signals should maintain a rise/fall time of less than 5 *u*s. The slew rate of the rise/fall time should not exceed 30 V/*u*S to avoid crosstalk. Your filters must be designed to ensure these rise/fall timing constraints are met.

You did not elaborate on the type of EMI/RFI you are experiencing. Filter types commonly deployed for RS-232 signals include:

- RC T filters (T for infiltrate and exfiltrate protection)
- In connector ferrite plates
- Ferrite beads (material based on filtering requirements)
- Hybrid cable grounds (if interference is affecting RS-232 chipset)

If you are able to describe the exact nature of the interference, perhaps specific guidance could be offered.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9318/baud-rate-frequency-bandwith-characters-per-second, by Dieter Vansteenwegen, Marcus Müller, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
