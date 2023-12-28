# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
    name = models.CharField('Nama', max_length=100)
    description = models.TextField('Deskripsi', blank=True)
    price = models.DecimalField('Harga', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    gambar_produk = models.ImageField(null=True, blank=True, upload_to="images/")
        

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
    
