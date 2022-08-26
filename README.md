# smath: shorthand for math
`smath` is intended for students and other frequent users of iPython for numerical and symbolic computations. It cuts down on the amount of keystrokes required to perform repetetive operations like initializing vectors and solving equations. This isn't helpful for writing scripts, but when you type things like
```python
import numpy as np
a = np.array([1,2,3])
np.linalg.norm(a)
a = np.array([4,5,6])
np.linalg.norm(a)
```
repeatedly (for example, if your homework set involves computing norms of 10 different vectors), then replacing the above with
```python
from smath import *
a = V(1,2,3)
n(a)
a = V(4,5,6)
n(a)
```
is more comfortable, ergonomic, and efficient.


## Installation and Use
- Clone this repository somewhere on your `$PYTHON_PATH`.
- Create a virtual environment with all dependencies.
```bash
git clone git@github.com:elicox0/smath
python3 -m venv smath_env
source smath_env/bin/activate
pip install -r requirements.txt
```

