# Can cellular radio be used for communication with a balloon?

*Tags: mobile, uhf, internet · score 9*

## Question

(Sorry, I don't know if this is the right forum for this question, but maybe someone will know the answer. If not, which StackExchange forum could be more suitable?)

Me and a few friends of mine are planning to build a remote controlled balloon probe. As there already were many projects involving stratosphere flights, we are rather trying to go just a few kilometers high, but establish a permanent data connection. The problem is that where I live (Germany), operating quite much any RF module with sufficient range is illegal for people without a radio license, which we happen not to have.

So instead of that we are thinking of connecting a RasPi to a 3G dongle and transmit our data over a TCP connection. But how high does the signal of cell towers usually reach? I have read very contrary opinions about this. And how good is the quality of a connection up there? Is it sufficient to send greater chunks of data like low-res pictures? Maybe it might be important that mobile connections in airplanes have the additional problem of needing to change cell towers very frequently because of the high moving speed, which would not be the case in a slow-moving balloon probe.

## Answer (score 2, by Charlie Melidosian)

I am by no means an expert, but here's my point of view on this. Cellphones get their data by a Cell Tower, and if you have ever been on a plane there is little to no reception once you are in the air. The reason this happens is because the cell towers are horizontally directional so that they can get the most range from the smallest amount of power possible. They don't waste RF by sending it up. I know it's not the answer your looking for, but I hope it helps!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5465/can-cellular-radio-be-used-for-communication-with-a-balloon, by ruthra, Charlie Melidosian. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
