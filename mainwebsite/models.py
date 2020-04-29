from django.db import models

# Create your models here.
class Platform(models.Model):
    platform_name = models.CharField(max_length=200)

    def __str__(self):
        return self.platform_name


class Creator(models.Model):
    creator_first_name = models.CharField(max_length=300,default="")
    creator_last_name = models.CharField(max_length=300,default="")
    creator_email = models.CharField(max_length=500,default="")
    creator_password = models.CharField(max_length=500)
    creator_phoneno = models.CharField(max_length=200)
    creator_adddress = models.CharField(max_length=1000)
    creator_short_descriptions = models.TextField(default="")
    creator_descriptions = models.TextField(default="")
    creator_platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    creator_platform_identification_id = models.CharField(max_length=50000, default="")
    creator_join_date = models.DateTimeField(auto_now_add=True)
    is_active_creator = models.BooleanField("Is Active Creator", default=False)
    is_verified_creator = models.BooleanField("Is Creator Verified", default=False)
    email_verificationid=models.CharField(max_length=1000,default="bibekitsnotvalid")
    unquie_id=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.creator_first_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=300)
    brand_email = models.CharField(max_length=500)
    brand_password = models.CharField(max_length=500)
    brand_phoneno = models.CharField(max_length=200)
    brand_adddress = models.CharField(max_length=1000)
    brand_short_descriptions = models.TextField()
    brand_descriptions = models.TextField()
    brand_join_date = models.DateTimeField(auto_now_add=True)
    is_active_brand = models.BooleanField("Is Active Brand", default=False)
    is_verified_brand = models.BooleanField("Is Brand Verified", default=False)
    email_verificationid = models.CharField(max_length=1000, default="bibekitsnotvalid")
    unquie_id = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.brand_name




class Youtubechannels(models.Model):
    creator_id=models.ForeignKey(Creator,on_delete=models.CASCADE,null=True)
    youtube_channelid=models.CharField(max_length=200)
    youtube_viewcount=models.CharField(max_length=100)
    youtube_commentcount=models.CharField(max_length=100)
    youtube_subscribercount=models.CharField(max_length=100)
    youtube_videocount=models.CharField(max_length=100)
    youtube_channelname=models.CharField(max_length=200)
    youtube_profileurl=models.CharField(max_length=1000)
    channeladded_date=models.DateTimeField(auto_now_add=True)
    unquie_id = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.youtube_channelname


class Campaign(models.Model):
    campaign_titel=models.CharField(max_length=200,default="")
    campaign_country=models.CharField(max_length=200,default="")
    platform=models.CharField(max_length=100,default="")
    campaign_type=models.CharField(max_length=100,default="")
    ads_category=models.CharField(max_length=100,default="")
    ads_url=models.CharField(max_length=100,default="")
    is_shipping_product=models.BooleanField("IS_Shipping_Product",default=True)
    about_product_or_service=models.TextField(max_length=5000,default="")
    campaign_listing_duration=models.CharField(max_length=50,default="")
    about_campaign=models.TextField(max_length=5000,default="")
    exact_requirement=models.TextField(max_length=5000,default="")
    traget_audience=models.CharField(max_length=100,default="")
    project_budget=models.CharField(max_length=100,default="")
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    createddate=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,default="Under Verification")
    is_admin_approved=models.BooleanField("Is Admin Approved",default=False)
    is_project_rejected=models.BooleanField("Is Project Rejected",default=False)
    is_payment_done = models.BooleanField("Is Payment Done", default=False)
    unquie_id = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.campaign_titel


class Creatorinivitation(models.Model):
    campaign_name=models.ForeignKey(Campaign,on_delete=models.CASCADE,null=True,related_name="Campaign")
    creator_name=models.ForeignKey(Creator,on_delete=models.CASCADE,null=True,related_name="Creator")
    request_date=models.DateTimeField(auto_now_add=True)
    is_creator_accept_request=models.BooleanField("Is Creator Accepted The Request",default=False)
    is_creator_reject_request = models.BooleanField("Is Creator Rejected The Request", default=False)
    is_project_submited = models.BooleanField("Is Project Submitted", default=False)
    is_project_delivered = models.BooleanField("Is Project Delivered", default=False)
    status=models.CharField(max_length=200)
    brand_approved_date = models.DateTimeField(null=True)
    unquie_id = models.CharField(max_length=100, default="")

class Submitedcampaign(models.Model):
    campaign=models.ForeignKey(Campaign,on_delete=models.CASCADE,null=True)
    submit_url=models.CharField(max_length=1000)
    submit_date=models.DateTimeField(auto_now_add=True)
    is_brand_approved=models.BooleanField("Is Brand Approved",default=False)
    brand_approved_date=models.DateTimeField(null=True)
    unquie_id = models.CharField(max_length=100, default="")

class Notification(models.Model):
    Notificationtype = [
        ("Creator", 'Creator'),
        ("Brands", 'Brands'),
        ("Others", 'Others'),

    ]
    notification_titel=models.CharField(max_length=300)
    notification_massage=models.TextField(max_length=6000)
    notification_for=models.CharField(choices=Notificationtype,default="Creator",max_length=100)
    notification_date=models.DateTimeField(auto_now_add=True)
    unquie_id = models.CharField(max_length=100, default="")

class Brands_invitation(models.Model):
    Campaign=models.ForeignKey(Campaign,on_delete=models.CASCADE,null=True)
    Creator=models.ForeignKey(Creator,on_delete=models.CASCADE,null=True)
    Invitations_send_date=models.DateTimeField(auto_now_add=True)
    unquie_id = models.CharField(max_length=100, default="")

