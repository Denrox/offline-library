# Experiences on a 70 cm band shared with radiolocation service

*Tags: license, band-plan, 70cm-band · score 4*

## Question

I currently live in Brazil and our governmental regulatory agency (www.anatel.gov.br) has recently started a public consultation process regarding the allocation, in secondary nature, of part of the 70 cm band to the radiolocation service.

Some of us amateur radio operators are concerned about this public consultation, fearing the impacts of the proposed band sharing, specially over educational cubesats communications using weak signals in 430-440 MHz.

By doing some research we realized that this band sharing actually already exists in many other countries and, in fact, so far we brazilians are enjoying a privileged position on that matter, having the whole band for amateur use.

So I would like to hear from you guys: do you have or know about some bad experiences about the coexistence of the radiolocation service and any amateur operation on the 70 cm band?

Moreover: do you have any knowledge of the specifics of the radiolocation service (output power, how often such service is usually activated over a given area and so on)?

## Answer (score 4, by rclocher3)

Here in the US ham radio is only a secondary user of the 70cm band, with the primary user being military radar. That didn't stop ham operators from setting up hundreds of repeaters on the band. Back in 2007 the US Air Force complained about interference, and the ARRL worked with them to create a plan to reduce the interference (article). I don't remember hearing anything more about the issue, so hopefully the problem was solved; presumably the ARRL asked the owners of the repeaters involved to reduce power.

So we as secondary users of the 70cm band in the US normally use the band without worrying about interfering with the primary user, except for a few repeaters near US Air Force bases. I hope that you hams in Brazil are able to cooperate successfully with the radiolocation service!

## Answer (score 3, by AndrejaKo)

I'm from Serbia, and there we have radio-location service as secondary user in almost whole (both ham and commercial) 70 cm band. In practice, this means ground-based or space-based RADARs. Space-based are following ITU-R SA 1260-1, which being only 15 pages long, I recommend that you read. It contains lots of interoperability information and tells you a bit about what to expect, basically answering in detail your question about power and duty cycle.

Now a bit of warning, my knowledge of RADARs comes from university course, not from practical experience, so I might be missing something obvious!

So first of all, space-based systems... I don't think there's too much to worry about you interfering them. They must already be designed (see 1260-1) to work properly if they're exposed to a ground-based RADAR illumination. There's pretty much nothing in amateur radio service that can compete with that level of interference. In addition, the signal from a ham station will basically show up as a sort of clutter and there are already very robust systems in place to deal with that.

On the other hand, the interference that can be coming from them might be a bit troubling in some cases.  
The type of RADARs used there is a so-called synthetic aperture radar. That means that the satellite will have a high-gain antenna pointed at a relatively small area on the ground that will be "scanned" by the RADAR. The satellite will then make a number of successive overflies over the area, each time "shaving" a strip of ground it scanned. The result of that is that the area that is under interference at one time moment will be relatively small and the interference will not last long, since the satellite keeps moving.

So in the picture here, the blue stripes are the "track" the satellite is covering on the ground and the red area is covered by the satellite at any one moment. Afterwards, the data is merged into a single image. When the track is passed, the satellite will, in the next orbit, shift it a bit to the side and repeat the procedure for the next track.

So what about signals that can be heard? Well if you want to hear something a bit similar to how it would sound, you can go to say http://websdr.ewi.utwente.nl:8901/ and on the waterfall look for signals that look like: ////////// or _ _ _ _ _ This would be over-the-horizon radars. Also keep in mind the "Woodpecker" nickname of the Cold-war era system. That's how they sound.  
The principles of operation are sort of the same, but you can expect much bigger difference in frequency and in pulse repetition period. Normally, the space-borne radars can be running with the peak power of several hundred watts (ITU recommendation used 400 W for some calculations) and can have few pulse repetition frequency of few kilohertz. Also the bandwidth will be several megahertz (ITU uses 6 as example), so you can expect them to be capable of covering big parts of the band. It should be kept in mind that for SAR systems, most of the gain comes from clever waveform design and off-line post-processing and not raw transmit power, so the aren't as bad as more traditional systems.

For your last part, I never actually heard of anyone reporting interference from space-based SAR systems, so I can only say what the ITU recommendation already says=> The systems are to be run in "campaign" mode with a duty cycle of 10%, but not exceeding 15%. Campaign mode means that the satellite will only scan a certain geographic area at a certain time and when outside of that area, it will switch the sensor off. This limits the possibility of creating interference to weak satellite systems in general. A specific pass might be jammed for a while, but situation should not repeat.

So my speculation is that you can expect some activity soon after the license is received and then a rapid decrease, after SAR pictures of interesting areas have already been made.

For ground-based systems, if they get allowed, I expect much bigger issues. They will have their few hundred watts on the ground, possibly near your antennas. This will most likely render the 70 cm band unusable to people in the affected area while the system is running, if you're unlucky enough to have a system running in the middle of the band. I haven't found any international documents regarding duty cycle or similar, but in my own opinion, I wouldn't expect the ground based systems to run continuously. They could run for several seconds every few minutes to get the update on the wind changes, but I don't see a reason why to keep them running continuously. This is also confirmed by some reports of interference to repeaters I've heard of. I myself haven't heard much about ground RADAR interference, because, based on reports I did hear of, such systems are only used sporadically in ham and neighboring bands in Serbia.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5992/experiences-on-a-70-cm-band-shared-with-radiolocation-service, by Rodrigo Magalhães, rclocher3, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
