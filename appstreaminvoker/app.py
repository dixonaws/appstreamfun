from chalice import Chalice
import boto3
import json

app = Chalice(app_name='appstreaminvoker')

client=boto3.client('appstream', region_name='eu-central-1')


@app.route('/')
def index():
    # create a streaming URL for the app
    response = client.create_streaming_url(StackName='dixonaws-AppstreamTestStack',FleetName='dixonaws-Appstream2Fleet', UserId='dixonaws',ApplicationId='notepad++')

    # print the url to CloudWatch
    print(response['StreamingURL'])

    dict_response={}
    dict_response['StreamingURL']=response['StreamingURL']

    return(json.dumps(dict_response))


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
