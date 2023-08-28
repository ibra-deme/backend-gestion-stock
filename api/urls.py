

from django.contrib import admin
from django.urls import path

from home.views import (
    CategorieListCreateView, CategorieDetailView,
    ClientListCreateView, ClientDetailView,
    FournisseurListCreateView, FournisseurDetailView,
    ProduitListCreateView, ProduitDetailView,
)

urlpatterns = [
    
   
    path('', CategorieListCreateView.as_view(), name='categorie-list'),
    path('categories/<int:pk>/', CategorieDetailView.as_view(), name='categorie-detail'),
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('fournisseurs/', FournisseurListCreateView.as_view(), name='fournisseur-list'),
    path('fournisseurs/<int:pk>/', FournisseurDetailView.as_view(), name='fournisseur-detail'),
    path('produits/', ProduitListCreateView.as_view(), name='produit-list'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
]