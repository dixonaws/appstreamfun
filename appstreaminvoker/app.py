from chalice import Chalice
import boto3
import json

app = Chalice(app_name='appstreaminvoker')

client=boto3.client('appstream', region_name='eu-central-1')

@app.route('/')
def index():
    # create a streaming URL for the app

    # list the available apps in a JSON object
    dict_response={}
    dict_available_apps={}
    dict_available_apps['Notepad++']='notepad'
    dict_available_apps['Google Chrome']='chrome_x64_v75.0.3770.100'
    dict_response['AvailableApps']=dict_available_apps

    return(json.dumps(dict_response))


@app.route('/notepad')
def notepad():
    # create a streaming URL for the app
    response = client.create_streaming_url(StackName='dixonaws-Appstream2Fleet-on',FleetName='dixonaws-Appstream2fleet-on', UserId='dixonaws',ApplicationId='notepad++')

    # print the url to CloudWatch
    print(response['StreamingURL'])

    dict_response={}
    dict_response['StreamingURL']=response['StreamingURL']

    return(json.dumps(dict_response))

@app.route('/chrome')
def chrome():
    # create a streaming URL for the app
    response = client.create_streaming_url(StackName='dixonaws-Appstream2Fleet-on',
                                           FleetName='dixonaws-Appstream2fleet-on', UserId='dixonaws',
                                           ApplicationId='chrome_x64_v75.0.3770.100')

    # print the url to CloudWatch
    print(response['StreamingURL'])

    dict_response = {}
    dict_response['StreamingURL'] = response['StreamingURL']

    return (json.dumps(dict_response))

