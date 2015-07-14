# plugin.program.iopy
Image Organising Python Kodi Addon.
N.B.
I've only tested this on a raspberry pi with openelec 5.0.8.  Before using this read the code to make sure you're happy with what its doing.

####Description
Kodi Addon to backup and organise image files.  Uses the EXIF date for the folder names.

####Instructions:
This addon has 2 settings - Source folder and Target folder.
Don't set the target folder to be a sub folder of the source folder as the world may end :)

After defining where your images are and where you would like to put them, you can run the addon.

It will then iterate through each file, if the file ends in .jpg or .jpeg (case insensitive) it will use the EXIF DateTimeOriginal to move the file to Target folder / YYYY / YYYY-MM-DD
Where YYYY is the year the photo was taken and YYYY-MM-DD is the date in that format the photo was taken.

If the filename ends in .mov, .m2ts, .mp4 or .avi it will use the filedate to work out the year / date

i.e. DATE = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(PHOTO)))

This is okay if you are copying from the original memory card, but if the file isn't in its original location and was moved on a different date you will get the incorrect date.

It will create any missing folders.
It will not overwrite files if the filename exists.

####Why?
Whilst travelling I wanted to take a few Movies and TV shows with me, and thought it would be a good idea to use my portable Hard drive to backup my photos.  But I didn't want to take a full laptop with me.

I've got a Raspberry Pi and a 1TB portable drive, and I use Openelec/Kodi at home.  So I was going to use the File manager in Kodi to copy the pictures from my camera's SD card onto the 1TB drive, but I thought it would be neater to run a script to copy each image into a folder with the date the photo was taken, to save me doing it.

It seemed the best way to run a script from Kodi is via an addon, but that needs to be written in python.


####Thoughts / TODO:
Perhaps I should prefix each image file with something unique, because e.g. iPhones images are all called IMG_0001.JPG, and if you backed up more than 1 iPhone there is a possiblity that the filenames would not be unique.  I think.

Use EXIF data for .mov, .mp4, .avi too.

