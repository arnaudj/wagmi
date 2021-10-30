# Generated by Django 3.2.8 on 2021-10-30 04:36

from django.db import migrations, models
import django.db.models.deletion
import execution.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, execution.models.AuditableMixin),
        ),
        migrations.CreateModel(
            name='Fill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execution.order')),
            ],
            bases=(models.Model, execution.models.AuditableMixin),
        ),
    ]
