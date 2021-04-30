from django.views.generic import ListView
from .models import Brand, Line, Model


class BrandList(ListView):
    model = Brand
    template_name = 'brands.html'
    context_object_name = 'brands'


class LineList(ListView):
    model = Line
    context_object_name = 'lines'
    template_name = 'lines.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = self.kwargs.get('brand')
        return context

    def get_queryset(self):
        name_ = self.kwargs.get('brand')
        return Line.objects.filter(brand=Brand.objects.get(name=name_))


class ModelList(ListView):
    model = Model
    context_object_name = 'models'
    template_name = 'list_md.html'

    def get_queryset(self):
        line = self.kwargs.get('line')
        return Model.objects.filter(line=Line.objects.get(name=line))
