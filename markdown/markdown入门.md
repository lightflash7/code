# <div id="id0">Markdown入门教程</div>

----------


&emsp;&emsp; 这篇博客就是用markdown写的，作者此时完全不会markdown语法，一步一步慢慢摸索写下这篇博客。编辑器选的是Typora。个人感觉这个编辑器的好处有

1. 界面简单，看起来舒服
2. 编辑和预览于一身
3. 有众多快捷键可以用来控制格式可以加快写的速度（比如多级标题不用按多个#，直接ctrl加数字）

## 下面进入正题
- [标题](#id1)
- [加粗和斜体](#id2)
- [删除线](#id3)
- [分割线](#id4)
- [列表](#id5)
- [表格](#id6)
- [引用](#id7)
- [代码块](#id8)
- [符号转义](#id9)
- [插入网页链接](#id10)
- [插入图片](#id11)
- [自动生成目录](#id12)
- [锚点的设置](#id13)
- [两个排版问题](#id14)

<br />

### <div id="id1">一、标题</div>

&emsp;&emsp; Markdown有6种格式的标题，与#数量有关，**具体实现方法为n个#加空格然后再输入文字**，分别对应

```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

显示效果如下：

#      一级标题
##     二级标题
###    三级标题
####   四级标题
#####  五级标题
###### 六级标题

**此外还有另外一种表示标题的方法，但有的地方可能不支持，如下所示**

```
这里是一级标题
===
这里是二级标题
---
```

显示效果如下所示：



这里是一级标题
===
这里是二级标题
---

<br />

### <div id="id2">二、加粗和斜体</div>

&emsp;&emsp; 这两种作为常用的划重点的方式，优先写出来

1. 加粗

   可以用**或者__围住要加粗的文字即可

   ```
   **这是一句粗体文字**
   __这也是一句粗体文字__
   ```

   效果：

   **这是一句粗体文字**
   __这也是一句粗体文字__

2. 斜体

   可以用单个的*或者_围住要加粗的文字即可

   ```
   *这是一句斜体文字*
   _这也是一句斜体文字_
   ```

   效果：

   *这是一句斜体文字*
   _这也是一句斜体文字_

### <div id="id3">三、删除线</div>

&emsp;&emsp; 删除线一般用来表示多人合作时要求修改时要删除的内容，或者一种特殊表达方式（滑稽护体），在markdown中实现也是挺简单的，**具体实现方法为在文字两端用~~围住**

```
~~这是一句有删除线的文字~~
```

效果如下：

~~这是一句有删除线的文字~~

### <div id="id4">四、分割线</div>

&emsp;&emsp; **分割线只要打‘---’或者‘\*\*\*’或‘___'（大于等于三个即可），效果如下**

---

### <div id="id5">五、列表</div>

&emsp;&emsp; markdown列表也是和html一样分成有序列表和无序列表

1. 无序列表

&emsp;&emsp; **在文字前加上’– 或 * 或+‘再加’空格或者Tab‘（显示出来符号空心点和实心点和实心方依次按层级递进显示）**

   ```
   - 苹果
   - 香蕉
   - 雪梨
   ```

   效果如下：

   - 苹果
   - 香蕉
   - 雪梨

2. 有序列表

&emsp;&emsp; **直接写1.空格+文字，2.空格+文字，......即可**

   ```
   1. 内容一
   2. 内容二
   3. 内容三
   ```

   效果如下：

   1. 内容一
   2. 内容二
   3. 内容三

3. 如果想写出1.1 ，1.2这样的暂时好像只有无序列表的方法，用**不同的缩进表示嵌套**，如：

   ```
   - 水果
   	- 苹果
   	- 香蕉
   	- 雪梨
   - 编程语言
   	- python
   	- c艹
   	- java
   ```

   显示效果如下：

   - 水果
     - 苹果
     - 香蕉
     - 雪梨
   - 编程语言
     - python
     - c艹
     - java

### <div id="id6">六、表格</div> 
&emsp;&emsp; 表格主要由|组成，并且用:---来控制对齐格式

如：

```
表头|内容一|内容二
:---|---:|:---:
名称|内容1|内容2
```

得到结果如下所示：

表头|内容一|内容二
:---|---:|:---:
名称|内容1|内容2

（注：typora模式下可用“|表头|内容一|内容二|”调出表格，然后在顶部进行调整）

其中，控制格式符号对应如下：

符号|作用
:---:|:---:
:---|左对齐
:---:|中间对齐
---：|右对齐

### <div id="id7">七、引用</div>

&emsp;&emsp; 引用会把文字放进框框里面，和代码块很像，但是**引用块里依然可以用markdown语法，如加粗的\*\*文字\*\*依然会对文字进行加粗，代码块内则不会。**

引用的语法也很简单，只要一个**>符号**就可以产生，并且也可以**按>的个数嵌套引用**，如：

```
> 第一层引用文字一
> 第一层引用文字二
>> 第二层引用文字一 
>> 第二层引用文字二
```

效果如下：

> 第一层引用文字一
> 第一层引用文字二
>
> > 第二层引用文字一 
> > 第二层引用文字二

### <div id="id8">八、代码块</div>

&emsp;&emsp; 代码块就和引用差不多，如果**只有一行代码可以用单个`围住代码**，而如果是**多行则用\`\`\`围住代码区域**。

**注意此处的`是英文输入法下Esc键下面那个**

代码块第三种写法就是**用缩进（tab）**或者**四个空格**表示，相同的缩进表示是同一块代码块。

代码块还能支持多种编程语言，会有语法高亮。[支持语言种类很多](https://www.jianshu.com/p/1f223eb78ad8),具体操作方法为在第一个```后加语言名字

多行代码例如:
```
​```python
import requests
url = 'http://www.baidu.com'
res = requests.get(url)
print(res.text)
​```
```

显示效果如下:

```python
import requests
url = 'http://www.baidu.com'
res = requests.get(url)
print(res.text)
```
而如果是单行的则可以用\`代码\`就会显示出这样的效果`代码`

### <div id="id9">九、符号转义</div>
&emsp;&emsp; 有时要显示\*\*这样的触发markdown语法的文字怎么办?那当然是和正常编程语言那样用转义符啦。只要在特殊符号前面加上\\即可
需要加转义符的有如下符号。
```
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  括弧
#   井号
+   加号
-   减号
.   英文句点
!   感叹号
```
如果忘记用转义符可能会导致显示和自己想法不同。

### <div id="id10">十、插入网页链接</div>
&emsp;&emsp; 如果想要实现点击[github](https://github.com/)就跳转到GitHub上要怎么做呢?
只要用\[描述\]\(url链接\)的格式就可以了。
如：
```
[github](https://github.com/)
```
就实现了上面的效果

### <div id="id11">十一、插入图片</div>
&emsp;&emsp; 插入图片不管是美观还是帮助别人理解层面上都有深远意义。插入图片和插入网页链接基本一模一样，**多了个\!**。
如下
```
![图片描述](本机位置/网络上位置)
```
由于发博客写本机位置别人是看不到图片的,还是只能用手动上传的方式了。
**但是在github上的markdown有个好处可以用相对文件位置（linux那种格式）**

>如果图片或者图片所在文件夹位于同级目录，则可以用`./图片`或者`./图片所在文件夹/图片`
>如果图片或者图片所在文件夹位于父目录(上级目录),则可以用`../图片`或者`../图片所在文件夹/图片`
>.的数量依次类推表示在多少级目录上

### <div id="id12">十二、自动生成目录</div>
&emsp;&emsp; markdown自动生成目录也很简单，只需要单行的：
```
[TOC]
```
即可对标题等级进行自动生成目录。

### <div id="id13">十三、锚点的设置</div>
&emsp;&emsp; 找了很久没有发现markdown有锚点设置的语法，只有锚点跳转的语法，如果要设置锚点要依赖于html的语言，具体设置和跳转方法如下
锚点的设置:在要设置的位置后加上`<div id="锚点名称(自己起)">文字段或者标题</div>`
锚点的跳转:和图片类似,用`[解释内容](#设置的锚点名称)`即可
如:
```
我已经在标题上设置了                   # <div id="id0">Markdown入门教程</div>
然后我在下面的"回到开头"用了    [回到开头](#id0)
```
[回到开头](#id0)
这样点击上方的回到开头就会跳转到文章开始的位置了



### <div id="id14">十四、两个排版问题</div>
1. 中文首行缩进问题：
&emsp;&emsp; 因为markdown设计是为英语设计的，英文没有首行缩进的问题，所以markdown就没有好的处理这个问题的办法。于是一番试探后，最终办法是用**\&emsp;等来代替空格**。
```
全方大的空白&emsp;或&#8195;
半方大的空白&ensp;或&#8194;
不断行的空白&nbsp;或&#160;
```
一般中文首行缩进两格只要用两个\&emsp;\&emsp;代替即可

2. 段落间间隔问题
&emsp;&emsp; 有时候会觉得两个内容不同的自然段间隔很近,想让他们间距合适点就用符号**\<br />**即可增加间距。

&emsp;&emsp; 用markdown书写一开始有点不流畅(可能是还不会用Typora的问题,而且一开始这个编辑器确实出了点小bug),后面完全用源代码模式书写感觉到了完全体的markdown的书写体验，虽然还不是很懂markdown的段落什么的原理，不过也算可以打得出一篇博客来了，总的来说还不错。
