from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from review.models import Alcohol_Review, Brewery_Review, Event_Review
from review.serializers import ReviewSerializer, ReviewCreateSerializer, ReviewListSerializer



# Create your views here.
class Alcohol_ReviewView(APIView):
    def get(self, request):
        alc_reviews = Alcohol_Review.objects.all()
        serializer = ReviewListSerializer(alc_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        # print(request.user)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Brewery_ReviewView(APIView):
    def get(self, request):
        bre_reviews = Brewery_Review.objects.all()
        serializer = ReviewListSerializer(bre_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        # print(request.user)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Event_ReviewView(APIView):
    def get(self, request):
        eve_reviews = Event_Review.objects.all()
        serializer = ReviewListSerializer(eve_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        # print(request.user)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        # if request.user == review.user:
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        # if request.user == review.user:
        #     review.delete()
        #     return Response("삭제되었습니다.", status=status.HTTP_204_NO_CONTENT)
        # else:
        #     return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    
class CommentView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    
class CommentDetailView(APIView):
    def put(self, request):
        pass
    def delete(self, request):
        pass
    
class LikeView(APIView):
    def post(self, request):
        pass