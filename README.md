Auspex
======
Auspex is a Python codebase for driving a 20x4 Character LCD on a Raspberry Pi to display Victory Point and Turn Counters for games of Warhammer 40,000.
I'm a Java and Rails programmer learning Python, so this is going to be hilarious at first.

Current Features
======
* Display VP and Turn counters
* Increment/decrement VP and Turn counters
* 3x event-triggered button inputs for cycle/increment/decrement

Features In Development
======
* Soft reset

Planned Features
======
* software switched LCD power
* Twitter integration with scrolling messages
* Sound effects
* Text to voice
* remote app support

Known Issues:
======
* DAKKA-22 LCD corruption on button presses

Version History
=====
* 0.3.0 | 433014.M2 | Working initial software features with hardware bug
* 0.2.0 | 420014.M2 | Working MET clock and event-triggered inputs
* 0.1.0 | 410014.M2 | Initial experiments, working static LCD display

References
=====
* http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
* http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2
* http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
* Wiring and LCD wrangling: https://github.com/dbrgn/RPLCD
* http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
