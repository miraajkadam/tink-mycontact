from django.db import models
from .user import User

class Contact(models.Model):
	contact_type = models.CharField(max_length=30, default=None, null=True, blank=True)
	full_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	first_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	middle_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	last_name = models.CharField(max_length=30, default=None, null=True, blank=True)

	company = models.CharField(max_length=30, default=None, null=True, blank=True)
	designation = models.CharField(max_length=30, default=None, null=True, blank=True)
	email = models.EmailField(max_length=60, default=None, null=True, blank=True)
	phone = models.CharField(max_length=30, default=None, null=True, blank=True)
	location = models.CharField(max_length=30, default=None, null=True, blank=True)
               gender = models.CharField(max_length=30, default=None, null=True, blank=True)
	title = models.CharField(max_length=30, default=None, null=True, blank=True)
	dept = models.CharField(max_length=30, default=None, null=True, blank=True)
	university = models.CharField(max_length=30, default=None, null=True, blank=True)
	degree = models.CharField(max_length=30, default=None, null=True, blank=True)
	passing_year = models.CharField(max_length=30, default=None, null=True, blank=True)
	college = models.CharField(max_length=30, default=None, null=True, blank=True)
	linkedin_url = models.CharField(max_length=30, default=None, null=True, blank=True)
	facebook_url = models.CharField(max_length=30, default=None, null=True, blank=True)
               skype_id = models.CharField(max_length=30, default=None, null=True, blank=True)
               industry = models.CharField(max_length=30, default=None, null=True, blank=True)
	country = models.CharField(max_length=30, default=None, null=True, blank=True)
	state = models.CharField(max_length=30, default=None, null=True, blank=True)
	zip_code = models.CharField(max_length=30, default=None, null=True, blank=True)
	key_skills = models.CharField(max_length=100, default=None, null=True, blank=True)
	total_exp = models.CharField(max_length=30, default=None, null=True, blank=True)
	years_in_business = models.CharField(max_length=30, default=None, null=True, blank=True)
               cin_no = models.CharField(max_length=30, default=None, null=True, blank=True)
               turnover = models.CharField(max_length=30, default=None, null=True, blank=True)
	incorporation_date = models.CharField(max_length=30, default=None, null=True, blank=True)
	employees = models.CharField(max_length=30, default=None, null=True, blank=True)
	ctc = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf01 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf02 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf03 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf04 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf05 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf06 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf07 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf08 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf09 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf010 = models.CharField(max_length=30, default=None, null=True, blank=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['email', 'phone', 'user'] # Needs Verification
