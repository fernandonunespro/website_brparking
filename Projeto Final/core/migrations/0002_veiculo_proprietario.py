# Generated by Django 4.2.2 on 2023-06-30 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
            preserve_default=False,
        ),
    ]
