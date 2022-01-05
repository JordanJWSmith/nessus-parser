from django.forms import model_to_dict
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
import logging, os
from .fileparser.nessusparser import parse
from .fileparser.upload import *
from .fileparser.verify import verify_data
from .fileparser.helpers import hash_file, file_list
from .serializers import policySerializer, serverPreferencesSerializer, pluginPreferencesSerializer, familySelectionSerializer, individualPluginSelectionSerializer, reportSerializer, reportHostSerializer, hostPropertiesSerializer, reportItemSerializer, reportItemPropertiesSerializer
from .models import policy, serverPreferences, pluginPreferences, familySelection, individualPluginSelection, report, reportHost, hostProperties, reportItem, reportItemProperties

logging.basicConfig(level=logging.DEBUG, filename="logging.log")

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        raise MethodNotAllowed('GET')

    if request.method == 'POST':
        serializer = AuthTokenSerializer(
            data=request.data,
            context={
                'request': request,
            },
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': model_to_dict(user)
        })


@api_view(['GET', 'POST'])
def policyViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = policy.objects.get(id=id)
            serializer = policySerializer(item)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = policy.objects.all()
        serializer = policySerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = policySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def serverPreferencesViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = serverPreferences.objects.filter(policy_id=id)
            serializer = serverPreferencesSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = serverPreferences.objects.all()
        serializer = serverPreferencesSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = serverPreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def pluginPreferencesViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = pluginPreferences.objects.filter(policy_id=id)
            serializer = pluginPreferencesSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = pluginPreferences.objects.all()
        serializer = pluginPreferencesSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = pluginPreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def familySelectionViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = familySelection.objects.filter(policy_id=id)
            serializer = familySelectionSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = familySelection.objects.all()
        serializer = familySelectionSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = familySelectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def individualPluginSelectionViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = individualPluginSelection.objects.filter(policy_id=id)
            serializer = individualPluginSelectionSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = individualPluginSelection.objects.all()
        serializer = individualPluginSelectionSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = individualPluginSelectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reportViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = report.objects.get(policy_id=id)
            serializer = reportSerializer(item)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = report.objects.all()
        serializer = reportSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = reportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reportHostViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = reportHost.objects.filter(policy_id=id)
            serializer = reportHostSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = reportHost.objects.all()
        serializer = reportHostSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = reportHostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def hostPropertiesViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = hostProperties.objects.filter(report_host_id=id)
            serializer = hostPropertiesSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = hostProperties.objects.all()
        serializer = hostPropertiesSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = hostPropertiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reportItemViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = reportItem.objects.filter(report_host_id=id)
            serializer = reportItemSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = reportItem.objects.all()
        serializer = reportItemSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = reportItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reportItemPropertiesViews(request, id=None):
    if request.method == 'GET':
        if id:
            item = reportItemProperties.objects.filter(report_item_id=id)
            serializer = reportItemPropertiesSerializer(item, many=True)
            return Response({
                "status": "success", 
                "data": serializer.data
                }, status=status.HTTP_200_OK)

        items = reportItemProperties.objects.all()
        serializer = reportItemPropertiesSerializer(items, many=True)
        return Response({
            "status": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = reportItemPropertiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error", 
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fileHashesViews(request):
    if request.method == 'GET':
        try:
            items = policy.objects.all()
            serializer = policySerializer(items, many=True, context={'fields': ['file_hash']})
            hashes = [log['file_hash'] for log in serializer.data]
            return Response({
                "status": "success",
                "data": hashes
            })
        except Exception as e:
            logging.info('error: ' + str(e))
            return Response({
                "status": "error", 
                "data": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def wipeAppData(request, id=None):
    if request.method == 'DELETE':
        if id: 
            policy_item = policy.objects.get(id=id)
            server_prefs_item = serverPreferences.objects.filter(policy_id=id)
            plugin_prefs_item = pluginPreferences.objects.filter(policy_id=id)
            family_selection_item = familySelection.objects.filter(policy_id=id)
            individual_plugin_selection_item = individualPluginSelection.objects.filter(policy_id=id)
            report_views_item = report.objects.get(policy_id=id)
            report_host_item = reportHost.objects.filter(policy_id=id)

            report_host_ser = reportHostSerializer(report_host_item, many=True)
            report_host_ids = [host['id'] for host in report_host_ser.data]

            for r_h_id in report_host_ids:
                host_properties_item = hostProperties.objects.filter(report_host_id=r_h_id)
                report_item_item = reportItem.objects.filter(report_host_id=r_h_id)
                report_item_ser = reportItemSerializer(report_item_item, many=True)
                report_item_ids = [item['id'] for item in report_item_ser.data]

                for r_i_id in report_item_ids:
                    report_item_properties_item = reportItemProperties.objects.filter(report_item_id=r_i_id)
                    report_item_properties_item.delete()

                report_item_item.delete()
                host_properties_item.delete()

            report_host_item.delete()
            report_views_item.delete()
            individual_plugin_selection_item.delete()
            family_selection_item.delete()
            plugin_prefs_item.delete()
            server_prefs_item.delete()
            policy_item.delete()

            return Response('success')

        policy.objects.all().delete()
        serverPreferences.objects.all().delete()
        pluginPreferences.objects.all().delete()
        familySelection.objects.all().delete()
        individualPluginSelection.objects.all().delete()
        report.objects.all().delete()
        reportHost.objects.all().delete()
        hostProperties.objects.all().delete()
        reportItem.objects.all().delete()
        reportItemProperties.objects.all().delete()

        return Response('success')



@api_view(['POST'])
def fileUploadView(request):
    if request.method == 'POST':
        try:
            myfile = request.FILES['file']
            ext = os.path.splitext(myfile.name)

            if ext[1] != ".nessus":
                raise Exception('File must be .nessus')

            parsed_file = parse(myfile)
            file_hash = hash_file(myfile)

            if file_hash in file_list():
                raise Exception('File already exists in database')
            
            if not verify_data(parsed_file, file_hash):
                raise Exception('Error in data verification')

            policy = policy_upload(parsed_file['policy'], file_hash)
            server_prefs = server_and_plugins_upload(parsed_file['server_and_plugins'], policy['id'])
            family_selection = family_selection_items_upload(parsed_file['family_selection_items'], policy['id'])
            individual_plugin_selection = individual_plugin_selection_items_upload(parsed_file['individual_plugin_selection_items'], policy['id'])
            report = report_name_uploader(parsed_file['report_name'], policy['id'])
            report_section = report_section_uploader(parsed_file['report_hosts'], policy['id'])
            
            return Response({
                "status": "success",
                "data": verify_data(parsed_file, file_hash)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logging.info('error: ' + str(e))
            return Response({
                "status": "error", 
                "data": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
