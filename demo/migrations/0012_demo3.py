# Generated by Django 3.0.5 on 2020-05-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20200114_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo3',
            fields=[
                ('demo1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.demo1')),
                ('f1', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f2', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f3', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f4', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f5', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f6', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f7', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f8', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f9', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f10', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f11', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f12', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f13', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f14', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f15', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f16', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f17', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f18', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f19', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f20', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f21', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f22', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f23', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f24', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f25', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f26', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f27', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f28', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f29', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('f30', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'demo2',
                'verbose_name_plural': 'demo2',
                'ordering': ('name',),
            },
            bases=('demo.demo1',),
        ),
    ]