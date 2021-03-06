import re

#去符号
RE_DE_SYMBOL = re.compile(r'[^：“”:"——]+')
#增减持公司全称
RE_ZJC_ORG = [re.compile(x) for x in
              [r'接到.*?股东(.+?)（',
               r'收到.*?股东(.+?)（']]
#增减持公司简称
RE_ZJC_SHORT_ORG = [re.compile(x) for x in
                    [r'（.*?简称(.+?)）',
                     r'（.*?下称(.+?)）']]
#日期
RE_DATE = [re.compile(x) for x in 
           [r'([0-9]+年[0-9]+月[0-9]+日)',
            r'([0-9]+\.[0-9]+\.[0-9]+)',
            r'([0-9]+\-[0-9]+\-[0-9]+)']]
#数字
RE_NUMBER = re.compile('[0-9\.,]+')

ZJC_T1 = ['股东名称减持方式减持时间减持均价减持股数（股）减持比例', 
          '股东名称增持方式增持时间增持均价增持股数（股）增持比例']

ZJC_T2 = ['股东名称股份性质本次减持前持有的股份本次减持后持有的股份', 
          '股东名称股份性质减持前持有股份减持后持有股份']

