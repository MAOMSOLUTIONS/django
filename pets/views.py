from rest_framework import generics
from .models import User, Pet
from .serializers import UserSerializer, PetSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrAdmin

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_destroy(self, instance):
        # Lógica personalizada para eliminar un usuario
        instance.delete()


class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class UserPetsListView(generics.ListAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Pet.objects.filter(petowner__owner_id=user_id)

class PetUserAssociationView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
