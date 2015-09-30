# TouSIX-Manager

Welcome to the TouSIX-Manager project.

Overview
--------

The name TouSIX comes from Toulouse SDN Internet eXchange.

The TouSIX-Manager is an Python application to run with ryu-manager and Django framework for automating openflow generation and BIRD router server configuration. 

An statistic collector and web graphic renderer it also present allowing the IXP member to visualized in details the amount of traffic exchanged  with their peers. 

The TouSIX-Manager has been designed to run on the Toulouse Internet eXchange at the beginning and could be easily extended to run Umbrella Fabric on other IXP topology.

The figure below show the actual TouSIX deployement with 3 PoPs with each an Pica8 P-3290 and seprarated OpenFlow control channel network. Any OpenFflow 1.3 switch hardware or software could be used in theory. 

TouSIX is running in production with Pica8 whitebox OpenFlow switch with PicOS 2.6 in OpenVSwitch mode. PicOS 2.6 provides is able to mainain the last OpenFlow table state even after a reboot or a power outage even is there is no OpenFlow controller  reachable. 



<img src=
http://195.154.106.70/topo_touSIX.021.png" alt="alt text" title="Topology of TouSIX" width="600" height="500" />


<img src="
http://195.154.106.70/soft_archi_tousix.001.png" alt="arch tousix" title="TouSIX software architecture" width="600" height="500" />

    
Installation
------------

This solution has been tested on Debian 8 "Jessie" server, but any GNU/Linux distribtuion which can provide basic depedencies should work.

First, you must provide a MySQL database install pip for Python 3.


    apt-get install python3-pip build-essentials mysql-server mysql-client


Then, you must use pip to install the python packages needed for TouSIX-Manager:
    

    pip install django-bootstrap3 django django-formtools django-fsm django-fsm-admin django-localflavor django-registration-redux


You can directly clone the project to get all the applications for running this project:
    

    git clone https://github.com/umbrella-fabric/TouSIX-Manager.git


In the Django settings file, be sure to activate at least these applications :
    

    INSTALLED_APPS = (
        'django.contrib.admin.apps.SimpleAdminConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admindocs',
        'django.contrib.sites',
        'formtools',
        'localflavor',
        'registration',
        'Authentication',
        'Administration',
        'fsm_admin',
        'Statistics_Manager',
        'BGP_Configuration',
        'Rules_Deployment',
        'Rules_Generation',
        'bootstrap3',
        'Log_Controller',
        'Log_Statistics',
        'Member_Manager',
        'Database',
    )

There is one field to add in the settings file for the security issues:

    ADDRESS_WHITELIST = ['127.0.0.1']

This option is used to verify the access on some critical components of the project. be sure to assign an address only used by your controller.

Then, you can launch the Django application by any method proposed on the Djnago official website.


Contact
-------
Rémy Lapeyrade (remy.lapeyrade@laas.fr)
Marc Bruyère (marc.bruyere@laas.fr)

