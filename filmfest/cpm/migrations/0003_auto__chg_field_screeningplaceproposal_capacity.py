# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ScreeningPlaceProposal.capacity'
        db.alter_column('cpm_screeningplaceproposal', 'capacity', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'ScreeningPlaceProposal.capacity'
        db.alter_column('cpm_screeningplaceproposal', 'capacity', self.gf('django.db.models.fields.CharField')(max_length=2))

    models = {
        'cpm.screeningplaceproposal': {
            'Meta': {'object_name': 'ScreeningPlaceProposal'},
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '110'}),
            'name_or_title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'proposals': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'screenings_amount': ('django.db.models.fields.CharField', [], {'max_length': '110', 'blank': 'True'}),
            'ticket_price': ('django.db.models.fields.CharField', [], {'max_length': '110'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'venue': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['cpm']