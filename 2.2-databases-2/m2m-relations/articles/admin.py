from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len([form for form in self.forms if form.cleaned_data.get('is_main')]) > 1:
            raise ValidationError('Проверка не прошла')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
