from django.contrib import admin
from .models import Employee
from .models import Technicien
from .models import Informaticien

admin.site.register(Employee)
admin.site.register(Technicien)
admin.site.register(Informaticien)