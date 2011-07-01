import urllib
import os, random, sys, math
from lxml import etree

def main():

    reddit = etree.HTML( urllib.urlopen("http://www.reddit.com/r/all/top").read() )
    reddit.xpath("//div[contains(@class,'title')]//b/text()")



if __name__ == "__main__":
    main()