# Is compression "encryption" under FCC regs?

*Tags: united-states, legal, digital-modes, encryption · score 5*

## Question

I read [this question](Signing%20of%20messages%20transmitted%20over%20ham%20radio.md) about digital signatures and FCC prohibitions on "obscuring" messages in amateur transmissions, and it cause me to think of something: the difference between encryption and compression is small.

If I send a file in compressed form via digital radio (say, a Mesh running on firmware-modified wifi routers, to support data rates that don't make this silly), the contents are easily decompressed by anyone who receives the file in error-free form (and most compression systems include redundant error correction codes to reduce the likelihood that the file will fail decompression) -- but without attempting decompression, there's no simple way to tell whether the file is encrypted within the compressed archive.

It would obviously be a no-no to send an encrypted archive by amateur radio, I think, but where is the line drawn? Does compression itself count as "obscuring" the contents?

## Accepted answer (score 6, by Glenn W9IQ)

For governments around the world to continue to trust that amateur radio has no nefarious purpose, it is essential that everyone that wishes to, can "listen in" to any amateur radio communications. Anything that hints at eroding this capability will likely be struck down in time through regulation.

To pass the FCC legal hurdle regarding obfuscation, it must first be evident that the purpose is not to obscure the message. Part of this test would likely be that the technique must accomplish some useful level of compression if that is really its purpose.

The legal second test would likely be that can anyone readily decompress the message to return it to its clear text form. This must be very easily achievable due to broad publication or acceptance of the compression method.

Both tests are important. For example, consider a symmetric encryption scheme using an industry standard and with the encryption key widely published on the web. This will possibly pass the second test but it would fail the first test because it doesn't actually compress the message in any real sense. It is also clear that the public standard is primarily for encryption (obscuring) and not compression (reducing).

On the other hand, FT8 makes extensive use of compression. The standard is well published so that anyone wishing to decode the bits can do so. Even though the compression "obscures" the message - it is clear the purpose of the technique is compression. Furthermore, the software to copy FT8 transmissions is readily available for free. Everyone can "listen in". So FT8 passes both tests.

Even Morse Code uses a form of compression by using shorter symbol lengths for the more commonly used letters. Clearly it passes both tests.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13009/is-compression-encryption-under-fcc-regs, by Zeiss Ikon, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
