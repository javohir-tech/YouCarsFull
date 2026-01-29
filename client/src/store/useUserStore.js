import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
    state: () => (
        {
            username: localStorage.getItem('username') || "",
            access_token: localStorage.getItem("access_token") || "",
            email: localStorage.getItem("email") || "",
            verify_token: localStorage.getItem("verify_token") || "",
            edit_password_token: localStorage.getItem("edit_password_token") || ""
        }
    ),
    getters: {
        get_user: (state) => state.username,
        avatarUrl: (state) => `https://api.dicebear.com/9.x/initials/svg?seed=${state.username}`
    },
    actions: {
        add_user(username, email, access_token) {
            this.username = username
            this.email = email
            this.access_token = access_token
            localStorage.setItem("username", username)
            localStorage.setItem("email", email)
        },

        add_email(email) {
            this.email = email
            localStorage.setItem("email", email)
        },
        add_verify_token(verify_token) {
            this.verify_token = verify_token
            localStorage.setItem("verify_token", verify_token)
        },
        remove_verify_token() {
            this.verify_token = "",
                localStorage.removeItem("verify_token")
        },
        add_edit_password_token(edit_password_token) {
            this.edit_password_token = edit_password_token
            localStorage.setItem("edit_password_token", edit_password_token)
        },
        remove_edit_password_token() {
            this.edit_password_token = "",
                localStorage.removeItem("edit_password_token")
        },
        clear() {
            this.username = ""
            this.email = ""
            this.access_token = ""
            this.verify_token = ""
            this.edit_password_token = ""
        }
    }

})