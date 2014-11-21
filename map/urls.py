from django.conf.urls import patterns, url



from map.views.pensum_views import *
urlpatterns = patterns('',
    url(
        regex=r'^pensum/archive/$',
        view=PensumArchiveIndexView.as_view(),
        name='map_pensum_archive_index'
    ),
    url(
        regex=r'^pensum/create/$',
        view=PensumCreateView.as_view(),
        name='map_pensum_create'
    ),
    url(
        regex=r'^pensum/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=PensumDateDetailView.as_view(),
        name='map_pensum_date_detail'
    ),
    url(
        regex=r'^pensum/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=PensumDayArchiveView.as_view(),
        name='map_pensum_day_archive'
    ),
    url(
        regex=r'^pensum/(?P<pk>\d+?)/delete/$',
        view=PensumDeleteView.as_view(),
        name='map_pensum_delete'
    ),
    url(
        regex=r'^pensum/(?P<pk>\d+?)/$',
        view=PensumDetailView.as_view(),
        name='map_pensum_detail'
    ),
    url(
        regex=r'^pensum/$',
        view=PensumListView.as_view(),
        name='map_pensum_list'
    ),
    url(
        regex=r'^pensum/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=PensumMonthArchiveView.as_view(),
        name='map_pensum_month_archive'
    ),
    url(
        regex=r'^pensum/today/$',
        view=PensumTodayArchiveView.as_view(),
        name='map_pensum_today_archive'
    ),
    url(
        regex=r'^pensum/(?P<pk>\d+?)/update/$',
        view=PensumUpdateView.as_view(),
        name='map_pensum_update'
    ),
    url(
        regex=r'^pensum/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=PensumWeekArchiveView.as_view(),
        name='map_pensum_week_archive'
    ),
    url(
        regex=r'^pensum/archive/(?P<year>\d{4})/$',
        view=PensumYearArchiveView.as_view(),
        name='map_pensum_year_archive'
    ),
)


from map.views.teacher_views import *
urlpatterns += patterns('',
    url(
        regex=r'^teacher/archive/$',
        view=TeacherArchiveIndexView.as_view(),
        name='map_teacher_archive_index'
    ),
    url(
        regex=r'^teacher/create/$',
        view=TeacherCreateView.as_view(),
        name='map_teacher_create'
    ),
    url(
        regex=r'^teacher/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=TeacherDateDetailView.as_view(),
        name='map_teacher_date_detail'
    ),
    url(
        regex=r'^teacher/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=TeacherDayArchiveView.as_view(),
        name='map_teacher_day_archive'
    ),
    url(
        regex=r'^teacher/(?P<pk>\d+?)/delete/$',
        view=TeacherDeleteView.as_view(),
        name='map_teacher_delete'
    ),
    url(
        regex=r'^teacher/(?P<pk>\d+?)/$',
        view=TeacherDetailView.as_view(),
        name='map_teacher_detail'
    ),
    url(
        regex=r'^teacher/$',
        view=TeacherListView.as_view(),
        name='map_teacher_list'
    ),
    url(
        regex=r'^teacher/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=TeacherMonthArchiveView.as_view(),
        name='map_teacher_month_archive'
    ),
    url(
        regex=r'^teacher/today/$',
        view=TeacherTodayArchiveView.as_view(),
        name='map_teacher_today_archive'
    ),
    url(
        regex=r'^teacher/(?P<pk>\d+?)/update/$',
        view=TeacherUpdateView.as_view(),
        name='map_teacher_update'
    ),
    url(
        regex=r'^teacher/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=TeacherWeekArchiveView.as_view(),
        name='map_teacher_week_archive'
    ),
    url(
        regex=r'^teacher/archive/(?P<year>\d{4})/$',
        view=TeacherYearArchiveView.as_view(),
        name='map_teacher_year_archive'
    ),
)


from map.views.student_views import *
urlpatterns += patterns('',
    url(
        regex=r'^student/archive/$',
        view=StudentArchiveIndexView.as_view(),
        name='map_student_archive_index'
    ),
    url(
        regex=r'^student/create/$',
        view=StudentCreateView.as_view(),
        name='map_student_create'
    ),
    url(
        regex=r'^student/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=StudentDateDetailView.as_view(),
        name='map_student_date_detail'
    ),
    url(
        regex=r'^student/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=StudentDayArchiveView.as_view(),
        name='map_student_day_archive'
    ),
    url(
        regex=r'^student/(?P<pk>\d+?)/delete/$',
        view=StudentDeleteView.as_view(),
        name='map_student_delete'
    ),
    url(
        regex=r'^student/(?P<pk>\d+?)/$',
        view=StudentDetailView.as_view(),
        name='map_student_detail'
    ),
    url(
        regex=r'^student/$',
        view=StudentListView.as_view(),
        name='map_student_list'
    ),
    url(
        regex=r'^student/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=StudentMonthArchiveView.as_view(),
        name='map_student_month_archive'
    ),
    url(
        regex=r'^student/today/$',
        view=StudentTodayArchiveView.as_view(),
        name='map_student_today_archive'
    ),
    url(
        regex=r'^student/(?P<pk>\d+?)/update/$',
        view=StudentUpdateView.as_view(),
        name='map_student_update'
    ),
    url(
        regex=r'^student/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=StudentWeekArchiveView.as_view(),
        name='map_student_week_archive'
    ),
    url(
        regex=r'^student/archive/(?P<year>\d{4})/$',
        view=StudentYearArchiveView.as_view(),
        name='map_student_year_archive'
    ),
)


from map.views.course_views import *
urlpatterns += patterns('',
    url(
        regex=r'^course/archive/$',
        view=CourseArchiveIndexView.as_view(),
        name='map_course_archive_index'
    ),
    url(
        regex=r'^course/create/$',
        view=CourseCreateView.as_view(),
        name='map_course_create'
    ),
    url(
        regex=r'^course/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=CourseDateDetailView.as_view(),
        name='map_course_date_detail'
    ),
    url(
        regex=r'^course/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=CourseDayArchiveView.as_view(),
        name='map_course_day_archive'
    ),
    url(
        regex=r'^course/(?P<pk>\d+?)/delete/$',
        view=CourseDeleteView.as_view(),
        name='map_course_delete'
    ),
    url(
        regex=r'^course/(?P<pk>\d+?)/$',
        view=CourseDetailView.as_view(),
        name='map_course_detail'
    ),
    url(
        regex=r'^course/$',
        view=CourseListView.as_view(),
        name='map_course_list'
    ),
    url(
        regex=r'^course/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=CourseMonthArchiveView.as_view(),
        name='map_course_month_archive'
    ),
    url(
        regex=r'^course/today/$',
        view=CourseTodayArchiveView.as_view(),
        name='map_course_today_archive'
    ),
    url(
        regex=r'^course/(?P<pk>\d+?)/update/$',
        view=CourseUpdateView.as_view(),
        name='map_course_update'
    ),
    url(
        regex=r'^course/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=CourseWeekArchiveView.as_view(),
        name='map_course_week_archive'
    ),
    url(
        regex=r'^course/archive/(?P<year>\d{4})/$',
        view=CourseYearArchiveView.as_view(),
        name='map_course_year_archive'
    ),
)


from map.views.section_views import *
urlpatterns += patterns('',
    url(
        regex=r'^section/archive/$',
        view=SectionArchiveIndexView.as_view(),
        name='map_section_archive_index'
    ),
    url(
        regex=r'^section/create/$',
        view=SectionCreateView.as_view(),
        name='map_section_create'
    ),
    url(
        regex=r'^section/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=SectionDateDetailView.as_view(),
        name='map_section_date_detail'
    ),
    url(
        regex=r'^section/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=SectionDayArchiveView.as_view(),
        name='map_section_day_archive'
    ),
    url(
        regex=r'^section/(?P<pk>\d+?)/delete/$',
        view=SectionDeleteView.as_view(),
        name='map_section_delete'
    ),
    url(
        regex=r'^section/(?P<pk>\d+?)/$',
        view=SectionDetailView.as_view(),
        name='map_section_detail'
    ),
    url(
        regex=r'^section/$',
        view=SectionListView.as_view(),
        name='map_section_list'
    ),
    url(
        regex=r'^section/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=SectionMonthArchiveView.as_view(),
        name='map_section_month_archive'
    ),
    url(
        regex=r'^section/today/$',
        view=SectionTodayArchiveView.as_view(),
        name='map_section_today_archive'
    ),
    url(
        regex=r'^section/(?P<pk>\d+?)/update/$',
        view=SectionUpdateView.as_view(),
        name='map_section_update'
    ),
    url(
        regex=r'^section/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=SectionWeekArchiveView.as_view(),
        name='map_section_week_archive'
    ),
    url(
        regex=r'^section/archive/(?P<year>\d{4})/$',
        view=SectionYearArchiveView.as_view(),
        name='map_section_year_archive'
    ),
)


from map.views.subject_views import *
urlpatterns += patterns('',
    url(
        regex=r'^subject/archive/$',
        view=SubjectArchiveIndexView.as_view(),
        name='map_subject_archive_index'
    ),
    url(
        regex=r'^subject/create/$',
        view=SubjectCreateView.as_view(),
        name='map_subject_create'
    ),
    url(
        regex=r'^subject/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=SubjectDateDetailView.as_view(),
        name='map_subject_date_detail'
    ),
    url(
        regex=r'^subject/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=SubjectDayArchiveView.as_view(),
        name='map_subject_day_archive'
    ),
    url(
        regex=r'^subject/(?P<pk>\d+?)/delete/$',
        view=SubjectDeleteView.as_view(),
        name='map_subject_delete'
    ),
    url(
        regex=r'^subject/(?P<pk>\d+?)/$',
        view=SubjectDetailView.as_view(),
        name='map_subject_detail'
    ),
    url(
        regex=r'^subject/$',
        view=SubjectListView.as_view(),
        name='map_subject_list'
    ),
    url(
        regex=r'^subject/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=SubjectMonthArchiveView.as_view(),
        name='map_subject_month_archive'
    ),
    url(
        regex=r'^subject/today/$',
        view=SubjectTodayArchiveView.as_view(),
        name='map_subject_today_archive'
    ),
    url(
        regex=r'^subject/(?P<pk>\d+?)/update/$',
        view=SubjectUpdateView.as_view(),
        name='map_subject_update'
    ),
    url(
        regex=r'^subject/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=SubjectWeekArchiveView.as_view(),
        name='map_subject_week_archive'
    ),
    url(
        regex=r'^subject/archive/(?P<year>\d{4})/$',
        view=SubjectYearArchiveView.as_view(),
        name='map_subject_year_archive'
    ),
)