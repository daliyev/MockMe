from django.contrib import admin
from .models import Subject, SubjectQuestion, QuestionOption, SubjectTest, SpecialQuestionOption, SpecialSubjectQuestion, SpecialSubject, SpecialSubjectTest, dtmtests, StudentTest, DtmDirection


class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 4
    fields = ['text', 'is_answer']


class SpecialQuestionOptionInline(admin.TabularInline):
    model = SpecialQuestionOption
    extra = 4
    fields = ['text', 'is_answer']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'name']
    search_fields = ['subject_code', 'name']


@admin.register(SpecialSubject)
class SpecialSubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'name']
    search_fields = ['subject_code', 'name']


@admin.register(SubjectQuestion)
class SubjectQuestionAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'question_no', 'text']
    list_filter = ['subject_code']
    search_fields = ['text']
    inlines = [QuestionOptionInline]


@admin.register(SpecialSubjectQuestion)
class SubjectQuestionAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'question_no', 'text']
    list_filter = ['subject_code']
    search_fields = ['text']
    inlines = [SpecialQuestionOptionInline]


@admin.register(dtmtests)
class dtmtestsAdmin(admin.ModelAdmin):
    list_display = ['dtmtest_code']
    search_fields = ['dtmtest_code']
    filter_horizontal = ['sp_subjeccttest', 'subjecttest']


# @admin.register(QuestionOption)
# class QuestionOptionAdmin(admin.ModelAdmin):
#     list_display = ['question_no', 'is_answer', 'text']
#     list_filter = ['question_no']
#     search_fields = ['text']


@admin.register(SubjectTest)
class SubjectTestAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'test_code', 'chosen_questions_count')
    search_fields = ('subject_code__name', 'test_code')

    raw_id_fields = ('subject_code',)
    filter_horizontal = ('questions',)

    def chosen_questions_count(self, obj):
        return obj.questions.count()
    chosen_questions_count.short_description = 'Chosen Questions Count'


@admin.register(SpecialSubjectTest)
class SpecialSubjectTestAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'test_code', 'chosen_questions_count')
    search_fields = ('subject_code__name', 'test_code')

    raw_id_fields = ('subject_code',)
    filter_horizontal = ('questions',)

    def chosen_questions_count(self, obj):
        return obj.questions.count()
    chosen_questions_count.short_description = 'Chosen Questions Count'


# class SubjectTestAdmin(admin.ModelAdmin):
#     list_display = ['subject_code', 'test_code']
#     list_filter = ['subject_code']
#     search_fields = ['test_code']
#
#     raw_id_fields = ('subject_code',)
#     filter_horizontal = ('questions',)
# #
# @admin.register(TestQuestion)
# class TestQuestionAdmin(admin.ModelAdmin):
#     list_display = ['test_code', 'question_no']
#     list_filter = ['test_code']
#
#     # def save_model(self, request, obj, form, change):


@admin.register(StudentTest)
class StudentTestAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'point', 'test_code', 'date']
    list_filter = ['test_code', 'date']
    search_fields = ['student_id', 'test_code']

# @admin.register(StudentResponse)
# class StudentResponseAdmin(admin.ModelAdmin):
#     list_display = ['student_id', 'subject_code', 'test_code', 'question_no', 'option_no']
#     list_filter = ['subject_code', 'test_code', 'question_no', 'option_no']
#     search_fields = ['student_id']


@admin.register(DtmDirection)
class DtmDirectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
