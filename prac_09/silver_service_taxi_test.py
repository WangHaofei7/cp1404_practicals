
"""
CP1404/CP5632 Practical
silver_service_taxi class test
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


silverservicetaxi = SilverServiceTaxi("My SilverServiceTaxi", 100, 2)
silverservicetaxi.drive(33)
print(silverservicetaxi)
print(silverservicetaxi.get_fare())