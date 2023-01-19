from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionShortAnswerSerializer


class CategoryCreateListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs.get('category_id'))


class QuestionAnswerListCreateAPIView(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionShortAnswerSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['category', 'question']


class QuestionAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    def get_object(self):
        return get_object_or_404(QuestionAnswer, pk=self.kwargs.get('question_id'))




