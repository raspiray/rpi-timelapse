#!/usr/bin/python

# RPi Timelapse - Timelapse software for the Raspberry Pi
# Copyright (c) 2021 by RBA Marketing
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
 
# Version 1

# Import Python Libraries
import os
import ConfigParser
import time
import picamera
import datetime
import sys

# Printme function prints to screen and log file
def printme( string_to_print ):
	rightnow =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	output =  "[" + str(rightnow) + "] " + string_to_print
	print output
	logfile.write(output)
	logfile.write("\n")
	return
	
def take_pictures( this_duration , tmp_picture_folder ):
	with picamera.PiCamera() as camera:
		camera.resolution = resolution
		camera.iso = iso
		camera.awb_mode = awb_mode
		camera.brightness = brightness
		camera.saturation = saturation
		camera.sharpness = sharpness
		camera.framerate = framerate
		camera.exposure_mode = exposure_mode
		camera.hflip = hflip
		camera.vflip = vflip
		#camera.led = led
		camera.meter_mode = meter_mode
		camera.rotation = rotation
		#printme ("Starting Pictures")
		number_pictures = pictures_per_hour * this_duration
		camera.start_preview()
		time.sleep(2)
		current_picture_number = 1
		printme ("Temp Picture Folder: " + tmp_picture_folder)
                #rightnow =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                #
                #mytimestamp = '/' + rightnow + '.jpg'
                #print mytimestamp
                current_picture_number = 1
		for i, filename in enumerate(camera.capture_continuous(tmp_picture_folder +'/{counter:09d}.jpg',quality=int(jpeg_quality))):
                        printme ('%s of %s pictures captured: %s' % (str(current_picture_number) ,str(int(number_pictures)), filename))
                        counter = '%0*d' % (9,i)
                       
                        time.sleep(interval-1) 
                        current_picture_number += 1
                        if current_picture_number > number_pictures:
                                break
                        rightnow =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                        
                        mytimestamp = '/' + rightnow + '.jpg'
                camera.close()
# End Functions

# Setup config parser and read config file
config = ConfigParser.ConfigParser()
scriptDirectory = os.path.dirname(os.path.realpath(__file__))
settingsFilePath = os.path.join(scriptDirectory, "config/timelapse.conf")

#Check to see if config file exists
if os.path.isfile(settingsFilePath):
	config.read(settingsFilePath)
else:
	print "Config file missing"
	print settingsFilePath
	sys.exit(1)

#Assign the config options to variables
duration = float(config.get('timelapse','duration'))
interval = float(config.get('timelapse','interval'))
file_prefix = config.get('timelapse','file_prefix')
picture_folder = config.get('timelapse','picture_folder')
completed_folder = config.get('timelapse','completed_folder')
log_folder = config.get('timelapse','log_folder')
make_mpg = config.get('timelapse','make_mpg')
delete_images = config.get('timelapse','delete_images')
jpeg_quality = config.get('camera','jpeg_quality')
iso = int(config.get('camera','iso'))
awb_mode = config.get('camera','awb_mode')
camera_height = config.get('camera','height')
camera_width = config.get('camera','width')
resolution = (int(camera_width),int(camera_height))
framerate = int(config.get('camera','framerate'))
exposure_mode = config.get('camera','exposure_mode')
brightness = int(config.get('camera','brightness'))
saturation = int(config.get('camera','saturation'))
sharpness = int(config.get('camera','sharpness'))
hflip = config.get('camera','hflip')
vflip = config.get('camera','vflip')
led = config.get('camera','led')
meter_mode = config.get('camera','meter_mode')
rotation = int(config.get('camera','rotation'))

#verify the log folder exists
if os.path.isdir(log_folder) == False:
        print ("Creating " + log_folder)
        system_command = "mkdir " + log_folder
        #print (system_command)
        os.system(system_command)

#Get the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
current_hour = datetime.datetime.now().hour

# Set the log file name

logfilename = log_folder + "/log_" + current_time

#open the logfile
logfile = open(logfilename, 'w')

file_time = ""

#Create the mp4filename
mp4filename = completed_folder + "/" + file_prefix + "_" + current_time + ".mp4"

# Calculate Total Number of Pictures
pictures_per_minute = 60 / interval
pictures_per_hour = pictures_per_minute * 60
pictures_per_day = int(pictures_per_hour * duration)
	
#output Configuration Settings for Logging Purposes
printme ("RPI TIMELAPSE REPORT")
printme ("Date:			" + str(current_time))
printme ("--------------------------------------------------------------")
printme ("TIMELAPSE SETTINGS")
printme ("--------------------------------------------------------------")
printme ("Duration: 		" + str(duration))
printme ("Interval: 		" + str(int(interval)))
printme ("Pictures Per Minute: 	" + str(int(pictures_per_minute)))
printme ("Pictures Per Hour: 	" + str(int(pictures_per_hour)))
#If your duration is under 1 hour, the pictures per day count will be wrong
printme ("Pictures Per Day: 	" + str(int(pictures_per_day)))
printme ("Picture Folder: 	" + picture_folder)
printme ("Completed Folder: 	"+ completed_folder)
printme ("Log Folder:		" + log_folder)
printme ("Log Filename:	" + logfilename)
printme ("File Prefix: 		" + file_prefix)
printme ("MP4 Filename:		" + mp4filename)
printme ("")
printme ("--------------------------------------------------------------")
printme ("CAMERA SETTINGS")
printme ("--------------------------------------------------------------")
printme ("ISO: 			" + str(iso))
printme ("JPEG Quality:		" + jpeg_quality)
printme ("AWB_Mode: 		" + awb_mode)
printme ("Resolution: 		" + str(resolution))
printme ("Frame Rate: 		" + str(framerate))
printme ("Exposure Mode: 		" + exposure_mode)
printme ("Brightness:		" + str(brightness))
printme ("saturation: 		" + str(saturation))
printme ("Sharpness: 		" + str(sharpness))
printme ("Hflip: 			" + hflip)
printme ("Vflip: 			" + vflip)
printme ("LED: 			" + led)
printme ("Meter Mode: 		" + meter_mode)
printme ("Rotation: 		" + str(rotation))
printme ("")

# delete all files in picture_folder
if delete_images == 'TRUE':
        system_command = "rm -fr "+picture_folder +"/"
        printme (system_command)
        os.system(system_command)
        system_command = "rm -fr "+picture_folder +"/tmp/"
        printme (system_command)
        os.system(system_command)

if os.path.isdir(picture_folder) == False:
	printme ("Creating " + picture_folder)
	system_command = "mkdir " + picture_folder
	printme (system_command)
	os.system(system_command)
	system_command = "mkdir " + picture_folder +"/tmp"
	printme (system_command)
	os.system(system_command)
	
if os.path.isdir(completed_folder) == False:
	printme ("Creating " + completed_folder)
	system_command = "mkdir " + completed_folder
	printme (system_command)
	os.system(system_command)

# This routine controls normal timelapse shooting without sunset deflicker
printme ("Normal Timelapse Started")
take_pictures( duration, picture_folder )
printme ("Normal Timelapse Finished")
	
# ffmpeg glob command
if make_mpg == 'TRUE':
		printme ("Starting ffmpeg")
		system_command = "ffmpeg -pattern_type glob -i '" + picture_folder + "/*.jpg' -s 1920x1080 -aspect 16:9 -r 24000/1001  -vcodec libx264   -an '"+  mp4filename +"' > /root/ffmpeg-" + current_time + ".log  2>&1 "
		printme (system_command)
		os.system(system_command)
		printme ("Finished ffmpeg")
logfile.close()
