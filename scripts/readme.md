# Scripts

This folder contains various scripts that can be joined to the models:

- `client_generator.py` which can be used to generate various attributes of a client coming in for a reading
- `draw_tarot.py` which can be used to draw a given number of tarot cards (Major Arcana only)

The point of passing a script is that it insures proper randomness and control of the output (compared to letting the model try and come up with the information) while being relatively fast to use (compared to having the model write or rewrite the code from scratch).

I recommend putting a snippet along the following lines in your prompt to teach your model how to call on the scripts you pass it:

```python
import sys, os

# Adding the file directory to the system path
sys.path.append(os.path.dirname('/mnt/data/'))

# Importing the scripts
from client_generator import generate_persona
from draw_tarot import draw_major_arcana

# Generating information for the session
client_info = generate_persona()
tarot_cards = draw_major_arcana(3)

client_info, tarot_cards
```