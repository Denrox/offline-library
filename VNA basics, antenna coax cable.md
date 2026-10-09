# VNA basics, antenna coax cable

*Tags: antenna, coaxial-cable, grounding, testing, vna · score 4*

## Question

Recently purchased my first VNA (Nano VNA) and I'm trying to learn the basics.

I have a 150MHz 1/4 wave whip antenna that I need to install on a large metal object so I was hoping to use a VNA to help me understand the performance of the metal object as a ground plane.

When I attach the antenna directly to the VNA I get results that seem to match the antenna specs. Optimum frequency is around 150MHz, SWR close to 1.

When I connect a length of coax cable (<1m) between the VNA and antenna everything shifts down to ~130MHz.

Is this telling me that the coax cable is detuning the system down to 130MHz or am I using the VNA incorrectly? Do I need to calibrate the VNA with my coax attached first? What is recommended for testing an antenna/ground plane in its final configuration?

Thanks

## Accepted answer (score 4, by webmarc)

You want to use the VNA against the final system configuration... or at least as much as practical. Why? The antenna's environment and transmission line **will** impact its characteristics.

It's pretty trivial to place and retrieve an antenna on a magmount on the roof of the car. So in this case, you simply plug the VNA in to the antenna in place of the radio. If you find you need to adjust placement of the magmount or length of the antenna, just grab it down and make the change. It's more challenging to do the same with a tower mounted yagi, so compromises will be made in testing configurations.

I *suspect* what you're finding is the need to place an appropriate choke at the antenna feed point. Dropping frequency by adding transmission line **may** indicate that the outside of the shield is a meaningful component of the system, which it should not be. Adding a choke at the feed point will help address the situation if that is indeed the cause.

When it comes to calibration, you'll want to do so with everything in the system attached to the VNA, replacing the antenna with the open/short/50Ω slugs that came with your VNA.

Happy engineering!!

## Answer (score 4, by nhw76)

If you want to understand what your radio "sees", which is probably the case, then you want to measure the entire system including the cabling to the antenna rather than just the antenna itself.

You calibrate the VNA for the configuration where it connects to the device under test.

So, from my point of view, the best test is to install the antenna; then measure at the coax connector that will attach to your radio. If you're connecting that directly to the VNA, then do your SOLT VNA calibration directly on the VNA port. If you're using a coax stub from the VNA, calibrate at the end of the stub.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20825/vna-basics-antenna-coax-cable, by P_J, webmarc, nhw76. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
