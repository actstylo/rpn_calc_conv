RPN Calculator and Converter
============================


## Requirements

Python >= 3.6


## Run Test


```bash

$ python -m unittest tests
 
```

## Example


### Reverse Polish Notation calculator

```
$ ./rpn_calculator.py
> 3 4 * 6 9 - 2 ^ +
21.0  

```


### infix to RPN converter

```
$ ./infix_to_rpn.py
> 3 * 4 + ( 6 - 9 ) ^ 2
3 4 * 6 9 - 2 ^ +

```

