import mymodule
mymodule.func_in_module()

import mymodule as mm
mm.func_in_module()

from mymodule import func_in_module
func_in_module()

#it's kind of waste lots of memeory. not preferable to use
from mymodule import *
func_in_module()