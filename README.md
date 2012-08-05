python-firebase
===============
http://github.com/mikexstudios/python-firebase
by Michael Huynh (mike@mikexstudios.com)

Purpose:
-------

A very simple wrapper for Firebase's REST API.

How to use
----------

1.  Install python-firebase using pip:

        pip install -e git://github.com/mikexstudios/python-firebase.git#egg=python-firebase
        
    or with easy_install (not recommended):

        easy_install http://github.com/mikexstudios/python-firebase/tarball/master

    Note that python-firebase depends on requests (http://python-requests.org),
    a REST/http client for python. If you used pip or easy_install, the
    dependency should automatically be installed. 

2.  Then simply import firebase at the top of your python script:

        from firebase import Firebase

    and then instantiate Firebase, passing in your root url:

        f = Firebase('http://demo.firebase.com/SampleChat')

    Now call the different methods of the Firebase class (see the Firebase
    REST API page: http://www.firebase.com/docs/rest-api.html and the source of
    `firebase/__init__.py` for what methods are available and how to call
    them). For example, to push a list of data:

        r = f.push('message_list', {'user_id': 'wilma', 'text': 'Hello'})

    The response `r` is a dictionary containing Firebase's REST response:

        {"name":"-INOQPH-aV_psbk3ZXEX"}


License
-------

django-firebase is BSD licensed.

