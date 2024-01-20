from linkedin_OOP import LinkedinJobs

USER_EMAIL = "rxccxcxcxcxcxxom"
USER_PASS = "1xxxxxxxxx710"
JOB_TITLE = "python developer"
JOB_LOCATION = "usa"

user = LinkedinJobs(login_mail=USER_EMAIL, login_pass=USER_PASS)
user.login_page()
user.home_page(job_detail=JOB_TITLE, job_location=JOB_LOCATION)