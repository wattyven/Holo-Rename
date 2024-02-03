# Holo-Rename
Renames folder and file names that were erroneously encoded by Windows using CP437 back to CP932

You may have noticed that some members-only content, especially zip archives, have broken subfolder and file names such as `ò╟Äå` (meant to be 壁紙) and `2îÄâüâôâoü[â{âCâX.wav` (meant to be 2月メンバーボイス.wav); this is because the archives were originally compressed on a machine with a Japanese Windows installation, where by default Windows encodes characters using [Code Page 932](https://en.wikipedia.org/wiki/Code_page_932_(Microsoft_Windows)). However, trying to access it on a machine with a different regional version of Windows, such as a North American machine that by default uses [Code Page 437](https://en.wikipedia.org/wiki/Code_page_437), will interpret the characters incorrectly and thus spit out the aforementioned gibberish strings. 

This is a short program that will help rename all the files and subfolders within a specified directory back into Japanese.

## To use:

Requirements: Python3 installation on your machine

Open up the program in a text editor of your choice and make sure the directory is correctly set. 

Additionally, make sure that the `wrong_encoding` variable is correctly set for your machine; I've preset its value as `CP437`. `correct_encoding` has already been preset to `CP932`.

Finally, run it! From the directory the program is in, in a terminal window simply run `py holorename.py`

Enjoy your Hololive membership content, now once again back within legible directories!
