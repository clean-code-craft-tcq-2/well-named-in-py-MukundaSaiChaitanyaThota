from color_test import *
from reference_manual import *

if __name__ == '__main__':
  color_manual()
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done:)')
