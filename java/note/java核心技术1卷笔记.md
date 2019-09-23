# java核心技术1卷笔记
---
[TOC]


## 书中规则
![1](./src/1.png)

## 笔记规则

tip表示突然插入的知识

注意表示值得关注的知识

## 源码网站

![Snipaste_2019-05-24_12-55-20](./src/Snipaste_2019-05-24_12-55-20.png)



## 下载Java开发包术语

![Snipaste_2019-05-24_13-17-30](./src/Snipaste_2019-05-24_13-17-30.png)



## 版本号说明

![Snipaste_2019-05-24_13-22-17](./src/Snipaste_2019-05-24_13-22-17.png)




## 安装库源文件和文档
（注：也可以在安装jdk时就勾选安装）
![Snipaste_2019-05-26_10-57-01](./src/Snipaste_2019-05-26_10-57-01.png)



## 命令行入门教程
[官方教程](https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html)

主要是：

1. javac 文件名.java先编译
2. java 文件名（没有.java）运行


## IDE入门教程

![Snipaste_2019-05-26_11-10-09](./src/Snipaste_2019-05-26_11-10-09.png)

>注：下面的图改为
>1. 在./src新建class，命名helloworld
>2. 在helloworld.java文件加入如下内容，然后ok
```
    public class HelloWorld {
        public static void main(String[] args){
            System.out.println("Hello World!");
        }
    }
```
![Snipaste_2019-05-26_11-11-05](./src/Snipaste_2019-05-26_11-11-05.png)

![Snipaste_2019-05-26_11-12-17](./src/Snipaste_2019-05-26_11-12-17.png)



## java程序
### 命名原则

![Snipaste_2019-05-27_13-08-41](./src/Snipaste_2019-05-27_13-08-41.png)

![Snipaste_2019-05-27_13-19-00](./src/Snipaste_2019-05-27_13-19-00.png)

[语言规范](https://docs.oracle.com/javase/specs/)

#### 注意 必须有一个main方法

![Snipaste_2019-05-27_13-22-02](./src/Snipaste_2019-05-27_13-22-02.png)

#### tip1 java类与C++类

![Snipaste_2019-05-27_22-43-57](./src/Snipaste_2019-05-27_22-43-57.png)

#### tip2 语句结构

![Snipaste_2019-05-27_22-49-33](./src/Snipaste_2019-05-27_22-49-33.png)

#### tip3 System.out.println(" ")

![Snipaste_2019-05-27_22-51-39](./src/Snipaste_2019-05-27_22-51-39.png)

### 注释

![Snipaste_2019-05-27_22-55-02](./src/Snipaste_2019-05-27_22-55-02.png)

![Snipaste_2019-05-27_22-55-12](./src/Snipaste_2019-05-27_22-55-12.png)

### 数据类型

![Snipaste_2019-05-27_22-58-50](./src/Snipaste_2019-05-27_22-58-50.png)

#### 整型

![Snipaste_2019-05-27_23-00-07](./src/Snipaste_2019-05-27_23-00-07.png)

##### tip1 长整型后缀
**长整型后数后面会有后缀L或l，如`4000000000L `**

##### tip2 二八十六进制的表示
| 进制     |  表示方法     |
| :---:    |  :---:        |
| 二进制   |  加前缀0b或0B |
| 八进制   |  加前缀0      |
| 十六进制 |  加前缀0x或0X |

##### tip3 数字下划线

**从 Java 7 开始，还可以为数字字面量加下划线， 如用 1_000_000 ，这些下划线只是为丫让人更易读。Java 编译器会去除这些下划线 。**

##### tip4 java整型与c++整型区别

![Snipaste_2019-05-27_23-34-55](./src/Snipaste_2019-05-27_23-34-55.png)

#### 浮点型

![Snipaste_2019-05-28_10-53-35](./src/Snipaste_2019-05-28_10-53-35.png)

##### tip1 后缀

![Snipaste_2019-05-28_10-54-52](./src/Snipaste_2019-05-28_10-54-52.png)

##### tip2 十六进制的p

![Snipaste_2019-05-28_10-57-14](./src/Snipaste_2019-05-28_10-57-14.png)

##### tip3 IEEE754规范和NaN的判断

![Snipaste_2019-05-28_10-59-10](./src/Snipaste_2019-05-28_10-59-10.png)

##### tip4 2.0-1.1≠0.9

![Snipaste_2019-05-28_11-02-08](./src/Snipaste_2019-05-28_11-02-08.png)

#### char型

![Snipaste_2019-05-28_12-21-50](./src/Snipaste_2019-05-28_12-21-50.png)

##### tip1 特殊字符转义序列

![Snipaste_2019-05-28_12-22-32](./src/Snipaste_2019-05-28_12-22-32.png)

##### 注意 unicode转义会在解析代码前执行

![Snipaste_2019-05-28_12-24-59](./src/Snipaste_2019-05-28_12-24-59.png)

##### tip2 不建议使用char除非要处理UTF-16

![Snipaste_2019-05-28_12-28-27](./src/Snipaste_2019-05-28_12-28-27.png)

##### tip3 UNICODE编码

[编码简介](https://www.cnblogs.com/tarol/p/7523642.html)

#### boolean类型（布尔类型）

![Snipaste_2019-05-28_12-32-56](./src/Snipaste_2019-05-28_12-32-56.png)

##### tip1 与C++区别

![Snipaste_2019-05-28_12-33-38](./src/Snipaste_2019-05-28_12-33-38.png)

### 变量

![Snipaste_2019-05-28_12-36-56](./src/Snipaste_2019-05-28_12-36-56.png)

#### 命名

![Snipaste_2019-05-28_12-38-43](./src/Snipaste_2019-05-28_12-38-43.png)

##### tip1 不提倡的做法

![Snipaste_2019-05-28_12-37-16](./src/Snipaste_2019-05-28_12-37-16.png)

#### 初始化

![Snipaste_2019-05-28_12-43-45](./src/Snipaste_2019-05-28_12-43-45.png)

##### tip1 与C++区别，不区分变量声明定义

![Snipaste_2019-05-28_12-44-29](./src/Snipaste_2019-05-28_12-44-29.png)

### 常量

![Snipaste_2019-05-28_12-47-31](./src/Snipaste_2019-05-28_12-47-31.png)

##### tip1 类常量

![Snipaste_2019-05-28_12-49-06](./src/Snipaste_2019-05-28_12-49-06.png)

##### tip2 与c++的区别

![Snipaste_2019-05-28_12-49-15](./src/Snipaste_2019-05-28_12-49-15.png)

### 运算符

#### 基本运算符

![Snipaste_2019-05-29_13-03-15](F:\code\java\note\src\Snipaste_2019-05-29_13-03-15.png)

**注意操作数都是整数，除法出来是整数，例如1/3=0**

##### tip1 精确浮点strictfp

基本不用,[资料](https://blog.csdn.net/redv/article/details/326444)


#### 数学函数


|   数学函数    |   作用   |
| :-----------: | :------: |
| Math.sqrt(x)  |  开平方  |
| Math.pow(x,a) | x的a次幂 |

以及

![Snipaste_2019-05-29_23-03-13](F:\code\java\note\src\Snipaste_2019-05-29_23-03-13.png)

##### tip1 偷懒不写Math的办法

![Snipaste_2019-05-29_23-34-50](F:\code\java\note\src\Snipaste_2019-05-29_23-34-50.png)

##### tip2 运算速度或者可预测结果

![Snipaste_2019-05-29_23-37-48](F:\code\java\note\src\Snipaste_2019-05-29_23-37-48.png)

#### 类型转换

##### 普通转换

1. 

```java
int n = 123456789;
float f = n; // f is 1.23456792E8
```

2. 自动转换

![Snipaste_2019-05-31_12-52-21](F:\code\java\note\src\Snipaste_2019-05-31_12-52-21.png)

##### tip1 类型之间的合法转换

![Snipaste_2019-05-31_12-54-11](F:\code\java\note\src\Snipaste_2019-05-31_12-54-11.png)

> 注:
>
> 1. 以上转化均为java合法转换
> 2. 实线箭头表示无信息丢失转换,虚线箭头表示转换可能有精度损失

##### 强制类型转换 

![Snipaste_2019-05-31_12-58-46](F:\code\java\note\src\Snipaste_2019-05-31_12-58-46.png)

##### tip2 大到小会截断

![Snipaste_2019-05-31_13-04-58](F:\code\java\note\src\Snipaste_2019-05-31_13-04-58.png)

##### tip3 不要将boolean类型拿来转换(可以用判断句转换)

![Snipaste_2019-05-31_13-05-52](F:\code\java\note\src\Snipaste_2019-05-31_13-05-52.png)

#### 结合运算符和赋值符

![Snipaste_2019-05-31_13-08-21](F:\code\java\note\src\Snipaste_2019-05-31_13-08-21.png)

##### 注意 运算类型与左侧操作数类型不同,最终会强制类型转换成左侧操作数类型

![Snipaste_2019-05-31_13-15-24](F:\code\java\note\src\Snipaste_2019-05-31_13-15-24.png)

#### 自增运算符与自减运算符

![Snipaste_2019-05-31_13-18-08](F:\code\java\note\src\Snipaste_2019-05-31_13-18-08.png)

![Snipaste_2019-05-31_13-19-31](F:\code\java\note\src\Snipaste_2019-05-31_13-19-31.png)

#### 关系和boolean运算符

|   关系   | 符号 |
| :------: | :--: |
|   小于   |  <   |
|   大于   |  >   |
|   等于   |  ==  |
|  不等于  |  !=  |
| 小于等于 |  <=  |
| 大于等于 | \>=  |

| boolean运算符 | 符号 |
| :-----------: | :--: |
|      与       |  &&  |
|      或       | \|\| |
|      非       |  !   |

##### tip1 如果第一表达式就能确定表达式值则停止计算

![Snipaste_2019-05-31_13-27-29](F:\code\java\note\src\Snipaste_2019-05-31_13-27-29.png)

##### tip2 三元操作符? :

![Snipaste_2019-05-31_13-28-20](F:\code\java\note\src\Snipaste_2019-05-31_13-28-20.png)

#### 位运算符

![Snipaste_2019-06-01_11-08-22](F:\code\java\note\src\Snipaste_2019-06-01_11-08-22.png)

![Snipaste_2019-06-01_11-08-32](F:\code\java\note\src\Snipaste_2019-06-01_11-08-32.png)

![Snipaste_2019-06-01_11-10-42](F:\code\java\note\src\Snipaste_2019-06-01_11-10-42.png)

##### tip1 对boolean所有都会计算

![Snipaste_2019-06-01_11-12-05](F:\code\java\note\src\Snipaste_2019-06-01_11-12-05.png)

##### 注意 移位操作符右操作数会先按左操作数的类型取模（取余数）

![Snipaste_2019-06-01_11-18-04](F:\code\java\note\src\Snipaste_2019-06-01_11-18-04.png)

> **这里35%32=3所以1<<35=1<<3,而8说的是最终值**

##### tip3 java位运算和c++区别

![Snipaste_2019-06-01_11-23-20](F:\code\java\note\src\Snipaste_2019-06-01_11-23-20.png)

#### 优先级

![Snipaste_2019-06-01_11-25-25](F:\code\java\note\src\Snipaste_2019-06-01_11-25-25.png)

> 加括号（）可以改变按优先级运算的关系

##### tip1 右结合运算符（表中最后一行）

![Snipaste_2019-06-01_11-27-34](F:\code\java\note\src\Snipaste_2019-06-01_11-27-34.png)

##### tip2  和c++区别

![Snipaste_2019-06-01_11-28-18](F:\code\java\note\src\Snipaste_2019-06-01_11-28-18.png)

![Snipaste_2019-06-01_11-30-30](F:\code\java\note\src\Snipaste_2019-06-01_11-30-30.png)

### 字符串

#### 子串

![Snipaste_2019-06-01_11-35-06](F:\code\java\note\src\Snipaste_2019-06-01_11-35-06.png)

#### 拼接

1. 用+直接拼接
2. 将一个字符串与一个非字符串的值进行拼接时，后者被转换成字符串（任何一个 Java 对象都可以转换成字符串）。 
3. ![Snipaste_2019-06-01_11-39-55](F:\code\java\note\src\Snipaste_2019-06-01_11-39-55.png)

#### 不可变字符串

