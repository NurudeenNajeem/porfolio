from django.contrib import admin

from .models import Project,WorkExperience,Education,Post

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "description","url","image"]
    search_fields = ["title","description"]
    list_filter = ["title","description"]
    list_per_page = 10
    list_filter = ["description","url","image"]


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ["title", "description","company"]
    search_fields = ["title","description","company"]
    

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["title", "description","education_level","start_date",'end_date']
    search_fields = ["title","education_level"]
    list_filter = ["title"]
    list_per_page = 10


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","phone_number","message","date"]
    search_fields = ["name","email"]
    list_filter = ["name","email"]
    list_per_page = 10
