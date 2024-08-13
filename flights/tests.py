from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Flight

class FlightTestCase(TestCase):
    def setUp(self):
        # Criando um grupo 'crew'
        crew_group = Group.objects.create(name='crew')
        
        # Criando um usuário de tripulação
        self.crew_user = User.objects.create_user(username='crew_member', password='test')
        self.crew_user.groups.add(crew_group)

        # Criando um voo de teste
        self.flight = Flight.objects.create(
            origin='São Paulo',
            destination='Rio de Janeiro',
            departure_time='2024-08-01 10:00:00',
            arrival_time='2024-08-01 12:00:00',
            created_by=self.crew_user
        )

    def test_flight_approval(self):
        # Logando como o usuário da tripulação
        self.client.login(username='crew_member', password='test')
        
        # Realizando a requisição de aprovação do voo
        response = self.client.post(f'/flights/{self.flight.id}/approve/')
        
        # Recarregando o voo do banco de dados
        self.flight.refresh_from_db()
        
        # Verificando se o voo foi aprovado
        self.assertTrue(self.flight.approved_by_crew)

    def test_flight_list_view(self):
        response = self.client.get('/flights/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.flight.origin)
