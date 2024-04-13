# Equal Search

## Introductions：

This is a lightweight Python library which can support users search data by data

## Features:

1. Lightweight

2. Native python

3. High speed

## How to use:

### 1. Search:

| Name  | color  | index |
| ----- | ------ | ----- |
| Apple | red    | 1     |
| Pear  | yellow | 2     |

And you are supposed to list all the fruits that the color is red ,so you can type:

```python
    import EqualSearch as es
    file_path = "./add your path here"
    es.equal_search(file_path,red,0)#(the path,the feature,the index)
```

and python will return "apple". So it allows you to search an object with its features.

### 2. Write:

If you'd like to write your data inthe file, you can type:

```python
    import EqualSearch as es
    es.write("write your data here")
```

**Notice:**please enter your data in forms of **"XXX.XXX.XXX"**, because EqualSearch divid each elements with** "."**.


