# Brad Bingo

## Included files:
- bingo.py     : Generates a printable sheet with 4 bingo boards
- phrases.txt  : A required file containing phrases that populate the boards
- README.md   : The file you're reading right now!

Creates 4x4 bingo boards using custom phrases.
4 Boards are tiled on each sheet of paper to allow for easy printing.

## Requirements and functionality:

### bingo.py
- Requires the "Pillow" library
- Reads from the phrases.txt file and creates a list of phrases
- Picks 16 random phrases and creates a bingo board
- Arranges 4 bingo boards onto a canvas for easy printing
- Saves the canvas as an image with a random number in the same folder

### phrases.txt
- A file that contains a single list of phrases (1 line)
- No restrictions on the number of list items
- Single commas separate list items (no comma after the last item)
- Must be in the same folder as bingo.py
- See included phrases.txt as an example
