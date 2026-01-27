<template>
    <div>
        <Navbar />
        <main>
            <RouterView />
        </main>
        <Footer />
    </div>
</template>

<script setup>
import { Navbar, Footer } from '@/components';
import { RouterView } from 'vue-router';
</script>

<style scoped></style>