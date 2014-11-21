from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from map.models import Course


class CourseView(object):
    model = Course

    def get_template_names(self):
        """Nest templates within course directory."""
        tpl = super(CourseView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'course'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class CourseDateView(CourseView):
    date_field = 'created_at'
    month_format = '%m'


class CourseBaseListView(CourseView):
    paginate_by = 10


class CourseArchiveIndexView(
    CourseDateView, CourseBaseListView, ArchiveIndexView):
    pass


class CourseCreateView(CourseView, CreateView):
    pass


class CourseDateDetailView(CourseDateView, DateDetailView):
    pass


class CourseDayArchiveView(
    CourseDateView, CourseBaseListView, DayArchiveView):
    pass


class CourseDeleteView(CourseView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map_course_list')


class CourseDetailView(CourseView, DetailView):
    pass


class CourseListView(CourseBaseListView, ListView):
    pass


class CourseMonthArchiveView(
    CourseDateView, CourseBaseListView, MonthArchiveView):
    pass


class CourseTodayArchiveView(
    CourseDateView, CourseBaseListView, TodayArchiveView):
    pass


class CourseUpdateView(CourseView, UpdateView):
    pass


class CourseWeekArchiveView(
    CourseDateView, CourseBaseListView, WeekArchiveView):
    pass


class CourseYearArchiveView(
    CourseDateView, CourseBaseListView, YearArchiveView):
    make_object_list = True



