from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Student


class StudentView(object):
    model = Student

    def get_template_names(self):
        """Nest templates within student directory."""
        tpl = super(StudentView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'student'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class StudentDateView(StudentView):
    date_field = 'created_at'
    month_format = '%m'


class StudentBaseListView(StudentView):
    paginate_by = 10


class StudentArchiveIndexView(
    StudentDateView, StudentBaseListView, ArchiveIndexView):
    pass


class StudentCreateView(StudentView, CreateView):
    pass


class StudentDateDetailView(StudentDateView, DateDetailView):
    pass


class StudentDayArchiveView(
    StudentDateView, StudentBaseListView, DayArchiveView):
    pass


class StudentDeleteView(StudentView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_student_list')


class StudentDetailView(StudentView, DetailView):
    pass


class StudentListView(StudentBaseListView, ListView):
    pass


class StudentMonthArchiveView(
    StudentDateView, StudentBaseListView, MonthArchiveView):
    pass


class StudentTodayArchiveView(
    StudentDateView, StudentBaseListView, TodayArchiveView):
    pass


class StudentUpdateView(StudentView, UpdateView):
    pass


class StudentWeekArchiveView(
    StudentDateView, StudentBaseListView, WeekArchiveView):
    pass


class StudentYearArchiveView(
    StudentDateView, StudentBaseListView, YearArchiveView):
    make_object_list = True



