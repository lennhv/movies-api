from collections import OrderedDict

from rest_framework import serializers

from .models import Movie, Person, Alias

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        return self._choices[obj]
    
    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''
        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class AliasStringField(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return {"name": value}


class PersonObjectSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    sex = ChoiceField(choices=Person.SEX, read_only=True)

class MovieObjectSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    title = serializers.CharField(read_only=True)
    release_year = serializers.IntegerField(read_only=True)



class MovieSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_year', 'poster')
        read_only_fields = ('id',)

    def get_poster(self, obj):
        return str(obj)

    def create(self, validated_data):
        return self.Meta.model.\
            objects.add(**validated_data)
    
    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            update_instance(instance, validated_data)
 
class MovieDetailSerializer(serializers.ModelSerializer):
    directors = serializers.StringRelatedField(many=True, read_only=True)
    producers = serializers.StringRelatedField(many=True, read_only=True)
    casting = serializers.StringRelatedField(many=True, read_only=True)
    poster = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_year', 'poster','directors', 'producers', 'casting')
        read_only_fields = ('id',)
    
    def get_poster(self, obj):
        return str(obj)

class MovieDirectorsSerializer(serializers.ModelSerializer):
    directors = PersonObjectSerializer(many=True)
    name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ('name','directors')

    def get_name(self, obj):
        return str(obj)

    def update(self, instance, validated_data):
        return Movie.objects.\
            add_director(instance, validated_data)

class MovieProducersSerializer(serializers.ModelSerializer):
    producers = PersonObjectSerializer(many=True)
    name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ('name','producers')

    def get_name(self, obj):
        return str(obj)

    def update(self, instance, validated_data):
        return Movie.objects.\
            add_producer(instance, validated_data)

class MovieCastingSerializer(serializers.ModelSerializer):
    casting = PersonObjectSerializer(many=True)
    name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ('name','casting')

    def get_name(self, obj):
        return str(obj)

    def update(self, instance, validated_data):
        return Movie.objects.\
            add_casting(instance, validated_data)


class PersonSerializer(serializers.ModelSerializer):
    sex = ChoiceField(choices=Person.SEX)
    aliasses = AliasStringField(many=True, required=False)

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'sex', 'aliasses',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return self.Meta.model.\
            objects.add(**validated_data)

class PersonDetailSerializer(serializers.ModelSerializer):
    sex = ChoiceField(choices=Person.SEX)
    aliasses = AliasStringField(many=True, required=False)
    movies_as_director = serializers.StringRelatedField(many=True, read_only=True)
    movies_as_producer = serializers.StringRelatedField(many=True, read_only=True)
    movies_as_casting = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'sex', 'aliasses', 
            'movies_as_director', 'movies_as_producer', 'movies_as_casting')
        read_only_fields = ('id',)
    
    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            update_instance(instance, validated_data)

class PersonAliasSerializer(serializers.ModelSerializer):

    aliasses = AliasStringField(many=True, required=False)

    class Meta:
        model = Person
        fields = ('fullname', 'aliasses',)
        read_only_fields = ('fullname',)

    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            add_alias(instance, validated_data)

class PersonAsDirectorSerializer(serializers.ModelSerializer):
    movies = MovieObjectSerializer(many=True, source="movies_as_director")

    class Meta:
        model = Person
        fields = ('fullname', 'movies',)
        read_only_fields = ('fullname',)

    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            add_movie_as_director(instance, validated_data)

class PersonAsProducerSerializer(serializers.ModelSerializer):
    movies = MovieObjectSerializer(many=True, source="movies_as_producer")

    class Meta:
        model = Person
        fields = ('fullname', 'movies',)
        read_only_fields = ('fullname',)

    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            add_movie_as_producer(instance, validated_data)

class PersonAsCastingSerializer(serializers.ModelSerializer):
    movies = MovieObjectSerializer(many=True, source="movies_as_casting")

    class Meta:
        model = Person
        fields = ('fullname', 'movies',)
        read_only_fields = ('fullname',)

    def update(self, instance, validated_data):
        return self.Meta.model.objects.\
            add_movie_as_casting(instance, validated_data)
