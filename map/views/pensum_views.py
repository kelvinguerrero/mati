from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Pensum


class PensumView(object):
    model = Pensum

    def get_template_names(self):
        """Nest templates within pensum directory."""
        tpl = super(PensumView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'pensum'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class PensumDateView(PensumView):
    date_field = 'created_at'
    month_format = '%m'


class PensumBaseListView(PensumView):
    paginate_by = 10


class PensumArchiveIndexView(
    PensumDateView, PensumBaseListView, ArchiveIndexView):
    pass


class PensumCreateView(PensumView, CreateView):
    pass


class PensumDateDetailView(PensumDateView, DateDetailView):
    pass


class PensumDayArchiveView(
    PensumDateView, PensumBaseListView, DayArchiveView):
    pass


class PensumDeleteView(PensumView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_pensum_list')


class PensumDetailView(PensumView, DetailView):
    pass


class PensumListView(PensumBaseListView, ListView):
    pass


class PensumMonthArchiveView(
    PensumDateView, PensumBaseListView, MonthArchiveView):
    pass


class PensumTodayArchiveView(
    PensumDateView, PensumBaseListView, TodayArchiveView):
    pass


class PensumUpdateView(PensumView, UpdateView):
    pass


class PensumWeekArchiveView(
    PensumDateView, PensumBaseListView, WeekArchiveView):
    pass


class PensumYearArchiveView(
    PensumDateView, PensumBaseListView, YearArchiveView):
    make_object_list = True



