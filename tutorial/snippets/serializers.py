from rest_framework import fields, serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES,Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.HyperlinkedIdentityField(view_name='snippet-highlight')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlighted', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='snippet-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']