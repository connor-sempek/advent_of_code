# imports
import os
from typing import List, Union

# Read in puzzle inputs from `data` folder at root of repo.
# Files containing puzzle inputs are formatted as 2021_day_<day number>_input.txt
INPUT_DIR = 'data'
INPUT_FN_TEMPLATE = '2021_day_{}_input.txt'

def get_puzzle_input(day: int, input_dir=INPUT_DIR, input_fn=None) -> List[str]:
    """load puzzle input for a given `day` value from the `data` folder at the root of the repo.
    """
    input_fn = input_fn if input_fn is not None else INPUT_FN_TEMPLATE.format(day)
    fp = os.path.join(input_dir, input_fn)
    with open(fp, 'r') as f:
        return [ln.strip() for ln in f.readlines()]