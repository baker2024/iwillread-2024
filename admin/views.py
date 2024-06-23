from sqladmin import ModelView

from orders.models import Order
from products.models import Product, Category
from users.models import User


class UsersAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.surname,
        User.name,
        User.patronymic,
        User.login,
        User.email,
        User.phone,
    ]
    column_details_exclude_list = [User.hashed_password, User.cart_items]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class ProductsAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.category,
        Product.name,
        Product.price,
        Product.count,
    ]
    column_details_exclude_list = [
        Product.cart_items,
        Product.order_items,
        Product.category_id,
    ]
    column_labels = {
        Product.id: "ID",
        Product.category: "Категория",
        Product.name: "Название",
        Product.description: "Описание",
        Product.price: "Цена",
        Product.year: "Год издания",
        Product.author: "Автор",
        Product.years_old: "Возрастные ограничения",
        Product.count_pages: "Количество страниц",
        Product.count: "Количество в наличии",
        Product.image: "Картинка товара",
    }
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-brands fa-product-hunt"


class CategoriesAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    column_labels = {
        Category.id: "ID",
        Category.name: "Название",
    }
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-list"


class OrdersAdmin(ModelView, model=Order):
    column_list = [
        Order.id,
        Order.user,
        Order.total_price,
        Order.created_at,
        Order.status,
    ]
    column_details_list = [
        Order.id,
        Order.user,
        Order.order_items,
        Order.total_price,
        Order.status,
        Order.created_at,
        Order.decline_desc,
    ]
    column_labels = {
        Order.id: "ID",
        Order.user_id: "user_id",
        Order.total_price: "Сумма",
        Order.status: "Статус",
        Order.created_at: "Дата и время",
        Order.decline_desc: "Причина отмены",
    }

    name = "Заказ"
    name_plural = "Заказы"
    icon = "fa-solid fa-dollar-sign"
