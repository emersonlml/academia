from django.urls import path
from .views import HomeView,PricingView,RegisterView,ProfileView,CoursesView,CourseCreateView,ErrorView, CourseEnrollmentView,CourseEditView,CourseDeleteView,StudentListMarkView,UpdateMarkView,ListEstudent
from .views import ToggleAddNotesView,StudentListMarkViewsacction
from .views import CoursesView_list,MateriaListView,materia_detail,superuser_edit
from .views import AdminProfesoresView,search_profesores,ProfilePasswordChangeView,AddUserView,CustomLoginView,UserDetailsView
from .views import evolution
from django.contrib.auth.decorators import login_required
from core.views import generate_pdf_student_list,UnidadEducativaView
from .views import generate_course_excel
from .views import attendance_prof,CourseDetailView
from .views import AddUsersFromCSVView
from django.contrib.auth import views as auth_views
from .views import  DeleteUserView,HorarioView,RegisterEntryOrExitView,GetMateriasByCourseView,ScheduleDetailView
from .views import MateriaEditView,ToggleViewEvolutionView,SinPermisoView,MoveStudentView
from . import views
from .views import ManageBooksView, AddBookView, EditBookView, DeleteBookView, ViewBooksView




urlpatterns = [
    path('',HomeView.as_view(), name='home'), # homepage
    path('pricing/', PricingView.as_view(), name='pricing'),
    #pagina de regristo y login
    path('register/',RegisterView.as_view(), name='register'),
    #pagina de perfil
    path('profile/',login_required(ProfileView.as_view()), name='profile'),
    #pagina de curos
    path('courses/',login_required(CoursesView.as_view()), name='courses'),
    #crear cursos interfaz
    path('courses/create/',login_required(CourseCreateView.as_view()), name='course_create'),
    #editar course
    path('courses/<int:pk>/edit/', login_required(CourseEditView.as_view()), name='course_edit'),
    #eliminar course
    path('courses/<int:pk>/delete/', login_required(CourseDeleteView.as_view()), name='course_delete'),
    #inscripcion de alumno a un curso
    path('enroll_courses/<int:course_id>', login_required(CourseEnrollmentView.as_view()), name='enroll_course'),
    # erro de permisos
    path('error/',login_required(ErrorView.as_view()), name='error'),
    #Pagina de muestra de notas alumnos
    path('materias/<int:materia_id>',login_required(StudentListMarkView.as_view()), name='student_list_mark'),
    #listar alumnos sin notas
    path('materia/<int:materia_id>/', login_required(StudentListMarkViewsacction.as_view()), name='student_2_list'),
    #pagina para actualisar notas
    path('materias/update_mark/<int:mark_id>' , login_required(UpdateMarkView.as_view()), name='update_mark'),
    #pagina para secetarai ver alumnos
    path('materia/<int:materia_id>/list_attendance/',login_required(ListEstudent.as_view()), name='list_attendance'),
    #vista de las notas en los estudiantes
    path('evolution/<int:materia_id>/<int:student_id>/',login_required(evolution), name='evolution'),
    #vista de on/off boton
    path('toggle-add-notes/',login_required( ToggleAddNotesView.as_view()), name='toggle_add_notes'),

    #PARA PODER BUSCAR PROFESORES
    path('admin-profesores/',login_required( AdminProfesoresView.as_view()), name='admin_profesores'),
    path('search-profesores/', search_profesores, name='search_profesores'),
    #para buscar ver cursos en el admin pestaña
    path('admin/courses/', login_required(CoursesView_list.as_view()), name='admin-courses'),
    #materias
    path('materias/', login_required(MateriaListView.as_view()), name='admin-materias'),
    #detalles
    path('courses/<int:pk>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('materia/<int:materia_id>/',login_required( materia_detail), name='materia_detail'),  # Detalle de la materia y estudiantes
    # CAMBIO DE CONTRASEÑA
    path('password_change/', login_required(ProfilePasswordChangeView.as_view()), name='profile_password_change'),
    # AGREGAR NUEVO USUARIO
    path('add_user/', login_required(AddUserView.as_view()), name='add_user'),
    path('get-materias/', GetMateriasByCourseView.as_view(), name='get_materias'),
    # NUEVO LOGIN
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    # VISUALIZAR EL PERFIL DE UN USUARIO
    path('user_details/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    # EDITAR DATOS DEL USUARIO
    path('superuser_edit/<int:user_id>/', login_required(superuser_edit), name='superuser_edit'),
    #genera pdf profesor
    path('generate_pdf/<int:materia_id>/', generate_pdf_student_list, name='generate_pdf_student_list'),
    #olvido su contraseña?
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #genera excel admin
    path('course/<int:course_id>/generate_excel/', generate_course_excel, name='generate_course_excel'),
    #acerda del cole
    path('unidad-educativa/', UnidadEducativaView.as_view(), name='unidad_educativa'),
    #registroprf -admin
    path('register-entry-exit/', login_required(RegisterEntryOrExitView.as_view()), name='register_entry_or_exit'),
    path('attendance-prof/', login_required(attendance_prof.as_view()), name='attendance_prof'),
    # path('attendance_report/', AttendanceReportView.as_view(), name='attendance_report'),
    #csv
    path('add-users-from-csv/', login_required(AddUsersFromCSVView.as_view()), name='add_users_from_csv'),
    # delete usuarios
    path('delete_user/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),  
    #horario
    path('horario/', login_required(HorarioView.as_view()), name='weekly_schedule'),
    # cambio de profesores por materia
    path('edit-materia/', MateriaEditView.as_view(), name='materia_edit'),
    #acerda del cole
    #subir pdf de horario
    path('upload/', login_required(views.upload_schedule), name='upload_schedule'),
    path('schedules/', login_required(views.ScheduleListView.as_view()), name='schedule_list'),
    path('schedule-detail/',login_required(ScheduleDetailView.as_view()), name='schedule_detail'),
    
    #descargar csv dede un curso
    path('generate_course_preview/<int:course_id>/', views.generate_course_preview, name='generate_course_preview'),
    path('download_course_csv/<int:course_id>/', views.download_course_csv, name='download_course_csv'),
    #sigiente curso

    path('generate-and-save-schedule-pdf/', views.generate_and_save_schedule_pdf, name='generate_and_save_schedule_pdf'),
    #ver notas estudent
    path('toggle-view-evolution/', ToggleViewEvolutionView.as_view(), name='toggle_view_evolution'),
    path('sin_permiso/',login_required(SinPermisoView.as_view()), name='SinPermiso'),
    #obtener alumnos course_detail
    path('get_course_students/<int:course_id>/', views.get_course_students, name='get_course_students'),
    # mover estudintes a otro curso
    path('move_students/', views.move_students_to_course, name='move_students'),
    path('get_available_courses/<int:current_course_id>/', views.get_available_courses, name='get_available_courses'),
    path('move-student/<int:course_id>/', MoveStudentView.as_view(), name='move_student'),
    #books
path('manage-books/', ManageBooksView.as_view(), name='manage_books'),
path('add-book/', AddBookView.as_view(), name='add_book'),
path('edit-book/<int:pk>/', EditBookView.as_view(), name='edit_book'),
path('delete-book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
path('view-books/', ViewBooksView.as_view(), name='view_books'),


]

