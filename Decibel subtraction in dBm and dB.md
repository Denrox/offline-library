# Decibel subtraction in dBm and dB

*Tags: rf-power, math · score 7*

## Question

1. If i have equations for subtraction of 27dBm-3dBm=27dBm how can this be written as 24 dB. I convert the 27dBm and 3dBm -> 10^2.7-10^0.3.But how can we simply subtract the two dBm
2. Whereas if we have a calculation of 8dBm - (-90dBm)= 98dB this is represented as 98dB and not 8dBm? Shouldn't we convert both the dBm like (10^0.8-10^(-9)) and then convert into dBm.

Could someone hep me explain why we represent the first equations result in dBm whereas the second equations result in dB?

## Accepted answer (score 9, by Kevin Reid AG6YO)

I convert the 27dBm and 3dBm -> 10^2.7-10^0.3. But how can we simply subtract the two dBm

If you convert to exponential form then you must simultaneously replace subtraction with division (or addition with multiplication), so you have $10^{2.7} / 10^{0.3}$ instead of $10^{2.7} - 10^{0.3}$. Then you will see that you get the same result:

$$2.7 - 0.3 = 2.4$$

$$\frac{10^{2.7}}{10^{0.3}} = 10^{2.4}$$

why we represent the first equations result in dBm whereas the second equations result in dB?

The first one is incorrect and the second one is correct. (There must be something else wrong with what you wrote down, because it is not the case that $27 - 3 = 27$, of course.)

Any time you subtract two dB values with a reference level specified (dBm, dBW, dBFS, etc.) you get a ratio expressed as decibels, which is independent of the reference level and therefore should not be written with one.

$$ 27\,\mathrm{dBm} - 3\,\mathrm{dBm}=24 \,\mathrm{dB} $$

$$ 27\,\mathrm{dBm} - 3\,\mathrm{dBm} \neq 24 \,\mathrm{dBm} \tag{dimensionally incorrect} $$

To understand *why* these are the rules, consider this exercise:

If we have 1000 mW (or 30 dBm), that is the same as 1 W (or 0 dBW).

Now suppose we compare that to 100 mW, 20 dBm; 0.1 W, -10 dBW. Again, all of these are the same power expressed differently. If we subtract decibels, or divide the regular values, then we get the same number out:

$$ \begin{align*} 1000\,\mathrm{mW} / 100\,\mathrm{mW} &= 10 & 30\,\mathrm{dBm} - 20\,\mathrm{dBm} &= 10 \,\mathrm{dB} \\ 1\,\mathrm{W} / 0.1\,\mathrm{W} &= 10 & 0\,\mathrm{dBW} - (-10\,\mathrm{dBW}) &= 10 \,\mathrm{dB} \end{align*} $$

When you **divide** two figures with equal units, you get a unitless (dimensionless) number. When you **subtract** two dB values with the same reference level, the reference level goes away. These are exactly the same mathematical phenomenon.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9786/decibel-subtraction-in-dbm-and-db, by Mayank Mehra, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
