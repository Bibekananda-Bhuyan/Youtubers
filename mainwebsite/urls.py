from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name="Index Page"),
    path('creator-signup/',views.Creator_signup,name="Creator Registration"),
    path('creator-successful-registration/',views.creator_successful_registration,name="Creator Successful Joined"),
    path('creator-email-verify/<slug:id>',views.creator_email_verify,name="Creator Email Verification"),
    path('brand-signup/',views.Brand_signup,name="Creator Registration"),
    path('brand-email-verify/<slug:id>',views.brand_email_verify,name="Brand Email Verification"),
    path('creator-login',views.creator_login,name="Creator Login"),
    path('logout/',views.logout,name="Logout"),
    path('brand-login',views.brand_login,name="Brand Login"),
    path('create-campaign/',views.create_campaign,name="Create Campaign"),
    path('creator-profile/',views.creator_profile,name="Creator Profile"),
    path('update-creator-profile',views.update_creator_profile,name="Update Creator Profile Details"),
    path('updatepassword',views.chagepassword,name="Change Creator Password"),
    path('addyoutubechannel', views.add_youtube_channel, name="Add Creator Youtube Channels"),
    path('youtube-channel-list',views.youtubechannelslist,name="All Listed Youtube Channels "),
    path('submit-campaign',views.submit_campaign,name="Submit Campaign"),
    path('success',views.success,name="success Massage"),
    path('created-campaigns',views.created_campaigns,name="All Created Campaigns"),
    path('pay/<int:id>/<slug:titel>',views.pay_for_campaign,name="Pay For Campaign"),
    path('youtubeer-channel-details/<slug:chnnelid>',views.youtuber_channel_details,name="Youtube Channel Details"),
    path('allcreated-campaigns/<slug:channelid>',views.allcreated_campaigns,name="View All Created Campaign By Admin "),
    path('submit-creator-invitaion',views.submit_creator_invitaions,name="Submit Creator Invitaions"),
    path('creator-all-invited-campaigns',views.creator_all_invited_campaigns,name="Creator All Invited Campaigns"),
    path('creator-invited-campaigns-details/<int:id>/<slug:type>',views.invited_campaign_details,name="Invited Campaign Details "),
    path('creator-response/<int:res>/<int:campid>',views.creator_invitations_response,name="Creator Invitations Response"),
    path('creator-ongoing-projects',views.creator_on_going_projects,name="Creator On Going Projects"),
    path('creator-submit-project/<int:id>/<slug:type>',views.creator_submit_project,name="Creator Submit Project "),
    path('creator-dashboard',views.creator_dashboard,name="Creator Dashboard"),
    path('brand-dashboard',views.brand_dashboard,name="Brand dashboard"),
    path('submit-project/<int:id>', views.submit_project, name="Submit Project"),
    path('brand-campign-details/<int:id>',views.brand_camping_details,name="Brand Campaign Details"),
    path('approve-creator-response/<int:id>',views.approve_creator_response,name="Approve Crator Response"),
    path('brand-payment-history',views.brand_payment_history,name="Brand Payment History"),
    path('projects',views.allprojects,name="All Projects"),
    path('project-details/<int:id>',views.project_details,name="Project Details"),
    path('send-campaign-ivititaion',views.send_campaign_invitaions,name="Send Campaign Invitaions")


]
