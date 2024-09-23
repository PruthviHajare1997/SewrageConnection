# Generated by Django 4.2.7 on 2024-09-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0004_documentmaster_alter_levelactionmapping_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizendocument',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentmaster',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicematrix',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workflowdetail',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='InternalUserDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('request_no_id', models.ForeignKey(blank=True, db_column='request_no_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_no_F', to='Masters.workflowdetail')),
            ],
            options={
                'db_table': 'tbl_internal_user_document',
            },
        ),
    ]
