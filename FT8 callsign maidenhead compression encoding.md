# FT8 callsign/maidenhead compression encoding

*Tags: software, callsign, math, ft8, encoding · score 7*

## Question

I have set myself a challenge to write a Matlab script as proof of concept to send an FT8 CQ call (not necessarily for live transmissions yet, but I may extend the project). So far I have:

- Generated and appended 14-bit CRC to precomputed message bits (from ft8code.exe utility in WSJT-X)
- Generated and appended 83-bit LDPC parity bits to give 174-bit channel symbols
- Implemented tone synthesis and audio-carrier modulation in Matlab for 8 FSK channel symbols

What I am missing is that I'd like to generate the message bits myself in Matlab from the callsign/grid locator. I understand that the callsign is converted to 2*28=56 bit field, locator is converted to a 15 bit field, and there are 6 message type bits giving 77 bits.

My question therefore is

- How do I convert the callsign to a 56-bit binary value and the locator to 15 bits?
- Does it use an ASCII table? Presumably it uses a 0-9, A-Z, space character set.
- What kind of compression is used to squeeze 4-character locator into 15 bits etc? I know the last 6 bits for CQ messages as these do not change so that's one piece of the puzzle.

## Accepted answer (score 8, by hobbs - KC2G)

You can find the code in packjt77.f90. Callsign encoding (for "standard" callsigns that don't require hashing) is in function pack28. A quick summary:

1. Adjust a few strange prefixes that don't follow the usual arrangement of letters and numbers. Swaziland 3DA0* will be encoded as if it was 3D0* instead, and Guinea 3XA1A will be encoded as if it was QA1A instead. This adjustment is reversed in the decoder, which is possible because it maps to unused parts of the callsign space.
2. "Align" the callsign into a 6-character field by identifying the last (or only) digit, and placing it in the third position. If there are fewer than two characters before the digit, or fewer than three characters after the digit, pad with spaces. If there are more than two characters before, or more than three characters after, this is a "nonstandard" callsign and has to be encoded by hashing. Example: my callsign KC2G becomes "KC2G ", N2XYZ becomes " N2XYZ", and 4U1ITU stays "4U1ITU".
3. Map the first character to its position (zero-indexed) in the list  
" 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" (37 possibilities), the second to its position in the list "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" (36), the third to its position in the list "0123456789" (10), and the fourth through sixth to their positions in the list  
" ABCDEFGHIJKLMNOPQRSTUVWXYZ" (27). Example: " K1BC " becomes (0, 20, 1, 2, 3, 0)
4. Read this off as a variable-base-(37, 36, 10, 27, 27, 27) integer, e.g.  
((((0*36 + 20)*10 + 1)*27 + 2)*27 + 3)*27 + 0 = 3957822, or equivalently  
36*10*27*27*27*0 + 10*27*27*27*20 + 27*27*27*1 + 27*27*2 + 27*3 + 0 = 3957822.
5. Add 6257896. The first 2,063,592 codes are used by CQ/QRZ calls, and the next 4,194,304 are used by 22-bit hashed callsigns; regular callsigns start after that. 3957822 + 6257896 = 10215718.
6. Encode the number as 28-bit binary, big-endian; 10215718 = 0000100110111110000100100110.

For grid squares, the encoding is similar except there's no alignment necessary, and it's a base-(18,18,10,10) integer, so FN20 becomes (5, 13, 2, 0), which becomes the integer 5*18*10*10 + 13*10*10 + 2*10 + 0 = 10320. This is then packed into 15 bits. Note that the "RR73" message is actually encoded as a callsign pair plus the grid RR73 (which is valid, but in an uninhabited bit of arctic ocean north of Siberia), and that reception reports are encoded as the values above RR99 (32480).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16216/ft8-callsign-maidenhead-compression-encoding, by jemussi, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
