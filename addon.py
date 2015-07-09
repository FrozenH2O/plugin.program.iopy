
import xbmcaddon
import xbmcgui
import sys, os
import EXIF
import shutil
import time

def format_dateTime(UNFORMATTED):
	DATE, TIME = UNFORMATTED.split()
	return DATE.replace(':','-')
 
 
def sortPhotos(path,targetpath):

	progress = xbmcgui.DialogProgress()
	progress.create('Backing Up', 'Press cancel to stop.')
    
	i = 0
	for root, dirnames, filenames in os.walk(path):
		#for filename in fnmatch.filter(filenames, '*.JPG'):
		for filename in filenames:
			i = i + 1.00
			if filename.lower().endswith(('.jpg', '.jpeg', '.mov','.m2ts', '.mp4','.avi')):
				PHOTO = os.path.join(root, filename)
	            
				percent = int( ( i / len(filenames) ) * 100)
				message = "Picture " + filename + " Checking"
				progress.update( percent, message)
	
				if filename.lower().endswith(('.jpg', '.jpeg')):
					f = open(PHOTO, 'rb')
					tags = EXIF.process_file(f, details=False, stop_tag='DateTimeOriginal')
	
					try :
						DATE = tags['EXIF DateTimeOriginal']
						DATE = format_dateTime(str(DATE))
					except :
						DATE = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(PHOTO)))
				else:
					DATE = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(PHOTO)))
					
				newpath = targetpath + DATE[0:4] + '/'
				if not os.path.exists(newpath):
					message = "Picture " + filename + " Create Target Folder " + DATE[0:4]
					progress.update( percent, message)
					os.mkdir(newpath)
	
				newpath = targetpath + DATE[0:4] + '/' + DATE + '/'
				if not os.path.exists(newpath):
					message = "Picture " + filename + " Create Target Folder " + DATE
					progress.update( percent, message)
					os.mkdir(newpath)
				
				if not os.path.isfile(newpath + filename):
					message = "Picture " + filename + " Copying to target folder"
					progress.update( percent, message)
					shutil.copy(PHOTO, newpath + filename)
				
				if progress.iscanceled():
					break

	progress.close()


# Main
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

 
line1 = "Are you ready to organise your images?"
xbmcgui.Dialog().ok(addonname, line1)

PATH = addon.getSetting("sdcard1")
TARGETPATH = addon.getSetting("backupfolder")

if PATH == "":
	line1 = "Go to IOpy Addon Settings and enter a source path."
	xbmcgui.Dialog().ok(addonname, line1)
	sys.exit

if TARGETPATH == "":
	line1 = "Go to IOpy Addon Settings and enter a target path."
	xbmcgui.Dialog().ok(addonname, line1)
	sys.exit

sortPhotos(PATH,TARGETPATH)

line1 = "Done"
xbmcgui.Dialog().ok(addonname, line1)








