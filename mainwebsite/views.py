from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from . forms import *
from django.contrib.messages import constants as messages
import string,random
from django.core.mail import send_mail
from Youtube.settings import EMAIL_HOST_USER
from googleapiclient.discovery import build
from django.contrib import messages
import datetime

# Create your views here.
youTubeApiKey = 'AIzaSyC0TGBAXO0eDTfvh-Le_RiDybfmv8X8Psk'
youtube = build('youtube', 'v3', developerKey=youTubeApiKey)


# Create Unique Id

def unque_id_generator():
    ts = datetime.datetime.now().timestamp()
    ts = str(ts)
    ts = ts.split(".")
    ts=ts[0]
    ran=random.randint(1,100)
    ran=str(ran)
    uid=ts+ran
    return uid



def creator_successful_registration(request):
    return render(request,"mainwebsite/creator-successful-registration.html")

def index(request):

    return render(request,'mainwebsite/index.html')


def Creator_signup(request):
    if "is_logedin" not in request.session:
        allpatforms=Platform.objects.all()
        regiform=Creatorregistationform()
        parms={"paltform":allpatforms,"form":regiform}
        if request.method=="POST":
            platform=request.POST.get("platformtype")
            creatorentredemail = request.POST.get("creator_email")
            formdata=Creatorregistationform(request.POST)
            formdata.creator_platform=platform
            formdata.unquie_id=unque_id_generator()
            print(formdata.unquie_id)
            checkisemailexist=Creator.objects.filter(creator_email=creatorentredemail).count()
            if checkisemailexist == 0:
                if formdata.is_valid():
                    formdata.save()
                    return render(request,'mainwebsite/creator-successful-registration.html')
                else:
                    print(formdata.creator_platform)
                    parms["formerror"] = formdata.errors
            else:
                return HttpResponse("Email Alrady Exist")

        return render(request,'mainwebsite/creator-register.html',parms)
    else:
        return redirect('/')


def creator_email_verify(request,id):
    checkisid=Creator.objects.filter(email_verificationid=id).count()
    if checkisid >0:
        get_creator=Creator.objects.get(email_verificationid=id)
        get_creator.is_active_creator=True
        get_creator.is_verified_creator=True
        get_creator.save()
        mass2={"smass":"Your Email Is Verified. You Can Login Now","ulr":"","urltext":"Login Now"}
        return render(request,'mainwebsite/successful.html',mass2)
    else:
        return HttpResponse("Invalid URL")


def Brand_signup(request):
    if "is_logedin" not in request.session:
        regiform = Brand_Signupform()
        parms = {"form": regiform}
        if request.method=="POST":
            brandentredemail = request.POST.get("brand_email")
            formdata=Brand_Signupform(request.POST)

            checkisemailexist=Brand.objects.filter(brand_email=brandentredemail).count()
            if checkisemailexist == 0:
                if formdata.is_valid():
                    formdata.save()
                    return render(request,'mainwebsite/creator-successful-registration.html')
                else:
                    parms["formerror"] = formdata.errors
            else:
                return HttpResponse("Email Alrady Exist")

        return render(request,'mainwebsite/brand-register.html',parms)
    else:
        return redirect('/')


def brand_email_verify(request,id):
    checkisid=Brand.objects.filter(email_verificationid=id).count()
    if checkisid >0:
        get_creator=Brand.objects.get(email_verificationid=id)
        get_creator.is_active_brand=True
        get_creator.is_verified_brand=True
        get_creator.save()
        mass2={"smass":"Your Email Is Verified. You Can Login Now","ulr":"","urltext":"Login Now"}
        return render(request,'mainwebsite/successful.html',mass2)
    else:
        return HttpResponse("Invalid URL")


def creator_login(request):
    if "is_logedin" not in request.session:
        loginform=Creator_loginform()
        params={"form":loginform}
        if request.method=="POST":
            formdata=Creator_loginform(request.POST)
            if formdata.is_valid():
                createrentredemail=request.POST.get("creator_email")
                creatorenteredpass=request.POST.get("creator_password")
                checkisuserexsit=Creator.objects.filter(creator_email=createrentredemail,creator_password=creatorenteredpass).count()
                if(checkisuserexsit>0):
                    request.session["is_logedin"]=True
                    request.session['logedin_email']=createrentredemail
                    request.session['role']="Creator"
                    return redirect('/')
                else:
                    return HttpResponse("You entred Wrong Credentials")
            else:
                params["formerror"] = formdata.errors
        return render(request,'mainwebsite/creator-login.html',params)
    else:
        return redirect('/')


def brand_login(request):
    if "is_logedin" not in request.session:
        loginform=Brand_loginform()
        params={"form":loginform}
        if request.method=="POST":
            formdata=Brand_loginform(request.POST)
            if formdata.is_valid():
                createrentredemail=request.POST.get("brand_email")
                creatorenteredpass=request.POST.get("brand_password")
                checkisuserexsit=Brand.objects.filter(brand_email=createrentredemail,brand_password=creatorenteredpass).count()
                if(checkisuserexsit>0):
                    request.session["is_logedin"]=True
                    request.session['logedin_email']=createrentredemail
                    request.session['role'] = "Brand"
                    messages.info(request, 'Your password has been changed successfully!')

                    return redirect('/')
                else:
                    params["formerror"]="You entred Wrong Credentials"

            else:
                params["formerror"] = formdata.errors
        return render(request,'mainwebsite/brand-login.html',params)
    else:
        return redirect('/')



def logout(request):
    del request.session["is_logedin"]
    del request.session['logedin_email']
    return redirect('/')



#Functionality Functions Starts From Here
def create_campaign(request):
    return render(request,'mainwebsite/create-campaign.html')

def creator_profile(request):
    if "is_logedin" in request.session:
        if request.session["role"]=="Creator":
            creatorsdata = Creator.objects.filter(creator_email=request.session["logedin_email"])
            params={"cdata":creatorsdata}
            return render(request, "mainwebsite/creatorprofile.html",params)
        else:
            return redirect("/")
    else:
        return redirect("/")


def is_user_creator_logedin(request):
    if "is_logedin" in request.session:
        if request.session["role"] == "Creator":
            return True
        else:
            return False
    else:
        return False

def update_creator_profile(request):
    if request.method=="POST":
        if is_user_creator_logedin(request):
            getcreatordata=Creator.objects.get(creator_email=request.session["logedin_email"])
            getcreatordata.creator_first_name=request.POST.get("fname")
            getcreatordata.creator_last_name = request.POST.get("lname")
            getcreatordata.creator_phoneno = request.POST.get("phoneno")
            getcreatordata.creator_adddress = request.POST.get("address")
            #getcreatordata.cre = request.POST.get("location")
            getcreatordata.creator_short_descriptions = request.POST.get("shortdescription")
            getcreatordata.creator_descriptions = request.POST.get("description")
            getcreatordata.save()
            return redirect("/creator-profile")

        else:
            return redirect("/")

def chagepassword(request):
    if request.method=="POST":
        getcreatordata = Creator.objects.get(creator_email=request.session["logedin_email"])
        userpass=getcreatordata.creator_password
        oldpass=request.POST.get("oldpassword")
        if oldpass==userpass:
            getcreatordata.creator_password=request.POST.get("newpassword")
            getcreatordata.save()
            return HttpResponse("Your Password Has Been Changed !")
        else:
            return HttpResponse("Current Password Does Not Match!")


def add_youtube_channel(request):
    if request.method=="POST":
        getcreatordata = Creator.objects.get(creator_email=request.session["logedin_email"])
        creatorid=getcreatordata.id
        youtube_channelid=request.POST.get("channelid")
        youtube_viewcount = request.POST.get("viewcount")
        youtube_commentcount = request.POST.get("commentcount")
        youtube_subscribercount = request.POST.get("subscribercount")
        youtube_videocount = request.POST.get("videocount")
        youtube_channelname = request.POST.get("channelname")
        youtube_profileurl = request.POST.get("profileurl")
        savechanneldata=Youtubechannels(creator_id=getcreatordata,youtube_channelid=youtube_channelid,youtube_profileurl=youtube_profileurl,
                                        youtube_videocount=youtube_videocount,youtube_viewcount=youtube_viewcount,
                                        youtube_channelname=youtube_channelname,youtube_subscribercount=youtube_subscribercount,
                                        youtube_commentcount=youtube_commentcount)
        checkisidexists=Youtubechannels.objects.filter(youtube_channelid=youtube_channelid).count()
        if checkisidexists==0:
            savechanneldata.save()
            return HttpResponse(200)
        else:
            return HttpResponse(209)



def youtubechannelslist(request):
    channels=Youtubechannels.objects.all()

    params={"channels":channels}
    return render(request,"mainwebsite/youtube-creator-lists.html",params)


def submit_campaign(request):
    if request.method=="POST":
        platform="Youtube"
        promotion_type=request.POST.get('promotion_type')
        campaign_category = request.POST.get('campaign_category')
        campaign_product_url = request.POST.get('campaign_product_url')
        is_shiping_product = request.POST.get('is_shiping_product')
        if is_shiping_product=="Yes":
            is_shiping_product=True
        else:
            is_shiping_product=False
        about_product = request.POST.get('about_product')
        campaign_titel = request.POST.get('campaign_titel')
        campaign_listing_time = request.POST.get('campaign_listing_time')
        about_campaign = request.POST.get('about_campaign')
        brif_about_campaign = request.POST.get('brif_about_campaign')
        trageted_country = request.POST.get('trageted_country')
        campaign_budget = request.POST.get('campaign_budget')
        uid=unque_id_generator()
        logedinbrand=Brand.objects.get(brand_email=request.session['logedin_email'])
        savedate=Campaign(platform=platform,campaign_titel=campaign_titel,campaign_country=trageted_country,
                          campaign_type=promotion_type,ads_category=campaign_category,ads_url=campaign_product_url,
                          is_shipping_product=is_shiping_product,about_product_or_service=about_product,
                          campaign_listing_duration=campaign_listing_time,about_campaign=about_campaign,
                          exact_requirement=brif_about_campaign,project_budget=campaign_budget,
                          brand=logedinbrand,traget_audience=trageted_country,unquie_id=uid)
        savedate.save()
        messages.add_message(request, messages.INFO, 'Your Campaign Has Been Submitted For The Review. ')
        return redirect('/success')



def success(request):
    return render(request,'mainwebsite/successful.html')


def created_campaigns(request):
    logedinbrand=Brand.objects.get(brand_email=request.session['logedin_email'])
    allcamp=Campaign.objects.filter(brand=logedinbrand)
    param = {"campaigns": allcamp}
    return render(request,"mainwebsite/created-campaigns.html",param)


def pay_for_campaign(request,id,titel):
    getcamp=Campaign.objects.filter(id=id,campaign_titel=titel,is_payment_done=False).count()
    if getcamp > 0:
        getcamp=Campaign.objects.get(id=id,campaign_titel=titel)
        getcamp.is_payment_done=True
        getcamp.status="Payment Done"
        getcamp.save()
        messages.add_message(request, messages.INFO, 'Thanks,Your Payment Has Been Completed')
        return redirect('/success')
    else:
        return HttpResponse("Error")




def youtuber_channel_details(request,chnnelid):
    channelId = chnnelid
    statdata = youtube.channels().list(part='statistics', id=channelId).execute()
    contentdata = youtube.channels().list(id=channelId, part='contentDetails,statistics').execute()
    playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults=5,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break
    # print(len(videos))
    stats = []
    video_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], videos))
    for i in range(0, len(video_ids), 40):
        res = (youtube).videos().list(id=','.join(video_ids[i:i + 40]), part='statistics').execute()
        stats += res['items']
        videolens = len(videos)
        if (videolens >= 6):
            videolens = 6
        else:
            videolens = videolens
    creator=Creator.objects.get(creator_platform_identification_id=chnnelid)
    youtubechannel=Youtubechannels.objects.get(youtube_channelid=chnnelid)
        # fetching Creator Details Like About Us Form Use Tabel And Channel Name And Thumbnil
    params={"youtubechannel":youtubechannel,"creator":creator,"videolens":videolens,"videos":videos[0:videolens],"stats":stats,"statdata":statdata['items'][0]['statistics']}
    return render(request,"mainwebsite/showcreatorprofile.html",params)



def allcreated_campaigns(request,channelid):
    logedinbrand = Brand.objects.get(brand_email=request.session['logedin_email'])
    allcamp = Campaign.objects.filter(brand=logedinbrand)
    totalcampaigncreated=len(allcamp)
    param = {"campaigns": allcamp,"totalcampaigncreated":totalcampaigncreated,"channel":channelid}
    return render(request, "mainwebsite/allactivecampaign.html", param)

def submit_creator_invitaions(request):
    creatoruniqueid=request.POST.get('creator')
    campainid=request.POST.get('campaignid')
    logedinbrand = Brand.objects.get(brand_email=request.session['logedin_email'])
    uid = unque_id_generator()
    creator=Creator.objects.get(creator_platform_identification_id=creatoruniqueid)
    campign=Campaign.objects.get(id=campainid)
    savedata=Creatorinivitation(campaign_name=campign,creator_name=creator,unquie_id=uid,status="Request Has Been Send To The Creator")
    savedata.save()
    campign.status="Request Has Been Send To The Creator"
    campign.save()
    messages.add_message(request, messages.INFO, 'Your Invitaions Has Been Send To Your Seleted Creator')
    return redirect('/success')



def creator_all_invited_campaigns(request):
    logedincreator = Creator.objects.get(creator_email=request.session['logedin_email'])
    all_invited_campaigns=Creatorinivitation.objects.filter(is_creator_accept_request=False,is_creator_reject_request=False)
    countallinc = len(all_invited_campaigns)
    fallcamp=""
    if countallinc >= 1:
        fallcamp = Campaign.objects.filter(id=all_invited_campaigns[0].campaign_name_id)
    if countallinc > 1:
        for i in range(1,countallinc):
            allcamp = Campaign.objects.filter(id=all_invited_campaigns[i].campaign_name_id)
            fallcamp=fallcamp|allcamp
        param={"totalinvitionsrecived":countallinc,"allchampains":fallcamp}
    else:
        param={"totalinvitionsrecived":countallinc,"allchampains":fallcamp}
    return render(request,"mainwebsite/creator-proposal.html",param)



def invited_campaign_details(request,id,type):
    allcamp = Campaign.objects.filter(id=id,campaign_type=type)
    param = {"campainslists": allcamp}
    return render(request, "mainwebsite/proposaldetails.html", param)



def creator_invitations_response(request,res,campid):
    response=""
    if res==0:
        response=False
    if res ==1:
        response=True

    if response != "":
        if response==True:
            creator_invitaiondetails=Creatorinivitation.objects.get(campaign_name_id=campid)
            creator_invitaiondetails.is_creator_accept_request=True
            creator_invitaiondetails.status="Creator Accepted The Invitations.Work Is In Progress"
            creator_invitaiondetails.save()
            campaign=Campaign.objects.get(id=campid)
            campaign.status="Creator Accepted The Invitations.Work Is In Progress"
            campaign.save()
            messages.add_message(request, messages.INFO, 'Thanks For Accepting The Request. Submit Your Work On Time')
            return redirect('/success')
    else:
        return HttpResponse("Invalid Url")


def creator_on_going_projects(request):
    logedincreator = Creator.objects.get(creator_email=request.session['logedin_email'])
    all_invited_campaigns = Creatorinivitation.objects.filter(is_creator_accept_request=True,is_project_submited=False)
    countallinc = len(all_invited_campaigns)
    fallcamp = ""
    if countallinc >= 1:
        fallcamp = Campaign.objects.filter(id=all_invited_campaigns[0].campaign_name_id)
    if countallinc > 1:
        for i in range(1, countallinc):
            allcamp = Campaign.objects.filter(id=all_invited_campaigns[i].campaign_name_id)
            fallcamp = fallcamp | allcamp
        param = {"totalinvitionsrecived": countallinc, "allchampains": fallcamp}
    else:
        param = {"totalinvitionsrecived": countallinc, "allchampains": fallcamp}
    return render(request, "mainwebsite/creator-ongoing-projects.html", param)



def creator_submit_project(request,id,type):
    allcamp = Campaign.objects.filter(id=id, campaign_type=type)
    param = {"campainslists": allcamp}
    return render(request, "mainwebsite/creator-submit-project.html", param)

def creator_dashboard(request):
    return render(request,"mainwebsite/creator-dashboard.html")

def brand_dashboard(request):
    return render(request,"mainwebsite/brands-dashboard.html")

def submit_project(request,id):
    submiturl=request.POST.get("project-url")
    campaign=Campaign.objects.get(id=id)
    campaign.status="Project Submited. Waiting For Approval."
    campaign.save()

    creatorinv=Creatorinivitation.objects.get(campaign_name_id=campaign)
    creatorinv.status="Project Submited. Waiting For Approval."
    creatorinv.is_project_submited=True
    creatorinv.save()

    savedata=Submitedcampaign(campaign=campaign,submit_url=submiturl)
    savedata.save()
    messages.add_message(request, messages.INFO, 'Your Project Has Been Submitted.Waiting For Client Approval')
    return redirect('/success')


def brand_camping_details(request,id):
    campaign=Campaign.objects.filter(id=id)

    is_project_submitted=Submitedcampaign.objects.filter(campaign_id=id).count()
    snippet = 0
    statscounts = 0
    video_id = 0
    project=0
    if is_project_submitted > 0:
        project=Submitedcampaign.objects.filter(campaign_id=id)
        url_data = project[0].submit_url
        print(Submitedcampaign)
        # Getting If Created Has Been Uploaded The Video Id  For The Client .
        if (url_data != ""):
            splitdata = url_data.split('v=')
            # print(splitdata)
            stats = []
            video_id = splitdata[1]
            video_ids = [video_id]
            for i in range(0, len(video_ids), 40):
                res = (youtube).videos().list(id=','.join(video_ids[i:i + 40]), part='snippet,statistics').execute()
                stats += res['items']
                # print(stats)
                statscounts = stats[0]['statistics']
                snippet = stats[0]['snippet']

    else:
        snippet=0
    params = {"campaigns": campaign, "stats":statscounts,"snippet":snippet, "video_id":video_id,"projectsubmit":project}
    return render(request,"mainwebsite/campaign-details.html",params)


def approve_creator_response(request,id):
    project_submitted=Submitedcampaign.objects.get(campaign_id=id)
    project_submitted.is_brand_approved=True
    project_submitted.brand_approved_date=datetime.datetime.now()
    project_submitted.save()


    creator_invitations=Creatorinivitation.objects.get(campaign_name_id=id)
    creator_invitations.is_project_delivered=True
    creator_invitations.brand_approved_date = datetime.datetime.now()
    creator_invitations.status="Project Delivered"
    creator_invitations.save()

    campaign=Campaign.objects.get(id=id)
    campaign.status="Project Delivered"
    campaign.save()

    messages.add_message(request, messages.INFO, 'Campaign Response Has Been Approved. Thanks For Using Our Service')
    return redirect('/success')



def brand_payment_history(request):
    logedinbrand = Brand.objects.get(brand_email=request.session['logedin_email'])
    campaign=Campaign.objects.filter(brand=logedinbrand,is_payment_done=True)
    params={"camp":campaign}
    return render(request,"mainwebsite/brand-payment-history.html",params)




def allprojects(request):
    allcamp=Campaign.objects.all()
    finalcamp=""
    count=0
    mecheck=0
    for i in allcamp:
        checkiscampaignexist=Creatorinivitation.objects.filter(campaign_name_id=allcamp[count].id,is_creator_reject_request=False).count()
        if checkiscampaignexist >0:
            pass
        else:
            mecheck=mecheck+1
            if mecheck ==1 :
                finalcamp = Campaign.objects.filter(id=allcamp[count].id)
            else:
                filtred_camp=Campaign.objects.filter(id=allcamp[count].id)
                finalcamp=finalcamp | filtred_camp
        count=count+1
    parms={"campaigns":finalcamp}
    return render(request,"mainwebsite/all-projects.html",parms)


def project_details(request,id):
    finalcamp = Campaign.objects.filter(id=id)
    parms = {"campaigns": finalcamp}
    return render(request,"mainwebsite/about-project.html",parms)


def send_campaign_invitaions(request):
    pass



