# Generated by Django 4.2.5 on 2023-09-17 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Produto')),
                ('descricao', models.TextField(verbose_name='Descrição do Produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.AlterField(
            model_name='compra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto', verbose_name='Produto'),
        ),
    ]
