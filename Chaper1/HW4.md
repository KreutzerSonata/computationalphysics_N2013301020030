#Homework 4

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

##摘要
本次练习，利用Python和Matplotlib，使用Euler方法画出了做自由落体运动的速度时间曲线以及位移时间曲线。代码可设置初始速度以及下落时间，并通过设置时间间隔的大小，达到控制拟合精度的目的。

##背景
做自由落体运动的物体的速度可由以下方程表示：
$$
\frac{dv}{dt} = -g
$$
其中，$v$ 是速度，$g=9.8m/s^2$ 为重力加速度。使用Euler方法，可得到方程的数值解。