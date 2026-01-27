<template>
  <div class="dropdown-container">
    <div class="dropdown-trigger" @click="toggleDropdown">
      <span>{{ selectedLabel }}</span>
      <svg 
        class="arrow-icon" 
        :class="{ 'arrow-open': isOpen }"
        width="14" 
        height="14" 
        viewBox="0 0 24 24" 
        fill="none"
      >
        <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>

    <transition name="dropdown">
      <div v-if="isOpen" class="dropdown-menu">
        <div class="dropdown-grid">
          <div 
            v-for="item in items" 
            :key="item.id"
            class="dropdown-item"
            @click="selectItem(item)"
          >
            {{ item.label }}
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

const props = defineProps({
  items: {
    type: Array,
    required: true,
    default: () => []
  },
  defaultLabel: {
    type: String,
    default: 'Автомобили'
  }
});

const emit = defineEmits(['select']);

const isOpen = ref(false);
const selectedItem = ref(null);

const selectedLabel = computed(() => {
  return selectedItem.value ? selectedItem.value.label : props.defaultLabel;
});

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const selectItem = (item) => {
  selectedItem.value = item;
  isOpen.value = false;
  emit('select', item);
};

const handleClickOutside = (event) => {
  const dropdown = event.target.closest('.dropdown-container');
  if (!dropdown) {
    isOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
.dropdown-container {
  position: relative;
  display: inline-block;
  min-width: auto;
}

.dropdown-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: 400;
  color: #010101;
  transition: all 0.2s ease;
  user-select: none;
  gap: 8px;
}

.dropdown-trigger:hover {
  color: #000;
}

.arrow-icon {
  transition: transform 0.2s ease;
  color: #2684E5;
}

.arrow-open {
  transform: rotate(90deg);
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  background: white;
  border: 1px solid #E5E5E5;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 1000;
  padding: 20px;
  min-width: 520px;
}

.dropdown-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px 20px;
  row-gap: 16px;
}

.dropdown-item {
  padding: 0;
  cursor: pointer;
  font-size: 14px;
  color: #434343;
  transition: color 0.2s ease;
  background: transparent;
  font-weight: 400;
}

.dropdown-item:hover {
  color: #2684E5;
  background: transparent;
}

/* Transition animations */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from {
  opacity: 0;
  transform: translateY(-8px);
}

.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>