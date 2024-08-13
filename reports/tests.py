from django.test import TestCase
from .models import FlightReport

class FlightReportModelTest(TestCase):

    def test_creating_a_new_report(self):
        report = FlightReport.objects.create(
            total_flights=10,
            total_hours_flown=150.0,
            average_occupancy_rate=85.5
        )
        self.assertEqual(report.total_flights, 10)
        self.assertEqual(report.total_hours_flown, 150.0)
        self.assertEqual(report.average_occupancy_rate, 85.5)
