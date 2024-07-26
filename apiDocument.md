# 接口文档

在本文档中对后端接口的实现进行描述，以便前后端配合。



| 接口名称（路由） | http方法   | 传入数据                                       | 返回数据                         |
| -------------- |----------|--------------------------------------------|------------------------------|
| **例**   /test  | GET/POST | JSON: {testid: "123", expected: "success"} | {status: 200, message: "ok"} |
|api/history_new/| get      | 和以前的history一样 | 见下文，表格不好打                    |
|                |          |                                            |                              |
|                |          |                                            |                              |

```txt
{
"groups": [{
        "group_name": "",
        "group_list": [{
                    "id": history.id,
                    'file1_name': history.file1_name,
                    'file2_name': history.file2_name,
                    'file1': history.file1,
                    'file2': history.file2,
                    'similarity_ratio': history.similarity_ratio,
                    'created_at': history.created_at,
                    'diff_content': history.diff_content,
                    'diff_content_html': history.diff_content_html,
                    'check_type': history.check_type,
                }, 
                ...
        ],
        "created_at": ""
    }]
}
```

