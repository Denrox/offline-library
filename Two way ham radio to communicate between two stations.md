# Two way ham radio to communicate between two stations

*Tags: antenna, propagation, equipment · score 4*

## Question

Apologies if this not the right place for this question.

I'm into electronics and now endeavouring into radios and communications. Unfortunately I'm not sure what terms to use to find what I'm looking for so I will describe it here.

I have my home and a rural property around 100km from home. I'd like to setup a radio system that I can communicate between both properties. In addition I'd like (if possible) to extend this to a unit in my truck as a third point of contact.

What system should I look for? FM, AM, VHF? In case of a disaster, which of the above would be more ideal to have?

## Accepted answer (score 6, by Glenn W9IQ)

The answer to your question involves both technical and regulatory issues.

**Technical Considerations**

Radio signals can travel between two locations on earth either by line of sight or by propagation which involves bouncing signals off of the atmosphere or other objects. In general, line of sight is a reliable means of communications whereas the use of propagation can yield variable results due to atmospheric conditions, weather, etc. The frequency of the signal determines if it can travel via the propagation of the atmosphere. As the frequency is increased, more of the signal tends to pass through the atmosphere out to space instead of being reflected back to earth.

For line of sight communications, the two antennas must be able to "see" each other. This means there can be no substantial RF barrier in the line drawn between the two antennas. This includes the earth. If we consider the earth to be a perfect sphere, the height of the antenna can be used to determine the distance a signal can travel until it meets the horizon. Radio waves can go slightly further than the horizon in practice. The following formula approximates necessary elevation to be able to reach a specified *radio horizon*:

$$\text{Antenna Height (meters)}\approx(D/4.12)^2 \tag 1$$

where D is the distance to the radio horizon in kilometers.

So your 100 km distance would require a tower of approximately 590 meters to support your antenna. If you place a tower at both locations, then they would need to be *only* a quarter of this height or approximately 147 meters each. Obviously, this is not a practical solution. If, however, your locations in New Zealand are strategically located on tall hills, you may get most of the needed elevation from the local geography.

Formula 1 is only a rough approximation. There are software packages and sites such as this one available that take into account the specific geography of the planned radio locations to reliably predict the suitability of particular frequencies, antenna heights, antenna gain, power, etc.

Certain radio frequencies regularly *bend the rules* and accomplish fairly reliable communications beyond the apparent radio horizon. In the US amateur radio frequency allocations, our 6 meters band (50 MHz) can often support 100 km range distances with modest antenna heights.

For frequencies below 50 MHz, the signals tend to travel longer distances than line of sight due to propagation. The most common form of propagation involves the signal bouncing off of the ionosphere and back down to earth at some distant location. It is even possible to obtain multiple bounces allowing the signal to circle the earth. Unfortunately, propagation conditions vary widely due to weather, conditions on the sun, and the time of day making it difficult to secure reliable communications between two locations. There are however fairly good tools to predict the distance a signal can travel via the current or forecasted propagation conditions.

One technique involving propagation that is frequently used by the military and by hams to obtain short range communications is to deploy simple antennas that essentially aim the RF signal straight up to the atmosphere. By choosing the right frequencies for the atmospheric conditions, the signal tends to be reflected nearly directly downward from the atmosphere effectively spreading the signal over a circle near area the station. Communications in the 800 km range and greater are regularly attainable. The frequencies involved are usually in the 3 MHz to 8 MHz range. The amateur radio 80 and 40 meter bands are often used for this mode of communications dubbed *near vertical incident skywave* or NVIS.

Particularly when relying on propagation to carry out communications, the amount of transmit power, the type of antenna, and the mode of communications play a substantial role in the effective distance of communications. Voice communication modes tend to be the least range efficient while specialty data communication modes (including Morse code) tend to be the most range efficient. Recent advances in modulation techniques and digital signal processing are blurring this distinction to some degree, however.

Amateur radio operators also make use of repeaters and satellites that pick up signals and retransmit them in order to increase the effective range of the station.

Finally, consider that emergency communications brings in other dimensions such as backup power for the radios, the ability to deploy temporary antennas to replace ones that are damaged, etc. The technical knowledge and experience of an amateur radio operator can prove valuable in emergency circumstances but it does not displace preparedness.

**Regulatory Considerations**

Most countries tightly regulate the use of the frequency spectrum within their territorial control. In most countries, amateur radio operators obtain a license by passing a technical written test. Once you have obtained an amateur radio license, you are typically restricted in the type of communications you can carry out with your license. In the US, for example, an amateur radio station may not be used for "pecuniary interests". This rules out most types of business communications. Also be aware that generally all parties wishing to use the radios without supervision must obtain an amateur radio license - but check your local regulations in this regard.

Another viable option available in many countries is to obtain a business license for your radio system. Regulations vary widely but you generally receive a fixed frequency allocation for your use and communications can be of a business or personal nature. Again, check your local regulations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10462/two-way-ham-radio-to-communicate-between-two-stations, by Desorder, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
