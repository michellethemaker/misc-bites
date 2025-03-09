# Brief description of scripts

## addAuthorToPDF
As described. Adds authorship to your pdf files. Modify script to add other metadata to your pdf.

```python
python addauthortopdf.py
```
Enter a partial filename to search for relevant pdfs, before entering the full filename.

Enter your author's name, and that's it.

## generate_bestfit_circle
As described. Based on 10 points, generate the best fit circle. Displays results in a plot. Best fit circle eqn provided too!

- Calculates geometric distance of points from centre

- Calculates how much given points deviates from mean distance (i.e. residuals) 

- Uses least squares method to minimize the residuals to find best fit circle's centre. 

- Radius is then found from the mean of data points optimised by least squares method.

- Equation of circle is now derived with radius and coords of centre found

```python
python generate_bestfit_circle.py
```

## generate_bestfit_polynomial_line
As described. Based on 10 points, generate the best fit line. Displays results in a plot. Best fit polynomial eqn provided too!

```python
python generate_bestfit_polynomial_line.py
```
## pdfextractor
Parses through all PDFs for specific texts, saving them in a .csv file called output.csv. This file will be found in the same directory as the script itself.

**Requirements:** 

* Python >= 3.9.0
* Install pymupdf:
```
pip install pymupdf
```
* Script must be in the folder containing the folder containing the PDFs. 

```python
python pdfextractor.py
```
## soundcontrol
Windows 10 macro. Honestly I think only I would use this. It's a macro to change specific apps' audio source btwn headphones or speakers. Friggin Realtek drivers broke again I think, so when I switch specific apps to headphones and restart my desktop, most apps won't register this change and insist to play from the speakers, and I'll have to go to Windows' Sound Settings, switch the option to speakers, and back to headphones. I'm sick of fixing my stupid audio drivers so instead I made this dumb macro. Honestly it's just an excuse to play more with pyautogui after working with it for my mouseglove2.0. There's a lot of code that could be optimised and cleaned up but since it's just for me and it works I refuse to spend more time on this. 

Tip 1: I created a bat file per major app+speaker/headphone combo for my desktop, so I just need to click on the right one to activate the right macro.

Tip 2: If you want you can make custom .ico for them, just right click the bat file-> Send to desktop, then change the .ico of the shortcut created.

**Requirements:** 

* Python >= 3.9.0
* Install psutil and pyautogui
* Captured images of the speaker/headphones options in Windows' Sound Settings page. Sample of 'symbol_sound_headphones.png' as follows. Do one for the speakers as 'symbol_sound_speakers.png' too:
  
![symbol_sound_headphones](https://github.com/user-attachments/assets/804690df-d7f7-4349-b232-1653f46296ad)
* Captured images of the icons of the apps you want options for. Capture with height that's as high as symbol_sound_headphones.png^, so pyautogui knows where to look for that option. Try to capture one white version and one grey version. Save the second one with '2' appended. Sample of 'symbol_sound_spotify.PNG' as follows. The grey one would be saved as 'symbol_sound_spotify2.PNG':

![symbol_sound_spotify](https://github.com/user-attachments/assets/a65dab23-cb93-4bde-ac6d-fb05b14040e4)

<ins> To simply open the sound settings window:</ins>
```python
python soundsettings.py --program soundsettings
```
<ins> To change the audio source of a specific app, you need to know what name your app runs under psutil. if you don't know, you can run this and try to find its name. </ins>
```python
python soundcontrol.py --program listapps
```
<ins> To actually change the audio source, use this. so if you already know what name your app runs under psutil, use that for your args under -app. For example, if spotify looks like 'spotify.exe' under psutil, use 'spotify' in the --program argument, no need for '.exe'. Use 'speakers' for speakers, and 'headphones' for headphones'.:</ins>
```python
python soundcontrol.py --program changesoundsource --app spotify --source speakers
```
