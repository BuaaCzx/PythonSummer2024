import difflib
from datetime import datetime
from html import escape

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from code_comparison.models import CodeComparisonHistory


# 这行要加，等登录登出功能实现完善之后再加上，并且如果未登录时接收到请求，返回一个错误码
# @login_required
@method_decorator(csrf_exempt, name='dispatch')
class CodeComparisonView(View):
    def post(self, request, *args, **kwargs):
        # print('receive post')
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
        user = request.user

        for file in files[1:]:
            file_content = file.read().decode('utf-8')
            ratio = difflib.SequenceMatcher(None, std_content, file_content).quick_ratio()

            diff_content = get_dif(std_content, file_content)

            # 存表
            CodeComparisonHistory.objects.create(
                user=user,
                file1=std_content,
                file2=file_content,
                file1_name=std_file.name,
                file2_name=file.name,
                similarity_ratio=ratio,
                created_at=datetime.now(),
                diff_content=diff_content
            )
            similarity_results.append({
                'file_name': file.name,
                'similarity_ratio': ratio,
                'diff_content': escape(diff_content)
            })

        # 按重复率从大到小排序
        similarity_results.sort(key=lambda x: x['similarity_ratio'], reverse=False)

        return JsonResponse({'results': similarity_results})

    def pairwise_comparison(self, request):
        # 这个方法可能用不上，需要进一步讨论确定分组查询的需求
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


@login_required
@require_http_methods(["GET"])
def code_comparison_history(request):
    # 查询当前用户历史记录，查表并返回list
    user_history = CodeComparisonHistory.objects.filter(user=request.user).order_by('-created_at')
    history_list = []
    for history in user_history:
        history_list.append({
            'id': history.id,
            'file1_name': history.file1_name,
            'file2_name': history.file2_name,
            'file1': history.file1,
            'file2': history.file2,
            'similarity_ratio': history.similarity_ratio,
            'created_at': history.created_at,
            'diff_content': history.diff_content,
        })
    # 按时间从最近的到最远的顺序排序
    history_list.sort(key=lambda x: x['created_at'], reverse=True)
    return JsonResponse({'history': history_list})


@login_required
@require_http_methods(["GET"])
def api_logout(request):
    # 注销用户
    logout(request)
    return JsonResponse({'status': 200, 'logout': True})


def get_dif(text1, text2):
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    differ = difflib.Differ()
    diff_result = differ.compare(lines1, lines2)
    diff_content = '\n'.join(diff_result)
    return diff_content
