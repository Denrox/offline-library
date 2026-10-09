# CHIRP on Mac in 2021

*Tags: chirp, macos · score 5*

## Question

Has anybody had success in running CHIRP on a modern Mac? I am running OSX 10.15.7 and the download I found for Mac looks like just source code, no app file at all. I'm considering trying a build from source code, but before I get into that let me ask, has anyone got this working?

## Accepted answer (score 2, by Joshua Nozzi W4JLN)

That's ... complicated. You indicated macOS 10.15, which adds a ton of strict security pertaining to just what third-party apps are allowed to do. The download page on the CHIRP website has a link for macOS downloads. The download list highlights the recommended download in green (the "unified daily app" build). Just beneath that, the "**Confused about what to download?**" heading states this is the correct choice. Download that and unzip it and there's the built app.

But wait! There's more!

That same "confused" point about macOS links to a macOS-specific tips page. This page mentions two things to consider:

1. The app security measures I mentioned above means you'll likely have to grant whole-disk access to the app in order to be able to be able to open certain data files you'll need to open (since this is not a signed app).
2. You'll also need to install a driver specific to the kind of USB adaptor cable you're using. Again due to macOS security, an unsigned app can't go through the blessed security gate, so can't get the correct access to install and load any old device drivers.

Give that tips page a thorough read (there's even a troubleshooting section). It's not the prettiest getting-started process but it's open-source software that's maintained to be multi-platform, so it's not going to be a particularly smooth ride for any one platform. Except maybe for Windows, which most ham software targets. Even then, it's often bumpy due to the age of some of these apps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18617/chirp-on-mac-in-2021, by Randy L, Joshua Nozzi W4JLN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
