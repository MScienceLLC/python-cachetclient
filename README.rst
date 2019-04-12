About
=====
python-mscience-cachetclient_ is a client and library that can be used to communicate
with OUR (M Science) Cachet_ API. This is forced from Cachet and includes things that
we use to track the health and status of Data Pipelines that run in Airflow.

It is forked from https://github.com/dmsimard/python-cachetclient

Disclaimer: This is a work in progress. Please feel free to provide feedback
and contribute to the project !

.. _python-mscience-cachetclient: https://github.com/MScienceLLC/python-mscience-cachetclient
.. _Cachet: https://cachethq.io/

Documentation
=============
Not much...

Install from Source as bellow... Then::

    import mscience_cachetclient.cachet as cachet

    factory = cachet.Factory(api_token=TOKEN, endpoint=ENDPOINT)
    ping = factory.get("Ping")
    print(ping.get())

TL;DR: See the provided `example file`_.

.. _example file: https://github.com/MScienceLLC/python-mscience-cachetclient/blob/master/simple-test.py

Installing
==========
From source::

    pip install git+https://github.com/MScienceLLC/python-mscience-cachetclient

Author
======
Ben Tallman (btallman@mscience.com)

Thanks to: David Moreau Simard

Copyright
=========
Copyright 2016 Red Hat, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
