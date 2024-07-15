# 修改日志



| 时间        | 修改人 | 具体内容                                                     |
| ----------- | ------ | ------------------------------------------------------------ |
| 7.13  13:35 | UUQ    | 新增changelog文件                                            |
| 7.13  14:25 | LPR    | 增加static/templates目录，并push一个test.html，支持多个代码文件传入（第一个文件为std）、切换功能。还没支持相似代码高亮功能； 14:40 fix by UUQ |
| 7.13 15:18  | CZX    | README 新增需求                                              |
| 7.13 16:01  | UUQ    | README 前端需求 & **新增接口文档**                           |
| 7.13 21:53  | LPR    | 绘制了一个登陆后的主页、封装了侧边栏的css以及时间和内容展示的js，使用方法可以见menu.html（注：需要修改导入的offcanvas的地址） |
| 7.13 23:48  | LPR    | 修改主页，统一为bootstrap和vue，弃用原生js                   |
| 7.14   0:18 | UUQ    | 将sidebar打包成为vue组件，增加了history页面，**需要/history接口** |
| 7.14 20:55  | WDL    | 初始化Django项目，增加.gitignore文件，链接template/menu.html至主页 |
| 7.15 12:42  | UUQ    | 修复了history页面CSS样式的bug（单击左侧menu会使得页面布局改变），初步完成logout功能 |
| 7.15 15:06  | LPR    | 增加代码上传界面codesCompare.html支持条形图显示、代码下载、standard代码高亮**（其它代码高亮会有bug，这个需要进一步排查）**，对sidebar的显示进行调整（头像放在上面）。**需要后端传入diff列表** |

