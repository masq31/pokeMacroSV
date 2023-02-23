# pokeMacroSV

This github repo hosts a macro script I worked on about a couple months ago. As of Janualy 2023 I’ve paused developing it out further due to not having enough time to put into this project, but it’s something I think would be a great project for someone interested in making macros, scripts for their favorite games or just finalizing to work within the technical constraints of the game it was made for itself. The project’s idea can be borrowed shared or use without any agreement or license. 

Game target: Pokemon Scarlet/Violet

Tools: Python 3.9, Raspberry PI 3b running Rasbian OS, NXBT and associated pip packages: https://github.com/Brikwerk/nxbt

Prerequisites: 

- Pairing the controller must be done on the switch menu. It can be done outside of this menu which is not recommended.
- The player character must have 3 spots on the map able to fly to.
- The cursor must be on the BOX icon in the pause menu
- The player storage box must be in a row at the top with select boxes empty, 4 boxes at a time. Each subsequent box must also have these slots empty.
The player character must be at the hub area. 

Tricks used in macro creation:

Getting around framerate inconsistencies relies on in game system mechanics. Intentional or not, these make this type of macro possible to use as a semi-autonomous system. To explain my mindset for a moment, these tricks are akin to video game speedrunners finding systems within the game that are turned to use to an advantage point. That is to say, RELIANCE ON THESE SYSTEMS WILL BE SUBJECT TO GAME FEATURE AND QUALITY OF LIFE UPDATES. I developed these scripts being fully aware of this. 

When the player is viewing the map screen. Moving the cursor has some leeway involved. Hovering over a marked destination will snap the cursor to the spot. Having inputs last a certain amount of time will move the map, but not far enough for a cursor to snap away if it is already over a marked spot. This allows us to get around framerate inconsistencies in the game, effectively anticipating the a worst case scenario and compensating with minor adjustments through the macro file. The solution isn't perfect and needs further refinement. This is the biggest obstacle to making sure this script runs. 

The rest of the write up updates is TBD as I have put this up haphazardly and on a late night whim. 
