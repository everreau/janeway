# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-21 13:59
from __future__ import unicode_literals

from django.db import migrations
OLD_VALUE = "Dear {{ review_assignment.reviewer.full_name  }},<br/><br/>We are requesting that you undertake a review of \"{{ article.title  }}\" in {{ article.journal.name  }}.<br/><br/>We woul       d be most grateful for your time as the feedback from our reviewers is of the utmost importance to our editorial decision-making processes.<br/><br/>You can let us know your decision or decline to under       take the review: {{ review_url  }} <br/><br/>Regards,<br/>{{ request.user.signature|safe  }}"
NEW_VALUE = "Dear {{ review_assignment.reviewer.full_name  }},<br/><br/>We are requesting that you undertake a review of \"{{ article.title  }}\" in {{ article.journal.name  }}.<br/><br/>We woul       d be most grateful for your time as the feedback from our reviewers is of the utmost importance to our editorial decision-making processes.<br/><br/>You can let us know your decision or decline to under       take the review: {{ review_url  }} <br/><br/>{{ article_details  }}<br/><br/>Regards,<br/>{{ request.user.signature|safe  }}"


def update_setting_values(apps, schema_editor):
    SettingValueTranslation = apps.get_model('core', 'SettingValueTranslation')

    setting_values = SettingValueTranslation.objects.filter(
        master__setting__name='review_assignment',
        master__setting__group__name='email',
    )

    for setting in setting_values:
        # IF it hasn't been modified, just update it with the new value
        if setting.value == OLD_VALUE:
            setting.value = NEW_VALUE
        elif "article_detail" not in setting.value:
            # otherwise, append the metadata at the end
            setting.value += ("<br/>{{ article_details }}")
        setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_remove_dots_from_urls'),
    ]

    operations = [
        migrations.RunPython(
            update_setting_values,
            reverse_code=migrations.RunPython.noop,
        ),
    ]