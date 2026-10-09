# How does AMPR work over IPIP tunnels?

*Tags: software, packet, mesh-network · score 3*

## Question

I'm experimenting with AMPR, and I have been allocated a 44.x.x.x IP address block which I'd like to use via an IPIP tunnel. There are some tutorials out there but none of them explain what happens behind the scenes. Can anyone explain?

In particular, When the IPIP tunnel is created, no endpoint is specified (see script https://github.com/NotMikeDEV/RIP44/blob/master/rip44.lua). When I send packets through the tunnels, how does Linux know where its endpoint is, i.e. where to send the packet?

My understanding is that this not just a mere tunnel but a mesh network. How does it work?

## Accepted answer (score 3, by Phil Frost - W8II)

FYI, I'm writing this as someone experienced with Linux IP routing, but only superficially familiar with AMPRNet.

All of the routing appears to happen through ordinary Linux facilities which can be inspected and modified with ip. AMPRNet appears to broadcast route advertisements to a multicast address, and this RIP44 daemon receives them and then runs ip to configure the kernel with the routes it discovers.

The lua script begins by configuring a rule to route traffic to LOCAL_SUBNET to the main routing table:

```
os.execute("ip rule add to " .. LOCAL_SUBNET .. " table main priority 20")

```

The main table is the route table Linux uses ordinarily, but it does so by a default rule which has a low priority. The script just adds a higher priority rule which does the same thing only for your local subnet.

Then, it adds a slightly lower priority rule to send everything else to a routing table called ROUTING_TABLE:

```
os.execute("ip rule add from " .. LOCAL_SUBNET .. " table " .. ROUTING_TABLE .. " priority 25")

```

The lua script adds routes to this other routing table (ROUTING_TABLE) according to the RIP44 multicasts it receives in the process_route() function. The most relevant line is 78:

```
os.execute("ip route replace " .. prefix .. " via " .. gateway .. " onlink dev tunl0 table " .. ROUTING_TABLE)

```

prefix and gateway are values the daemon received from a RIP44 multicast. onlink dev tunl0 is the part that makes the AMPRNet traffic use the ipip tunnel. The option is described by ip-route(7) as:

**onlink** pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.

The table option tells ip route to add this rule to this table containing only AMPRNet routes rather than the default main table.

Because these routes are not in the main table you will not see them with ip route show unless you ask to see the table specifically with ip route show table ROUTING_TABLE (replacing ROUTING_TABLE with the value configured in rip44.conf) or all the route tables with ip route show table all.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18799/how-does-ampr-work-over-ipip-tunnels, by divB, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
