# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Submission'
        db.create_table('cpm2013_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('section', self.gf('django.db.models.fields.IntegerField')()),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('aspect_ratio', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('premiere', self.gf('django.db.models.fields.IntegerField')()),
            ('film_awards', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('director_awards', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('budget', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('attend', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('backlink', self.gf('django.db.models.fields.IntegerField')()),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('director_address', self.gf('django.db.models.fields.TextField')()),
            ('director_email', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('director_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('director_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('producer', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('producer_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('producer_email', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('producer_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('producer_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('screenwriter', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('music', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('director_photography', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('owner_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('owner_email', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('owner_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('owner_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('distributor', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('distributor_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('distributor_email', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('distributor_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('distributor_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('allow_tv', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('allow_noncommercial', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('allow_network', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('applicant', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('applicant_address', self.gf('django.db.models.fields.TextField')()),
            ('applicant_email', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('applicant_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('applicant_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('cpm2013', ['Submission'])

        # Adding model 'NewsEntryTranslation'
        db.create_table('cpm2013_newsentry_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_text', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['cpm2013.NewsEntry'])),
        ))
        db.send_create_signal('cpm2013', ['NewsEntryTranslation'])

        # Adding unique constraint on 'NewsEntryTranslation', fields ['language_code', 'master']
        db.create_unique('cpm2013_newsentry_translation', ['language_code', 'master_id'])

        # Adding model 'NewsEntry'
        db.create_table('cpm2013_newsentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cpm2013', ['NewsEntry'])

        # Adding model 'PageTranslation'
        db.create_table('cpm2013_page_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['cpm2013.Page'])),
        ))
        db.send_create_signal('cpm2013', ['PageTranslation'])

        # Adding unique constraint on 'PageTranslation', fields ['language_code', 'master']
        db.create_unique('cpm2013_page_translation', ['language_code', 'master_id'])

        # Adding model 'Page'
        db.create_table('cpm2013_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('cpm2013', ['Page'])


    def backwards(self, orm):
        # Removing unique constraint on 'PageTranslation', fields ['language_code', 'master']
        db.delete_unique('cpm2013_page_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'NewsEntryTranslation', fields ['language_code', 'master']
        db.delete_unique('cpm2013_newsentry_translation', ['language_code', 'master_id'])

        # Deleting model 'Submission'
        db.delete_table('cpm2013_submission')

        # Deleting model 'NewsEntryTranslation'
        db.delete_table('cpm2013_newsentry_translation')

        # Deleting model 'NewsEntry'
        db.delete_table('cpm2013_newsentry')

        # Deleting model 'PageTranslation'
        db.delete_table('cpm2013_page_translation')

        # Deleting model 'Page'
        db.delete_table('cpm2013_page')


    models = {
        'cpm2013.newsentry': {
            'Meta': {'object_name': 'NewsEntry'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cpm2013.newsentrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsEntryTranslation', 'db_table': "'cpm2013_newsentry_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['cpm2013.NewsEntry']"}),
            'short_text': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cpm2013.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'cpm2013.pagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PageTranslation', 'db_table': "'cpm2013_page_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['cpm2013.Page']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cpm2013.submission': {
            'Meta': {'object_name': 'Submission'},
            'allow_network': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'allow_noncommercial': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'allow_tv': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'applicant': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'applicant_address': ('django.db.models.fields.TextField', [], {}),
            'applicant_email': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'applicant_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'applicant_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'aspect_ratio': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'attend': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'backlink': ('django.db.models.fields.IntegerField', [], {}),
            'budget': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'director_address': ('django.db.models.fields.TextField', [], {}),
            'director_awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'director_email': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'director_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'director_photography': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'director_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'distributor': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'distributor_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'distributor_email': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'distributor_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'distributor_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'film_awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'music': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'owner_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner_email': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'owner_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'owner_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'premiere': ('django.db.models.fields.IntegerField', [], {}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'producer_email': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'screenwriter': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'section': ('django.db.models.fields.IntegerField', [], {}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['cpm2013']