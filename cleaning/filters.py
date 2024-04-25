import django_filters
from .models import Cleaning

class JobFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Cleaning
        fields = '__all__'
        exclude = ('image','exact','slug','published_at','vacancy', 'owner','salary')
        

def cleaning_list(request):
    filter = JobFilter(request.GET, queryset=Cleaning.objects.all())
    return render(request, 'my_app/template.html', {'filter': filter})