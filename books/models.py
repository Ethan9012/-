from django.db import models


class Book(models.Model):
  BOOK_TYPE = [     # 使用 list 來做列舉
    ("0", "總類"),  # 第一欄為真實儲存的資料，第二欄為呈現的字
    ("1", "哲學"),
    ("2", "宗教"),
    ("3", "科學"),
    ("4", "應用科學"),
    ("5", "社會科學"),
    ("6", "兩岸史地"),
    ("7", "世界史地"),
    ("8", "語言文學"),
    ("9", "藝術"),
  ]  
  

  bookname = models.CharField(max_length=255)
  ISBN = models.CharField(default = "000-0-00-000000-0", max_length = 20)
  author = models.CharField(default = "No Name", max_length = 50)
  type = models.CharField(max_length=1, choices=BOOK_TYPE, default = "0")
  lastQuantity = models.IntegerField(default = 1)
  maxQuantity = models.IntegerField(default = 1)
  rate = models.FloatField(default = 0.0)
  photo = models.ImageField(upload_to='book_photos/', null=True, blank=True)

  def __str__(self):
    return f"{self.bookname}"
