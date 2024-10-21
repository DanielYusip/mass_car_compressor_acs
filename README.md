# mass_car_compressor_acs
Compress cars from Content Manger Server tab into 7z files, before uploading to CDN.

Tool for Content Manager, that takes entry_list json file, looks up the cars in the assetto corsa/content/cars folder, compresses (into .7z format) the cars from the entry_list and puts them in a separate folder.

This tool was inteded to save time, by automating compression before uploading the car files to the CDN for auto-install-missing-content feature.

One .py script, multiple use cases:

1. Run in bg, by setting cpu cores to something low like 1 or 2.
2. Run and compress asap, by setting the processes to a high number (999999 won't work. Check max Cpu cores u have)

# how to use:

1. Open config.json
2. Edit your file location/cpu core usage
3. Run python script by opening command line, cd into your directory with the code and type in python car_compressor.py
4. Enjoy precious time and mouse clicks saved.


Notes: for config.json

"num_procs": 4,  # Number of processes to use for compression (limited by ur cpu cores I think). Setting to something low will make it way slower but makes sure it doesnt crash ur shitty intel cpu heheh

"compression_preset": 1  # Presets but I didn't test if all of them work. This one should. Read more about py7zr if u wanna touch this ting


Keep in mind - I never coded with python, and this is my first public code for Assetto Corsa.

I will prolly post more updates becoz this is somewhat fun.


=======================================

If you modify this file - give me credit and make the code open source. If you use the modified version in commercial (to earn money one way or another, related), you need to share the code by creating a github page and sharing it there.
