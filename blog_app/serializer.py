from rest_framework import serializers
from .models import Blog, Category

def blog_title_valid(value):
    if len(value) < 4:
        raise serializers.ValidationError("Blog title is very short")

class BlogSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    blog_title = serializers.CharField(validators = [blog_title_valid])
    class Meta:
        model = Blog
        fields = '__all__'

    def validate(self, data):
        if data['blog_title'] == data['description']:
            raise serializers.ValidationError('blog title and description cannot be the same')
        else:
            return data
        
class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category_post = BlogSerializer(many=True, read_only=True)

    # String relatedfield
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = '__all__'