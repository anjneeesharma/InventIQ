'''
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from celery import Celery
import logging
logger = logging.getLogger(__name__)
#from akismet import Akismet

app = Celery(broker='amqp://')


@app.task
def sendEmail(emailid):
	logger.info("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	logger.info(emailid)
	logger.info("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	send_mail('email successfully','created your account','anjnee.k.sharma@gmail.com', ['anjneesharma@gmail.com'],fail_silently=False)
'''