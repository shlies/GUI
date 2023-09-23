import sys,time,re,os,html2text,subprocess,threading,asyncio,aiohttp
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtWidgets import QApplication,QWidget,QListWidgetItem, QListView
from qfluentwidgets import Dialog, InfoBarIcon, InfoBar,InfoBarPosition
from requests.exceptions import RequestException
import Ui_biligui,requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0', 'referer': 'https://w.linovelib.com/'}
flag=0
max_retries=10
path="C:/Users/WYC20/OneDrive - swartart/1-books/"

class book_type:
    def __init__(self, id, name, num):
        self.name = name
        self.id = id
        self.num = num
        self.len=0
def compare_urls(url1, url2):
    pattern = r'(\d+)(_\d+)?\.html$'
    match1 = re.search(pattern, url1)  # 匹配第一个URL
    match2 = re.search(pattern, url2)  # 匹配第二个URL
    if match1 and match2:
        if match1.group(1) == match2.group(1):
            return True
    return False
def decode(h):
    h=re.sub("\u201C","「",h,flags=re.IGNORECASE)
    h=re.sub("\u201D","」",h,flags=re.IGNORECASE)
    h=re.sub("\u2018","『",h,flags=re.IGNORECASE)
    h=re.sub("\u2019","』",h,flags=re.IGNORECASE)
    h=re.sub("\uE80C","的",h,flags=re.IGNORECASE)
    h=re.sub("\uE80D","一",h,flags=re.IGNORECASE)
    h=re.sub("\uE80E","是",h,flags=re.IGNORECASE)
    h=re.sub("\uE806","了",h,flags=re.IGNORECASE)
    h=re.sub("\uE807","我",h,flags=re.IGNORECASE)
    h=re.sub("\uE808","不",h,flags=re.IGNORECASE)
    h=re.sub("\uE80F","人",h,flags=re.IGNORECASE)
    h=re.sub("\uE810","在",h,flags=re.IGNORECASE)
    h=re.sub("\uE811","他",h,flags=re.IGNORECASE)
    h=re.sub("\uE812","有",h,flags=re.IGNORECASE)
    h=re.sub("\uE809","这",h,flags=re.IGNORECASE)
    h=re.sub("\uE80A","个",h,flags=re.IGNORECASE)
    h=re.sub("\uE80B","上",h,flags=re.IGNORECASE)
    h=re.sub("\uE813","们",h,flags=re.IGNORECASE)
    h=re.sub("\uE814","来",h,flags=re.IGNORECASE)
    h=re.sub("\uE815","到",h,flags=re.IGNORECASE)
    h=re.sub("\uE802","时",h,flags=re.IGNORECASE)
    h=re.sub("\uE803","大",h,flags=re.IGNORECASE)
    h=re.sub("\uE804","地",h,flags=re.IGNORECASE)
    h=re.sub("\uE805","为",h,flags=re.IGNORECASE)
    h=re.sub("\uE817","子",h,flags=re.IGNORECASE)
    h=re.sub("\uE818","中",h,flags=re.IGNORECASE)
    h=re.sub("\uE819","你",h,flags=re.IGNORECASE)
    h=re.sub("\uE81D","说",h,flags=re.IGNORECASE)
    h=re.sub("\uE81E","生",h,flags=re.IGNORECASE)
    h=re.sub("\uE816","国",h,flags=re.IGNORECASE)
    h=re.sub("\uE800","年",h,flags=re.IGNORECASE)
    h=re.sub("\uE801","着",h,flags=re.IGNORECASE)
    h=re.sub("\uE81A","就",h,flags=re.IGNORECASE)
    h=re.sub("\uE81B","那",h,flags=re.IGNORECASE)
    h=re.sub("\uE81C","和",h,flags=re.IGNORECASE)
    h=re.sub("\uE81F","要",h,flags=re.IGNORECASE)
    h=re.sub("\uE820","她",h,flags=re.IGNORECASE)
    h=re.sub("\uE821","出",h,flags=re.IGNORECASE)
    h=re.sub("\uE822","也",h,flags=re.IGNORECASE)
    h=re.sub("\uE823","得",h,flags=re.IGNORECASE)
    h=re.sub("\uE824","里",h,flags=re.IGNORECASE)
    h=re.sub("\uE825","后",h,flags=re.IGNORECASE)
    h=re.sub("\uE826","自",h,flags=re.IGNORECASE)
    h=re.sub("\uE827","以",h,flags=re.IGNORECASE)
    h=re.sub("\uE828","会",h,flags=re.IGNORECASE)
    h=re.sub("\uE82D","家",h,flags=re.IGNORECASE)
    h=re.sub("\uE82E","可",h,flags=re.IGNORECASE)
    h=re.sub("\uE831","下",h,flags=re.IGNORECASE)
    h=re.sub("\uE832","而",h,flags=re.IGNORECASE)
    h=re.sub("\uE833","过",h,flags=re.IGNORECASE)
    h=re.sub("\uE834","天",h,flags=re.IGNORECASE)
    h=re.sub("\uE82F","去",h,flags=re.IGNORECASE)
    h=re.sub("\uE830","能",h,flags=re.IGNORECASE)
    h=re.sub("\uE829","对",h,flags=re.IGNORECASE)
    h=re.sub("\uE82A","小",h,flags=re.IGNORECASE)
    h=re.sub("\uE82B","多",h,flags=re.IGNORECASE)
    h=re.sub("\uE82C","然",h,flags=re.IGNORECASE)
    h=re.sub("\uE837","于",h,flags=re.IGNORECASE)
    h=re.sub("\uE838","心",h,flags=re.IGNORECASE)
    h=re.sub("\uE839","学",h,flags=re.IGNORECASE)
    h=re.sub("\uE835","么",h,flags=re.IGNORECASE)
    h=re.sub("\uE846","之",h,flags=re.IGNORECASE)
    h=re.sub("\uE847","都",h,flags=re.IGNORECASE)
    h=re.sub("\uE83A","好",h,flags=re.IGNORECASE)
    h=re.sub("\uE83B","看",h,flags=re.IGNORECASE)
    h=re.sub("\uE836","起",h,flags=re.IGNORECASE)
    h=re.sub("\uE84A","发",h,flags=re.IGNORECASE)
    h=re.sub("\uE84B","当",h,flags=re.IGNORECASE)
    h=re.sub("\uE84C","没",h,flags=re.IGNORECASE)
    h=re.sub("\uE84D","成",h,flags=re.IGNORECASE)
    h=re.sub("\uE83C","只",h,flags=re.IGNORECASE)
    h=re.sub("\uE83D","如",h,flags=re.IGNORECASE)
    h=re.sub("\uE83E","事",h,flags=re.IGNORECASE)
    h=re.sub("\uE841","把",h,flags=re.IGNORECASE)
    h=re.sub("\uE842","还",h,flags=re.IGNORECASE)
    h=re.sub("\uE843","用",h,flags=re.IGNORECASE)
    h=re.sub("\uE844","第",h,flags=re.IGNORECASE)
    h=re.sub("\uE845","样",h,flags=re.IGNORECASE)
    h=re.sub("\uE83F","道",h,flags=re.IGNORECASE)
    h=re.sub("\uE840","想",h,flags=re.IGNORECASE)
    h=re.sub("\uE858","作",h,flags=re.IGNORECASE)
    h=re.sub("\uE859","种",h,flags=re.IGNORECASE)
    h=re.sub("\uE85A","开",h,flags=re.IGNORECASE)
    h=re.sub("\uE84F","美",h,flags=re.IGNORECASE)
    h=re.sub("\uE848","乳",h,flags=re.IGNORECASE)
    h=re.sub("\uE849","阴",h,flags=re.IGNORECASE)
    h=re.sub("\uE84E","液",h,flags=re.IGNORECASE)
    h=re.sub("\uE855","茎",h,flags=re.IGNORECASE)
    h=re.sub("\uE856","欲",h,flags=re.IGNORECASE)
    h=re.sub("\uE857","呻",h,flags=re.IGNORECASE)
    h=re.sub("\uE850","肉",h,flags=re.IGNORECASE)
    h=re.sub("\uE851","交",h,flags=re.IGNORECASE)
    h=re.sub("\uE852","性",h,flags=re.IGNORECASE)
    h=re.sub("\uE853","胸",h,flags=re.IGNORECASE)
    h=re.sub("\uE854","私",h,flags=re.IGNORECASE)
    h=re.sub("\uE85D","穴",h,flags=re.IGNORECASE)
    h=re.sub("\uE85E","淫",h,flags=re.IGNORECASE)
    h=re.sub("\uE85F","臀",h,flags=re.IGNORECASE)
    h=re.sub("\uE860","舔",h,flags=re.IGNORECASE)
    h=re.sub("\uE85B","射",h,flags=re.IGNORECASE)
    h=re.sub("\uE85C","脱",h,flags=re.IGNORECASE)
    h=re.sub("\uE861","裸",h,flags=re.IGNORECASE)
    h=re.sub("\uE862","骚",h,flags=re.IGNORECASE)
    h=re.sub("\uE863","唇",h,flags=re.IGNORECASE)


    '''h=re.sub('“',"「",h,flags=re.IGNORECASE)
    h=re.sub('”',"」",h,flags=re.IGNORECASE)
    h=re.sub('‘',"『",h,flags=re.IGNORECASE)
    h=re.sub('’',"』",h,flags=re.IGNORECASE)
    h=re.sub("","\u7684",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e00",h,flags=re.IGNORECASE)
    h=re.sub("","\u662f",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e86",h,flags=re.IGNORECASE)
    h=re.sub("","\u6211",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e0d",h,flags=re.IGNORECASE)
    h=re.sub("","\u4eba",h,flags=re.IGNORECASE)
    h=re.sub("","\u5728",h,flags=re.IGNORECASE)
    h=re.sub("","\u4ed6",h,flags=re.IGNORECASE)
    h=re.sub("","\u6709",h,flags=re.IGNORECASE)
    h=re.sub("","\u8fd9",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e2a",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e0a",h,flags=re.IGNORECASE)
    h=re.sub("","\u4eec",h,flags=re.IGNORECASE)
    h=re.sub("","\u6765",h,flags=re.IGNORECASE)
    h=re.sub("","\u5230",h,flags=re.IGNORECASE)
    h=re.sub("","\u65f6",h,flags=re.IGNORECASE)
    h=re.sub("","\u5927",h,flags=re.IGNORECASE)
    h=re.sub("","\u5730",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e3a",h,flags=re.IGNORECASE)
    h=re.sub("","\u5b50",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e2d",h,flags=re.IGNORECASE)
    h=re.sub("","\u4f60",h,flags=re.IGNORECASE)
    h=re.sub("","\u8bf4",h,flags=re.IGNORECASE)
    h=re.sub("","\u751f",h,flags=re.IGNORECASE)
    h=re.sub("","\u56fd",h,flags=re.IGNORECASE)
    h=re.sub("","\u5e74",h,flags=re.IGNORECASE)
    h=re.sub("","\u7740",h,flags=re.IGNORECASE)
    h=re.sub("","\u5c31",h,flags=re.IGNORECASE)
    h=re.sub("","\u90a3",h,flags=re.IGNORECASE)
    h=re.sub("","\u548c",h,flags=re.IGNORECASE)
    h=re.sub("","\u8981",h,flags=re.IGNORECASE)
    h=re.sub("","\u5979",h,flags=re.IGNORECASE)
    h=re.sub("","\u51fa",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e5f",h,flags=re.IGNORECASE)
    h=re.sub("","\u5f97",h,flags=re.IGNORECASE)
    h=re.sub("","\u91cc",h,flags=re.IGNORECASE)
    h=re.sub("","\u540e",h,flags=re.IGNORECASE)
    h=re.sub("","\u81ea",h,flags=re.IGNORECASE)
    h=re.sub("","\u4ee5",h,flags=re.IGNORECASE)
    h=re.sub("","\u4f1a",h,flags=re.IGNORECASE)
    h=re.sub("","\u5bb6",h,flags=re.IGNORECASE)
    h=re.sub("","\u53ef",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e0b",h,flags=re.IGNORECASE)
    h=re.sub("","\u800c",h,flags=re.IGNORECASE)
    h=re.sub("","\u8fc7",h,flags=re.IGNORECASE)
    h=re.sub("","\u5929",h,flags=re.IGNORECASE)
    h=re.sub("","\u53bb",h,flags=re.IGNORECASE)
    h=re.sub("","\u80fd",h,flags=re.IGNORECASE)
    h=re.sub("","\u5bf9",h,flags=re.IGNORECASE)
    h=re.sub("","\u5c0f",h,flags=re.IGNORECASE)
    h=re.sub("","\u591a",h,flags=re.IGNORECASE)
    h=re.sub("","\u7136",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e8e",h,flags=re.IGNORECASE)
    h=re.sub("","\u5fc3",h,flags=re.IGNORECASE)
    h=re.sub("","\u5b66",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e48",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e4b",h,flags=re.IGNORECASE)
    h=re.sub("","\u90fd",h,flags=re.IGNORECASE)
    h=re.sub("","\u597d",h,flags=re.IGNORECASE)
    h=re.sub("","\u770b",h,flags=re.IGNORECASE)
    h=re.sub("","\u8d77",h,flags=re.IGNORECASE)
    h=re.sub("","\u53d1",h,flags=re.IGNORECASE)
    h=re.sub("","\u5f53",h,flags=re.IGNORECASE)
    h=re.sub("","\u6ca1",h,flags=re.IGNORECASE)
    h=re.sub("","\u6210",h,flags=re.IGNORECASE)
    h=re.sub("","\u53ea",h,flags=re.IGNORECASE)
    h=re.sub("","\u5982",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e8b",h,flags=re.IGNORECASE)
    h=re.sub("","\u628a",h,flags=re.IGNORECASE)
    h=re.sub("","\u8fd8",h,flags=re.IGNORECASE)
    h=re.sub("","\u7528",h,flags=re.IGNORECASE)
    h=re.sub("","\u7b2c",h,flags=re.IGNORECASE)
    h=re.sub("","\u6837",h,flags=re.IGNORECASE)
    h=re.sub("","\u9053",h,flags=re.IGNORECASE)
    h=re.sub("","\u60f3",h,flags=re.IGNORECASE)
    h=re.sub("","\u4f5c",h,flags=re.IGNORECASE)
    h=re.sub("","\u79cd",h,flags=re.IGNORECASE)
    h=re.sub("","\u5f00",h,flags=re.IGNORECASE)
    h=re.sub("","\u7f8e",h,flags=re.IGNORECASE)
    h=re.sub("","\u4e73",h,flags=re.IGNORECASE)
    h=re.sub("","\u9634",h,flags=re.IGNORECASE)
    h=re.sub("","\u6db2",h,flags=re.IGNORECASE)
    h=re.sub("","\u830e",h,flags=re.IGNORECASE)
    h=re.sub("","\u6b32",h,flags=re.IGNORECASE)
    h=re.sub("","\u547b",h,flags=re.IGNORECASE)
    h=re.sub("","\u8089",h,flags=re.IGNORECASE)
    h=re.sub("","\u4ea4",h,flags=re.IGNORECASE)
    h=re.sub("","\u6027",h,flags=re.IGNORECASE)
    h=re.sub("","\u80f8",h,flags=re.IGNORECASE)
    h=re.sub("","\u79c1",h,flags=re.IGNORECASE)
    h=re.sub("","\u7a74",h,flags=re.IGNORECASE)
    h=re.sub("","\u6deb",h,flags=re.IGNORECASE)
    h=re.sub("","\u81c0",h,flags=re.IGNORECASE)
    h=re.sub("","\u8214",h,flags=re.IGNORECASE)
    h=re.sub("","\u5c04",h,flags=re.IGNORECASE)
    h=re.sub("","\u8131",h,flags=re.IGNORECASE)
    h=re.sub("","\u88f8",h,flags=re.IGNORECASE)
    h=re.sub("","\u9a9a",h,flags=re.IGNORECASE)
    h=re.sub("","\u5507",h,flags=re.IGNORECASE)'''
    return h

async def download_html_n(url):
    #print("down")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                response.raise_for_status()
                content = await response.read()

        return BeautifulSoup(content, "html.parser"), None
    except (aiohttp.ClientError, aiohttp.InvalidURL,aiohttp.ServerTimeoutError) as e:
        return None, str(e)
async def download_image_n(img_url, dir):
    global flag
    print("dimgs")
    img_url = img_url.replace("?", "")
    if not os.path.exists(dir+"/"+img_url.split("/")[-1]):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(img_url, headers=headers, timeout=5) as response:
                    response.raise_for_status()
                    img_response = await response.read()
        except (aiohttp.ClientError, asyncio.TimeoutError):
            return 404
        img_name = img_url.split("/")[-1]
        with open(dir+"/"+img_name, 'wb') as f:
            f.write(img_response)
        if flag == 0:
            with open(dir+"/cover.jpg", 'wb') as f:
                f.write(img_response)
            flag = 1
        return 200
    else:
        return 500
async def convert_to_epub(seriesdir, id, stitle, title, path):
    command = f'gitbook epub ./cache/{seriesdir}/{id} "{path}{stitle}/{stitle}_{title}.epub"'
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # 等待命令执行完成并获取结果
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        print(f'命令执行失败: {command}')
        print(f'Stdout: {stdout.decode()}')
        print(f'Stderr: {stderr.decode()}')

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_biligui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.get.clicked.connect(self.get)
        self.ui.Start.setDisabled(1)
        self.ui.Start.clicked.connect(self.get_series)
        self.ui.ListWidget.setSelectionMode(QListView.MultiSelection)
        self.ui.seriesnum.returnPressed.connect(self.get)
        self.setWindowTitle("Bilidown")
    
    def createInfoBar(self,title,content):
        w = InfoBar(
            icon=InfoBarIcon.INFORMATION,
            title=title,
            content=content,
            orient=Qt.Vertical,    # vertical layout
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )
        w.show()
    def createSuccessInfoBar(self,title,content):
        # convenient class mothod
        w=InfoBar.success(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )
        w.show()
    def createErrorInfoBar(self,title,content):
        w=InfoBar.error(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=4000,    # won't disappear automatically
            parent=self
        )
        w.show()
    def createWarningInfoBar(self,title,content):
        w=InfoBar.warning(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=False,   # disable close button
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )
        w.show()
    def Dialog(self,title,content):
        title = title
        content = content
        w = Dialog(title, content, self)
        # w.setTitleBarVisible(False)
        w.show()
        if w.exec():
            return 1
        else:
            return 0

    def download_html(self,url):
        loop = asyncio.get_event_loop()
        task = loop.create_task(download_html_n(url))

        while not task.done():
            QApplication.processEvents()  # 执行Qt事件处理，避免界面冻结
            loop.run_until_complete(asyncio.sleep(0.01))  # 执行事件循环直到下一个任务就绪

        soup, error_msg = task.result()
        #loop.close()
        return soup, error_msg

    def download_html_old(self,url):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding=response.apparent_encoding
            response.raise_for_status()
        except RequestException as e:
        # 处理请求异常，并输出错误信息
            return None,e
        return BeautifulSoup(response.content, "html.parser"),""

    def download_image(self,img_url,dir):
        #self.createInfoBar("正在下载", img_url)
        loop = asyncio.get_event_loop()
        task = loop.create_task(download_image_n(img_url, dir))

        while not task.done():
            QApplication.processEvents()  # 执行Qt事件处理，避免界面冻结
            loop.run_until_complete(asyncio.sleep(0.01))  # 执行事件循环直到下一个任务就绪

        if task.result()==500:
            self.createWarningInfoBar("已存在",img_url)
        elif task.result()==404:
            self.createErrorInfoBar("连接超时或出错","正在重连...")
            time.sleep(2)
            self.download_image(img_url,dir)
        else:
            self.createSuccessInfoBar("下载完成",img_url)
        #loop.close()
        return #soup, error_msg
    
    def download_image_old(self,img_url,dir):
        global flag
        img_url=img_url.replace("?", "")
        if not os.path.exists(dir+"/"+img_url.split("/")[-1]):
            self.createInfoBar("正在下载",img_url)
            #waitflash(0.3)
            for retry in range(max_retries):
                try:
                    img_response = requests.get(img_url, headers=headers, timeout=5)
                    img_response.raise_for_status()
                    break  # 请求成功，跳出循环
                except (RequestException,TimeoutError):
                    self.createWarningInfoBar("连接超时或出错","正在进行第"+str(retry+1)+"次重连...")
                    print(f"\r连接超时或连接出错，正在进行第{retry+1}次重连...")
                    time.sleep(retry+1)
                    continue  # 连接超时或连接出错，进行下一次重连
            img_name = img_url.split("/")[-1]
            with open(dir+"/"+img_name, 'wb') as f:
                f.write(img_response.content)
            if flag==0:
                with open(dir+"/cover.jpg", 'wb') as f:
                    f.write(img_response.content)
                flag=1
        else:
            self.createInfoBar("已存在",img_url)
    def extract(self,soup,dir):
        acontent_div = soup.find("div", {"id": "acontent"})
        for img_tag in acontent_div.find_all("img"):
            try:
                img_url = img_tag["data-src"]
            except:
                img_url = img_tag["src"]
            alt_text = img_tag.get("alt", "")
            filename = img_url.split("/")[-1]
            markdown_image = f"![{alt_text}]({filename})\n"
            img_tag.replace_with(markdown_image)
            print("dimg")
            self.download_image(img_url,dir)
        content = str(acontent_div)
        markdown_content = html2text.html2text(content)
        markdown_content=decode(markdown_content)
        return markdown_content
    def get_chapter(self,url,dir,mode=1):
        #print("获取"+url)
        while 1:
            response,e=self.download_html(url)
            if e:
                self.createErrorInfoBar("错误",str(e))
                time.sleep(1)
            else:
                break

        content=self.extract(response,dir)
        match = re.search(r'var nextpage="(.*?)";', str(response))
        #print(url.split("/")[-1],match.group(1).split("/")[-1],compare_urls(url.split("/")[-1],match.group(1).split("/")[-1]))
        if mode==1:
            if match and compare_urls(url.split("/")[-1],match.group(1).split("/")[-1]):
                #print("下一页："+match.group(1))
                return content+"\n"+self.get_chapter("https://w.linovelib.com"+match.group(1),dir)
            else:
                return content
        else:
            if match and compare_urls(url.split("/")[-1],match.group(1).split("/")[-1]):
                #print("下一页："+match.group(1))
                return self.get_chapter("https://w.linovelib.com"+match.group(1),dir,2)
            else:
                return match.group(1)
    def get_book(self,soup,start,title,seriesdir,id,introduction,stitle,author,path):
        global flag
        flag=0
        start+=1
        cid=0
        threads = []
        thread_num=0
        self.createInfoBar("创建文件夹","")
        dir="./cache/"+seriesdir+"/"+str(id)
        print("\rmkdir "+dir)
        try:
            os.mkdir(dir)
        except OSError as e:
            print("\rerror: "+str(e))
            self.createWarningInfoBar("文件夹"+str(id)+"已存在","")
        try:
            os.remove(dir+"/SUMMARY.md")
        except:
            self.createInfoBar("SUMMARY.md不存在","")
            print("\rSUMMARY.md不存在")
        data='{"description": "Gitbook 文档","language": "zh-hans","author": "'+author+'","title": "'+title+'"}'
        with open(dir+"/book.json", 'w', encoding='utf-8') as file:
            file.write(data)
        with open(dir+"/SUMMARY.md", 'w', encoding='utf-8') as file:
            file.write("# Summary\n\n* [Introduction](README.md)\n")
        with open(dir+"/README.md", 'w', encoding='utf-8') as file:
            file.write("# 简介\n"+introduction)
        while(1):
            try:
                li_tag=soup.find_all('li')[start]
                link = li_tag.find('a')
            except:
                link = None
            if link:
                href = link['href']
                self.createInfoBar("正在下载",li_tag.text.strip())
                print(title,href, li_tag.text.strip())
                if str(href)=="javascript:cid(0)":
                    self.createWarningInfoBar("错误，回溯中","")
                    print("\r错误，回溯中")
                    try:
                        href=self.get_chapter("https://w.linovelib.com"+soup.find_all('li')[start-1].find('a')['href'],dir,2)
                    except:
                        href=self.get_chapter("https://w.linovelib.com"+soup.find_all('li')[start-2].find('a')['href'],dir,2)
                content=self.get_chapter("https://w.linovelib.com"+href,dir)
                self.process+=1
                print(self.process,self.all,(self.process/self.all)*100)
                self.ui.ProgressBar.setValue(int((self.process/self.all)*100))#int(self.process/self.all)
                #print(content)
                with open(dir+"/"+str(cid)+".md", 'w', encoding='utf-8') as file:
                    file.write("# "+li_tag.text.strip()+"\n"+content)
                with open(dir+"/SUMMARY.md", 'a', encoding='utf-8') as file:
                    file.write("* ["+li_tag.text.strip()+"](./"+str(cid)+".md)\n")
                cid+=1
                start+=1
            else:
                self.createInfoBar("创建书籍",stitle+'_'+title+'.epub"')
                print('\rgitbook epub '+seriesdir+'/'+str(id)+' "'+stitle+'_'+title+'.epub"')
                loop = asyncio.get_event_loop()
                task = loop.create_task(convert_to_epub(seriesdir, id, stitle, title,path))
                while not task.done():
                    QApplication.processEvents()  # 执行Qt事件处理，避免界面冻结
                    loop.run_until_complete(asyncio.sleep(0))  # 执行事件循环直到下一个任务就绪
                #os.system('gitbook epub '+seriesdir+'/'+str(id)+' "'+stitle+'"/"'+stitle+'_'+title+'.epub"')
                self.createSuccessInfoBar("书籍创建成功！",stitle+'_'+title+'.epub"')
                break
    def get(self):
        print("get")
        idnum=self.ui.seriesnum.text()
        url = "https://w.linovelib.com/novel/"+idnum+".html"
        self.ui.get.setDisabled(True)
        self.ui.seriesnum.setEnabled(False)
        self.ui.Start.setEnabled(False)
        self.createInfoBar("正在下载元数据",url)
        respond,e=self.download_html(url)
        if e==None:
            pass
        else:
            self.createErrorInfoBar("错误",str(e))
            self.ui.get.setEnabled(True)
            self.ui.seriesnum.setEnabled(1)
            return 0
        self.stitle = respond.find('meta', {'property': 'og:title'})['content']
        self.description = respond.find('meta', {'property': 'og:description'})['content']
        self.catalog = respond.find('meta', {'property': 'og:novel:read_url'})['content']
        coverurl = respond.find('meta', {'property': 'og:image'})['content']
        self.author = respond.find('meta', {'property': 'og:novel:author'})['content']
        res=requests.get(coverurl,headers=headers)
        self.createSuccessInfoBar("下载完成",url)
        img=QImage.fromData(res.content)
        self.ui.cover.setPixmap(QPixmap.fromImage(img).scaled(self.ui.cover.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.ui.title.setText(self.stitle)
        self.ui.author.setText("作者："+self.author)
        self.ui.description.setText(self.description)
        self.createInfoBar("正在下载目录",url)
        self.soup,e=self.download_html(self.catalog)
        num=0
        self.books=[]
        self.gets=[]
        title_num=0
        self.ui.ListWidget.clear()
        for li_tag in self.soup.find_all('li'):
            link = li_tag.find('a')
            if not link:
                current_book=book_type(title_num,li_tag.text.strip(),num)
                try:
                    self.books[-1].len=num-self.books[-1].num
                except:
                    pass
                self.books.append(current_book)
                item=QListWidgetItem(current_book.name)
                #item.setCheckState(0)
                self.ui.ListWidget.addItem(item)
                #print("\r"+str(current_book.id)+" "+current_book.name+" "+str(current_book.num))
                title_num+=1
            num+=1
        self.books[-1].len=num-self.books[-1].num
        for book in self.books:
            print(str(book.id)+" "+book.name+" "+str(book.num)+" "+str(book.len))
        self.createSuccessInfoBar("下载完成",self.catalog)
        self.ui.get.setEnabled(True)
        self.ui.Start.setEnabled(1)
        self.ui.seriesnum.setEnabled(1)
    def get_series(self):
        self.all=0
        self.process=0
        self.ui.ProgressBar.setValue(0)
        self.gets.clear()
        selected=self.ui.ListWidget.selectedIndexes()
        for index in selected:
            self.all+=self.books[index.row()].len-1
            self.gets.append(self.books[index.row()])
        print(self.all)
        dialog=""
        for i in self.gets:
            dialog+=i.name+"\n"
        if self.Dialog("即将下载",dialog):
            pass
        else:
            return
        self.ui.Start.setEnabled(False)
        self.ui.get.setEnabled(False)
        self.ui.seriesnum.setEnabled(False)
        pattern = r"/(\d+)/"
        seriesdir = re.search(pattern, self.catalog).group(1)
        self.createInfoBar("创建文件夹","")
        print("\rmkdir ./cache/"+str(seriesdir))
        try:
            os.mkdir(str("./cache/"+seriesdir))
        except OSError as e:
            print("\rerror: "+str(e))
            self.createWarningInfoBar("文件夹"+str(seriesdir)+"已存在","")
        print('\rmkdir "'+self.stitle+'"')
        try:
            os.mkdir(path+self.stitle)
        except OSError as e:
            print("\rerror: "+str(e))
            self.createWarningInfoBar("文件夹"+self.stitle+"已存在","")
        for i in self.gets:
            self.get_book(self.soup,i.num,i.name,seriesdir,i.id,self.description,self.stitle,self.author,path)
        self.Dialog("下载完成",dialog)
        self.ui.Start.setEnabled(True)
        self.ui.get.setEnabled(True)
        self.ui.seriesnum.setEnabled(1)
        
        
        
        



        

if __name__ == '__main__':
    try:
        os.mkdir("cache")
    except OSError as e:
        print("\rerror: "+str(e))
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow=main()
    mainwindow.show()
    sys.exit(app.exec_())