# Generated by Django 2.2.4 on 2020-05-25 08:17

from django.db import migrations, models
import django.db.models.deletion
import otree.common
import otree.db.models
import otree.db.serializedfields
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowserBotsLauncherSessionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('is_only_record', models.BooleanField(default=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.serializedfields._PickleField(default=dict)),
                ('label', otree.db.models.StringField(max_length=50, null=True)),
                ('id_in_session', otree.db.models.PositiveIntegerField(null=True)),
                ('payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('time_started', models.DateTimeField(null=True)),
                ('mturk_assignment_id', otree.db.models.StringField(max_length=50, null=True)),
                ('mturk_worker_id', otree.db.models.StringField(max_length=50, null=True)),
                ('_index_in_subsessions', otree.db.models.PositiveIntegerField(default=0, null=True)),
                ('_index_in_pages', otree.db.models.PositiveIntegerField(db_index=True, default=0, null=True)),
                ('_waiting_for_ids', otree.db.models.StringField(max_length=300, null=True)),
                ('code', otree.db.models.StringField(default=otree.common.random_chars_8, max_length=16, null=True, unique=True)),
                ('visited', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False, null=True)),
                ('_last_page_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('_last_request_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('is_on_wait_page', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_current_page_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='page')),
                ('_current_app_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='app')),
                ('_round_number', otree.db.models.PositiveIntegerField(null=True)),
                ('_current_form_page_url', models.URLField()),
                ('_max_page_index', otree.db.models.PositiveIntegerField(null=True)),
                ('_browser_bot_finished', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_is_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('is_browser_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ParticipantLockModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_code', models.CharField(max_length=16, unique=True)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantRoomVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('participant_label', models.CharField(max_length=200)),
                ('tab_unique_id', models.CharField(max_length=20, unique=True)),
                ('last_updated', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.serializedfields._PickleField(default=dict)),
                ('config', otree.db.serializedfields._PickleField(default=dict, null=True)),
                ('label', otree.db.models.StringField(blank=True, help_text='For internal record-keeping', max_length=300, null=True)),
                ('experimenter_name', otree.db.models.StringField(blank=True, help_text='For internal record-keeping', max_length=300, null=True)),
                ('code', otree.db.models.StringField(default=otree.common.random_chars_8, max_length=16, null=True, unique=True)),
                ('mturk_HITId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('mturk_HITGroupId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('mturk_num_participants', otree.db.models.IntegerField(default=-1, help_text='Number of participants on MTurk', null=True)),
                ('mturk_use_sandbox', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text='Should this session be created in mturk sandbox?', null=True)),
                ('mturk_expiration', otree.db.models.FloatField(null=True)),
                ('archived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False, null=True)),
                ('comment', otree.db.models.LongStringField(blank=True, null=True)),
                ('_anonymous_code', otree.db.models.StringField(db_index=True, default=otree.common.random_chars_10, max_length=10, null=True)),
                ('is_demo', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_admin_report_app_names', otree.db.models.LongStringField(default='', null=True)),
                ('_admin_report_num_rounds', otree.db.models.StringField(default='', max_length=255, null=True)),
                ('num_participants', otree.db.models.PositiveIntegerField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='UndefinedFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WaitPagePassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch_time', models.PositiveIntegerField(null=True)),
                ('is_enter', models.BooleanField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
        ),
        migrations.CreateModel(
            name='RoomToSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255, unique=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.CreateModel(
            name='PageCompletion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=300)),
                ('page_index', models.PositiveIntegerField()),
                ('page_name', models.CharField(max_length=300)),
                ('epoch_time', models.PositiveIntegerField(null=True)),
                ('seconds_on_page', models.PositiveIntegerField()),
                ('subsession_pk', models.PositiveIntegerField()),
                ('auto_submitted', models.BooleanField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantToPlayerLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_code', models.CharField(max_length=20)),
                ('page_index', models.PositiveIntegerField()),
                ('app_name', models.CharField(max_length=300)),
                ('player_pk', models.PositiveIntegerField()),
                ('subsession_pk', models.PositiveIntegerField()),
                ('session_pk', models.PositiveIntegerField()),
                ('url', models.CharField(max_length=300)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
            ],
            options={
                'unique_together': {('participant', 'page_index')},
                'index_together': {('participant', 'page_index')},
            },
        ),
        migrations.AlterIndexTogether(
            name='participant',
            index_together={('session', 'mturk_worker_id', 'mturk_assignment_id')},
        ),
        migrations.CreateModel(
            name='PageTimeout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('expiration_time', models.FloatField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
            ],
            options={
                'index_together': {('participant', 'page_index')},
            },
        ),
        migrations.CreateModel(
            name='CompletedSubsessionWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'index_together': {('page_index', 'session')},
            },
        ),
        migrations.CreateModel(
            name='CompletedGroupWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('id_in_subsession', models.PositiveIntegerField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'index_together': {('page_index', 'session', 'id_in_subsession')},
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('timestamp', models.FloatField(default=time.time)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages_core', to='otree.Participant')),
            ],
            options={
                'index_together': {('channel', 'timestamp')},
            },
        ),
    ]
