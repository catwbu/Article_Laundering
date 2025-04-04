
使用語言模型:

語詞等級之預訓練詞嵌入模型
https://nlp.tmu.edu.tw/word2vec/index.html


Colab:
(初版)https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9

# 文章洗稿工具 (Article Laundering Tool)

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![许可证](https://img.shields.io/badge/许可证-MIT-green)

## 简介

这是一个基于Python的文章洗稿工具，通过Word2Vec模型和中文分词技术，能够智能替换文章中的关键词，生成相似但不完全相同的内容。该工具特别适用于内容创作者、SEO优化和文章改写需求。

## 使用的语言模型

本工具使用臺北醫學大學 (TMU) 自然語言處理實驗室开发的「語詞等級之預訓練詞嵌入模型」:
- 模型链接: [https://nlp.tmu.edu.tw/word2vec/index.html](https://nlp.tmu.edu.tw/word2vec/index.html)
- 模型说明: 此模型针对中文语言优化，提供高质量的词向量表示

## Colab笔记本

您可以通过以下Colab笔记本直接使用本工具:
- 初版: [https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9](https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9)

## 功能特点

- 基于Word2Vec模型进行相似词替换
- 支持简繁体中文转换
- 可调节替换词的相似度阈值
- 可控制修改幅度百分比
- 直观显示修改前后的文章对比

## 安装需求

```bash
pip install gensim
pip install opencc-python-reimplemented
pip install jieba
```

## 使用方法

1. 下载TMU NLP实验室的Word2Vec模型文件并放置于指定位置
2. 配置模型路径：`model = gensim.models.KeyedVectors.load_word2vec_format('路径/qqqq.model.bin', unicode_errors='ignore', binary=True)`
3. 设置参数：
   - `turnout`: 词语相似度阈值(默认0.7)
   - `spread`: 修改幅度上限(默认0.25)
4. 运行程序并输入需要改写的文章内容

## 参数说明

- **turnout**: 控制替换词的相似度阈值，值越高替换的词语越相似
- **spread**: 控制文章的修改幅度百分比，值越高修改越多

## 使用示例

```python
# 设置参数
turnout = 0.7  # 词语相似度阈值
spread = 0.25  # 修改幅度

# 输入文章
input2 = input('输入文章内容:')

# 程序将显示:
# 1. 提取的关键词
# 2. 替换用的相似词及其相似度
# 3. 修改前后的文章对比
```

## 输出格式

程序将显示三部分信息：
1. 提取出的关键词列表
2. 每个关键词的替换词及相似度数值
3. 修改前后的文章对比，替换的词语将用方括号标记，如：[替换词]

## 注意事项

- 需要预先下载臺北醫學大學 NLP实验室的Word2Vec模型
- 模型文件较大，请确保有足够的存储空间
- 替换质量取决于Word2Vec模型的质量和覆盖范围

## 贡献指南

欢迎提交问题报告和改进建议，请通过GitHub Issues或Pull Requests参与项目改进。

## 许可证

本项目采用MIT许可证，详情请参阅LICENSE文件。
