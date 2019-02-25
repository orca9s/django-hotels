from django.db import models

property_type = (
    ('S', 'Sale'),
    ('R', 'rent'),
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    # integerfield와 같지만 양수 또는 0이어야된다.
    prices = models.PositiveIntegerField()
    # FloatField, DecimalField 둘다 실수를 나타내지 만 그 수를 다르게 표현,
    # Decimal은 소수로 표
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name


