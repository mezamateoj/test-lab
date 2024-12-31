
from rest_framework import viewsets
from sets import models
from sets import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SetsAllView(APIView):
    """GET all Sets in the db"""

    serializer_class = serializers.SetsSetializer
    # queryset = models.Set.objects.all().order_by('-release_date')
    def get(self, request):
        try:
            sets = models.Set.objects.all().order_by('-release_date')
            serializer = self.serializer_class(sets, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class SetsCardsView(APIView):
    """GET all cards in a set"""

    serializer_class = serializers.CardsSetializer

    def get(self, request, id: str = None):
        try:
            if not models.Set.objects.filter(id=id).exists():
                return Response(
                    {"error": f'Set {id} not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            cards = models.Card.objects.filter(set=id)

            if not cards.exists():
                return Response(
                    {"error": f"No cards found for set {id}"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = self.serializer_class(cards, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class CardsViewSet(APIView):
    """View to sets"""

    serializer_class = serializers.CardsSetializer

    def get(self, request, id: str):
        """GET a card by id"""
        try:
            card = models.Card.objects.get(id=id)
            serializer = self.serializer_class(card)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except models.Card.DoesNotExist:
            return Response(
                {"error": f"Card {id} not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
