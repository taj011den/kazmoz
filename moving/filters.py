import django_filters
from .models import Moving

class JobFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Moving
        fields = '__all__'
        exclude = ('image','exact','slug','published_at','vacancy', 'owner','salary')
        

def moving_list(request):
    filter = JobFilter(request.GET, queryset=Moving.objects.all())
    return render(request, 'my_app/template.html', {'filter': filter})