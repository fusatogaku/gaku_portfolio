from django.db import models

class GachaWeightModel(models.Model):
    # ガチャのレアリティと排出率
    Rarity = models.IntegerField(default=0, blank=True, null=True)
    Probability = models.FloatField(default=0, blank=False, null=False)
    
class GachaPickUpModel(models.Model):
    # ピックアップするIDとピックアップ率。
    Goods = models.CharField(max_length=100)
    PickUpProb = models.FloatField(default=0, blank=True, null=True)

class GachaMasterModel(models.Model):
    # ガチャの景品のデータ
    Goods = models.CharField(max_length=50)
    RarityMaster = models.IntegerField(default=0, blank=True, null=True)
