import django_filters
from .models import Main

class JobFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Main
        fields = '__all__'
        exclude = ('image','exact','slug','published_at','vacancy', 'owner','salary')
        

def main_list(request):
    filter = JobFilter(request.GET, queryset=Main.objects.all())
    return render(request, 'my_app/template.html', {'filter': filter})