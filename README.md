# Equal Search
## Introductions：
This is a lightweight Python library which can support users search data by data
## Features:
1. Lightweight
2. Native python
3. High speed
## How to use:
For example you have three set of data:
|  Name  | color  | index  |
|  ----  | ----  | ----  |
| Apple | red | 1 |
| Pear | yellow | 2 |

And you are supposed to list all the fruits that the color is red ,so you can type:
```python
import Equal_Search as eq
file_path = "./add your path here"
eq.equal_search(file_path,red,0)#(the path,the feature,the index) 
```
and python will return "apple". 
So it allows you to search an object with its features.
