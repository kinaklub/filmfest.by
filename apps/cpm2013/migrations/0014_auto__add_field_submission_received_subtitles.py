# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.received_subtitles'
        db.add_column('cpm2013_submission', 'received_subtitles',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.received_subtitles'
        db.delete_column('cpm2013_submission', 'received_subtitles')


    models = {
        'cpm2013.actionregistry': {
            'Meta': {'object_name': 'ActionRegistry'},
            'at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cpm2013.lettertemplate': {
            'Meta': {'object_name': 'LetterTemplate'},
            'code': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cpm2013.lettertemplatetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'LetterTemplateTranslation', 'db_table': "'cpm2013_lettertemplate_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['cpm2013.LetterTemplate']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
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
        'cpm2013.previewer': {
            'Meta': {'object_name': 'Previewer'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cinephilia': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'coefficient': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'education': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'how_often_screenings': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'how_often_watch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cpm2013.Submission']", 'through': "orm['cpm2013.PreviewMark']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'occupation_cinema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'participation_in_film_creation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'working': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cpm2013.previewmark': {
            'Meta': {'object_name': 'PreviewMark'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.IntegerField', [], {}),
            'previewer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cpm2013.Previewer']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cpm2013.Submission']"})
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
            'received_company_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_company_logo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_director_bio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_director_photo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_producer_bio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_producer_photo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_screenshots': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_subtitles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_viza_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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

    complete_apps = ['cpm2013']