from rest_framework import serializers
from .models import Language

class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        # mode to use
        model = Language
        # fields to be displayed
        fields = ('url','id','name', 'paradigm')

