# Generated by Django 2.1.4 on 2019-06-20 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_dinnerplatter_pasta_pizzatopping_salad_subtopping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=1)),
                ('topping', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platters', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastas', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='salad',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salads', to='orders.Order'),
        ),
    ]