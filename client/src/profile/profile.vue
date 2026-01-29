<template>
    <div class="container">
        <div style="margin: 30px 0px">
            <h1>Profile</h1>

            <div style="margin-bottom: 20px;">
                <p>Logout</p>
                <a-button :loading="loading" @click="handleLogOut" type="primary">logout</a-button>
            </div>

            <form @submit.prevent="handleEmailRetriew">
                <p>Edit Email</p>
                <div style="margin-bottom: 10px;">
                    <input type="email" v-model="email">
                </div>
                <div>
                    <a-button type="primary" html-type="submit">Saqlash</a-button>
                </div>
            </form>

            <form action="">
                <div>
                    <p>Change User</p>
                    <div style="margin-bottom: 10px;">
                        <input type="text" placeholder="username">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <input type="text" placeholder="first_name">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <input type="text" placeholder="last_name">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <input type="file">
                    </div>

                    <a-button type="primary">Saqlash</a-button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import api from '@/utils/axios';
import { message } from 'ant-design-vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/store/useUserStore';

const userStore = useUserStore()
const email = ref(userStore.email)
const loading = ref(false)
const router = useRouter()
const handleLogOut = async () => {
    loading.value = true
    try {

        const refresh_token = localStorage.getItem('refresh_token')

        const { data } = await api.post('auth/logout/', {
            refresh: refresh_token
        })

        if (data.success) {
            localStorage.clear()
            userStore.clear()
            message.success(data.message)
            router.push("/")
        }
    } catch (error) {
        console.log(error)
    } finally {
        loading.value = false
    }
}

const handleEmailRetriew = async () => {
    try {
        const { data } = await api.post("auth/email/",
            {
                old_email: userStore.email,
                email: email.value
            }
        )
        message.success(data.message)
        router.push("email_verify")
        userStore.add_email_edit_token(data.data.token.email_edit_token)
        userStore.add_new_email(email.value)
        console.log(data)
    } catch (error) {
        if (error.response) {
            const errors = error.response.data
            if (errors.old_email) {
                message.error(errors.old_email[0])
            } else if (errors.email) {
                message.error(errors.email[0])
            } else if (errors.dateil) {
                message.error(errors.dateil)
            } else {
                message.error("An error occurred.")
            }

            console.log(error.response)
        } else {
            message.error("No connection to the server.")
            console.log(error)
        }
    } finally {

    }
}
</script>

<style scoped></style>