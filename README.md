# Tencent_class_check_in
emmmm这就是一个用在腾讯课堂自动签到的脚本。目的就是为了能在**一些不那么重要的课**上可以去睡大觉而不错过签到。如果是一些重要的课的话还是**建议不要睡觉了**。我只是迫不得已。:laughing::stuck_out_tongue_closed_eyes::laughing:。前期只是简单的签到，后来加上了识别跟保存签到成功的证据图片。就很有意思:sunglasses:。  
	
|Author|苏一休|
|---|---
|E-mail|2270678755@qq.com  

![image](https://ae01.alicdn.com/kf/H676fffff7c384439aaa4124f082647994.gif)

## 原理
很简单，真的很简单。核心想法就是python调鼠标一直点屏幕的一个地方。对，就是这么简单，然后你就可以去睡大觉了。比如我就是把腾讯课堂窗口化到屏幕的左上角，然后签到按钮出现的位置就在(1520,410)的位置。这个可以通过画图自己找准位置。  
<p align="center">
  <img src="https://s1.ax1x.com/2020/04/25/JsUJOJ.png"/>
</p>  
然后每隔10秒或者多少秒点一次那个位置就好了。腾讯课堂有两种签到，一种是30秒的一种是90秒的。也许你可能会问为啥不识别出按钮之后再点击？我一开始的想法是：管它那么多呢，老子都去睡觉了，直接一直狂点一个地方不就完事了？搞那么麻烦干嘛哈哈哈:stuck_out_tongue_closed_eyes:。后来有一次看课程的回放，老师说还有两个同学没签上，我有种后怕就是我不知道我自己有没有签上，这就很蛋疼，所以就想着加上个截图来保留自己签到成功的证据！这样自己醒来之后看到自己签到成功就很安心了有木有:expressionless:。    
<p align="center">
  <img src="https://s1.ax1x.com/2020/04/25/JsaKnH.png"/>
</p>  
所以为了一个安心还是加了识别上去:satisfied:。识别也很简单，把一个签到成功的图片比如上面那个图片截下来作为模板，然后每10秒调一次鼠标点击之后就截取腾讯课堂中签到按钮出现的区域的图片，用opencv的匹配来实现就好啦。匹配点多到一定程度(我设置的是200个点)就表明签到成功了然后就把当前签到成功的图片截取下来保存好。若有N次签到则保存N张图片。然后等你醒来之后就知道签了多少次到了:stuck_out_tongue:。签到成功之后保存的样张如下图    
<p align="center">
  <img src="https://s1.ax1x.com/2020/04/25/JsBNin.png"/>
</p>  

## 搭建与运行  
* [你总得有python吧？](https://www.python.org/)
* [下载我这份脚本](https://codeload.github.com/Suyixiu/Tencent_class_check_in/zip/master
)
* Win+R，CMD，然后pip安装以下这些依赖(缺啥装啥)
    ```Bash
    pip install wheel
    pip install numpy
    pip install opencv-python
    pip install pyautogui
    pip install pywin32
    ```
* 如果你有IDE的话就放进去F5如果没有那就cd进目录然后
    ```Bash
    python Tencent_class_check_in.py
    ```
    要退出的话ctrl+c即可退出
* 我的屏幕是1920x1080的，每个人的屏幕可能不一样所以代码中的一切关系到位置的坐标需要修改，这个看注释改改就行  
    ```python
    # 腾讯课堂右上角窗口化之后的大小950x509 #
    saveBitMap.CreateCompatibleBitmap(mfcDC, 950, 509)

    # 图片左上角起点在1920*1080这么大的左边的(965,6)这个位置 #
    saveDC.BitBlt((0, 0), (950, 509), mfcDC, (965, 6), win32con.SRCCOPY)

    # 签到按钮灰色块块所在的区域 #
    ROI_img = img[313:444,407:701]

    # 设置的匹配点的阈值 #
        if matches.__len__()>200:
    ```

## 效果
代码跑起来之后你就可以去睡大觉了，每隔10秒鼠标会点击一次你设置的签到按钮的位置，然后会截个图保存为result.png。如果这个图中包含识别的模板那么就保存这张图片为successN.png，这里的N是第N次签到。在你醒来停掉代码前它会一直跑:sunglasses:。你醒来之后你可以看到你的文件夹里差不多像下面这样  
<center><img src="https://s1.ax1x.com/2020/04/25/Js2aK1.png" /></center>

## 最后说明
* 这是一份很简单，真的超级简单的脚本，用很简单的东西来实现很实在的功能
* 在这份脚本运行的时候你的鼠标会隔段时间就去点屏幕的固定区域，所以你要用电脑的时候就不要想着跑这份东西了，**你要是不睡觉呢就老老实实认真听课啊还玩什么电脑**:satisfied:
* 这份东西没有写选择题判断题自动作答那些，要是做的话肯定能实现的，但我的课似乎不怎么提问所以这里就不考虑这个了。**况且要是有提问的课那也是重要的课啊！那怎么能睡觉呢？**:neutral_face:
* **还是应该要好好学习，此脚本造成的一切不良后果本人可不负责哈**:laughing:
