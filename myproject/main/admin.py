from django.contrib import admin

# Register your models here.
from .models import Plants, Microorganisms, MicroVsPlants, Publications, CompVsMicro, Compounds, ExtractsMicroImpact, Extracts, MicroorganismsForImpact


admin.site.register(Plants)
admin.site.register(Microorganisms)
admin.site.register(MicroVsPlants)
admin.site.register(Publications)
admin.site.register(CompVsMicro)
admin.site.register(Compounds)
admin.site.register(ExtractsMicroImpact)
admin.site.register(Extracts)
admin.site.register(MicroorganismsForImpact)