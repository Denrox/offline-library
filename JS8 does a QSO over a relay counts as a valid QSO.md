# JS8: does a QSO over a relay counts as a valid QSO?

*Tags: digital-modes · score 4*

## Question

I'm playing with the new JS8 mode. One feature I find particularly interesting is an ability to relay messages using rigs of other OP's. Though I'm not sure whether such QSOs should count as valid ones. Especially if it turns out that the station you try to contact runs in AUTO mode. I feel like I'm cheating.

Here is a particular example:

```
22:37:31 - (2187) - R2AUK: HB9AVK STATUS? ⌁
22:37:59 - (2185) - HB9AVK: R2AUK STATUS HB AUTO RELAY SPOT 0M V1.0.0 ⌁
22:38:49 - (2180) - R2AUK: HB9AVK SNR? ⌁
22:39:29 - (2185) - HB9AVK: R2AUK SNR +05 ⌁
22:39:37 - (2180) - R2AUK: HB9AVK HEARING? ⌁
22:40:14 - (2184) - HB9AVK: R2AUK HEARING KD8UJG KB8HTU KK4WTI CO2DC ⌁
22:41:24 - (2187) - R2AUK: HB9AVK> KD8UJG LETS QSO VIA RELAY HW CPY? EIH ⌁
22:42:44 - (2185) - HB9AVK: KD8UJG> LETS QSO VIA RELAY HW CPY? VIA R2AUK -UR ⌁
22:44:14 - (2184) - HB9AVK: R2AUK> ACK VIA KD8UJG ⌁

```

In this case I got a response from KD8UJG, though the template 'ACK' response suggests that this station runs in AUTO mode. Unfortunately I got no response for a relayed 'STATUS?' message or any other messages to confirm this - it looks like the station disspeared.

Though technically there was a contact. I don't see how it differs from using a satellite or a repeater in UHF case except that HF were used here. Wikipedia says:

An amateur radio contact, more commonly referred to as simply a "contact", is an exchange of information between two amateur radio stations. The exchange usually consists of an initial call, a response by another amateur radio operator at an amateur radio station, and possibly a signal report. A contact is often referred to by the Q code QSO. It is often limited to just a minimal exchange of such station IDs.

According to this definition a QSO over a relay counts, even if one of the stations (besides the relay) runs in AUTO mode. The only problem is that I'm not sure whether this is a generally accepted definition of QSO. Is there any reason (like existence of other definitions of QSO, or any other) why described case may not counts as a QSO?

## Accepted answer (score 3, by Brian K1LI)

Whether a contact "counts" depends on who does the counting.

For example, the rules for the ARRL DXCC Award state, "Contacts made through 'repeater' devices or *any other power relay methods* (other than satellites for Satellite DXCC) are **invalid** for DXCC credit." Similarly for the Worked All States Award (WAS), "Contacts made through repeaters or *any other power relay method* **cannot** be used for WAS credit."

There may, however, be reasons for organizations with different goals to count contacts on a different basis. For example, the Radio Amateurs of Northern Vermont (RANV) sponsored the RANV QSO Party to, "Bring life back to the FM repeater frequencies!" In this case, valid event contacts were *required* to be made through an analog or digital repeater.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13215/js8-does-a-qso-over-a-relay-counts-as-a-valid-qso, by Aleksander Alekseev - R2AUK, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
