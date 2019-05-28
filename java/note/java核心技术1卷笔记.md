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

