from django.db import models
from django.db.models import fields
from rest_framework import serializers
from watchlist_app.models  import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ("watchlist",)
        #fields = "__all__"
        


class WatchListSerializer(serializers.ModelSerializer):
    #reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source="platform.name")

    class Meta:
        model = WatchList
        fields = "__all__"



# class StreamPlatformSerializer(serializers.ModelSerializer): #serializers.HyperlinkedModelSerializer
#     watchlist = WatchListSerializer(many=True, read_only=True)

#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"





# class WatchListSerializer(serializers.ModelSerializer):
#     #name_len = serializers.SerializerMethodField()
#     class Meta:
#         model = WatchList
#         fields = "__all__"
        #fields = ["id", "name", "description"]
        #exclude = ['active']
        
    # def get_name_len(self,object):
    #     return len(object.name)

    # # Object Level Validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be diferent!")
    #     return data

    ##Filed Level Validation
    # def validate_name(self, value):
    #     if len(value) <2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value

# # Validators
# def name_length(value):
#     if len(value) <2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validates_data):
#         return Movie.objects.create(**validates_data)
    
#     def update(self,instance, validates_data):
#         instance.name=  validates_data.get('name', instance.name)
#         instance.description=  validates_data.get('description', instance.description)
#         instance.active= validates_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be diferent!")
#         return data


    # Filed Level Validation
    # def validate_name(self, value):
    #     if len(value) <2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value

    