# Holo-Rename
Renames folder and file names that were erroneously encoded by Windows using CP437 back to CP932

You may have noticed that some members-only content, especially zip archives, have broken subfolder and file names such as `ò╟Äå` and `2îÄâüâôâoü[â{âCâX.wav`; this is because the archives were originally compressed on a machine with a Japanese Windows installation, where by default Windows encodes characters using [Code Page 932](https://en.wikipedia.org/wiki/Code_page_932_(Microsoft_Windows)). However, trying to access it on a machine with a different regional version of Windows, such as a North American machine that by default uses [Code Page 437](https://en.wikipedia.org/wiki/Code_page_437), will interpret the characters incorrectly and thus spit out the aforementioned gibberish strings. 

This is a short program that will help rename all the files and subfolders within a specified directory back into Japanese. Enjoy your Hololive membership content, now once again back within legible directories!
