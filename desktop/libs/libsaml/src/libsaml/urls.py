#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, handler500, url

urlpatterns = patterns(
    'djangosaml2.views',
    url(r'^logout/$', 'logout', name='saml2_logout'),
    url(r'^ls/$', 'logout_service', name='saml2_ls')
)

urlpatterns += patterns('libsaml.views',
                        url(r'^acs/$', 'assertion_consumer_service', name='saml2_acs'),
                        url(r'^login/$', 'login', name='saml2_login'),
                        url(r'^metadata/$', 'metadata', name='saml2_metadata'),
                        url(r'^test/$', 'echo_attributes'))
