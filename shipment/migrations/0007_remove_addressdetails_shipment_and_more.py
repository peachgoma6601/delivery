# Generated by Django 4.0.5 on 2022-06-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0006_rename_orgin_trackingdetails_origin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressdetails',
            name='shipment',
        ),
        migrations.AlterField(
            model_name='shipmentdetails',
            name='consignment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentdetails',
            name='created_at',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentdetails',
            name='shipment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentdetails',
            name='shipment_state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentdetails',
            name='tracking_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='origin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='shipment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackingdetails',
            name='tracking_page_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
