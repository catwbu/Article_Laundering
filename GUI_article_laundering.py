import tkinter as tk
from tkinter import scrolledtext
import gensim
from opencc import OpenCC
import jieba
import jieba.analyse
import textwrap

from gensim.models.word2vec import Word2Vec
model = gensim.models.KeyedVectors.load_word2vec_format('C:/Users/W7/Downloads/qqqq.model.bin', unicode_errors='ignore', binary=True)

#context=''
def process_text(input_text, turnout, spread):

    global context,before,xxx

    input2=input_text

    tag_pocket=[]
    token_pocket=[]

    context = input2
    before = context

    cc = OpenCC('tw2sp')
    input2 = cc.convert(input2)

    keywords = jieba.analyse.extract_tags(input2, topK=int(len(input2)*spread) ,withWeight=True)

    for item,v in keywords:
        cc = OpenCC('s2twp')
        tag_master=cc.convert(item)
        tag_pocket.append(tag_master)
        #print(tag_master)
    print(tag_pocket)
    xxx=[]
    for i in tag_pocket:
        try:
            lst = model.most_similar(i)
            print(lst, lst[0][1])
        except Exception as e:
            lst = []
            print(f"An error occurred: {e}")
        if lst and lst[0][1] > turnout:
                xxx.append(lst[0][0])
                print(str(lst[0][0]), str(lst[0][1]))
                context = context.replace(i, str(lst[0][0]))
    return context
    #result=context
'''

'''


class WordReplacementGUI:
    def __init__(self, master):
        self.master = master
        master.title("文字替換程序")

        # 輸入文本框
        self.input_label = tk.Label(master, text="輸入文章內容:")
        self.input_label.pack()
        self.input_text = scrolledtext.ScrolledText(master, height=10)
        self.input_text.pack()

        # 參數輸入
        self.turnout_label = tk.Label(master, text="篩選門檻值:")
        self.turnout_label.pack()
        self.turnout_entry = tk.Entry(master)
        self.turnout_entry.insert(0, "0.7")
        self.turnout_entry.pack()

        self.spread_label = tk.Label(master, text="修改幅度上限:")
        self.spread_label.pack()
        self.spread_entry = tk.Entry(master)
        self.spread_entry.insert(0, "0.25")
        self.spread_entry.pack()

        #
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        '''
        # 處理按鈕
        self.process_button = tk.Button(master, text="處理文本", command=self.process)
        self.process_button.pack()
        '''
        # 處理按鈕
        self.process_button = tk.Button(self.button_frame, text="處理文本", command=self.process)
        self.process_button.pack(side=tk.LEFT)

        # 對比按鈕
        self.compare_button = tk.Button(self.button_frame, text="對比", command=self.compare)
        self.compare_button.pack(side=tk.LEFT)

        # 輸出文本框
        self.output_label = tk.Label(master, text="處理結果:")
        self.output_label.pack()
        self.output_text = scrolledtext.ScrolledText(master, height=10)
        self.output_text.pack()

    def process(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        turnout = float(self.turnout_entry.get())
        spread = float(self.spread_entry.get())

        try:
            result = process_text(input_text, turnout, spread)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"處理過程中發生錯誤：{str(e)}")

    def compare(self):
        global context,before,xxx
        if context:
            print()
            print('before:\n'+'\n'.join(textwrap.wrap(before,width=150))+'\n'+'\nafter:\n'+'\n'.join(textwrap.wrap(context,width=250)))

            for i in set(xxx):
                context=context.replace(i, '['+i+']')
                print('before:\n'+'\n'.join(textwrap.wrap(before,width=150))+'\n'+'\nafter:\n'+'\n'.join(textwrap.wrap(context,width=250)))
                result = f"{textwrap.fill(context, width=250)}"

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)
        else:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "請先處理文本，然後再進行對比。")

if __name__ == "__main__":
    root = tk.Tk()
    gui = WordReplacementGUI(root)
    root.mainloop()
