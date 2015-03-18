from django.contrib import admin
from polls.models import Question, Choice 

class ChoiceInline(admin.StackedInline):
	model=Choice
	extra=3

class QuestionAdmin(admin.ModelAdmin):
	# fields=['pub_date','question_text']
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
	('Text Information',	{'fields':['question_text']}),
	('Date Information',	{'fields':['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_filter=['pub_date']
	search_fields=['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)