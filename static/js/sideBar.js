export default {
    props: {
        now: String,
        username: String
    },
    template: `
        <div class="sidebar-container">
           <div class="sidebar d-flex flex-column flex-shrink-0 p-3 bg-light"
                style="width: 20vw; max-width: 280px; min-width: 200px; position: fixed; left: 0; top: 0; height: 100vh;">
                <a href="#" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
                    <svg class="bi me-2" width="40" height="32">
                        <use xlink:href="#bootstrap"/> 
                    </svg>
                    <span class="fs-4">Duplication Check</span>
                </a>
                <hr>
                <ul class="nav nav-pills flex-column mb-auto">
                    <div class="dropdown">
                        <a href="#" class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle"
                           id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false" style="margin-bottom: 30px;">
                            <img src="https://buaaczx.github.io/image/background.jpg" alt="" width="32" height="32" class="rounded-circle me-2">
                            <strong>{{ username }}</strong>
                        </a>
                        <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2">
                            <li><a class="dropdown-item" href="#">New project...</a></li>
                            <li><a class="dropdown-item" href="#">Settings</a></li>
                            <li><a class="dropdown-item" href="#">Profile</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" @click="logout">退出登录</a></li>
                        </ul>
                    </div>
                    <li v-for="item in navLinks" :key="item.id" class="nav-item">
                        <a :href="item.link" :class="['nav-link', now == item.title ? 'active' : 'link-dark']" aria-current="page">

                            <i :class="['bi', item.icon] "></i>
                            &nbsp{{item.title}}
                        </a>
                    </li>
                </ul>
                <hr>
            </div>
        </div>
    `,
    data() {
        return {
            navLinks: [
                {
                    id: 0,
                    title: "主页",
                    link: "/",
                    icon:"bi-house"
                },
                {
                    id: 1,
                    title: "代码重复检测",
                    link: "/check",
                    icon:"bi-search"
                },
                {
                    id: 2,
                    title: "分组检测",
                    link: "/group",
                    icon:"bi-bag-dash"
                },
                {
                    id: 3,
                    title: "历史记录",
                    link: "/history",
                    icon:"bi-clock-history"
                }

            ]
        }
    },
    methods: {
        logout() {
            let that = this;
            axios.get("/api/logout", {
                params: {}
            }).then((response) => {
                console.log(response);
                if (response.status === 200 && response.data.logout === true) {
                    window.location.href = '/users/login/';
                }
            }).catch((error) => {
                console.log(error);
            });
        }
    }
}
