Note that all of the programs are not mine. All credits go to their respective owners...

All patches are done by me.

Good links to use are: 
  - Nyan Satan's Dual Boot Guide https://nyansatan.github.io/dualboot/ Cydia Repo: nyansatan.github.io/apt
  - ShadowLee19's Dual/Triple Boot Guide: http://www.pmbonneau.com/apple/ios/multiboot.php (Use Google Translate if you don't know French) Cydia Repo: pmbonneau.com/cydia
  
  Credits:
  
	-Nyan Satan: Dual boot guide, WayOut, Dualbootstuff via Cydia repo, and for helping me :D
	
	-Planetbeing: Dmg, Imagetool, Ibootim, Xpwntool from xpwn
	
	-Danzatt: Reimagine

	-Jonathan Levin: Imagine, Jtool

	-Darwin-On-Arm: Image3maker

	-Zeex: ida_patcher

	-iH8Sn0w/Tihmstar: iBoot32Patcher
	
	-Axi0mX: kloader 32-bit (4.0-9.3.5) 64-bit (7.0-8.4.1)
	
	-Jonathan Seals: Helped clear some things up for me :D

###

Guide on using fuzzy_patcher

If you want to create a diff from a patched file, do "--diff --delta x.json (replace x with path and name you want your .json file) --orig (original/unpatched file) --patched (patched file)

If you want to use a diff file and use one of the main features on fuzzy_patcher "fuzz" to use fuzzy_patcher to fuzz the patches in the json file and apply them to an unpatched file.
Do --patch --fuzz (use 80 to begin with, if patches are not 100% go down, in decrements of 5 or 10) --orig (original/unpatched file) --patched (name of patched file)

