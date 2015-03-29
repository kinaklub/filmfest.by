# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('events_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'])),
        ))
        db.send_create_signal('events', ['Place'])

        # Adding model 'CityTranslation'
        db.create_table('events_city_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['events.City'])),
        ))
        db.send_create_signal('events', ['CityTranslation'])

        # Adding unique constraint on 'CityTranslation', fields ['language_code', 'master']
        db.create_unique('events_city_translation', ['language_code', 'master_id'])

        # Adding model 'SubmissionScreening'
        db.create_table('events_submissionscreening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submissions.Submission'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Program'])),
        ))
        db.send_create_signal('events', ['SubmissionScreening'])

        # Adding unique constraint on 'SubmissionScreening', fields ['submission', 'program']
        db.create_unique('events_submissionscreening', ['submission_id', 'program_id'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('starts_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Place'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Program'], null=True, blank=True)),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding model 'EventTranslation'
        db.create_table('events_event_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['events.Event'])),
        ))
        db.send_create_signal('events', ['EventTranslation'])

        # Adding unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.create_unique('events_event_translation', ['language_code', 'master_id'])

        # Adding model 'Program'
        db.create_table('events_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('section', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('events', ['Program'])

        # Adding model 'PlaceTranslation'
        db.create_table('events_place_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['events.Place'])),
        ))
        db.send_create_signal('events', ['PlaceTranslation'])

        # Adding unique constraint on 'PlaceTranslation', fields ['language_code', 'master']
        db.create_unique('events_place_translation', ['language_code', 'master_id'])

        # Adding model 'City'
        db.create_table('events_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('events', ['City'])

        # Adding model 'ProgramTranslation'
        db.create_table('events_programtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Program'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('events', ['ProgramTranslation'])

        # Adding unique constraint on 'ProgramTranslation', fields ['language', 'program']
        db.create_unique('events_programtranslation', ['language', 'program_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProgramTranslation', fields ['language', 'program']
        db.delete_unique('events_programtranslation', ['language', 'program_id'])

        # Removing unique constraint on 'PlaceTranslation', fields ['language_code', 'master']
        db.delete_unique('events_place_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.delete_unique('events_event_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SubmissionScreening', fields ['submission', 'program']
        db.delete_unique('events_submissionscreening', ['submission_id', 'program_id'])

        # Removing unique constraint on 'CityTranslation', fields ['language_code', 'master']
        db.delete_unique('events_city_translation', ['language_code', 'master_id'])

        # Deleting model 'Place'
        db.delete_table('events_place')

        # Deleting model 'CityTranslation'
        db.delete_table('events_city_translation')

        # Deleting model 'SubmissionScreening'
        db.delete_table('events_submissionscreening')

        # Deleting model 'Event'
        db.delete_table('events_event')

        # Deleting model 'EventTranslation'
        db.delete_table('events_event_translation')

        # Deleting model 'Program'
        db.delete_table('events_program')

        # Deleting model 'PlaceTranslation'
        db.delete_table('events_place_translation')

        # Deleting model 'City'
        db.delete_table('events_city')

        # Deleting model 'ProgramTranslation'
        db.delete_table('events_programtranslation')


    models = {
        'events.city': {
            'Meta': {'object_name': 'City'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        'events.citytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CityTranslation', 'db_table': "'events_city_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['events.City']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Place']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Program']", 'null': 'True', 'blank': 'True'}),
            'starts_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        'events.eventtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventTranslation', 'db_table': "'events_event_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['events.Event']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'events.place': {
            'Meta': {'object_name': 'Place'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'events.placetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PlaceTranslation', 'db_table': "'events_place_translation'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['events.Place']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'events.program': {
            'Meta': {'object_name': 'Program'},
            'code': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.IntegerField', [], {})
        },
        'events.programtranslation': {
            'Meta': {'unique_together': "[('language', 'program')]", 'object_name': 'ProgramTranslation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Program']"})
        },
        'events.submissionscreening': {
            'Meta': {'unique_together': "[('submission', 'program')]", 'object_name': 'SubmissionScreening'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Program']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['submissions.Submission']"})
        },
        'submissions.submission': {
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
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_email_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment_film_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment_papers_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment_vob_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'director_address': ('django.db.models.fields.TextField', [], {}),
            'director_awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'director_email': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'director_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'director_photography': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'director_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'email_sent_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'extra_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'film_awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'film_link': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'film_link_pwd': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'film_received_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'music': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'other_credits': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'papers_received_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'premiere': ('django.db.models.fields.IntegerField', [], {}),
            'preview': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'preview_average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'previewers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'producer_email': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_phone': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'producer_site': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'screenwriter': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'section': ('django.db.models.fields.IntegerField', [], {}),
            'submission_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'vob_received_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['events']