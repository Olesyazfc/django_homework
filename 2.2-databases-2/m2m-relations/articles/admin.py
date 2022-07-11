from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Category, ArticleCategory


class ArticleCategoryInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        for form in self.forms:
            if len(form.cleaned_data) > 0:
                if form.cleaned_data['is_main']:
                    count_main += 1

        if count_main == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if count_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ArticleCategoryInline(admin.TabularInline):
    model = ArticleCategory
    formset = ArticleCategoryInlineFormset


@admin.register(Category)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [ArticleCategoryInline]


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [ArticleCategoryInline]

