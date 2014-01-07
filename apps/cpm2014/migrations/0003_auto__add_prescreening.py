# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prescreening'
        db.create_table('cpm2014_prescreening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('cpm2014', ['Prescreening'])

        # Adding M2M table for field submissions on 'Prescreening'
        m2m_table_name = db.shorten_name('cpm2014_prescreening_submissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prescreening', models.ForeignKey(orm['cpm2014.prescreening'], null=False)),
            ('submission', models.ForeignKey(orm['cpm2014.submission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['prescreening_id', 'submission_id'])


    def backwards(self, orm):
        # Deleting model 'Prescreening'
        db.delete_table('cpm2014_prescreening')

        # Removing M2M table for field submissions on 'Prescreening'
        db.delete_table(db.shorten_name('cpm2014_prescreening_submissions'))


    models = {
        'cpm2014.newsentry': {
            'Meta': {'object_name': 'NewsEntry'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cpm2014.newsentrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsEntryTranslation', 'db_table': "'cpm2014_newsentry_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['cpm2014.NewsEntry']"}),
            'short_text': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cpm2014.prescreening': {
            'Meta': {'object_name': 'Prescreening'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cpm2014.Submission']", 'symmetrical': 'False'})
        },
        'cpm2014.submission': {
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
            'film_awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'film_link': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
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

    complete_apps = ['cpm2014']