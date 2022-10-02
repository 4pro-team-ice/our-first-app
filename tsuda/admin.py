from django.contrib import admin
from .models import Post
from .models import Classroom
from .models import Syllabus
from .models import SyllabusComment

admin.site.register(Post)
admin.site.register(Classroom)
admin.site.register(Syllabus)
admin.site.register(SyllabusComment)
