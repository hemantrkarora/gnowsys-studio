# Copyright (c) 2011,  2012 Free Software Foundation

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.



from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.settings import *
from gstudio.models import *
from objectapp.models import *
from gstudio.methods import *
import hashlib
from django.template.defaultfilters import slugify
import os

def loomstatus(request,sysid):
        print "sys=",sysid
        dic={}
	if request.method=="GET":
		dic=loom_status(sysid)
		print "dic=",dic
	vars=RequestContext(request,{'dic':dic})
	template="gstudio/loomstatus.html"
	return render_to_response(template,vars)

