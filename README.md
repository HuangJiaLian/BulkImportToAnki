# BulkImportToAnk
An example to demonstrate how to import [Anki](https://apps.ankiweb.net/#download) cards in a batch.
And demonstrate how to generate an example of each word in the sentence and generate a PDF.

## Usage 
### First
1. 导入依赖
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
2. 设置字体
下载SimSun.ttf字体，并把它放在/python/site-packages/reportlab/fonts

3. 注册翻译平台的key填充进代码内

### Using 
```bash
python main.py
```
You can convert the PDF to a csv file `DataExportToAnki.csv`. 

Then, on your computer, open `Anki-> File -> Import`, and then choose the csv file.

<p align='center'>
<img src="./src/anki.png"  width='70%'>
</p>

Then, done. Thanks for using this. 
You can check [How to import to Anki from CSV file](https://huangjialian.github.io/learn/Tools/how_to_import_to_anki_from_csv.html) for more detail.
