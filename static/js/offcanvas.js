function updateTime() {
    var now = new Date();
    var formattedTime = now.getFullYear() + '-' +
                        ('0' + (now.getMonth() + 1)).slice(-2) + '-' +
                        ('0' + now.getDate()).slice(-2) + ' ' +
                        ('0' + now.getHours()).slice(-2) + ':' +
                        ('0' + now.getMinutes()).slice(-2) + ':' +
                        ('0' + now.getSeconds()).slice(-2);
    document.getElementById('current-time').textContent = '当前系统时间: ' + formattedTime;
}

function recordLoginTime() {
    var now = new Date();
    var formattedTime = now.getFullYear() + '-' +
                        ('0' + (now.getMonth() + 1)).slice(-2) + '-' +
                        ('0' + now.getDate()).slice(-2) + ' ' +
                        ('0' + now.getHours()).slice(-2) + ':' +
                        ('0' + now.getMinutes()).slice(-2) + ':' +
                        ('0' + now.getSeconds()).slice(-2);
    document.getElementById('login-time').textContent = '登录时间: ' + formattedTime;
}

function showSection(sectionId) {
    var sections = document.getElementsByClassName('section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].classList.remove('active');
    }
    document.getElementById(sectionId).classList.add('active');
}

window.onload = function() {
    updateTime();
    setInterval(updateTime, 1000); // 每秒更新一次时间
    showSection('home'); // 默认显示主页
    recordLoginTime(); // 记录登录时间
};
