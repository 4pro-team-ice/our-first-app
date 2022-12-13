from django.contrib import admin
from .models import Post
from .models import Classroom
from .models import Allclass
from .models import Syllabus
from .models import SyllabusComment

from .models import T1
from .models import T2
from .models import T3
from .models import T4


from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from .models import Account


admin.site.register(Post)
# admin.site.register(Classroom)
admin.site.register(Allclass)
admin.site.register(T1)
admin.site.register(T2)
admin.site.register(T3)
admin.site.register(T4)


# admin.site.register(Syllabus)
admin.site.register(SyllabusComment)

admin.site.register(Account)

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


# シラバス
class SyllabusResource(resources.ModelResource):
    # field名とcsvの列名が異なる場合はここで指定する。
    # ここでは、postalcode / postalCode、category / categoriesと微妙に異なる。
    classID = Field(attribute='classID', column_name='科目番号')
    className = Field(attribute='className', column_name='科目')
    className_eng = Field(attribute='className_eng', column_name='科目名(英語)')
    teacher_name = Field(attribute='teacher_name', column_name='担当者名')
    term = Field(attribute='term', column_name='開講期')
    tanni = Field(attribute='tanni', column_name='単位')
    gengo = Field(attribute='gengo', column_name='使用言語')
    nenji = Field(attribute='nenji', column_name='配当年次')
    bunya = Field(attribute='bunya', column_name='学問分野')
    level = Field(attribute='level', column_name='推奨レベル')
    gakka = Field(attribute='gakka', column_name='科目区分')
    syllabusinfo = Field(attribute='syllabusinfo', column_name='講義の目的と内容')
    mokuhyo = Field(attribute='mokuhyo', column_name='授業の到達目標')
    keikaku = Field(attribute='keikaku', column_name='授業計画')
    text = Field(attribute='text', column_name='テキスト')
    sankosho = Field(attribute='sankosho', column_name='参考書')
    junbi = Field(attribute='junbi', column_name='準備学習(予習・復習等)の内容')
    hyoka = Field(attribute='hyoka', column_name='評価方法・基準')
    feedback = Field(attribute='feedback', column_name='課題に対するフィードバック')
    office_hour = Field(attribute='office_hour', column_name='オフィスアワー')
    tokushoku = Field(attribute='tokushoku', column_name='授業の特色')
    sonota = Field(attribute='sonota', column_name='その他')
    # django-import-exportのModel設定
    class Meta:
        model = Syllabus
        # Controls if the import should skip unchanged records. Default value is False
        skip_unchanged = True
        use_bulk = True

@admin.register(Syllabus)
 # ImportExportModelAdminを継承したAdminクラスを作成する
class SyllabusAdmin(ImportExportModelAdmin):
    # ordering = ['id']
    # list_display = ('id', 'day_of_week', 'period_of_time', 'className', 'term', 'class_number')
    list_display = ('classID', 'className', 'className_eng', 'teacher_name','term', 'tanni',
                    'gengo', 'nenji', 'bunya', 'level','gakka', 'syllabusinfo',
                    'mokuhyo', 'keikaku', 'text', 'sankosho','junbi', 'hyoka',
                    'feedback', 'office_hour', 'tokushoku', 'sonota')
    # resource_classにModelResourceを継承したクラス設定
    resource_class = SyllabusResource
