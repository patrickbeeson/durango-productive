from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Project, Asset


class AssetSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = Asset
        fields = (
            'pk',
            'description',
            'project',
            'art',
        )


class ProjectSerializer(serializers.ModelSerializer):
    project_detail = serializers.SerializerMethodField()
    assets = AssetSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'pk',
            'client_name',
            'slug',
            'description',
            'description_html',
            'lead_art',
            'completion_date',
            'project_detail',
            'assets',
        )

    def get_project_detail(self, obj):
        """Returns URI for object into the project_detail field"""
        request = self.context['request']
        return {
            'self': reverse_lazy(
                'portfolio_project_detail',
                kwargs={'slug': obj.slug},
                request=request,
            )
        }
