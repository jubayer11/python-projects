from django.contrib import admin
from basic_app.models import School, Student
from django.utils import timezone


class SchoolAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'principa', 'location', 'slug', 'is_valid', 'date_created', 'last_modified', 'days_since_creation')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 2
    actions = ('set_blogs_to_publish',)
    fields = (('name', 'location',), 'slug')

    def days_since_creation(self, School):
        diff = timezone.now() - School.date_created
        return diff.days
    days_since_creation.short_description ='count'

    def set_blogs_to_publish(self, request, queryset):
        count = queryset.update(is_valid=1)
        self.message_user(request, '{} have completed'.format(count))

    set_blogs_to_publish.short_description = 'Mark Selected'


# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Student)
