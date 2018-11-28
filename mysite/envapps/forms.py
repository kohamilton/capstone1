from django import forms
from . import models

class envapp_1(forms.ModelForm):
    class Meta:
        model = models.Storm_App
        fields = ['projname', 'projectlocation', 'owner_fnam', 'owner_lname', 'owner_address', 'phonenumber', 'tceq_noi',
        'site_contact_fname', 'site_contact_lname', 'site_contactphone', 'site_contactemail', 'inspect_fname', 'inspect_lname',
        'inspect_phone', 'inspect_email', 'startdate', 'plat_id', 'lot_id', 'block_id']

class envapp_2(forms.ModelForm):
    class Meta:
        model = models.Ossf
        fields = ['owner_fname', 'owner_lname', 'owner_addr', 'owner_city', 'owner_state', 'owner_zipcode', 'owner_phone',
        'owner_email', 'agent_fname', 'agent_lname', 'agent_addr', 'agent_city', 'agent_state', 'agent_zipcode', 'agent_phone',
        'agent_email', 'subdivision_name', 'plat_id', 'lot_id', 'block_id', 'acre', 'legal_desc', 'prop_addr', 'prop_city', 'prop_zip',
        'startdate', 'single_type', 'single_facility', 'bedrooms', 'sq_ft', 'commercial', 'comm_facility', 'facility_occp', 'facility_seats',
        'facility_beds', 'bldg_costs', 'FEMA_yes', 'FEMA_no', 'SE_yes', 'SE_no', 'site_eval_name', 'sys_descrip', 'tanksize',
        'app_area_size', 'gpd']
