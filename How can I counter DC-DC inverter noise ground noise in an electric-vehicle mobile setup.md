# How can I counter DC-DC inverter noise / ground noise in an electric-vehicle mobile setup?

*Tags: mobile, rfi, grounding, dc-power, battery · score 5*

## Question

So, I'm relatively new to all this; and I've gotten an ICOM IC-7100 on sale, which looks like an *excellent* transceiver … unfortunately, this very specific line shows up in the manual:

The transceiver may not receive well on some frequencies when installed in a hybrid vehicle, or any type of electric vehicle (fuel cell vehicle). This is because vehicle’s electric components such as the inverter system generate a lot of electric noise.

To boot, reading other questions on this site, I came across [this excellent news](How%20do%20I%20power%20my%20radio%20in%20a%20vehicle%20mobile%20install.md):

… In the worst case, your cigarette lighter may be wired for "chassis ground return", where [the] current is not being returned through a copper ground wire, but through the car's steel chassis. This is OK for stuff like an AM/FM radio or the cabin lighting, but that same resistance equates to a higher voltage drop with your [radio], which can distort your output signal or even cause devices to sense an "undervolt" condition and shut down.

Taking a look under the hood, so to speak, this is *precisely* the situation in my car … except not for a cigarette-lighter port, rather literally for the entire car — of the 50A primary-12V “battery terminals” you're supposed to jump her with, the negative is simply a post on the chassis:

So, how should I best wire up my transceiver? (I've tried to google up some sort of ‘line noise filter’ for DC power, but 1. they all seem like extremely sketchy products, 2. most of them have lots of ‘this did nothing for me’ reviews, and 3. most of them are rated for small amperages.)

## Answer (score 2, by rclocher3)

Allow me to refer you to Alan Applegate K0BG's excellent page about mobile radio wiring and grounding. That page recommends that you power the radio with a fused negative lead connected to the chassis, and a fused positive lead connected to the main battery. Here's a picture:

Alan's site is chock-full of excellent advice about seemingly every aspect of mobile operating.

Regarding your specific question, I'd of course recommend that you don't use the cigarette lighter to power your radio, but you knew that already. There's nothing stopping you from using the same chassis ground point as the ELD (electronic load detector) in the picture for your fused negative lead. That way you won't have the steel chassis in your current path.

Alan also has a page on mobile radios in hybrid cars that specifically confronts the noise in electric cars issue. (There's no difference between a hybrid and an all-electric car when the hybrid is running on battery power alone, of course.) That page says that electric and hybrid cars generate "copious" amounts of RFI. He then goes on to say, "The next question is, can it be tamed? Yes, but it is a herculean task requiring countless hours, and hundreds of dollars spent reducing the RFI to a level compatible with HF operation."

If you do decide to take on the Herculean task, know that the noise isn't just coming in through the power supply; the electronics generating the three-phase power for the motor generate RFI directly. So filtering the radio's DC power would only solve one aspect of the problem. It might be easier to do as Alan suggests and just pull over and stop the car when you want to operate HF. Good luck.

Be safe, and enjoy your IC-7100!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6734/how-can-i-counter-dc-dc-inverter-noise-ground-noise-in-an-electric-vehicle-mob, by ELLIOTTCABLE, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
