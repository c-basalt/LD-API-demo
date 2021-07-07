bili_colors={'16777215': '白色', '14893055': '紫色', '5566168': '松石绿', '5816798': '雨后蓝', '4546550': '星空蓝', 
            '9920249': '紫罗兰', '12802438': '梦境红', '16747553': '热力橙', '16774434': '香槟金', '16738408': '红色', 
            '6737151': '蓝色', '65532': '青色', '16772431': '黄色', '16766720': '盛典金', '4286945': '升腾蓝', 
            '8322816': '绿色', '16750592': '橙色', '16741274': '粉色'}

bili_modes={'1':'⋘', '4':'▁▁', '5':'▔▔'}

# 转义处理规则
html_transform_rules = {
    r"&apos;": "'",
    r"&quot;": "\"",
    r"&amp;": "＆",
    r"&nbsp;| ": " ",#注意"|"后的空格是&#160
}

# 压缩处理规则
compress_rules = {
    r"[\.・]{2,}": "…",
    r"[!！]{2,}": "!",
    r"[\?？]{2,}": "?",
    r"(。|，|\.|,)$": "",
    # 连续空格已在屏蔽字处理中进行了压缩，这里不再重复处理
}

# 文件名特殊字符处理规则
char_transform_rules = {
    "/":"／", "\\":"＼", "|":"｜", "*":"＊", "?":"？",
    ":":"：", "<":"＜", ">":"＞", "\"":"“",
}

# 正则表达式特殊字符处理规则
regex_transform_rules = {
    "(":r"\(", ")":r"\)", "$":r"\$", "^":r"\^", "?":r"\?",
    "[":r"\[", "]":r"\]", "+":r"\+", "*":r"\*", ".":r"\.", 
    "{":r"\{", "}":r"\}", "|":r"\|", #"\\":r"\\", 
}

# 中文歌词补充处理规则
preprocess_cn_rules = {
    "妳":"你",
    "(?<![名巨显昭卓译编土原执])著(?![称有名作述于书籍])": "着",
    #"(?<![包缠妆])著(?![着在住足尸])": "里", # 偶尔会遇到"裏"(li)错写成"裹"(guo)的情况
    r"[\(（].*?翻译\s*?[:：].*?[\)）]": "",
}

# 可忽略的歌词规则
ignore_lyric_pattern=r"(?i)^[^0-9A-Za-z\u4e00-\u9fa5\u3040-\u31ff]{0,3}(终|完|undefined|[终終お]わ(る|り|った)|end|fin|music|[伴间]奏)[^0-9A-Za-z\u4e00-\u9fa5\u3040-\u31ff]{0,3}$|.(:|：|︰| - |不得翻唱)."

# 恋口上默认预设
default_custom_text="<texts>\n<text title=\"古守恋口上\">\n我有些话想要对你说\n古守实在是太可爱了\n喜欢喜欢超喜欢 果然喜欢\n好不容易找到的吸血鬼\n"+ \
                "肉肉来到世上的理由\n就是为了和古守相遇\n和肉肉一起共度一生\n世界上第一的家里蹲\n</text>\n</texts>"