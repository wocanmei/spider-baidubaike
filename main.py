import sys
import os
from scrapy.cmdline import execute

# 将项目根目录加入系统环境变量中国。
# os.path.abspath(__file__)为当前文件所在绝对路径
# os.path.dirname() 获取文件的父目录。

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    execute(["scrapy", "crawl", "baikespider","-s", "JOBDIR=mybaike/001"])
