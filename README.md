# 语音同传demo

该项目是对 [LyricDanmu](https://github.com/FHChen0420/LyricDanmu) 1.5.3的简单魔改。通过向LyricDanmu添加一个HTTP API，从而允许外部的语音识别来代替键盘输入。
视频效果：[Bilibili](https://www.bilibili.com/video/BV1jY411Z7rn/)

项目的目的仅仅是提供一个proof of concept实现，从而展示和探讨通过语音进行同传的可能。项目添加的API并没有经过设计，项目本身的定位也只是一个demo，并没有进一步开发的打算。

常见的云厂商的语音识别API均支持连续的音频识别，并会以句子为单位生成事件。如果不考虑人工订正识别内容，理论上只需要一个商业的语音API，同传译员就可以只说话不动手，传译内容也能以句子为单位自动发送。同理，也可以设想从观众端进行自动的语音识别和机翻，当然因为有背景音乐等的干扰，识别效果必然会比主播端直接识别差很多。

## 使用方式

1. 打包修改后的LyricDanmu，放入原exe文件目录并运行。原项目提供了一些基础的使用说明和配置，建议先从[这里](https://github.com/FHChen0420/LyricDanmu/releases)下载原项目的打包版本
	  - 安装Python依赖，并使用Pyinstaller进行打包，打包指令可参照[原项目文档](https://github.com/FHChen0420/LyricDanmu#pyinstaller打包指令)。
	  - 或者从[Release](https://github.com/c-basalt/LD-API-demo/releases)直接下载修改后的exe
2. 安装油猴脚本
	  - 首先在浏览器安装油猴脚本的扩展，如Tampermonkey
	  - 然后在油猴脚本扩展的设置中，添加/安装`Bing translate to LyricDanmu.user.js`
3. （可选）安装直播追帧插件
	  - 可自行安装相应追帧插件降低直播延迟
	  - 我公开了一份油猴脚本的追帧实现，可以从[这里](https://greasyfork.org/zh-CN/scripts/453967)安装

