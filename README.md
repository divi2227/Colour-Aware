# Colour-Aware

🎯 GOAL:

Help red-green colorblind people identify if a packaged food item is vegetarian or non-vegetarian, based on the symbol printed on the package (green or red dot in a square).


🖼️ EXPECTED VISUAL OUTPUT (on screen):


When you hold a packaged food item up to your webcam that has the veg or non-veg symbol, you’ll see:

✅ A rectangle drawn around the detected symbol

🟢 If it's green (veg):

The rectangle is green

Text "VEG" is shown near the symbol (in green)

🔴 If it's red (non-veg):

The rectangle is red

Text "NON-VEG" is shown near the symbol (in red)


🔊 EXPECTED AUDIO OUTPUT (via speaker):

If the veg/non-veg symbol is detected, the computer will speak aloud:

"Vegetarian" for a green symbol

"Non Vegetarian" for a red symbol

This only plays once per detection to avoid repeating constantly while the object is still in frame.


🧪 HOW TO TEST IT:

1) Hold up a packaged food item with a veg/non-veg symbol toward your webcam.

2) Make sure it's well-lit and visible (try with a white background if needed).

3) The camera window will show the symbol outlined and labeled.

4) You should hear the voice say "Vegetarian" or "Non Vegetarian".

5) Press q to quit.
