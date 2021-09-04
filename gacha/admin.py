from django.contrib import admin
from .models import GachaMasterModel, GachaWeightModel, GachaPickUpModel

"""
superuser
user: user
password: a
"""
# admin.site.register(GachaModel)

class WeightAdmin(admin.ModelAdmin):
    model = GachaWeightModel
    fields = ['Rarity', 'Probability']
    list_display = ['Rarity', 'Probability']
class PickUpAdmin(admin.ModelAdmin):
    model = GachaPickUpModel
    fields = ['Goods', 'PickUpProb']
    list_display = ['Goods', 'PickUpProb']
class MasterAdmin(admin.ModelAdmin):
    model = GachaMasterModel
    fields = ['Goods', 'RarityMaster']
    list_display = ['Goods', 'RarityMaster']
admin.site.register(GachaWeightModel, WeightAdmin)
admin.site.register(GachaPickUpModel, PickUpAdmin)
admin.site.register(GachaMasterModel, MasterAdmin)