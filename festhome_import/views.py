from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.shortcuts import render_to_response
from django.template import RequestContext
import openpyxl

from festhome_import.forms import FesthomeImportForm
from festhome_import.models import FesthomeData, FesthomeSubmission


EXPECTED_COLUMN_NAME = [
    '#', 'ID', 'Title (Original)', 'Title (English)', 'Custom', 'Duration',
    'Ratings', 'Total', 'Section', 'Status', 'Name', 'Last name:',
    'Date of birth', 'Code', 'Phone', 'E-mail', 'Street', 'City',
    'Postal Code', 'State', 'Country', 'Organization', 'E-mail', 'Street',
    'City', 'Postal Code', 'State', 'Country', 'Title\'s original language',
    'Title (in original language)', 'Title (in english)', 'Production country',
    'Production date', 'Other production countries', 'Categories', 'Genre',
    'Theme', 'Original Language', 'Dialogues', 'Shooting country',
    'Synopsis Original Language', 'Short synopsis original language',
    'Short synopsis english', 'Long synopsis original language',
    'Long synopsis english', 'Opera Prima', 'School', 'Tags'
]


@transaction.commit_on_success
@staff_member_required
def import_festhome(request):
    form = FesthomeImportForm(request.POST or None, request.FILES)
    context = {'form': form}

    if form.is_valid():
        wb = openpyxl.load_workbook(form.cleaned_data['document'].file)
        ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])

        column_names = [col.value for col in ws.rows[1]]
        submission_rows = ws.rows[2:]

        if column_names[:len(EXPECTED_COLUMN_NAME)] != EXPECTED_COLUMN_NAME:
            raise Exception('Unexpected column names')

        existing_submissions = \
            FesthomeSubmission.objects.filter(
                festhome_id__in=[row[1].value for row in submission_rows]
            )
        new_submissions = []
        existing_fethome_ids = set(
            subm.festhome_id for subm in existing_submissions
        )

        for row in submission_rows:
            row = row[:len(EXPECTED_COLUMN_NAME)]
            festhome_data = FesthomeData(*[col.value for col in row])
            if int(festhome_data.festhome_id) in existing_fethome_ids:
                continue

            subm = FesthomeSubmission.from_data(festhome_data)
            subm.save()
            new_submissions.append(subm)

        context['existing_submissions'] = existing_submissions
        context['new_submissions'] = new_submissions
        context['submit'] = True

    return render_to_response(
        'festhome_import/import_festhome.html',
        context,
        context_instance=RequestContext(request)
    )
