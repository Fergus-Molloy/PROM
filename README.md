# PROM
For storing code and other files releated to the PROM project

## Introduction
For this project we will be implementing a the game of pong using a headless raspberry pi that communicates the game via I2C for inputs and transmitting ASCII escape cahracters across a serial bus to output the game. 

## Requirements
The core requirements of this project are as follows:
1. The game implementation is to be displayed on a serial terminal on a
remote machine.
2. All graphical display commands must be displayed on this terminal and
transmitted across an RS232 serial link using ANSI escape code
sequences. For more information on this topic refer to:
https://en.wikipedia.org/wiki/ANSI_escape_code
3. All game software must be executed on the Raspberry Pi. Only a serial
terminal may run on the remote machine i.e. you may run a single SSH
terminal on the remote machine to control the Raspberry Pi, however,
this must not be used in the game.

## Game Display
The default serial terminal screen size is 80 columns × 20 rows i.e.
characters, as shown in figure 1.
![figure 1](https://imgur.com/a/4CE6fob)
Within the display, the following sizes are required :
1. Bat: size 1 × 3, placed three columns from the edge.
2. Ball: size 1 × 1.
3. Net: placed in column 40, dashed line, one column thick by two rows
long
4. Scores: size 3 × 5, numerical display, 0 to 9, placed 8 columns from the
net.

## Player Controls
1. Each player's bat should be controlled using a rotatational variable
resistor.
2. When the variable resistor is rotated clockwise the bat should move up
and when the variable resistor is rotated anti-clockwise the bat should
move down.
3. One bat controller must use the ready-integrated ADC and the other
must use a group designed ADC (see guidance note in section 2.5.2).
4. The bat should stop if it reaches the top or bottom display limits.
5. The bat should not move forwards or backwards i.e. it should only
move up or down the Y-axis.
6. Each player should additionally have two push buttons on their
controller: button 1 and button 2 (see guidance note in section 2.5.3).
7. Button 1 controls the serve of the ball. At the start of each point the ball
is fixed in front of the serving players bat. This player can serve from
any position on their base line, by pressing this button.
8. Button 2 controls the size of the bat. During the game a player may
change the size of their bat. Pressing this button will double the length
of the bat for 15 seconds. This option may only be used twice during a
game.

## Game Execution
1. In the game each player has five serves, when they have completed
these, service switches to the other player.
2. The ball should take approximately 3 seconds to travel across the
display.
3. When a player servers, the ball will travel towards the other player. If
the ball hits the top or bottom display limits and it is at least four
columns away from the left or right display limits it will bounce off this
edge and continue towards the other player.
4. When the ball reaches the fourth column away from the left or right
display limit, if any part of the that player's bat is in 'contact' with the
ball, the ball will bounce off the bat and travel back to the other player.
5. If ball does not make contact with that player's bat, it will continue
through and off the screen. At this point the other player's score is
increased by one and service returns to the serving player.
6. Each player's score is displayed as shown in figure 1.
7. The first player to ten is the winner and declared as such.

## Hardware individual work
1. Each group will require two controllers, containing a variable resistor
and two switches. The hardware team member must make these
controllers (requires using the soldering iron).
2. You must also develop a diagnostic display on the SSH terminal
running the python program. This display must not scroll i.e.
information should appear in fixed locations on the terminal. As a
minimum the information displayed should included: ADC values,
Button states, Bat positions and their state.
Page 7 of 20COM00010C


## Interfacing individual work
All switches must use either hardware or software de-bounce and must be
implemented by the interfacing team member.
1. Construct a hardware de-bounce circuit for at least one switch.
2. Design a software routine to de-bounce at least one switch.
Refer to the appropriate FESC lectures and laboratory scripts for further
information.


## Software individual work
The software team member must:
1. Use the eight onboard LEDs, shown in Appendix F, to construct a
linear display to show the progress of the ball across the court, as
shown in figure 2. (For more information on the onboard LEDs i.e.
which Raspberry Pi GPIO pins are connected to which LED refer to the
Raspberry Pi circuit diagrams available on the VLE. )
2. Use a PCF8574 I/O expander to build the appropriate hardware and
replicate this display on a bread board. (The data sheet for this device
can be found on the VLE in the data sheet folder. You cannot use
general purpose outputs or other I2C devices for this functions.)

## Optional Software Components
Note that the sum of all HW/SW optional component marks is capped to 40.
### Display colours (2 marks)
On the serial terminal use different colours for the net, ball, bats and player
scores.
### Light effects using PiGlow (3 marks)
When a player wins a point a light effect is produced on the PiGlow. Refer to
the PROM laboratory scripts for further information on this display. To score
full marks a number of different LEDs must be used and varying brightness.
Page 8 of 20COM00010C
### Scale ADC data (3 marks)
Analogue to digital converters (ADC) have problems working with very small
signals, for the ADC used in this hardware, around 0V, as background noise
tends to swap the input signal. They can also have difficulties with very large
signals, for this ADC near +3V, as analogue components tend to enter a non-
linear region of their response curve i.e. saturate. To overcome these
problems rescale the ADC input signal such that the voltage range 0.5V to
2.5V correspond to the MIN and MAX positions i.e. top and bottom of the
display, increasing the sensitivity of the controller.
The maximum and minimum ADC values must be defined as constants within
the python code. You will be asked during the demonstration to alter these
values and demonstrate that the new voltage range moves the bats to the
appropriate positions. Before the demonstration starts you must connect a
multi-meter to one of the analogue inputs so that the input voltage is
displayed. Failure to do some will prevent the awarding of full marks.
### Noise rejection (3 marks)
If the position of the analogue control signal is set near the boundary of two
positions random noise can cause the bat to oscillate between these two
points. Write a software function to rejects these small change whilst allowing
the bat to respond quickly to significant input changes. Full marks will only be
awarded if there is no significant latency in bat position updates. During your
demonstration you will need to describe how this software works for different
types of input signals e.g. random noise, slow changes and fast changes.
More information on these types of filter is available here:
https://en.wikipedia.org/wiki/Moving_average
### Sound effects using piezoelectric buzzer (3-8 marks)
When the ball hits the bat a sound effect is produced by the piezoelectric
buzzer. Additional marks are available for multiple tones, start of game
'music', etc, see marking scheme for further details. Refer to the PROM
laboratory scripts for further information on how to use this device.
### Random speed (5 marks)
To simulate different return strengths the speed of the ball may vary e.g. once
the ball has left the bat it normally takes 3 seconds for the ball to travel from
one side to the other, fast returns will take 2 seconds, slow will take 7
seconds. The speed at which the bats move up and down the baseline should
not change. These times are only approximate, different speeds may be
defined by the group for fast and slow.
### Different trajectories (8 marks)
To simulate different types of stroke, if the ball hits the bat in its top third, the
ball will travel back in an upwards trajectory. If the ball hits the bat in its middle
third, the ball will travel back in a straight trajectory. If the ball hits the bat in its
bottom third, the ball will travel back in a downwards trajectory. The position
on the bat that defines top, middle and bottom can be defined by the group.


## Optional Hardware Components
Note that the sum of all HW/SW optional component marks is capped to 40.
### Filters (3 marks)
A common problem associated with analogue signals is noise e.g. transient
spikes, or white noise on top of the required signal. To improve the quality of
the rotation sensor signals i.e. the variable resistors, these signals should be
filtered using a low pass filter. Refer to the appropriate FESC lectures and
laboratory scripts for further information. A nice article on low pass filter
design is available here:
http://tinyurl.com/6caw4u
When implementing this filter you may need to use an operational amplifier
you are not allowed to use the 741 operational amplifier, or +12 / -12V power
supplies. Circuits using either of these will be awarded a zero mark. The
operational amplifier that must be used to implement this circuit is a LM324,
powered using +5V and 0V power supply.
### Voltage Reference (3 marks)
The analogue to digital converters used by the Raspberry Pi will convert input
voltages from 0V to +3V. Voltages larger can +3V can cause interference
resulting in an incorrect conversion. Design a voltage reference source to
ensure that the voltage produced by the variable resistors can not exceed
+3V.
### Sound effects using piezoelectric buzzer (3-8 marks)
Using a 555 timer or an operational amplifier generate a waveform that can
drive the piezoelectric buzzer. One possible implementation is shown in figure
3. The output of this circuit VOUT should be combined with digital logic gates
to produce the final siren circuit. Then under software control use this
hardware to generate a sound effect when the ball hits the bat. Additional
points are available for multiple tones, start of game 'music' etc. A nice article
on the 555 timer:
https://en.wikipedia.org/wiki/555_timer_IC
PTO
Page 10 of 20COM00010C
Figure 3: Astable multi-vibrator
### Piezoelectric buzzer amplification (3 marks)
To increase the loudness of the piezoelectric buzzer a push-pull driver stage
using five 7404 inverters can be constructed. One possible implementation is
shown in figure 4. During your demonstration you will need to describe how
this circuit works to score full marks. You may also wish to consider
constructing an exponential horn:
https://en.wikipedia.org/wiki/Horn_loudspeaker
Figure 4: push-pull driver
Page 11 of 20COM00010C
### Seven segment display (5-12 marks)
Using the I2C PCA9534 GPIO expander, shown in Appendix H, design a 7
segment LED display driver to count down the sequence 3,2,1,0 to indicate
the start of the game. You are not allowed to connect this LED display directly
to the Raspberry Pi GPIO lines, or a different I2C device.
Note, you will need current limiting resistors and an appropriate output buffer
when driving these LEDs, otherwise they will be damaged.
Additional marks will be awarded if you can design and implement a digital
2-to-7 decoder allowing you to drive the appropriate LED segment using a 2bit
binary code. You must implement this circuit from basic logic gates. You may
also use diodes to implement a simple memory element.
Further marks will be awarded if you can design and implement a digital
4-to-7 decoder allowing you to drive the appropriate LED segment using a 4bit
binary code such that you can display a full count sequence i.e.
9,8,7,6,5,4,3,2,1,0. You must implement this circuit from basic logic gates.
You may also use diodes to implement a simple memory element.
4.6 CPLD Analogue to Digital Converter (8 marks)
Using a CPLD board construct a Digital to Analogue converter (DAC) as
described in the data sheet below:
http://www.xilinx.com/support/documentation/application_notes/xapp154.pdf
Use either a delta-sigma or loadable ring counter, implement a DAC in VHDL.
Combine this DAC with an external analogue comparator, implement an 8bit
ramp Analogue to Digital Converter (ADC). The ADC's eight bit output should
be connected to the Raspberry Pi using GPIO lines, or an I2C device. Then
within the constants.py file replace the I2C ADC controller input with this
hardware. The CPLD should use a 4 MHz clock oscillator module, available
from the component cabinet.
As previously discussed you are not allowed to use the 741 operational
amplifier, or +12 / -12V power supplies. Circuits using either of these will be
awarded a zero mark. The operational amplifier that must be used as the
analogue comparator is a LM324, powered using +5V and 0V power supply.
If you implement this ADC you must still demonstrate the original I2C ADC
controller's functionality to obtain the core system marks.

