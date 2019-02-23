from django.contrib import admin
from .models import Software, Hardware, Others, Achievement, Education, Work, About

admin.site.register(About)
admin.site.register(Software)
admin.site.register(Others)
admin.site.register(Hardware)
admin.site.register(Achievement)
admin.site.register(Education)
admin.site.register(Work)

# Register your models here.
