from rest_framework import serializers

from users.models import MyUser
from . models import Tournament


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'bio']


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = '__all__'


class TournamentDetailSerializer(TournamentSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['participants'] = ParticipantSerializer(instance.participants, many=True, context=self.context).data
        return representation


class ChampionSerializer(serializers.Serializer):
    champion = serializers.PrimaryKeyRelatedField(read_only=True)
    tournament = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['champion'] = ParticipantSerializer(instance.champion, context=self.context).data
        representation['tournament'] = TournamentDetailSerializer(instance.tournament, context=self.context). data
        return representation


class GallerySerializer(serializers.Serializer):
    image = serializers.ImageField()
