# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Submission'
        db.create_table('submissions_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('section', self.gf('django.db.models.fields.IntegerField')()),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('aspect_ratio', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('premiere', self.gf('django.db.models.fields.IntegerField')()),
            ('film_awards', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('director_awards', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('budget', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('film_link', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
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
            ('other_credits', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('allow_tv', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('allow_noncommercial', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('allow_network', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('applicant', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('applicant_address', self.gf('django.db.models.fields.TextField')()),
            ('applicant_email', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('applicant_site', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('applicant_phone', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('submission_language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('extra_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_email_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment_film_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment_papers_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment_vob_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('submitted_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_sent_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('film_received_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('papers_received_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('vob_received_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('preview', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('preview_average', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('previewers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('submissions', ['Submission'])

        # Adding model 'SubmissionTranslation'
        db.create_table('submissions_submissiontranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submissions.Submission'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('genre', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(default='')),
            ('synopsis_short', self.gf('django.db.models.fields.TextField')(default='')),
            ('director', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
        ))
        db.send_create_signal('submissions', ['SubmissionTranslation'])

        # Adding unique constraint on 'SubmissionTranslation', fields ['submission', 'language']
        db.create_unique('submissions_submissiontranslation', ['submission_id', 'language'])

    from south.db.postgresql_psycopg2 import DatabaseOperations as PgDbOps
    if isinstance(db, PgDbOps):
        next_id = db.execute('select max(id) + 1 from cpm2014_submission')[0][0]
        db.execute(
            "alter sequence submissions_submission_id_seq "
            "restart with %s;" % next_id
        )


    def backwards(self, orm):
        # Removing unique constraint on 'SubmissionTranslation', fields ['submission', 'language']
        db.delete_unique('submissions_submissiontranslation', ['submission_id', 'language'])

        # Deleting model 'Submission'
        db.delete_table('submissions_submission')

        # Deleting model 'SubmissionTranslation'
        db.delete_table('submissions_submissiontranslation')


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
