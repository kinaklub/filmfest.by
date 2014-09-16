# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.film_link_pwd'
        db.add_column('submissions_submission', 'film_link_pwd',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.film_link_pwd'
        db.delete_column('submissions_submission', 'film_link_pwd')


    models = {
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
        },
        'submissions.submissiontranslation': {
            'Meta': {'unique_together': "[('submission', 'language')]", 'object_name': 'SubmissionTranslation'},
            'director': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['submissions.Submission']"}),
            'synopsis': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'synopsis_short': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        }
    }

    complete_apps = ['submissions']