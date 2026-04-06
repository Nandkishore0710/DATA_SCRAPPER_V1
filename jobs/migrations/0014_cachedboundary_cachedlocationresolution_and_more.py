from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_package_features_alter_package_grid_strategies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedBoundary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=500)),
                ('min_lat', models.FloatField()),
                ('max_lat', models.FloatField()),
                ('min_lng', models.FloatField()),
                ('max_lng', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CachedLocationResolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True)),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='place',
            name='opening_hours',
            field=models.TextField(blank=True),
        ),
    ]
