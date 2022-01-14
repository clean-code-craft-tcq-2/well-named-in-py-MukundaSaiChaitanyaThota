from pair_color_transition import *

def color_manual():
        pair_no = 1
        print("Pair_Number" ,color_pair_to_string("Major_color","Minor_Color"))
        for color1 in MAJOR_COLORS:
            for color2 in MINOR_COLORS:
                print(pair_no,color_pair_to_string(color1,color2))
                pair_no += 1

def color_pair_to_string(major_color, minor_color):
   return f'{major_color} {minor_color}'
