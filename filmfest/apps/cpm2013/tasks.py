import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import translation
from django.template import loader

from apps.cpm2013.models import Submission, LetterTemplate, ActionRegistry
from celery import Task

logger = logging.getLogger('cpm2013.tasks')


class SendSubmissionEmail(Task):
    def create_pdf(self, submission):
        from apps.cpm2013.pdf import get_submission_confirmation_report
        return get_submission_confirmation_report(submission)

    def get_email_message(self, submission):
        lang = translation.get_language().lower()
        return loader.render_to_string(
            'cpm2013/email/submission_%s.txt' % lang, {
                'name': submission.applicant,
                'film_title': submission.title,
            }
        )
        
    def run(self, submission):
        logger.info('SendSubmissionEmail for submission %s' % (
            submission.id
        ))
        try:
            translation.activate(submission.submission_language)

            email = EmailMessage(
                'Cinema Perpetuum Mobile 2013',
                self.get_email_message(submission),
                'no-reply@filmfest.by',
                [submission.applicant_email],
                list(settings.MAIL_BCC_LIST),
                headers = {'Reply-To': '2013@filmfest.by'})

            email.attach(
                'cpm2013.pdf', self.create_pdf(submission), 'application/pdf'
            )

            email.send()
        except:
            logger.exception('')
            raise
        finally:
            translation.deactivate()
            try:
                submission = Submission.objects.get(pk=submission.pk)
            except Submission.DoesNotExist:
                logger.exception('Failed to update "email sent" status')
            else:
                submission.comment_email_sent = True
                submission.save()



class SendEmailFromTemplate(Task):
    def run(self, submission, template_code):
        logger.info('SendEmailFromTemplate:%d template %s' % (
                submission.id, template_code
        ))
        
        try:
            translation.activate(submission.submission_language)

            letter = LetterTemplate.objects.language().get(slug=template_code)
            email = EmailMessage(
                letter.subject,
                letter.text % {'name': submission.applicant},
                'no-reply@filmfest.by',
                [submission.applicant_email],
                list(settings.MAIL_BCC_LIST),
                headers = {'Reply-To': '2013@filmfest.by'}
            )
            email.send()
        except:
            logger.info('SendEmailFromTemplate:%d template %s exception' % (
                submission.id, template_code
            ))
            raise
        finally:
            translation.deactivate()
        logger.info('SendEmailFromTemplate:%d template %s done' % (
            submission.id, template_code
        ))


class SendEmailUpdate(Task):
    def run(self, submission_id, fact_name):
        logger.info('SendEmailUpdate:%d fact %s' % (submission_id, fact_name))

        submission = Submission.objects.get(id=submission_id)
        fact = getattr(submission, fact_name)
        if not fact:
            logger.info('SendEmailUpdate:%d False' % submission_id)
            return

        if fact_name == 'comment_film_received':
            if submission.comment_vob_received:
                template_code = 'film_received_vob'
            else:
                template_code = 'film_received'
        elif fact_name == 'comment_papers_received':
            template_code = 'papers_received'
        else:
            logger.error('SendEmailUpdate:%d unknown fact' % submission_id)
            return

        action_code = 'submission:%s:%s' % (submission_id, fact_name)
        if ActionRegistry.objects.filter(code=action_code).count() > 0:
            logger.error('SendEmailUpdate:%d registered fact %s' % (
                submission_id, fact_name
            ))
            return

        SendEmailFromTemplate().run(submission, template_code)
        ActionRegistry(code=action_code).save()

        logger.info('SendEmailUpdate:%d done' % submission_id)
