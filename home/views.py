from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Categorie, Client, Fournisseur, Produit
from .serializers import CategorieSerializer, ClientSerializer, FournisseurSerializer, ProduitSerializer

@api_view(['GET'])
def index(request):
    courses={
        'course_name':'python',
        'learn':['flask','django','tornado'],
        'course_provider':'scaler'
    }  
    print("GET Method")
    return  Response(courses)
class CategorieListCreateView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class FournisseurListCreateView(generics.ListCreateAPIView):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class FournisseurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class ProduitListCreateView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer        