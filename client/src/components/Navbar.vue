<template>
  <header class="navbar">
    <!-- Top Bar (Desktop) -->
    <div class="top-bar desktop-only">
      <div class="top-bar-container">
        <!-- Left: Main Navigation -->
        <nav class="top-nav">
          <a href="#" class="top-nav-link">Главная</a>
          <a href="#" class="top-nav-link">Каталог</a>
          <a href="#" class="top-nav-link">О нас</a>
          <a href="#" class="top-nav-link">Новости</a>
          <a href="#" class="top-nav-link">Контакты</a>
        </nav>

        <!-- Right: Contact & Social -->
        <div class="top-bar-right">
          <div class="social-links">
            <a href="#" class="social-icon" aria-label="VKontakte">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15.07 2H8.93C3.33 2 2 3.33 2 8.93v6.14C2 20.67 3.33 22 8.93 22h6.14c5.6 0 6.93-1.33 6.93-6.93V8.93C22 3.33 20.67 2 15.07 2zm3.45 14.41h-1.31c-.57 0-.74-.46-1.76-1.48-.89-.89-1.28-1.01-1.5-1.01-.31 0-.4.09-.4.52v1.34c0 .36-.12.58-1.06.58-1.56 0-3.29-.95-4.51-2.72-1.84-2.59-2.34-4.53-2.34-4.93 0-.22.09-.43.52-.43h1.31c.39 0 .54.18.69.6.76 2.2 2.04 4.13 2.56 4.13.2 0 .29-.09.29-.59v-2.29c-.07-1.13-.66-1.22-.66-1.62 0-.18.15-.36.39-.36h2.06c.33 0 .45.18.45.57v3.08c0 .33.15.45.24.45.2 0 .36-.12.72-.48 1.1-1.24 1.89-3.15 1.89-3.15.1-.22.29-.43.68-.43h1.31c.47 0 .57.24.47.57-.15.81-1.92 3.55-1.92 3.55-.17.27-.23.39 0 .69.17.23.73.72 1.1 1.15.68.79 1.2 1.45 1.34 1.91.13.47-.07.71-.61.71z"/>
              </svg>
            </a>
            <a href="#" class="social-icon" aria-label="WhatsApp">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
              </svg>
            </a>
            <a href="#" class="social-icon" aria-label="Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
          </div>

          <div class="contact-links">
            <a href="tel:+77777777777" class="contact-link">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              +7 (777) 777-77-77
            </a>
            <a href="mailto:info@mail.ru" class="contact-link">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
              info@mail.ru
            </a>
          </div>

          <button class="lang-btn">
            RU
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Main Navigation Bar -->
    <div class="main-navbar">
      <div class="main-navbar-container">
        <!-- Logo -->
        <router-link to="/" class="navbar-logo">
          <span class="logo-text">You</span><span class="logo-accent">Car</span>
        </router-link>

        <!-- Breadcrumb Navigation (Desktop) -->
        <nav class="breadcrumb desktop-only" aria-label="Breadcrumb">
          <a href="#" class="breadcrumb-link">
            Автомобили
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </a>
          <a href="#" class="breadcrumb-link">
            Коммерческий транспорт
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </a>
          <a href="#" class="breadcrumb-link">
            Мотоциклы
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </a>
        </nav>

        <!-- Search Bar (Desktop) -->
        <div class="search-bar desktop-only">
          <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/>
            <path d="m21 21-4.35-4.35"/>
          </svg>
          <input type="text" placeholder="Поиск по названию" class="search-input">
        </div>

        <!-- Right Actions (Desktop) -->
        <div class="navbar-actions desktop-only">
          <button class="notification-btn" aria-label="Notifications">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
            </svg>
          </button>

          <div class="user-info">
            <span class="user-name">Хамзат Хусейнович<br>Арсланалиев</span>
          </div>

          <div class="user-badge">XX</div>
        </div>

        <!-- Mobile Actions -->
        <button class="mobile-search-btn mobile-only" aria-label="Search">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/>
            <path d="m21 21-4.35-4.35"/>
          </svg>
        </button>

        <button 
          class="mobile-menu-btn mobile-only" 
          @click="toggleMobileMenu"
          aria-label="Toggle menu"
        >
          <svg v-if="!isMobileMenuOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="12" x2="21" y2="12"/>
            <line x1="3" y1="6" x2="21" y2="6"/>
            <line x1="3" y1="18" x2="21" y2="18"/>
          </svg>
          <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu Overlay -->
    <transition name="slide">
      <div v-if="isMobileMenuOpen" class="mobile-menu">
        <div class="mobile-menu-content">
          <!-- Mobile Search -->
          <div class="mobile-search">
            <input type="text" placeholder="Поиск по названию" class="search-input">
            <button class="search-btn" aria-label="Search">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/>
                <path d="m21 21-4.35-4.35"/>
              </svg>
            </button>
          </div>

          <!-- Mobile Navigation -->
          <nav class="mobile-nav">
            <a href="#" class="mobile-nav-link">Главная</a>
            <a href="#" class="mobile-nav-link">Каталог</a>
            <a href="#" class="mobile-nav-link">О нас</a>
            <a href="#" class="mobile-nav-link">Новости</a>
            <a href="#" class="mobile-nav-link">Контакты</a>
          </nav>

          <!-- Mobile Categories -->
          <div class="mobile-categories">
            <button class="mobile-category-btn" @click="toggleCategory">
              Автомобили
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </button>
            <button class="mobile-category-btn" @click="toggleCategory">
              Коммерческий транспорт
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </button>
            <button class="mobile-category-btn" @click="toggleCategory">
              Мотоциклы
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </button>
          </div>

          <!-- Mobile Contact Info -->
          <div class="mobile-contact">
            <a href="tel:+77777777777" class="mobile-contact-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              +7 (777) 777-77-77
            </a>
            <a href="mailto:info@mail.ru" class="mobile-contact-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
              info@mail.ru
            </a>
          </div>

          <!-- Mobile Social Links -->
          <div class="mobile-social">
            <a href="#" class="mobile-social-icon" aria-label="VKontakte">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15.07 2H8.93C3.33 2 2 3.33 2 8.93v6.14C2 20.67 3.33 22 8.93 22h6.14c5.6 0 6.93-1.33 6.93-6.93V8.93C22 3.33 20.67 2 15.07 2zm3.45 14.41h-1.31c-.57 0-.74-.46-1.76-1.48-.89-.89-1.28-1.01-1.5-1.01-.31 0-.4.09-.4.52v1.34c0 .36-.12.58-1.06.58-1.56 0-3.29-.95-4.51-2.72-1.84-2.59-2.34-4.53-2.34-4.93 0-.22.09-.43.52-.43h1.31c.39 0 .54.18.69.6.76 2.2 2.04 4.13 2.56 4.13.2 0 .29-.09.29-.59v-2.29c-.07-1.13-.66-1.22-.66-1.62 0-.18.15-.36.39-.36h2.06c.33 0 .45.18.45.57v3.08c0 .33.15.45.24.45.2 0 .36-.12.72-.48 1.1-1.24 1.89-3.15 1.89-3.15.1-.22.29-.43.68-.43h1.31c.47 0 .57.24.47.57-.15.81-1.92 3.55-1.92 3.55-.17.27-.23.39 0 .69.17.23.73.72 1.1 1.15.68.79 1.2 1.45 1.34 1.91.13.47-.07.71-.61.71z"/>
              </svg>
            </a>
            <a href="#" class="mobile-social-icon" aria-label="WhatsApp">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
              </svg>
            </a>
            <a href="#" class="mobile-social-icon" aria-label="Instagram">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
          </div>

          <!-- Mobile Auth Buttons -->
          <div class="mobile-auth">
            <button class="btn-register-mobile">Регистрация</button>
            <button class="btn-login-mobile">Войти</button>
          </div>
        </div>
      </div>
    </transition>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
  
  // Prevent body scroll when menu is open
  if (isMobileMenuOpen.value) {
    document.body.style.overflow = 'hidden';
  } else {
    document.body.style.overflow = '';
  }
};

const toggleCategory = (event) => {
  // Category expansion logic here
  console.log('Category clicked:', event.target.textContent);
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.navbar {
  background: #ffffff;
  position: sticky;
  top: 0;
  z-index: 1000;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

/* Top Bar */
.top-bar {
  background: #fafafa;
  border-bottom: 1px solid #ececec;
}

.top-bar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.top-nav {
  display: flex;
  gap: 32px;
  align-items: center;
}

.top-nav-link {
  color: #404040;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
  transition: color 0.2s ease;
  position: relative;
}

.top-nav-link:hover {
  color: #2563eb;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 24px;
}

.social-links {
  display: flex;
  gap: 10px;
}

.social-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #737373;
  transition: color 0.2s ease;
  text-decoration: none;
}

.social-icon:hover {
  color: #2563eb;
}

.contact-links {
  display: flex;
  gap: 16px;
  align-items: center;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #404040;
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s ease;
}

.contact-link:hover {
  color: #2563eb;
}

.lang-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 6px 10px;
  background: transparent;
  border: none;
  color: #404040;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: color 0.2s ease;
}

.lang-btn:hover {
  color: #2563eb;
}

/* Main Navbar */
.main-navbar {
  background: #ffffff;
}

.main-navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 32px;
}

/* Logo */
.navbar-logo {
  font-size: 28px;
  font-weight: 700;
  text-decoration: none;
  display: flex;
  align-items: center;
  white-space: nowrap;
  transition: transform 0.2s ease;
}

.navbar-logo:hover {
  transform: scale(1.02);
}

.logo-text {
  color: #2563eb;
}

.logo-accent {
  color: #1e40af;
}

/* Breadcrumb */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}

.breadcrumb-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #404040;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
  transition: color 0.2s ease;
}

.breadcrumb-link:hover {
  color: #2563eb;
}

.breadcrumb-link svg {
  flex-shrink: 0;
}

/* Search Bar */
.search-bar {
  position: relative;
  width: 100%;
  max-width: 340px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: #999;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 10px 16px 10px 44px;
  border: 1px solid #e5e5e5;
  border-radius: 8px;
  font-size: 14px;
  color: #404040;
  background: #fafafa;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #2563eb;
  background: white;
}

.search-input::placeholder {
  color: #a3a3a3;
}

/* Navbar Actions */
.navbar-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-left: auto;
}

.notification-btn {
  background: none;
  border: none;
  color: #404040;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
  position: relative;
}

.notification-btn:hover {
  color: #2563eb;
}

.user-info {
  display: flex;
  align-items: center;
}

.user-name {
  font-size: 13px;
  color: #404040;
  line-height: 1.4;
  text-align: right;
}

.user-badge {
  width: 36px;
  height: 36px;
  background: #2563eb;
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
}

/* Mobile Only Elements */
.mobile-only {
  display: none;
}

.mobile-menu-btn,
.mobile-search-btn {
  background: none;
  border: none;
  color: #404040;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.mobile-menu-btn:hover,
.mobile-search-btn:hover {
  color: #2563eb;
}

/* Mobile Menu */
.mobile-menu {
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  background: white;
  overflow-y: auto;
  z-index: 999;
}

.mobile-menu-content {
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.mobile-search {
  position: relative;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-bottom: 20px;
  border-bottom: 1px solid #f3f4f6;
}

.mobile-nav-link {
  padding: 14px 16px;
  color: #404040;
  text-decoration: none;
  font-size: 16px;
  font-weight: 400;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.mobile-nav-link:hover {
  background: #f9fafb;
  color: #2563eb;
}

.mobile-categories {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-bottom: 20px;
  border-bottom: 1px solid #f3f4f6;
}

.mobile-category-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 16px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: #404040;
  font-size: 15px;
  font-weight: 400;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
}

.mobile-category-btn:hover {
  background: white;
  border-color: #2563eb;
  color: #2563eb;
}

.mobile-contact {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-bottom: 20px;
  border-bottom: 1px solid #f3f4f6;
}

.mobile-contact-link {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #404040;
  text-decoration: none;
  font-size: 15px;
  padding: 8px;
  transition: color 0.2s ease;
}

.mobile-contact-link:hover {
  color: #2563eb;
}

.mobile-social {
  display: flex;
  gap: 12px;
  justify-content: center;
  padding-bottom: 20px;
  border-bottom: 1px solid #f3f4f6;
}

.mobile-social-icon {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #737373;
  background: #f3f4f6;
  border-radius: 10px;
  transition: all 0.2s ease;
  text-decoration: none;
}

.mobile-social-icon:hover {
  color: #2563eb;
  background: #dbeafe;
}

.mobile-auth {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.btn-register-mobile,
.btn-login-mobile {
  padding: 14px 20px;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  width: 100%;
}

.btn-register-mobile {
  background: #2563eb;
  color: white;
}

.btn-register-mobile:hover {
  background: #1d4ed8;
}

.btn-login-mobile {
  background: transparent;
  color: #404040;
  border: 1px solid #e5e7eb;
}

.btn-login-mobile:hover {
  background: #f9fafb;
}

/* Animations */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateY(-20px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Desktop Only */
.desktop-only {
  display: flex;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .desktop-only {
    display: none !important;
  }
  
  .mobile-only {
    display: flex;
  }
  
  .top-bar {
    display: none;
  }
  
  .main-navbar-container {
    padding: 12px 16px;
    gap: 12px;
  }
  
  .navbar-logo {
    font-size: 24px;
  }
}

@media (max-width: 768px) {
  .main-navbar-container {
    padding: 12px 16px;
  }
  
  .navbar-logo {
    font-size: 22px;
  }
}
</style>