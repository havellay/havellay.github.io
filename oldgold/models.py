import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

class GoldPrice(models.Model):
    rate    = models.DecimalField(max_digits=25, decimal_places=10)
    def clean(self):
        validate_only_one_instance(self)

class Item(models.Model):
    # Member variables
    # need to figure out a way to show a compressed image in the index page
    # need to have a facility for multiple images
        # have another model named images and then associate that to Item?
    cover_img   = models.ImageField(upload_to = "oldgold/static/oldgold/images/products/" ) # find out how to get the static thing right
    description = models.CharField(max_length=200)
    weight      = models.DecimalField(max_digits=19, decimal_places=10)
    pub_date    = models.DateTimeField('date published')
    valid_for   = models.IntegerField('valid until')

    # Member methods
    def __str__(self):
        return self.description

    def is_item_available(self):
        if self.pub_date + datetime.timedelta(days=self.valid_for) > timezone.now():
            return False
        return True

    def price(self):
        # if there are more than one gold price entries, purge
        if len(GoldPrice.objects.all()) > 1:
            for x in GoldPrice.objects.all():
                x.clean()
        price = GoldPrice.objects.all()[0]
        return price.rate*self.weight*1.0

    def show_details(self):
        imgs = DetailImg.objects.filter(item = self.id)
        return True

class DetailImg(models.Model):
    item        = models.ForeignKey(Item)
    detail_img  = models.ImageField(upload_to = "images/products/")

