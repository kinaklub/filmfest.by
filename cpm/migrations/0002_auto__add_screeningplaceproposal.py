# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScreeningPlaceProposal'
        db.create_table('cpm_screeningplaceproposal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_or_title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=110)),
            ('venue', self.gf('django.db.models.fields.TextField')()),
            ('capacity', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('ticket_price', self.gf('django.db.models.fields.CharField')(max_length=110)),
            ('screenings_amount', self.gf('django.db.models.fields.CharField')(max_length=110, blank=True)),
            ('proposals', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('cpm', ['ScreeningPlaceProposal'])


    def backwards(self, orm):
        # Deleting model 'ScreeningPlaceProposal'
        db.delete_table('cpm_screeningplaceproposal')


    models = {
        'cpm.screeningplaceproposal': {
            'Meta': {'object_name': 'ScreeningPlaceProposal'},
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
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