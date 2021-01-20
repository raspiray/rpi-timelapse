# RPi TIMELAPSE README #

Easy to use timelaspe script for the Raspberry Pi.

### Required Software ###
python
python-picamera
python-gdata
imagemagick
ffmpeg


### How to install required software ####

apt-get install python python-picamera python-gdata imagemagick

### Installing ffmpeg on Raspberry Pi reunning Dietpi
On my Raspberry Pi timelapse cameras, I use the dietpi operating system.  DietPi is an extremely lightweight Debian OS, highly optimised for minimal CPU and RAM resource usage, ensuring your SBC always runs at its maximum potential.  Installing ffmpeg on the dietpi is a menu option and hassle-free.  I would suggest you check out this fantastic operating system at https://dietpi.com

### Installing ffmpeg on Rasbian and others
Here is a link to Google search results on how to install ffmpeg on Raspberry Pi computers.
https://www.google.com/search?q=raspi+install+ffmpeg

Sorry, I have never installed it anywhere else so I can't be of more help.

##Installing the RPi Timelapse software

Download the zip or clone using git into a folder on your pi.

# CONFIGURATION #

All configuration options are stored in config/timelapse.conf file.  

# USAGE #
python timelaspe.py

### License ###
This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, version 3.
