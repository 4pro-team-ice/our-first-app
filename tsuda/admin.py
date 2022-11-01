from django.contrib import admin
from .models import Post
from .models import Classroom
from .models import Allclass
from .models import Syllabus
from .models import SyllabusComment

from .models import Monday1
from .models import Monday2
from .models import Monday3
from .models import Monday4
from .models import Monday5
from .models import Monday6
from .models import Tuesday1
from .models import Tuesday2
from .models import Tuesday3
from .models import Tuesday4
from .models import Tuesday5
from .models import Tuesday6
from .models import Wednesday1
from .models import Wednesday2
from .models import Wednesday3
from .models import Wednesday4
from .models import Wednesday5
from .models import Wednesday6
from .models import Thursday1
from .models import Thursday2
from .models import Thursday3
from .models import Thursday4
from .models import Thursday5
from .models import Thursday6
from .models import Friday1
from .models import Friday2
from .models import Friday3
from .models import Friday4
from .models import Friday5
from .models import Friday6
from import_export import resources  # 追加
from import_export.admin import ImportExportModelAdmin  # 追加
from import_export.fields import Field # 追加





admin.site.register(Post)
# admin.site.register(Classroom)
admin.site.register(Allclass)
admin.site.register(Monday1)
admin.site.register(Monday2)
admin.site.register(Monday3)
admin.site.register(Monday4)
admin.site.register(Monday5)
admin.site.register(Monday6)
admin.site.register(Tuesday1)
admin.site.register(Tuesday2)
admin.site.register(Tuesday3)
admin.site.register(Tuesday4)
admin.site.register(Tuesday5)
admin.site.register(Tuesday6)
admin.site.register(Wednesday1)
admin.site.register(Wednesday2)
admin.site.register(Wednesday3)
admin.site.register(Wednesday4)
admin.site.register(Wednesday5)
admin.site.register(Wednesday6)
admin.site.register(Thursday1)
admin.site.register(Thursday2)
admin.site.register(Thursday3)
admin.site.register(Thursday4)
admin.site.register(Thursday5)
admin.site.register(Thursday6)
admin.site.register(Friday1)
admin.site.register(Friday2)
admin.site.register(Friday3)
admin.site.register(Friday4)
admin.site.register(Friday5)
admin.site.register(Friday6)



admin.site.register(Syllabus)
admin.site.register(SyllabusComment)

class ClassroomResource(resources.ModelResource):
   # field名とcsvの列名が異なる場合はここで指定する。
   # ここでは、postalcode / postalCode、category / categoriesと微妙に異なる。
   day_of_week = Field(attribute='day_of_week', column_name='day_of_week')
   period_of_time = Field(attribute='period_of_time', column_name='period_of_time')
   className = Field(attribute='className', column_name='className')
   term = Field(attribute='term', column_name='term')
   class_number = Field(attribute='class_number', column_name='class_number')
   # django-import-exportのModel設定
   class Meta:
       model = Classroom
       # Controls if the import should skip unchanged records. Default value is False
       skip_unchanged = True
       use_bulk = True

@admin.register(Classroom)
# ImportExportModelAdminを継承したAdminクラスを作成する
class ClassroomAdmin(ImportExportModelAdmin):
   # ordering = ['id']
   # list_display = ('id', 'day_of_week', 'period_of_time', 'className', 'term', 'class_number')
   list_display = ('day_of_week', 'period_of_time', 'className', 'term', 'class_number')
   # resource_classにModelResourceを継承したクラス設定
   resource_class = ClassroomResource
