from pair_color_transition import *

def color_manual():
        pair_no=1
        print("**************Reference Manual *****************")
        print("Pair_No.|Major_color\t|Minor_Color")
        for major_color in MAJOR_COLORS:
            for minor_color in MINOR_COLORS:
                print(f'{pair_no}\t|{color_pair_to_string(major_color,minor_color)}')
                pair_no+=1

def color_pair_to_string(major_color, minor_color):
   return f'{major_color}\t\t|{minor_color}'
