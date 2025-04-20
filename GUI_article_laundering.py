print("載入套件中..")
import wx
import wx.richtext as rt
import gensim
from opencc import OpenCC
import jieba
import jieba.analyse
import os

import textwrap


# 載入模型
print("載入模型中..")
model_path = os.path.join("model", "qqqq.model.bin")
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, unicode_errors='ignore', binary=True)

context = ''
before = ''
xxx = []
last_output = ''
is_highlighted = False  # 新增標記來跟踪當前是否處於高亮狀態

def process_text(input_text, turnout, spread):
    global context, before, xxx, is_highlighted

    tag_pocket = []
    context = input_text
    before = input_text

    cc = OpenCC('tw2sp')
    input2 = cc.convert(input_text)

    keywords = jieba.analyse.extract_tags(input2, topK=int(len(input2) * spread), withWeight=True)

    for item, _ in keywords:
        cc = OpenCC('s2twp')
        tag_master = cc.convert(item)
        tag_pocket.append(tag_master)
        print(tag_master)

    xxx = []
    for i in tag_pocket:
        try:
            lst = model.most_similar(i)
        except Exception as e:
            lst = []
        if lst and lst[0][1] > turnout:
            xxx.append(lst[0][0])
            context = context.replace(i, str(lst[0][0]))
            print(str(lst[0][0]),str(lst[0][1]))
    is_highlighted = False  # 處理文本後重置
    return context

class WordReplacementApp(wx.Frame):
    def __init__(self, parent, title):

        super().__init__(parent, title=title, size=(800, 700))
        #self.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 輸入框
        vbox.Add(wx.StaticText(panel, label="輸入文章內容："), flag=wx.LEFT | wx.TOP, border=10)
        self.input_text = rt.RichTextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(self.input_text, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # 門檻與幅度參數
        hbox_params = wx.BoxSizer(wx.HORIZONTAL)
        hbox_params.Add(wx.StaticText(panel, label="篩選門檻值："), flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=5)
        self.turnout = wx.TextCtrl(panel, value="0.7")
        hbox_params.Add(self.turnout, flag=wx.RIGHT, border=20)

        hbox_params.Add(wx.StaticText(panel, label="修改幅度上限："), flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=5)
        self.spread = wx.TextCtrl(panel, value="0.25")
        hbox_params.Add(self.spread)

        vbox.Add(hbox_params, flag=wx.ALL, border=10)

        # 按鈕列
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.process_btn = wx.Button(panel, label="處理文本", size=(120, 40))
        self.compare_btn = wx.Button(panel, label="對比", size=(120, 40))
        self.clear_btn = wx.Button(panel, label="清空輸出", size=(120, 40))

        hbox_buttons.Add(self.process_btn, flag=wx.RIGHT, border=10)
        hbox_buttons.Add(self.compare_btn, flag=wx.RIGHT, border=10)
        hbox_buttons.Add(self.clear_btn)

        vbox.Add(hbox_buttons, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        # 輸出區
        vbox.Add(wx.StaticText(panel, label="處理結果："), flag=wx.LEFT, border=10)
        self.output_text = rt.RichTextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.output_text, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        # 綁定事件
        self.process_btn.Bind(wx.EVT_BUTTON, self.on_process)
        self.compare_btn.Bind(wx.EVT_BUTTON, self.on_compare)
        self.clear_btn.Bind(wx.EVT_BUTTON, self.on_clear)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def on_process(self, event):
        global last_output, is_highlighted
        input_text = self.input_text.GetValue()
        try:
            turnout = float(self.turnout.GetValue())
            spread = float(self.spread.GetValue())

            result = process_text(input_text, turnout, spread)
            last_output = result
            self.output_text.SetValue(result)
            is_highlighted = False  # 處理文本後重置高亮狀態
        except Exception as e:
            self.output_text.SetValue(f"處理過程中發生錯誤：{str(e)}")

    def on_compare(self, event):
        global context, before, xxx, last_output, is_highlighted

        if not last_output:
            self.output_text.SetValue("請先處理文本，然後再進行對比。")
            return

        if is_highlighted:
            # 如果已經是高亮狀態，則恢復原始輸出
            self.output_text.SetValue(last_output)
            is_highlighted = False
        else:
            # 如果不是高亮狀態，則顯示高亮版本
            highlighted = last_output
            for word in set(xxx):
                highlighted = highlighted.replace(word, f"[{word}]")
            self.output_text.SetValue(highlighted)
            is_highlighted = True

    def on_clear(self, event):
        global is_highlighted
        self.output_text.SetValue("")
        is_highlighted = False

if __name__ == "__main__":
    app = wx.App(False)
    WordReplacementApp(None, title="Article Laundering")
    app.MainLoop()
