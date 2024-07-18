from django.shortcuts import render
import difflib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


def home_page(request):
    return render(request, 'menu.html')


def code_check(request):
    return render(request, 'codesCompare.html')


def history(request):
    return render(request, 'history.html')


@method_decorator(csrf_exempt, name='dispatch')
class CodeComparisonView(View):
    def post(self, request, *args, **kwargs):
        # 根据请求中的参数决定执行哪种比较，默认为一对多
        comparison_type = request.POST.get('comparison_type', 'single_to_multiple')

        if comparison_type == 'single_to_multiple':
            return self.single_to_multiple_comparison(request)
        elif comparison_type == 'pairwise':
            return self.pairwise_comparison(request)
        else:
            return JsonResponse({'error': 'Invalid comparison type'}, status=400)

    def single_to_multiple_comparison(self, request):
        files = request.FILES.getlist('files')
        if len(files) < 2:
            return JsonResponse({'error': 'At least two files are required.'}, status=400)

        std_file = files[0]
        std_content = std_file.read().decode('utf-8')
        similarity_results = []

        for file in files[1:]:
            file_content = file.read().decode('utf-8')
            ratio = difflib.SequenceMatcher(None, std_content, file_content).quick_ratio()
            similarity_results.append({
                'file_name': file.name,
                'similarity_ratio': ratio
            })

        return JsonResponse({'results': similarity_results})

    def pairwise_comparison(self, request):
        files = request.FILES.getlist('files')
        if len(files) < 2:
            return JsonResponse({'error': 'At least two files are required for pairwise comparison.'}, status=400)

        file_contents = [file.read().decode('utf-8') for file in files]
        matrix_size = len(file_contents)
        similarity_table = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

        for i in range(matrix_size):
            for j in range(matrix_size):
                if i != j:
                    ratio = difflib.SequenceMatcher(None, file_contents[i], file_contents[j]).quick_ratio()
                    similarity_table[i][j] = ratio
                else:
                    similarity_table[i][j] = 1.0  # 相同文件之间的相似度为1

        file_names = [file.name for file in files]
        results = {
            'file_names': file_names,
            'similarity_table': similarity_table
        }

        return JsonResponse({'results': results})