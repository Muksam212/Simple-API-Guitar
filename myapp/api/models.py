from django.db import models

# Create your models here.
class DateTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Band(DateTimeStamp):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='band/logo', null=True, blank=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = "Bands"

    def __str__(self):
        return "{}".format(self.name)


class BandMember(DateTimeStamp):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name = "band_members")
    image = models.ImageField(upload_to='band/member', blank=True, null=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = "BandMembers"

    def __str__(self):
        return "{}".format(self.name)

class Guitar(DateTimeStamp):
    GUITAR = (
        ('Acoustic','Acoustic'),
        ('Electric','Electric'),
        ('Bass','Bass')
    )
    name = models.CharField(max_length=40, choices=GUITAR)
    member = models.ForeignKey(BandMember, on_delete=models.CASCADE, related_name="guitars")

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Guitars"
    
    def __str__(self):
        return "{}".format(self.name)