# phap
### *Programing Helpful Algorithm Package*
#### *一个对编程有帮助的算法包*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
### [English](README.md)  | 简体中文

# 项目链接
[Github](https://github.com/DashBing/phap/ "Github") | [Pypi](https://pypi.org/project/phap/ "Pypi") | [Pypi (stralgo)](https://pypi.org/project/stralgo/ "Pypi (stralgo)")
<br><br>
[Kgithub](https://kgithub.com/DashBing/phap/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 版本
## 稳定版本
+ v0.1.0 (stralgo)
+ v1.1.1 (stralgo)
+ v2.1.2
+ v2.2.1

## 最新正式版本
+ v2.2.1

## 最新版本
### *(master分支下数据不准确, 具体查看dev分支)*
+ v3.0.0-beta4

# 使用
## 阅读开发文档
### *(尽量打开项目链接中的[Github](https://github.com/DashBing/phap/ "Github")链接打开，使用Pypi或其他链接可能会发生打不开的情况)*
+ [开发文档链接](doc/README.md)

# 从源码构建
## 准备工作
+ 安装git和make (方法自行百度)
+ 安装Python(3.9版本或者3.11版本皆可)
+ 从源码仓库克隆源代码
```
git clone git@github.com:DashBing/phap.git
```
#### 或者
```
git clone https://github.com/DashBing/phap.git
```
### 国内网比较差可以尝试：
```
git clone https://kgithub.com/DashBing/phap.git
```

## 初始化打包环境
```
make init
```
#### 或者
#### 尝试手动安装以下包:
+ build
+ twine
#### 以下是在Windows环境下的示例命令行:
```
python -m pip install build
python -m pip install twine
```

## 构建包
```
make build
```
