from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete

# materia antes curso
class Materia(models.Model):
    name = models.CharField(max_length=90, verbose_name='Nombre')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'profesores'}, verbose_name='Profesor')
    class_quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad de clases')
    #boton de activacion
    activate_grading = models.BooleanField(default=True, verbose_name='Activar Calificaciones')  # Nuevo campo
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

class Course(models.Model):
    name = models.CharField(max_length=90, verbose_name='Nombre')
    description = models.TextField(max_length=20, blank=True, null=True, verbose_name='Descripción')
    materias = models.ManyToManyField(Materia, related_name='courses', verbose_name='Materias')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso', default=1)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'estudiantes'}, verbose_name='Estudiante')
    enabled = models.BooleanField(default=True, verbose_name='Alumno Regular')

    def __str__(self):
        return f'{self.student.username} - {self.course.name}'

    class Meta:
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

#asistencias
class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances', limit_choices_to={'groups__name': 'estudiantes'}, verbose_name='Estudiante')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    present = models.BooleanField(default=False, blank=True, null=True, verbose_name='Presente')
    def __str__(self):
        return f'Asistencia {self.id}'
    #Lógica para generar el estado del alumno regular / irregular (enabled)


    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'  
# NOTAS
class Mark(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name='Materia')
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'estudiantes'}, verbose_name='Estudiante')
    # Notas ahora solo trimestral
    mark_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Primer trimestre')
    mark_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Segundo trimestre')
    mark_3 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Tercer trimestre')
    average = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='Promedio')
    #para poder poner un mensaje
   # teacher_message = models.TextField(null=True, blank=True)  # Campo para el mensaje del profesor

    def __str__(self):
        return f'{self.materia} - {self.student}'

    # Calcular el promedio de un trimestre
    def calculate_average(self):
            marks = [self.mark_1, self.mark_2, self.mark_3]
            valid_marks = [mark for mark in marks if mark is not None]
            if valid_marks:
                return sum(valid_marks) / len(valid_marks)
            return None

    def save(self, *args, **kwargs):
            # Verifico si alguna nota cambio
            if self.mark_1 or self.mark_2 or self.mark_3:
                self.average = self.calculate_average()     # Calcular el promedio (llamo a una función)
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        #notas 
        #mover estudente a curso
    def is_approved(self):
        # Aquí puedes ajustar el valor de aprobación según tu criterio, por ejemplo, si el promedio es 60 o más
        return self.average is not None and self.average >= 51
    
class GlobalConfig(models.Model):
    allow_add_notes = models.BooleanField(default=True)

    def __str__(self):
        return "Configuración Global"
        
#model para asistencia de profesores tabla primero
class CITeacher(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'profesores'}, verbose_name='Usuario')  # FK a auth_user
    first_name = models.CharField(max_length=50, verbose_name='Nombre')  # Nombre del profesor
    last_name = models.CharField(max_length=50, verbose_name='Apellido')  # Apellido del profesor
    ci = models.CharField(max_length=20, unique=True, verbose_name='CI')  # Campo para el CI único del profesor

    class Meta:
        verbose_name = 'CI de Profesor'
        verbose_name_plural = 'CIs de Profesores'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - CI: {self.ci}'

#model de registro entrada salida
class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(CITeacher, on_delete=models.CASCADE, verbose_name='Profesor')
    entry_time = models.DateTimeField(null=True, blank=True, verbose_name='Hora de Entrada')
    exit_time = models.DateTimeField(null=True, blank=True, verbose_name='Hora de Salida')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Registrado en')

    class Meta:
        verbose_name = 'Asistencia de Profesor'
        verbose_name_plural = 'Asistencias de Profesores'

    def __str__(self):
        return f'{self.teacher.first_name} {self.teacher.last_name} - Entrada: {self.entry_time} / Salida: {self.exit_time}'
    

#excluidos
class ExcludedStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'estudiantes'}, verbose_name='Estudiante')
    course = models.CharField(max_length=90, verbose_name='Curso')
    reason = models.CharField(max_length=255, verbose_name='Razón de Exclusión')

    def __str__(self):
        return f"{self.student.username} - {self.course} ({self.reason})"

    class Meta:
        verbose_name = 'Estudiante Excluido'
        verbose_name_plural = 'Estudiantes Excluidos'
        

#subir pdf horario
class Schedule(models.Model):
    name = models.CharField(max_length=255)  # Nombre del archivo PDF
    file = models.FileField(upload_to='schedules/')  # Ruta de carga para los archivos PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Fecha de carga

    def __str__(self):
        return self.name