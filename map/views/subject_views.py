from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Subject


class SubjectView(object):
    model = Subject

    def get_template_names(self):
        """Nest templates within subject directory."""
        tpl = super(SubjectView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'subject'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class SubjectDateView(SubjectView):
    date_field = 'created_at'
    month_format = '%m'


class SubjectBaseListView(SubjectView):
    paginate_by = 10


class SubjectArchiveIndexView(
    SubjectDateView, SubjectBaseListView, ArchiveIndexView):
    pass


class SubjectCreateView(SubjectView, CreateView):
    pass


class SubjectDateDetailView(SubjectDateView, DateDetailView):
    pass


class SubjectDayArchiveView(
    SubjectDateView, SubjectBaseListView, DayArchiveView):
    pass


class SubjectDeleteView(SubjectView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_subject_list')


class SubjectDetailView(SubjectView, DetailView):
    pass


class SubjectListView(SubjectBaseListView, ListView):
    pass


class SubjectMonthArchiveView(
    SubjectDateView, SubjectBaseListView, MonthArchiveView):
    pass


class SubjectTodayArchiveView(
    SubjectDateView, SubjectBaseListView, TodayArchiveView):
    pass


class SubjectUpdateView(SubjectView, UpdateView):
    pass


class SubjectWeekArchiveView(
    SubjectDateView, SubjectBaseListView, WeekArchiveView):
    pass


class SubjectYearArchiveView(
    SubjectDateView, SubjectBaseListView, YearArchiveView):
    make_object_list = True



