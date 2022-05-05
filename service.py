from flask import Flask, request, jsonify, Response
import os
import json
from sesamutils import sesam_logger

app = Flask(__name__)
logger = sesam_logger("Steve the logger", app=app)

@app.route('/')
def index():
    output = {
        'service': 'Learn Sesam - up and running',
        'remote_addr': request.remote_addr
    }
    return jsonify(output)

###
# Do the magic.
###
@app.route('/company', methods=['GET','POST'])
def get_company_data():
    
    embedded_data = [{"_id": "4849408740",
      "archived": False,
      "createdAt": "2021-09-20T14:01:02.483Z",
      "id": "4849408740",
      "properties": {
        "type": None,
        "name": "Zwipe AS",
        "description": "Our technology comprises a mix of power harvesting & management systems, biometric algorithms, manufacturing and packaging methods to deliver a secure, fast and intuitive authentication experience for users of biometric cards and wearables for payment, access control & ID",
        "about_us": None,
        "address": "Rådhusgata 24",
        "address2": None,
        "annualrevenue": None,
        "city": "Oslo",
        "closedate": None,
        "country": "Norway",
        "createdate": "2021-09-20T14:01:02.483Z",
        "days_to_close": None,
        "domain": "zwipe.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2009",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-05-01T12:58:18.955Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849408740",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": "COMPUTER_SOFTWARE",
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/zwipe/",
        "linkedinbio": "Making convenience safe and secure.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Oslo",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": "Zwipe",
        "web_technologies": None,
        "website": "zwipe.com",
        "zip": "0151"
      },
      "updatedAt": "2022-05-01T12:58:18.955Z"
    }, {
      "_id": "4848090102",
      "archived": False,
      "createdAt": "2021-09-20T06:42:06.233Z",
      "id": "4848090102",
      "properties": {
        "type": None,
        "name": "ADITRO BPO AS",
        "description": "En av Nordens største og mest anerkjente leverandører av lønnssystem, HR-system og outsourcing av lønnstjenester til større selskaper.",
        "about_us": "813285762",
        "address": "POSTBOKS 23",
        "address2": None,
        "annualrevenue": "10000000",
        "city": "Gran",
        "closedate": None,
        "country": "Norway",
        "createdate": "2021-09-20T06:42:06.233Z",
        "days_to_close": None,
        "domain": "aditro.no",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2014",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-26T11:33:11.336Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4848090102",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/aditro",
        "linkedinbio": "En av Nordens største og mest anerkjente leverandører av lønnssystem, HR-system og outsourcing av lønnstjenester til større selskaper.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Oppland",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": "aditroonline",
        "web_technologies": "youtube;typekit_by_adobe;nginx;google_maps;wordpress;google_cloud;google_tag_manager;pardot;wistia;double_click",
        "website": "aditro.no",
        "zip": "2711"
      },
      "updatedAt": "2022-04-26T11:33:11.336Z"
    }, {
      "_id": "4849414393",
      "archived": False,
      "createdAt": "2021-09-20T14:07:10.721Z",
      "id": "4849414393",
      "properties": {
        "type": None,
        "name": "Zovio Inc",
        "description": "Education has transformed. Has your classroom? At Zovio, we know there’s a smarter way to learn by using data, and we have over a decade of experience creating personalized educational opportunities. From finding and enrolling students to optimizing learning solutions, our approach is designed to deliver change that matters.",
        "about_us": "915713769",
        "address": "1811 East Northrop Boulevard",
        "address2": None,
        "annualrevenue": None,
        "city": "Chandler",
        "closedate": None,
        "country": "United States",
        "createdate": "2021-09-20T14:07:10.721Z",
        "days_to_close": None,
        "domain": "zovio.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": "https://www.facebook.com/ZovioSolutions",
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2004",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-22T14:59:47.252Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849414393",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": None,
        "linkedinbio": None,
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Arizona",
        "timezone": "MST/Arizona",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": "zovio",
        "web_technologies": None,
        "website": "zovio.com",
        "zip": "85286"
      },
      "updatedAt": "2022-04-22T14:59:47.252Z"
    }, {
      "_id": "4849463506",
      "archived": False,
      "createdAt": "2021-09-20T14:02:24.010Z",
      "id": "4849463506",
      "properties": {
        "type": None,
        "name": "THEMOON AS",
        "description": "TheMOON offers complete flexibility to create and develop shops which incorporate new design and new solutions on an everyday basis. The size and shape can change as the concept changes. This high tech community provides the solution that matches your exact needs. TheMOON and its unique tools take retailers closer to consumers.",
        "about_us": "991721355",
        "address": "4 Øvre Slottsgate",
        "address2": None,
        "annualrevenue": "1000000",
        "city": "Oslo",
        "closedate": None,
        "country": "Norway",
        "createdate": "2021-09-20T14:02:24.010Z",
        "days_to_close": None,
        "domain": "themoon.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2014",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-20T13:28:20.166Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849463506",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/themoon",
        "linkedinbio": "TheMOON offers complete flexibility to create and develop shops which incorporate new design and new solutions on an everyday basis. The size and shape can change as the concept changes. This high tech community provides the solution that matches your exact needs. TheMOON and its unique tools take retailers closer to consumers.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Oslo",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": None,
        "web_technologies": "microsoft_exchange_online;microsoft_office_365;vimeo;wordpress;outlook;amazon__cloudfront;google_tag_manager;cloud_flare",
        "website": "themoon.com",
        "zip": "0157"
      },
      "updatedAt": "2022-04-20T13:28:20.166Z"
    }, {
      "_id": "4849410239",
      "archived": False,
      "createdAt": "2021-09-20T14:03:36.844Z",
      "id": "4849410239",
      "properties": {
        "type": None,
        "name": "UFORMIA AS",
        "description": "Creating a new generation 3D modeling system, based on real volumes - changing what is made, who makes it and how it is produced.",
        "about_us": "994297139",
        "address": "POSTBOKS 60",
        "address2": None,
        "annualrevenue": "1000000",
        "city": "Lyngseidet",
        "closedate": None,
        "country": "Norway",
        "createdate": "2021-09-20T14:03:36.844Z",
        "days_to_close": None,
        "domain": "uformia.no",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2009",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-19T02:46:11.073Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849410239",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": None,
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/uformia",
        "linkedinbio": "Creating a new generation 3D modeling system, based on real volumes - changing what is made, who makes it and how it is produced.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Troms",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": "Uformia",
        "web_technologies": "amazon_s3;mailchimp;wordpress;woo_commerce",
        "website": "uformia.no",
        "zip": "9069"
      },
      "updatedAt": "2022-04-19T02:46:11.073Z"
    }, {
      "_id": "4849409498",
      "archived": False,
      "createdAt": "2021-09-20T14:01:58.894Z",
      "id": "4849409498",
      "properties": {
        "type": None,
        "name": "Solutiance AG",
        "description": "",
        "about_us": None,
        "address": "Großbeerenstrasse 179",
        "address2": None,
        "annualrevenue": None,
        "city": "Potsdam",
        "closedate": None,
        "country": "Germany",
        "createdate": "2021-09-20T14:01:58.894Z",
        "days_to_close": None,
        "domain": "solutiance.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": "https://www.facebook.com/solutiance",
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "1982",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-16T15:40:17.317Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849409498",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/solutiance/?originalSubdomain=de",
        "linkedinbio": "Plattform-Services für Immobilienbetreiber – Ihr High-Tech-Dachdecker und Ihr Betreiberpflichten-Controller",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": None,
        "timezone": "Europe/Potsdam",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": None,
        "web_technologies": None,
        "website": "solutiance.com",
        "zip": "14482"
      },
      "updatedAt": "2022-04-16T15:40:17.317Z"
    }, {
      "_id": "4849396673",
      "archived": False,
      "createdAt": "2021-09-20T13:39:14.318Z",
      "id": "4849396673",
      "properties": {
        "type": None,
        "name": "Zaptec AS",
        "description": "Vi skal forandre verden til det bedre gjennom å skape en mer bærekraftig og elektrisk fremtid.",
        "about_us": "985095779",
        "address": "Professor Olav Hanssens vei 7A",
        "address2": None,
        "annualrevenue": None,
        "city": "Stavanger",
        "closedate": None,
        "country": "Norway",
        "createdate": "2021-09-20T13:39:14.318Z",
        "days_to_close": None,
        "domain": "zaptec.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2012",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-15T09:14:46.026Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849396673",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/gozaptec/",
        "linkedinbio": "Zaptec is a world leader in cloud-connected charging systems for multiple​ electric vehicles.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Stavanger",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": None,
        "web_technologies": None,
        "website": "zaptec.com",
        "zip": "4021"
      },
      "updatedAt": "2022-04-15T09:14:46.026Z"
    }, {
      "_id": "4849889247",
      "archived": False,
      "createdAt": "2021-09-20T20:22:17.560Z",
      "id": "4849889247",
      "properties": {
        "type": None,
        "name": "Zynerba Pharmaceuticals Inc",
        "description": "Next-generation transdermal cannabinoid therapeutics to improve the lives of patients affected by rare and near-rare neuropsychiatric conditions.",
        "about_us": None,
        "address": "80 W. Lancaster Avenue, Suite 300",
        "address2": None,
        "annualrevenue": None,
        "city": "Devon",
        "closedate": None,
        "country": "United States",
        "createdate": "2021-09-20T20:22:17.560Z",
        "days_to_close": None,
        "domain": "zynerba.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2007",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-14T08:03:04.537Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849889247",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/zynerba-pharmaceuticals/",
        "linkedinbio": "Zynerba (NASDAQ: ZYNE) is dedicated to improving the lives of people with rare and near rare neuropsychiatric disorders where there is a high unmet medical need by pioneering the development and commercialization of next-generation pharmaceutically-produced cannabinoid therapeutics formulated for transdermal delivery.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "",
        "timezone": None,
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": None,
        "web_technologies": None,
        "website": "zynerba.com",
        "zip": "19333"
      },
      "updatedAt": "2022-04-14T08:03:04.537Z"
    }, {
      "_id": "5271855290",
      "archived": False,
      "createdAt": "2022-02-10T07:21:28.489Z",
      "id": "5271855290",
      "properties": {
        "type": None,
        "name": "Techstep ASA",
        "description": "Ved hjelp av mobilteknologi bidrar vi til positive endringer i arbeidslivet. Vi hjelper arbeidstakere å jobbe mer effektivt, trygt og bærekraftig.",
        "about_us": None,
        "address": "Brynsallèen 4",
        "address2": "",
        "annualrevenue": None,
        "city": "Oslo",
        "closedate": None,
        "country": "Norway",
        "createdate": "2022-02-10T07:21:28.489Z",
        "days_to_close": None,
        "domain": "techstep.io",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": None,
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "1996",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-13T09:43:19.281Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "5271855290",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": None,
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/techstep-company/",
        "linkedinbio": "Techstep is a complete mobile technology enabler, making positive changes to the world of work; freeing people to work more effectively, securely and sustainably.",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "Oslo",
        "timezone": "Europe/Oslo",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": None,
        "web_technologies": None,
        "website": "techstep.io",
        "zip": "0667"
      },
      "updatedAt": "2022-04-13T09:43:19.281Z"
    }, {
      "_id": "4849357255",
      "archived": False,
      "createdAt": "2021-09-20T13:36:13.744Z",
      "id": "4849357255",
      "properties": {
        "type": None,
        "name": "DESKTOP.COM AS",
        "description": "Desktop.com offers you the best digital workplace software for organizing and managing teams. Chat, video call, and collaborate across apps from one place today!",
        "about_us": "994956701",
        "address": "NEW YORK",
        "address2": None,
        "annualrevenue": "1000000",
        "city": "New York",
        "closedate": None,
        "country": "United States",
        "createdate": "2021-09-20T13:36:13.744Z",
        "days_to_close": None,
        "domain": "desktop.com",
        "engagements_last_meeting_booked": None,
        "engagements_last_meeting_booked_campaign": None,
        "engagements_last_meeting_booked_medium": None,
        "engagements_last_meeting_booked_source": None,
        "facebook_company_page": "https://www.facebook.com/idealab",
        "facebookfans": None,
        "first_contact_createdate": None,
        "first_deal_created_date": None,
        "founded_year": "2019",
        "googleplus_page": None,
        "hs_analytics_first_timestamp": None,
        "hs_analytics_first_touch_converting_campaign": None,
        "hs_analytics_first_visit_timestamp": None,
        "hs_analytics_last_timestamp": None,
        "hs_analytics_last_touch_converting_campaign": None,
        "hs_analytics_last_visit_timestamp": None,
        "hs_analytics_num_page_views": None,
        "hs_analytics_num_visits": None,
        "hs_analytics_source": None,
        "hs_analytics_source_data_1": None,
        "hs_analytics_source_data_2": None,
        "hs_createdate": None,
        "hs_ideal_customer_profile": None,
        "hs_is_target_account": None,
        "hs_last_booked_meeting_date": None,
        "hs_last_logged_call_date": None,
        "hs_last_open_task_date": None,
        "hs_last_sales_activity_timestamp": None,
        "hs_lastmodifieddate": "2022-04-01T22:24:15.304Z",
        "hs_lead_status": None,
        "hs_num_blockers": "0",
        "hs_num_child_companies": "0",
        "hs_num_contacts_with_buying_roles": "0",
        "hs_num_decision_makers": "0",
        "hs_num_open_deals": "0",
        "hs_object_id": "4849357255",
        "hs_parent_company_id": None,
        "hs_total_deal_value": None,
        "hubspot_owner_assigneddate": None,
        "hubspot_owner_id": None,
        "hubspot_team_id": None,
        "industry": "COMPUTER_SOFTWARE",
        "is_public": "False",
        "lifecyclestage": None,
        "linkedin_company_page": "https://www.linkedin.com/company/desktop-com",
        "linkedinbio": "Desktop.com offers you the best digital workplace software for organizing and managing teams. Chat, video call, and collaborate across apps from one place today!",
        "notes_last_contacted": None,
        "notes_last_updated": None,
        "notes_next_activity_date": None,
        "num_associated_contacts": "0",
        "num_associated_deals": None,
        "num_contacted_notes": None,
        "numberofemployees": None,
        "phone": None,
        "recent_deal_amount": None,
        "recent_deal_close_date": None,
        "state": "NY",
        "timezone": "America/New_York",
        "total_money_raised": None,
        "total_revenue": None,
        "twitterbio": None,
        "twitterfollowers": None,
        "twitterhandle": "Desktop_dot_com",
        "web_technologies": "amazon_s3;google_tag_manager;facebook_connect;google_analytics;intercom;google_apps;hubspot;facebook_advertiser;amazon__cloudfront;cloud_flare",
        "website": "desktop.com",
        "zip": "94133"
      },
      "updatedAt": "2022-04-01T22:24:15.304Z"
    }]

    return Response(json.dumps(embedded_data, separators=(',', ': ')), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)