export default {
    props: {
        now: String
    },
    template: `
        <div class="sidebar d-flex flex-column flex-shrink-0 p-3 bg-light"
             style="width:20vw; height: 100vh; max-width: 280px; min-width: 200px;">
            <a href="#" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
                <svg class="bi me-2" width="40" height="32">
                    <use xlink:href="#bootstrap"/>
                </svg>
                <span class="fs-4">Duplication Check</span>
            </a>
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
                <li v-for="item in navLinks" :key="item.id" class="nav-item">
                    <a :href="item.link" :class="['nav-link', now==item.title ? 'active': 'link-dark']" aria-current="page">
                        <svg class="bi me-2" width="16" height="16">
                            <use xlink:href="#home"/>
                        </svg>
                        {{item.title}}
                    </a>
                </li>
            </ul>
            <hr>
            <div class="dropdown">
                <a href="#" class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle"
                   id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="https://github.com/mdo.png" alt="" width="32" height="32" class="rounded-circle me-2">
                    <strong>mdo</strong>
                </a>
                <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2">
                    <li><a class="dropdown-item" href="#">New project...</a></li>
                    <li><a class="dropdown-item" href="#">Settings</a></li>
                    <li><a class="dropdown-item" href="#">Profile</a></li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <li><a class="dropdown-item" @click="logout">Sign out</a></li>
                </ul>
            </div>
        </div>
    `,
    data() {
        return {
            navLinks: [
                {
                    id: 0,
                    title: "主页",
                    link: "/"
                },
                {
                    id: 1,
                    title: "代码重复性检测",
                    link: "/check"
                },
                {
                    id: 2,
                    title: "历史记录",
                    link: "/history"
                }
            ]
        }
    },
    methods: {
        logout() {
            alert("logout!");
            let that = this;
            axios.get("/logout", {
                params: {

                }
            }).then((response) => {
                console.log(that);
            }).catch((error) => {
                console.log(error);
            });
        }
    }
}