from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSetSerializer
import numpy as np
import pandas as pd


class PearsonCorrelationView(APIView):
    def post(self, request):
        serializer = DataSetSerializer(data=request.data)
        if serializer.is_valid():
            data1, data2 = None, None

            if 'file' in request.FILES:
                file = request.FILES['file']
                try:
                    df = pd.read_excel(file)
                    data1 = df.iloc[:, 0].tolist()
                    data2 = df.iloc[:, 1].tolist()
                except Exception as e:
                    return Response({"error": f"Error processing file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                data1 = serializer.validated_data.get('data1', None)
                data2 = serializer.validated_data.get('data2', None)

            if not data1 or not data2:
                return Response({"error": "Both data1 and data2 are required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                correlation = np.corrcoef(data1, data2)[0, 1]
                return Response({'pearson_correlation': correlation}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"Error calculating Pearson correlation: {str(e)}"},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def root_view(request):
    return HttpResponse("Welcome to the Pearson Correlation API. Use /api/pearson/ to access the API.")

