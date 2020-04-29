from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Platform)


class Creatoradminmodels(admin.ModelAdmin):
  list_display = ("creator_first_name","creator_last_name","creator_email","creator_phoneno","creator_platform","creator_join_date","is_active_creator")
  list_filter = ("creator_platform","is_active_creator","is_verified_creator")
  search_fields = ["creator_name","creator_email","creator_phoneno"]
admin.site.register(Creator,Creatoradminmodels)


class Brandadminmodel(admin.ModelAdmin):
    list_display = (
    "brand_name", "brand_email", "brand_phoneno", "brand_join_date", "is_active_brand")
    list_filter = ("is_active_brand", "is_verified_brand")
    search_fields = ["brand_name", "brand_email", "brand_phoneno"]
admin.site.register(Brand, Brandadminmodel)

class Youtubechnnels_adminmodel(admin.ModelAdmin):
    list_display = ["creator_id","youtube_channelname","youtube_subscribercount","youtube_viewcount","youtube_videocount","youtube_commentcount"]
    search_fields = ["youtube_channelname","youtube_subscribercount","youtube_viewcount","youtube_videocount","youtube_commentcount"]
    #list_filter = ["youtube_subscribercount"]
admin.site.register(Youtubechannels, Youtubechnnels_adminmodel)


class Campaignsadminmodel(admin.ModelAdmin):
    list_display = ["brand","campaign_titel","project_budget","traget_audience","platform","ads_category","createddate","status","is_admin_approved"]
    list_filter = ["is_admin_approved","traget_audience","platform","ads_category","is_project_rejected"]
    search_fields = [ "campaign_titel", "project_budget", "traget_audience", "platform", "ads_category",
                    "campaign_listing_duration", "createddate"]


admin.site.register(Campaign,Campaignsadminmodel)


class Creatorinvitationsadminmodel(admin.ModelAdmin):
    list_display = ["campaign_name","creator_name","status","request_date","is_creator_accept_request","is_project_submited","is_project_delivered","is_creator_reject_request"]

admin.site.register(Creatorinivitation,Creatorinvitationsadminmodel)

class Submittedcampaginadminmde(admin.ModelAdmin):
    list_display = ["campaign","submit_url","submit_date","is_brand_approved"]
admin.site.register(Submitedcampaign,Submittedcampaginadminmde)


class Notifications(admin.ModelAdmin):
    list_display = ["notification_titel","notification_for","notification_date"]
    list_filter = ["notification_for"]
    search_fields = ["notification_titel"]

admin.site.register(Notification,Notifications)


class Brandsinvitionsadmin(admin.ModelAdmin):
    list_display = ["Campaign","Creator","Invitations_send_date"]

admin.site.register(Brands_invitation,Brandsinvitionsadmin)

