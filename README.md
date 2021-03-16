# mushroom-dataset
A JSON dataset filled with mushroom data. 

Follow the structure as seen if you want to comitt data.

Create a merge request and it'll be added as long as you follow the structure and the data is correct.

Structure for each mushroom is as follows

**All fields are strings unless specified as something different**
**? after varible means optional field
** Colors are hexadecimal strings

name_lat: latin name
name_swe?: swedish name 
name_x?: name in language x

color: array of colors

hymenium: hymenium type
hymenium_attatchment: hymenium attachment type
cap: shape of the cap
stipe: stipe modifications
spore_print: {color: array of colors, literal: the name of the color}
ecology: mushrooms ecology
edible: edibility of the mushroom, it can be either "edible, non-edible, poisonous or psychoactive"

division: 
class:
order:
family:
genus:
