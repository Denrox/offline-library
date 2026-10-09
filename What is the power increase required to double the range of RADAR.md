# What is the power increase required to double the range of RADAR?

*Tags: rf-power, range · score 8*

## Question

Studying for a Pivate Pilot's Licence (PPL) and I've hit something in the study material that doesn't make sense to me. Typical of the PPL study material, it's quite shallow, so the full explanation may have been omitted.

To double the range of a radio wave, you need 4x the power.

I understand this, because of the inverse square law.

To double the range of RADAR you need 16x the power.

This is where I'm stuck.

If a radar system has a range of 3km, the wave must travel 6km, so the received return has 1/36 the power of the transmission.

Now if I want to double the range of the system, to 6km, the wave must now travel 12km. Without power increase, the return signal has 1/144 the original transmission. To get back to 1/36, I need to multiply by 4. - Twice the range, 4x the power.

Are my PPL notes wrong, or am I misunderstanding?

## Answer (score 6, by Phil Frost - W8II)

Here's what you are thinking: if the radar station and the target are 1km away, then the distance there-and-back is 2km. If the distance doubles to 2km, then the distance there-and-back is 4km, just twice what it was. So the there-and-back distance also doubles, so you should need only a 4x increase in power, right?

If the radar target were a flat reflector aimed in just the right direction, this would be true. A target can also employ a corner reflector, which works like a mirror but without the aiming requirement.

$$ P_\text{received} \propto {P_\text{transmitted} \over 2d^2} $$

That $ \propto $ symbol means "proportional to". The power received is also going to depend on the gain of the antenna, the size of the target (more specifically, the solid angle subtended by the target), etc. But if all the factors (except distance) are held constant, then the relationship of power received to power transmitted will obey this proportionality.

A flat target, like a bathroom mirror, forms a virtual image behind it. So the radar station "sees itself" behind the target, twice the distance away. Since in radar the receiver and transmitter are the same station, we can also think of this as the virtual image transmitting to the real station.

But most targets aren't mirrors. The power they receive from the radar station isn't reflected back towards where it came from (like a mirror). Aircraft aren't shaped like mirrors. Since the wavelength of radar is many orders of magnitude greater than light, diffraction will also make the target less like an ideal mirror. Given all these variables, it's a reasonable assumption that the power intercepted by the aircraft will be scattered randomly in all directions. That is, it's a diffuse reflector.

$$ P_\text{received} \propto {P_\text{transmitted} \over d^2 \cdot d^2} $$

Here's one way to think of it:

Imagine the radar target isn't passively reflecting, but instead is a transmitter in itself.

If the target doubles its distance to the station, the target must now "transmit" with 4 times the power.

But targets aren't transmitters: they are passive reflectors of the power they intercept from the station. So to get 4 times the power at the target which is now twice as far away, you need to multiply the power by 4 again. 4*4 gives you 16.

Another example: a mirror can reflect nearly all of the power it receives from a laser pointer back at the source. A white sheet of paper receives the same power from the laser pointer, but that power is diffusely reflected everywhere, and so the power received back at the source is much less.

If it's still not making sense, think about how the reflection off the target affects the divergence of the beam. We can also do better than a flat reflector: we can use a parabolic reflector, with the radar station at the focal point:

$$ P_\text{received} \propto P_\text{transmitted} $$

As long as the antenna is in the focal point, a parabolic reflector will *reverse* the divergence of the beam. Thus, it will make a real image of the antenna right on top of the actual antenna. *All* of the power transmitted (in the direction of the reflector) is received, and there's no distance term at all!

## Answer (score 2, by user20224)

I feel the answers here have gotten too complex. The simple answer to OP's question is for his radio transmission example there is only 1-way propagation hence the inverse square law. For radar transmission it is 2-way propagation, hence the 1/R^4 as per the radar range equation. Note this is for primary radar, where the radar's transmitted signal is reflected back to the radar's receiver. For secondary surveillance radar (which is quite similar to the radio transmission example), the aircraft transponder is detecting the radar's transmitted signal and broadcasting back a radio signal with the squawk code and altitude encoding (and more if mode S). This is (one of the reasons) why SSR has longer range than primary radar.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5828/what-is-the-power-increase-required-to-double-the-range-of-radar, by Matt, Phil Frost - W8II, user20224. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
