#coding=utf-8
from lxml import etree
text1 = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''
#利用etree.HTML，将字符串解析为HTML文档
# html = etree.HTML(text1)
# content = html.xpath('//ul/li[@class="item-0"]/a/text()')
# content1 = html.xpath('//ul/li/a/@href')
# print(content)
# print(content1)
text = """
 <DIV class="nr">
 <DL class="xhlist" id="xh_210911">
 <SPAN><DD>
 <A href="/article/210911" target="_blank">
 STRONG>这么可爱的老给我多来点</STRONG>
 </A></DD></SPAN>
 <DD><p>出差在外，老婆突然来电，哭着求安慰:“前天在闺密那里领养一只小兔子，由于最近气温骤降今天竟然冷死了。”我百般安慰，她继续不停地哭泣说:“本想着是冷死的，准备用炭火给它火化，呜呜呜呜呜呜........！”我又安慰:“你做得很好，不用伤心！”然后她说:“谁知道那味道竟然那么香，我一下子没忍住............”&nbsp;</p></DD>
 <div class="c_a"><div class="active c_l"><a href="javascript:;" class="pinattn msg" data_attr=""><p class="pp">评论</p></a></div><div class="active c_r"><a href="javascript:;" class="pinattn good" data_attr="583"><p class="zan">583</p></a> <a href="javascript:;" class="pinattn bad" data_attr="22"><p class="bs">22</p></a></div></div></DL>
 <DL class="xhlist" id="xh_210910"><SPAN><DD><A href="/article/210910" target="_blank"><STRONG>大家说我这样做好吗</STRONG>
 </A></DD></SPAN>
 <DD><p>在我还在上大学那会，有一天去系办找辅导员，正好在楼梯遇到一个平日很装的同学，我上楼同学下楼，相遇的刹那，同学一仰头，很是高傲的瞄了我一眼，嘴角划过一丝不屑的笑，保持这种姿态直接一步跨出，然后我羞羞的伸出了脚，然后整栋楼传来嗷的一声……</p></DD>
 <div class="c_a"><div class="active c_l"><a href="javascript:;" class="pinattn msg" data_attr=""><p class="pp">评论</p></a></div><div class="active c_r"><a href="javascript:;" class="pinattn good" data_attr="103"><p class="zan">103</p></a> <a href="javascript:;" class="pinattn bad" data_attr="8"><p class="bs">8</p></a></div></div></DL>
 <DL class="xhlist" id="xh_180839"><SPAN><DD><A href="/article/180839" target="_blank"><STRONG>动物说起话来很幽默..~！</STRONG></A></DD></SPAN><DD><p><font face="Verdana">

</p><p><font face="Verdana">1。袋鼠：吃不了的，咱兜着走。</font></p>"""
#利用etree.HTML，将字符串解析为HTML文档
# text1 = text.lower()
# # print(text1)
# html = etree.HTML(text1)
# content = html.xpath('//dl[@class="xhlist"]/span/dd/a/strong/text()')
# # content1 = html.xpath('//ul/li/a/@href')
# print(content)
# # print(content1)


with open('tiebatupian.txt', 'rb') as f:
    html1 = f.read().decode('utf-8')
    print(html1)
content = etree.HTML(html1)

title = content.xpath('//a[@class="j_th_tit "]/text()')
print(title)



# https://www.zhihu.com/signin?next=%2F