import {ref, onMounted} from 'vue';

export default {
    props: {
        now: String,
    },
    created() {
        this.checkLocalLoginStatus();
    },
    template: `
        <div class="sidebar-container">
           <div class="sidebar d-flex flex-column flex-shrink-0 p-3 bg-light"
                style="width: 20vw; max-width: 280px; min-width: 200px; position: fixed; left: 0; top: 0; height: 100vh;">
                <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
                    <i class="bi bi-file-earmark-code fs-2"></i>
                    <span class="fs-5">Duplication Check</span>
                </a>
                <hr>
                <ul class="nav nav-pills flex-column mb-auto">
                    
                    <li v-for="item in navLinks" :key="item.id" class="nav-item">
                        <a :href="item.link" :class="['nav-link', now == item.title ? 'active' : 'link-dark']" aria-current="page">

                            <i :class="['bi', item.icon] "></i>
                            &nbsp{{item.title}}
                        </a>
                    </li>
                    
                </ul>
                <hr>
                <div v-if="isLoggedIn" class="dropdown">
                        <a href="#" class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle"
                           id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false" style="margin-bottom: 30px;">
                            <img :src="avatar_url" alt="" width="32" height="32" class="rounded-circle me-2">
                            <strong>{{ username }}</strong>
                        </a>
                        <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2">
                            <li><a class="dropdown-item" href="#">New project...</a></li>
                            <li><a class="dropdown-item" href="#">Settings</a></li>
                            <li><a class="dropdown-item" href="/users/profile/">个人资料</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" @click="logout">退出登录</a></li>
                        </ul>
                    </div>
            </div>
        </div>
    `,
    data() {
        return {
            isLoggedIn: false,
            username: "",
            avatar_url: "/media/avatars/default.jpg", //https://buaaczx.github.io/image/background.jpg
            navLinks: [
                {
                    id: 0,
                    title: "主页",
                    link: "/",
                    icon: "bi-house"
                },
                {
                    id: 1,
                    title: "代码重复检测",
                    link: "/check",
                    icon: "bi-search"
                },
                {
                    id: 2,
                    title: "分组检测",
                    link: "/group",
                    icon: "bi-bag-dash"
                },
                {
                    id: 3,
                    title: "历史记录",
                    link: "/history",
                    icon: "bi-clock-history"
                }

            ]
        }
    },
    methods: {
        logout: function() {
            let that = this;
            axios.get("/users/logout", {
                params: {}
            }).then((response) => {
                console.log(response);
                if (response.status === 200 && response.data.logout === true) {
                    localStorage.removeItem('isLoggedIn');
                    localStorage.removeItem('username');
                    localStorage.removeItem('avatar');
                    window.location.href = '/users/login/';
                }
            }).catch((error) => {
                console.log(error);
            });
        },
        checkLocalLoginStatus() {
            const storedIsLoggedIn = localStorage.getItem('isLoggedIn');
            const storedUsername = localStorage.getItem('username');
            const storedAvatar = localStorage.getItem('avatar');
            console.log("local:" + storedIsLoggedIn);
            if (storedIsLoggedIn === 'true') {
                this.isLoggedIn = true;
                this.username = storedUsername;
            } else {
                this.checkLoginStatus();
            }
        },
        async checkLoginStatus()  {
            try {
                const response = await axios.get('/users/check_login');
                // { "login": true }
                this.isLoggedIn = response.data.login;
                if (this.isLoggedIn) {
                    this.username = response.data.username;
                    this.avatar_url = response.data.avatar;
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('username', response.data.username);
                    localStorage.setItem('avatar', response.data.avatar);
                } else {
                    localStorage.removeItem('isLoggedIn');
                    localStorage.removeItem('username');

                    localStorage.removeItem('avatar');
                }
                console.log("成功检测，当前登录状态为：" + response.data.login)
            } catch (error) {
                console.log("error:" + error)
                this.isLoggedIn = false;
                localStorage.removeItem('isLoggedIn');
                localStorage.removeItem('username');
            }
        }
    },

}
