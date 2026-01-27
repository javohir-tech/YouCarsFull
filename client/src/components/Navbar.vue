<template>
    <header class="navbar">
        <!-- ///////////////////////////////// -->
        <!-- ////////// UNDER NAVBAR /////// -->
        <!-- /////////////////////////////// -->
        <div class="under_navbar">
            <div class="container">
                <Row align="center">
                    <Col :span="14">
                        <ul class="menu_list">
                            <li><router-link>Главная</router-link></li>
                            <li><router-link>Каталог</router-link></li>
                            <li><router-link>О нас</router-link></li>
                            <li><router-link>Новости</router-link></li>
                            <li><router-link>Контакты</router-link></li>
                        </ul>
                    </Col>
                    <Col :span="10">
                        <div class="under_rigth">
                            <div class="icons">
                                <a href="#">
                                    <InstagramOutlined class="icon" />
                                </a>
                                <a href="#">
                                    <WhatsAppOutlined class="icon" />
                                </a>
                                <a href="#">
                                    <LinkedinOutlined class="icon" />
                                </a>
                            </div>
                            <div>
                                <a href="#">
                                    <PhoneOutlined class="icon" />
                                    <span> +77 123 29 04</span>
                                </a>
                            </div>
                            <div>
                                <a href="#">
                                    <MailOutlined class="icon" />
                                    <span> suvonovjavohir625@gmail.com</span>
                                </a>
                            </div>
                            <div>
                                <a-select ref="select" v-model:value="value1" style="width: 100px" @focus="focus"
                                    @change="handleChange">
                                    <a-select-option value="ru">RU</a-select-option>
                                    <a-select-option value="en">EN</a-select-option>
                                    <a-select-option value="uz">UZ</a-select-option>
                                </a-select>
                            </div>
                        </div>
                    </Col>
                </Row>
            </div>
        </div>
        <!-- ///////////////////////////////// -->
        <!-- ////////// BOTTOM NAVBAR /////// -->
        <!-- /////////////////////////////// -->
        <div class="bottom_navbar">
            <div class="container">
                <Row align="middle">
                    <Col :span="19">
                        <div class="bottom_left">
                            <div class="banner">
                                <span class="you">You</span>
                                <span class="car">Car</span>
                            </div>
                            <div class="dropdown-wrapper">
                                <DropdownMenu :items="carItems" defaultLabel="Автомобили" @select="handleCarSelect" />
                                <DropdownMenu :items="carItems" defaultLabel="Коммерческий транспорт"
                                    @select="handleCarSelect" />
                                <DropdownMenu :items="carItems" defaultLabel="Мотоциклы" @select="handleCarSelect" />
                            </div>
                            <div class="search">
                                <a-input-search v-model:value="value" placeholder="input search text"
                                    style="width: 400px" @search="onSearch" />
                            </div>
                            <div class="message">
                                <a-badge count="0">
                                    <CommentOutlined class="messanger" />
                                </a-badge>
                            </div>
                        </div>
                    </Col>
                    <Col :span="5">
                        <div class="bottom_rigth">
                            <Button>Войти</Button>
                            <Button type="primary">Регистрация</Button>
                        </div>
                    </Col>
                </Row>
            </div>
        </div>
    </header>
</template>

<script setup>
import { Button, Row, Col, Collapse } from 'ant-design-vue';
import { CommentOutlined, InstagramOutlined, LinkedinOutlined, MailOutlined, PhoneOutlined, WhatsAppOutlined } from "@ant-design/icons-vue"
import { ref } from 'vue';
import { DropdownMenu } from '.';

const value1 = ref('RU');

// Dropdown uchun ma'lumotlar
const carItems = ref([
    { id: 1, label: 'Авто из США' },
    { id: 2, label: 'Авто из Европы' },
    { id: 3, label: 'Авто из Кореи' },
    { id: 4, label: 'Авто из Китая' },
    { id: 5, label: 'Авто из ОАЭ' },
]);

const focus = () => {
    console.log('focus');
};

const handleChange = value => {
    console.log(`selected ${value}`);
};

// Dropdown select handler
const handleCarSelect = (item) => {
    console.log('Tanlangan avtomobil:', item);
    // Bu yerda kerakli logikani qo'shishingiz mumkin
};
</script>

<style scoped>
/* .navbar {} */
/* UNDER NAVBAR */
.under_navbar {
    background-color: #F6F6F6;
    padding: 15px 0;
}


.menu_list {
    display: flex;
    height: 100%;
    gap: 15px;
    padding-left: 0;
    margin-bottom: 0;
    align-items: center;

    li {
        list-style: none;
        font-weight: 500;
        font-size: 14px;
        color: #434343;

        a {
            color: inherit;
        }
    }
}

.under_rigth {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 20px;
    justify-content: space-between;

    span {
        font-weight: 400;
        color: #989898;
        font-size: 14px;
    }
}

.under_navbar>div {
    flex: 1;
}

.icons {
    display: flex;
    gap: 10px;
    align-items: center;
}

.icon {
    font-size: 18px;
    color: #989898;
}

/* BUTTON NAVBAR */
.bottom_navbar {
    padding: 20px 0;
    background-color: #FFFFFF;
    box-shadow: 0 4px 6px -2px rgba(0, 0, 0, 0.15);
}

.banner {
    span {
        font-size: 30px;
        font-weight: 700;
    }

    .you {
        color: #2684E5;
    }

    .car {
        color: #010101;
    }
}

.bottom_left {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.messanger {
    font-size: 20px;
}

.bottom_rigth {
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: end;
}

/* Dropdown wrapper styling */
.dropdown-wrapper {
    display: flex;
    gap: 10px;
}
</style>