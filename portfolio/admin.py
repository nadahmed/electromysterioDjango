from django.contrib import admin
from .models import Software, Hardware, Graphics, Achievement, Education, Work

admin.site.register(Software)
admin.site.register(Graphics)
admin.site.register(Hardware)
admin.site.register(Achievement)
admin.site.register(Education)
admin.site.register(Work)

# Register your models here.
