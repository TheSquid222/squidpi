== Thermocouple ==

To read from the thermocouple, get a Maxim Integrated MAX6675 thermocouple
sensor.  Connect SO pin on the 6675 to GPIO 9 (physical pin 21) on the
Raspberry Pi.  Connect the CS pin on the 6675 to GPIO 8 (physical pin 24,
SPIO CE0) on the Pi.  Connect the SCK pin on the 6675 to GPIO 11 (physical
pin 23, SPIO SCLK).  Connect the Max 6675 VCC to either a 3.3V or 5V pin
on the Pi or another power source, and Gnd to ground.

Start your Raspberry Pi configuration application (under your Raspberry Pi
menu, under Preferences).

Select the Interfaces tab and turn on SPI by clicking Enable.

Attach the thermocouple to the terminals.
