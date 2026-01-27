<template>
    <div class="container">
        <form @submit.prevent="handleSingUp" class="form">
            <input type="text" v-model="username">
            <input type="email" v-model="email">
            <input type="password" v-model="password">
            <input type="password" v-model="confirm_password">
            <button type="submit">Sing Up</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';


const username = ref("")
const email = ref("")
const password = ref("")
const confirm_password = ref("")

async function handleSingUp() {
    try {
        const data = await axios.post("http://127.0.0.1:8000/auth/singup/", {
            username: username.value,
            email: email.value,
            password: password.value,
            confirm_password: confirm_password.value
        })
        console.log(data)
    } catch (error) {
        console.log(error)
    }
}
</script>

<style scoped>
.form {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
</style>