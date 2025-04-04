
使用語言模型:

語詞等級之預訓練詞嵌入模型
https://nlp.tmu.edu.tw/word2vec/index.html


Colab:
(初版)https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9
# 文章洗稿工具 (Article Laundering Tool)

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![許可證](https://img.shields.io/badge/許可證-MIT-green)

## 簡介

這是一個基於Python的文章洗稿工具，透過Word2Vec模型和中文分詞技術，能夠智慧替換文章中的關鍵字，產生相似但不完全相同的內容。該工具特別適用於內容創作者、SEO優化和文章改寫需求。

## 使用的語言模型

本工具使用北醫大學 (TMU) 自然語言處理實驗室開發的「語詞等級之預訓練詞嵌入模型」:
- 模型連結: [https://nlp.tmu.edu.tw/word2vec/index.html](https://nlp.tmu.edu.tw/word2vec/index.html)
- 模型說明: 此模型針對中文語言最佳化，提供高品質的詞向量表示

## Colab筆記本

您可以透過以下Colab筆記本直接使用本工具:
- 初版: https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9

## 功能特點

- 基於Word2Vec模型進行相似詞替換
- 支援簡繁體中文轉換
- 可調節替換詞的相似度閾值
- 可控修改幅度百分比
- 直觀顯示修改前後的文章對比

## 安裝需求

```bash
pip install gensim
pip install opencc-python-reimplemented
pip install jieba
```

## 使用方法

1. 下載TMU NLP實驗室的Word2Vec模型檔案並放置於指定位置
2. 配置模型路徑：`model = gensim.models.KeyedVectors.load_word2vec_format('路徑/qqqq.model.bin', unicode_errors='ignore', binary=True)`
3. 設定參數：
 - `turnout`: 詞語相似度閾值(預設0.7)
 - `spread`: 修改幅度上限(預設0.25)
4. 執行程式並輸入需要改寫的文章內容

## 參數說​​明

- **turnout**: 控制替換詞的相似度閾值，值越高替換的詞語越相似
- **spread**: 控製文章的修改幅度百分比，數值越高修改越多

## 使用範例

```python
# 設定參數
turnout = 0.7 # 詞語相似度閾值
spread = 0.25 # 修改幅度

# 輸入文章
input2 = input('輸入文章內容:')

# 程式將顯示:
# 1. 擷取的關鍵字
# 2. 替換用的相似詞及其相似度
# 3. 修改前後的文章對比
```

## 輸出格式

程式將顯示三部分資訊：
1. 提取出的關鍵字列表
2. 每個關鍵字的替換詞及相似度數值
3. 修改前後的文章對比，替換的字詞會用方括號標記，如：[替換字]

## 注意事項

- 需預先下載北醫大學 NLP實驗室的Word2Vec模型
- 模型檔案較大，請確保有足夠的儲存空間
- 替換品質取決於Word2Vec模型的品質和覆蓋範圍

## 貢獻指南

歡迎提交問題報告和改進建議，請透過GitHub Issues或Pull Requests參與專案改進。

## 許可證

詳情請參閱LICENSE文件。

