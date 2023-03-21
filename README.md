# sarasa-deshuffle
针对sarasa-shuffle.woff2加密字体进行解密的一个项目

下面这段代码可以用来翻译一段sarasa-shuffle加密的句子，将其翻译成非'乱码'形式的字体，Windows常用对应字体
```python
def convert2normal(encode_str):
    ret = ''
    for ch in encode_str:
        str_res_key = ch.encode("unicode_escape").decode().strip("\\u")
        try:
            value = cmap_code_word["uni" + str_res_key.upper()]
        except KeyError as e:
            value = ch
        ret = ret + value
    return ret
```
