from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Section


class SectionView(object):
    model = Section

    def get_template_names(self):
        """Nest templates within section directory."""
        tpl = super(SectionView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'section'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class SectionDateView(SectionView):
    date_field = 'created_at'
    month_format = '%m'


class SectionBaseListView(SectionView):
    paginate_by = 10


class SectionArchiveIndexView(
    SectionDateView, SectionBaseListView, ArchiveIndexView):
    pass


class SectionCreateView(SectionView, CreateView):
    pass


class SectionDateDetailView(SectionDateView, DateDetailView):
    pass


class SectionDayArchiveView(
    SectionDateView, SectionBaseListView, DayArchiveView):
    pass


class SectionDeleteView(SectionView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_section_list')


class SectionDetailView(SectionView, DetailView):
    pass


class SectionListView(SectionBaseListView, ListView):
    pass


class SectionMonthArchiveView(
    SectionDateView, SectionBaseListView, MonthArchiveView):
    pass


class SectionTodayArchiveView(
    SectionDateView, SectionBaseListView, TodayArchiveView):
    pass


class SectionUpdateView(SectionView, UpdateView):
    pass


class SectionWeekArchiveView(
    SectionDateView, SectionBaseListView, WeekArchiveView):
    pass


class SectionYearArchiveView(
    SectionDateView, SectionBaseListView, YearArchiveView):
    make_object_list = True



