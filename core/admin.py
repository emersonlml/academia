from django.contrib import admin
from .models import Materia,Registration,Attendance,Mark,Course
from .forms import MateriaForm

# Register your models here.

#curso renombrado a materia
class MateriaInline(admin.TabularInline):
    model = Course.materias.through
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [MateriaInline]
    exclude = ('materias',)

#@admin.register(Materia)
#class MateriaAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'description', 'teacher', 'class_quantity')


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    form = MateriaForm
    list_display = ('name', 'description', 'get_teacher_full_name', 'class_quantity', 'activate_grading')

    def get_teacher_full_name(self, obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}"

    get_teacher_full_name.short_description = 'Profesor'



#end
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'enabled')
    list_filter = ('course', 'student', 'enabled')
    
class AttendanceAdmin(admin.ModelAdmin):
    # Definir las opciones de visualización, filtros, etc., si es necesario
    list_display = ['student', 'date', 'present']
    list_filter = ['date', 'present']
    search_fields = ['student__username', 'student__first_name', 'student__last_name']

# Registrar el modelo Attendance con su clase de administración personalizada
admin.site.register(Attendance, AttendanceAdmin)
#cursos por trimestres
class MarkAdmin(admin.ModelAdmin):
    list_display = (
        'materia', 'student', 
        'mark_1', 'mark_2', 'mark_3',
        'average'
    )
    list_filter = ('materia', 'student')

admin.site.register(Mark, MarkAdmin)