import textwrap
from abc import ABC

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from .base_loader import BaseBookLoader


class PDFBookLoader(BaseBookLoader, ABC):
    def __init__(self, filename):
        self.filename = filename

    def make_book(self, sentences):
        c = canvas.Canvas(self.filename, pagesize=letter)
        pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))

        for sentence in sentences:
            c.setFont("SimSun", 16)  # 使用自定义字体

            # 添加不常用词和对应的翻译（处理换行）
            y = 660  # 初始纵坐标位置

            # 处理英文文本的换行
            lines = self.wrap_text(sentence.english_text, 60)  # 按每行50个字符换行
            for line in lines:
                c.drawString(50, y, line)
                y -= 20  # 调整纵坐标位置

            # 处理中文文本的换行
            chinese_lines = textwrap.wrap(sentence.chinese_text, 30)  # 按每行20个字符换行
            for line in chinese_lines:
                c.drawCentredString(300, y, line)
                y -= 20  # 调整纵坐标位置

            # 添加不常用词和对应的翻译
            for i, (word, translation) in enumerate(sentence.translations.items()):
                c.drawString(50, y, f"{word}: {translation}")
                y -= 20  # 调整纵坐标位置

            c.showPage()

        c.save()

    @staticmethod
    def wrap_text(text, width):
        lines = []
        current_line = ""

        for word in text.split():
            if len(current_line) + len(word) + 1 <= width:
                current_line += f"{word} "
            else:
                lines.append(current_line)
                current_line = f"{word} "

        if current_line:
            lines.append(current_line)

        return lines
