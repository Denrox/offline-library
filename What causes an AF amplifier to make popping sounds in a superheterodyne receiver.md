# What causes an AF amplifier to make popping sounds in a superheterodyne receiver?

*Tags: receiver, diy, electronics, superheterodyne · score 3*

## Question

Recently I've made a simple single IF superheterodyne SSB receiver for 40 meter band. The schematic is [available here [PDF]](https://eax.me/files/2021/01/40m-superhet-receiver.pdf). VFO and BFO are based on Si5351, the AF amplifier is LM386. It works OK but there is one annoying issue I couldn't solve so far. When I change the frequency I can hear a popping sound in the headphones.

I thought this could be an RFI from an 1602 LCD and/or the I2C bus. However this theory was not confirmed. When the text is updated on the LCD without changing the frequency there is no popping sound. I also tried to add a simple RC high-pass filter to the AF amplifier. According to the datasheet, LM386 has input impedance ~50 kOhm. Thus with 10 nF capacitor on the input it will form an high-pass filter with cutoff frequency ~300 Hz. This didn't help either.

Then I thought maybe the problem will go away when I place the receiver in a proper aluminum enclosure with good ground plane and move AF amplifier away from the VFO. Sadly this made no difference.

The problem is that I have little understanding of what exactly causes this popping sound and how to diagnose such problems. Hopefully someone who also encountered such an issue could explain how to deal with it? I tried to Google the problem. It seems to be quite common, but I didn't manage to find a solution or an explanation of the effect.

## Accepted answer (score 4, by Aleksander Alekseev - R2AUK)

I think I figured this out. By looking at VFO with an oscilloscope I could catch a brief glitch (~1.5ms) in the signal when the frequency is changed:

It was hard to notice because you can't easily trigger on this. I had to manually trigger single captures while tuning for some time to see this.

Then by googling "si5351 output glitches" I've found this piece of code on the QRP Labs website. The comment states:

```
Reset the PLL. This causes a glitch in the output. For small changes to
the parameters, you don't need to reset the PLL, and there is no glitch.

```

Then I realized the source of the problem and how to fix it. Here is the original version of my code:

```
void changeFrequency(int32_t delta) {
targetFrequency += frequencyStep*delta;
if(targetFrequency < 7000000) {
targetFrequency = 7000000;
} else if(targetFrequency > 7200000) {
targetFrequency = 7200000;
}

```
if(targetFrequency &lt; 10000000) {
Fvfo  = Fbfo-targetFrequency; // LSB
} else {
Fvfo = Fbfo+targetFrequency; // USB
}
si5351_EnableOutputs((1&lt;&lt;2));
si5351_SetupCLK0(Fvfo, SI5351_DRIVE_STRENGTH_4MA);
si5351_EnableOutputs((1 &lt;&lt; 2)|(1&lt;&lt;0));
```

}

```

Here si5351_SetupCLK0 is called every time the frequency is changed. The procedure changes the PLL, MS and Rdiv settings for the channel. As an author of this Si5351 driver I'm well aware that PLL settings are always the same for frequencies below 81 MHz (also this is a documented behavior which can be relied on in the future versions).

Thus the code was changed as following:

```
void changeFrequency(int32_t delta) {
static bool pllSetupDone = false;
si5351PLLConfig_t pll_conf;
si5351OutputConfig_t out_conf;

```
targetFrequency += frequencyStep*delta;
if(targetFrequency &lt; 7000000) {
targetFrequency = 7000000;
} else if(targetFrequency &gt; 7200000) {
targetFrequency = 7200000;
}

if(targetFrequency &lt; 10000000) {
Fvfo  = Fbfo-targetFrequency; // LSB
} else {
Fvfo = Fbfo+targetFrequency; // USB
}
si5351_EnableOutputs((1&lt;&lt;2));

si5351_Calc(Fvfo, &amp;pll_conf, &amp;out_conf);
if(!pllSetupDone) {
// Setting up the PLL causes a brief (~1.5ms) glitch in the VFO output
// which sounds like a loud popping sound the the speaker.
// By setting up the PLL only once we get rid of this popping sound.
si5351_SetupPLL(SI5351_PLL_A, &amp;pll_conf);
pllSetupDone = true;
}
si5351_SetupOutput(0, SI5351_PLL_A, SI5351_DRIVE_STRENGTH_4MA, &amp;out_conf);

si5351_EnableOutputs((1 &lt;&lt; 2)|(1&lt;&lt;0));
```

}

```

Now the expansive call si5351_SetupPLL is made only once, the glitch is gone and the popping sound is eliminated. Well, almost. You can still hear a very quiet popping when the antenna is disconnected. But there is no popping when the antenna is connected. Interestingly you can observe the exactly same behavior in QCX transceiver made by guess which company.

## Answer (score 3, by niels nielsen)

Try powering the LM386 temporarily off a battery. if the popping stops, then the cause is a surge being conducted into the 386 from the supply that feeds the rest of your circuit.

Normally, you would bypass the power input of the 386 to ground with a hefty electrolytic capacitor (50 to 100mfd) and then shunt that with a fast-acting cap (0.01 to 0.1uF) to prevent surges from upsetting the 386. If your circuit doesn't have these bypass caps, try adding them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17897/what-causes-an-af-amplifier-to-make-popping-sounds-in-a-superheterodyne-receiv, by Aleksander Alekseev - R2AUK, niels nielsen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
