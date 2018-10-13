The purpose to these scripts is to take an SVG and automatically generate a series of images from it, with my purpose being for YouTube Thumbnails.

To function the SVG needs to have two pieces of text in them !TYPE! and !PART!

For my reviews I work with two different types of videos that need thumbnails: review playthrough videos and general videos to share. The !TYPE! string is to mark which it is and !PART! will be either the 'Part #' identifier or the specific name for the general video.
	
Once the SVG has been made and contains the appropriate strings (!TYPE! and !PART!), simply drag-and-drop it onto the YouTube Thumbnails.bat file. The Batch file will ask how many parts there are, this is for the 'Part #' thumbnails. The PNG files produced for these will have zero padding to two digits, but the padding will not be within the image.

If you wish to generate thumbnails for other videos fromt he same background image, create a plain text file with the names you want on separate lines. With both the SVG and this text file selected, click and drag from the SVG file onto the Batch file. You will still be asked about the number of parts, but you can press Enter to skip this, give it 0, or give it the desired number. The appropriate images will be made and the file names will contain the name from the list you provided.

To tune the size of the thumbnails, so you can meet and not exceed the 2 MB limit, there is a height variable in 'YouTube Thumbnails.py'
