from Article.models import Article
from rest_framework import serializers

class ArticleSeiralizer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self,verified_data):
        return Article.objects.create(**verified_data)

