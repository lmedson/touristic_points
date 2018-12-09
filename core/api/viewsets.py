from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import TouristAttraction
from .serializers import TouristAttractionSerializer


class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristAttractionSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = TouristAttraction.objects.all()

        if id:
            queryset = TouristAttraction.objects.filter(pk=id)

        if name:
            queryset = queryset.filter(name__iexact=name)

        if description:
            queryset = queryset.filter(description__iexact=description)

        print(queryset, 'okokok')
        return queryset

    def list(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def report(self, request, pk=None):
        return super(TouristAttractionViewSet, self).report(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def check(self, request):
        return super(TouristAttractionViewSet, self).check(request, *args, **kwargs)
