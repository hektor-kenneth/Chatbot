# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_hstore import hstore

class WebhookTransaction(models.Model):
    UNPROCESSED = 1
    PROCESSED = 2
    ERROR = 3

    STATUSES = (
        (UNPROCESSED, 'Unprocessed'),
        (PROCESSED, 'Processed'),
        (ERROR, 'Error'),
    )

    date_generated = models.DateTimeField()
    date_received = models.DateTimeField(default=timezone.now)
    body = hstore.SerializedDictionaryField()
    request_meta = hstore.SerializedDictionaryField()
    status = models.CharField(max_length=250, choices=STATUSES, default=UNPROCESSED)

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return u'{0}'.format(self.date_event_generated)


class Question(models.Model):
    Name = models.CharField(max_length=100, primary_key=True)
    PhoneNumber = models.IntegerField(max_length=8, unique=True)
    Email = models.EmailField(max_length=100)
    NRIC = models.VarChar(max_length=9)
