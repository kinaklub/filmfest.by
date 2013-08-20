from rest_framework import serializers

from apps.cpm2014.models import Submission


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'id', 'title', 'title_en', 'country', 'language', 'genre',
            'section', 'synopsis', 'length', 'aspect_ratio', 'year',
            'premiere', 'film_awards', 'director_awards', 'budget',
            'film_link', 'attend', 'backlink', 'director', 'director_address',
            'director_email', 'director_site', 'director_phone', 'producer',
            'producer_address', 'producer_email', 'producer_site',
            'producer_phone', 'screenwriter', 'editor', 'music',
            'director_photography', 'other_credits', 'allow_tv',
            'allow_noncommercial', 'allow_network', 'applicant',
            'applicant_address', 'applicant_email', 'applicant_site',
            'applicant_phone', 'submission_language', 'comment',
            'comment_email_sent', 'comment_film_received',
            'comment_papers_received', 'comment_vob_received',
            'submitted_at', 'email_sent_at', 'film_received_at',
            'papers_received_at', 'vob_received_at', 'preview',
            'preview_average', 'previewers'
        ]
