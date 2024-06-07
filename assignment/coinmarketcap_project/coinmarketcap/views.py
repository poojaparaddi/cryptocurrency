from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .tasks import scrape_coin_data
from celery.result import AsyncResult
class StartScraping(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        job = []
        for coin in coins:
            job.append(scrape_coin_data.delay(coin))
        job_ids = [j.id for j in job]
        return Response({"job_id": job_ids}, status=status.HTTP_202_ACCEPTED)
class ScrapingStatus(APIView):
    def get(self, request, job_id):
        result = AsyncResult(job_id)
        if result.ready():
            return Response(result.result, status=status.HTTP_200_OK)
        else:
            return Response({"status": "pending"}, status=status.HTTP_200_OK)
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import scrape_coin_data

@api_view(['POST'])
def start_scraping(request):
    coin_acronyms = request.data.get('coin_acronyms', [])
    for coin_acronym in coin_acronyms:
        scrape_coin_data.delay(coin_acronym)
    return Response({"message": "Scraping job started successfully."})

@api_view(['GET'])
def scraping_status(request, job_id):
    # Implement logic to retrieve and return the status and data for the specified job ID
    return Response({"job_id": job_id, "status": "In progress", "data": "D"})