# Generated by Django 3.2.13 on 2022-07-18 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('contact_person', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('bulk_customer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=255)),
                ('epra_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('order_quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Scanned', 'Scanned'), ('Rejected', 'Rejected'), ('Safety', 'Safety'), ('Lab', 'Lab'), ('Labresults', 'Labresults'), ('Loading', 'Loading'), ('Loaded', 'Loaded'), ('Released', 'Released')], default='Pending', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_driver', to='customers.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=255)),
                ('transporter', models.CharField(max_length=255)),
                ('epra_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loaded_quantity', models.CharField(max_length=255, null=True)),
                ('loaded_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('coid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.order')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='customers.driver')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.product')),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trailer', to='customers.vehicle')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck', to='customers.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='trailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_trailer', to='customers.vehicle'),
        ),
        migrations.AddField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_truck', to='customers.vehicle'),
        ),
        migrations.CreateModel(
            name='CustomerTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('truck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerTrailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('trailer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_trailer', to='customers.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.driver')),
            ],
            options={
                'db_table': 'customers_customerdriver',
            },
        ),
        migrations.CreateModel(
            name='BulkOrderBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField(default=1)),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='BulkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('product', models.IntegerField(default=1)),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.AddConstraint(
            model_name='customertrailer',
            constraint=models.UniqueConstraint(fields=('customer', 'trailer'), name='unique_customer_trailer'),
        ),
        migrations.AddConstraint(
            model_name='customerdriver',
            constraint=models.UniqueConstraint(fields=('customer_id', 'driver'), name='unique_customer_driver'),
        ),
        migrations.AddConstraint(
            model_name='bulkorderbalance',
            constraint=models.UniqueConstraint(fields=('customer', 'product'), name='unique_bulk_balance'),
        ),
    ]
