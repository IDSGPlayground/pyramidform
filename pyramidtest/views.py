from pyramid.response import Response
from pyramid.view import view_config
"""import colander
from deform import Form
from deform import ValidationFailure """

from sqlalchemy.exc import DBAPIError

from .models import (
    AccountForm,
    DBSession,
    MyModel,
    )
"""
class Submission(colander.MappingSchema):
    firstname = colander.SchemaNode(colander.String())   
 """

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one':one, 'project':'pyramid-test'}

@view_config(renderer='templates/testform.pt', route_name='form')
def form_view(request):
    replyto = ''
    usertype = ''
    lastname = 'adfadsf'
    firstname = 's'
    nickname = ''
    dept = ''
    if 'form.submitted' in request.params:
        replyto = request.params['reply-to']
        usertype = request.params['usertype']
        lastname = request.params['lastname']
        firstname = request.params['firstname']
        nickname = request.params['nickname']
        dept = request.params['dept']



    return {'url':'Results', 'name':'Doug', 'email':'doug@eecs',
            'replyto': replyto}

@view_config(renderer='templates/results.pt', route_name='Results')
def result_view(request):
    
    result_name = DBSession.query(AccountForm).all()[-1].firstname
    return{'replyto':result_name}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid-test_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

