from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import scrape_internships
from .models import Internship
from django.shortcuts import render
import traceback

def home(request):
    return render(request, 'internships/index.html')

@csrf_exempt
def start_scraping(request):
    if request.method == 'POST':
        try:
            # Debug: Log the request body
            print("🔍 Raw Request Body:", request.body.decode('utf-8'))

            data = json.loads(request.body.decode('utf-8'))
            skills = data.get('skills', [])

            # Debug: Log received skills
            print("✅ Skills Received:", skills)

            # Clear previous internships
            Internship.objects.all().delete()

            # Scraping function
            internships = scrape_internships(skills)

            return JsonResponse({'status': 'success', 'message': 'Scraping completed successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print("❌ Error in scraping:", traceback.format_exc())  # Print full error in console
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def get_internships(request):
    # Fetch internships from the database
    internships = list(Internship.objects.values(
        'internship_name',
        'company_name',
        'location',
        'time_period',
        'stipend',
        'internship_link'
    ))
    
    return JsonResponse({
        'internships': internships
    })