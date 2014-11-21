from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Teacher


class TeacherView(object):
    model = Teacher

    def get_template_names(self):
        """Nest templates within teacher directory."""
        tpl = super(TeacherView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class TeacherDateView(TeacherView):
    date_field = 'created_at'
    month_format = '%m'


class TeacherBaseListView(TeacherView):
    paginate_by = 10


class TeacherArchiveIndexView(
    TeacherDateView, TeacherBaseListView, ArchiveIndexView):
    pass


class TeacherCreateView(TeacherView, CreateView):
    pass


class TeacherDateDetailView(TeacherDateView, DateDetailView):
    pass


class TeacherDayArchiveView(
    TeacherDateView, TeacherBaseListView, DayArchiveView):
    pass


class TeacherDeleteView(TeacherView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_teacher_list')


class TeacherDetailView(TeacherView, DetailView):
    pass


class TeacherListView(TeacherBaseListView, ListView):
    pass


class TeacherMonthArchiveView(
    TeacherDateView, TeacherBaseListView, MonthArchiveView):
    pass


class TeacherTodayArchiveView(
    TeacherDateView, TeacherBaseListView, TodayArchiveView):
    pass


class TeacherUpdateView(TeacherView, UpdateView):
    pass


class TeacherWeekArchiveView(
    TeacherDateView, TeacherBaseListView, WeekArchiveView):
    pass


class TeacherYearArchiveView(
    TeacherDateView, TeacherBaseListView, YearArchiveView):
    make_object_list = True



