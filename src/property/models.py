from django.db import models

property_type = (
    ('sale', 'sale'),
    ('rent', 'rent'),
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    # integerfield와 같지만 양수 또는 0이어야된다.
    price = models.PositiveIntegerField()
    # FloatField, DecimalField 둘다 실수를 나타내지 만 그 수를 다르게 표현,
    # Decimal은 소수로 표시된다.
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # admin 사이트 상에서
        # Property를 Properties로 대체
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        # admin사이트 상에서
        # Category를 Categories로 대체
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name
