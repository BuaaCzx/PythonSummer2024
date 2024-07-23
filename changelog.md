# 修改日志



| 时间          | 修改人 | 具体内容                                                                                                                                                                          |
|-------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7.13  13:35 | UUQ | 新增changelog文件                                                                                                                                                                 |
| 7.13  14:25 | LPR | 增加static/templates目录，并push一个test.html，支持多个代码文件传入（第一个文件为std）、切换功能。还没支持相似代码高亮功能； 14:40 fix by UUQ                                                                               |
| 7.13 15:18  | CZX | README 新增需求                                                                                                                                                                   |
| 7.13 16:01  | UUQ | README 前端需求 & **新增接口文档**                                                                                                                                                      |
| 7.13 21:53  | LPR | 绘制了一个登陆后的主页、封装了侧边栏的css以及时间和内容展示的js，使用方法可以见menu.html（注：需要修改导入的offcanvas的地址）                                                                                                    |
| 7.13 23:48  | LPR | 修改主页，统一为bootstrap和vue，弃用原生js                                                                                                                                                  |
| 7.14   0:18 | UUQ | 将sidebar打包成为vue组件，增加了history页面，**需要/history接口**                                                                                                                               |
| 7.14 20:55  | WDL | 初始化Django项目，增加.gitignore文件，链接template/menu.html至主页                                                                                                                            |
| 7.15 12:42  | UUQ | 修复了history页面CSS样式的bug（单击左侧menu会使得页面布局改变），初步完成logout功能                                                                                                                         |
| 7.15 15:06  | LPR | 增加代码上传界面codesCompare.html支持条形图显示、代码下载、standard代码高亮**（其它代码高亮会有bug，这个需要进一步排查）**，对sidebar的显示进行调整（头像放在上面）。**需要后端传入diff列表**                                                        |
| 7.15 18:10  | LPR | 修改了sidebar样式                                                                                                                                                                  |
| 7.16 14：12  | LPR | 修改了图标的样式，增加人工标记抄袭/取消标记抄袭按钮，可支持将抄袭文件统一导出为zip的功能                                                                                                                                |
| 7.16 17:53  | UUQ | 增加了sidebar.js icon样式，修复了codesCompare页面模板中宽度过窄导致的margin占位div过窄问题<br>**未修复**：codesCompare页面右侧overflow-x滚动时优先级高于左侧offcanvas条、右侧页面宽度较大，是否改为按比例缩放？                                 |
| 7.16 02:36  | WDL | 完成了部分用户登录和认证部分，增加了两个URL：users/login, users/register， **已migrate**                                                                                                             |
| 7.17 12：05  | LPR | 将之前写好的html移动到users目录下，将static移入app中 **（发现有bug，回滚到上一次提交）**                                                                                                                     |
| 7.17 14：43  | LPR | 完成登录注册页面，@WDL 可以看一下我在你的user app里面viewer留言                                                                                                                                     |
| 7.18  0：25  | WDL | _(上述注释中的问题已解决)_ 合并登录与注册功能，链接check/，codesCompare/与对应的template, 和其他的一些小改动                                                                                                       |
| 7.18  1：13  | LPR | demo版本（后续可以用组合式api彻底解决，现在属于能够正常运行）在codesCompare和menu中非django传参部分禁止django渲染，解决上一次push后的问题                                                                                      |
| 7.18  13:40 | CZX | Codecheck 里，在urls和views里加了处理代码重复率的调用接口，一对多返回一个一维的列表，多对多返回一个二维数组，请求里应包含'pairwise'或'single_to_multiple'参数，表示进行哪种查询                                                              |
| 7.18 19：27  | LPR | 对settings进行跨域修改，修改codeCompare.html 现在codeCompare能从后端收到前端发来的东西了，具体数据还没有在前端显示                                                                                                   |
| 7.22 13:00  | czx | 查重加了 diff 的返回，并存进数据库中                                                                                                                                                         |
| 7.22 14:07  | czx | 历史记录返回diff，加了个程设分组查询的代码 group_check_copy.py，有空看看怎么实现的                                                                                                                         |
| 7.22 16:10  | UUQ | 后端增加**/api/logout/接口**，并在前端sidebar组件中**对接完毕**（亲测可用），增加了**对/history/的鉴权**（login required，否则跳转到users/login/，方便测试），**修改history.html，实现了初步的信息展示**（但是跳转和一些具体的信息展示还没有写好，**细节需要讨论**） |
| 7：22 16：24  | LPR | 修改codeCompared                                                                                                                                                                |
| 7：22 16：50  | LPR | 修改codeCompared文件，将diff文件接入，图形化垂直展示（具体见页面，太多了）                                                                                                                                 |
| 7.23 1:01   | WDL | 增加了history每一条比对历史的详细界面（写了初步的html和css），**发现本地logout若提示‘logout at static’则无法登出, 原因不清楚**                                                                                         |
| 7.23 2:47   | czx | 增加分组查询，并进行简单测试                                                                                                                                                                |
| 7.23 13：37  | LPR | 让czx帮新的页面跳转过去的push czx：弄好了，我就不写log了                                                                                                                                           |
| 7.23 16:16  | czx | 修改了分组查询返回的东西，新增返回一个二维矩阵存储文件两两间比对信息在'matrix'字段里，'group'字段返回id                                                                                                                  |
